import os
import glob
import re

def escape_math_underscores(math_str):
    # Replaces unescaped _ with \_
    return re.sub(r'(?<!\\)_', r'\\_', math_str)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Split into markdown vs code blocks so we never touch code blocks
    code_block_pattern = re.compile(r'(```.*?```)', re.DOTALL)
    parts = code_block_pattern.split(content)

    for idx in range(len(parts)):
        # If it's a code block, skip
        if parts[idx].startswith('```'):
            continue

        text = parts[idx]

        # Step 2: Escape unescaped underscores inside inline math: \\( ... \\)
        def fix_inline(m):
            math_content = m.group(1)
            # escape unescaped _
            fixed = escape_math_underscores(math_content)
            return r'\\(' + fixed + r'\\)'

        text = re.sub(r'\\\\\((.*?)\\\\\)', fix_inline, text, flags=re.DOTALL)

        # Step 3: Ensure all display math blocks \\[ ... \\] are properly isolated
        lines = text.splitlines()
        new_lines = []
        i = 0
        while i < len(lines):
            line = lines[i]

            # Case A: Entire display math on single line: \\[ ... \\]
            single_match = re.match(r'^(\s*)\\+(\[)(.+?)\\+(\])\s*$', line)
            if single_match:
                indent = single_match.group(1)
                math_body = single_match.group(3).strip()
                # Escape underscores inside display math as well
                math_body = escape_math_underscores(math_body)

                if new_lines and new_lines[-1].strip() != '' and not new_lines[-1].strip().startswith('---'):
                    new_lines.append('')

                new_lines.append(f'{indent}\\\\[')
                new_lines.append(f'{indent}{math_body}')
                new_lines.append(f'{indent}\\\\]')

                if i + 1 < len(lines) and lines[i+1].strip() != '' and not lines[i+1].strip().startswith('---') and not lines[i+1].strip().startswith('#'):
                    new_lines.append('')

                i += 1
                continue

            # Case B: Opening of multiline display math: \\[
            open_match = re.match(r'^(\s*)\\+(\[)\s*$', line)
            if open_match:
                indent = open_match.group(1)
                if new_lines and new_lines[-1].strip() != '' and not new_lines[-1].strip().startswith('---'):
                    new_lines.append('')

                new_lines.append(f'{indent}\\\\[')
                i += 1
                while i < len(lines):
                    cur_line = lines[i]
                    close_match = re.match(r'^(\s*)\\+(\])\s*$', cur_line)
                    if close_match:
                        new_lines.append(f'{indent}\\\\]')
                        if i + 1 < len(lines) and lines[i+1].strip() != '' and not lines[i+1].strip().startswith('---') and not lines[i+1].strip().startswith('#'):
                            new_lines.append('')
                        i += 1
                        break
                    else:
                        # Escape unescaped underscores in multiline display math lines
                        escaped_line = escape_math_underscores(cur_line)
                        new_lines.append(escaped_line)
                        i += 1
                continue

            new_lines.append(line)
            i += 1

        parts[idx] = '\n'.join(new_lines)

    result = ''.join(parts)
    # Fix excess consecutive blank lines
    result = re.sub(r'\n{3,}', '\n\n', result)

    if result != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(result)
        return True
    return False

if __name__ == '__main__':
    files = sorted(glob.glob('src/**/*.md', recursive=True) + glob.glob('src/*.md'))
    modified = 0
    for f in files:
        if process_file(f):
            print(f'Modified: {f}')
            modified += 1
    print(f'Total files modified: {modified}')

import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.splitlines()
    new_lines = []
    
    in_code_block = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
            i += 1
            continue
            
        if in_code_block:
            new_lines.append(line)
            i += 1
            continue

        # Case A: Entire display math on single line: \\[ ... \\] or \\[ ... \\] or \[ ... \]
        single_line_match = re.match(r'^(\s*)\\+(\[)(.+?)\\+(\])\s*$', line)
        if single_line_match:
            indent = single_line_match.group(1)
            math_body = single_line_match.group(3).strip()
            
            # Ensure blank line before
            if new_lines and new_lines[-1].strip() != '' and not new_lines[-1].strip().startswith('---'):
                new_lines.append('')
                
            new_lines.append(f'{indent}\\\\[')
            new_lines.append(f'{indent}{math_body}')
            new_lines.append(f'{indent}\\\\]')
            
            # Lookahead
            if i + 1 < len(lines) and lines[i+1].strip() != '' and not lines[i+1].strip().startswith('---') and not lines[i+1].strip().startswith('#'):
                new_lines.append('')
            
            i += 1
            continue

        # Case B: Opening of multiline display math: \\[ or \[
        open_match = re.match(r'^(\s*)\\+(\[)\s*$', line)
        if open_match:
            indent = open_match.group(1)
            # Ensure blank line before
            if new_lines and new_lines[-1].strip() != '' and not new_lines[-1].strip().startswith('---'):
                new_lines.append('')
                
            new_lines.append(f'{indent}\\\\[')
            i += 1
            # Collect lines until \\] or \]
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
                    new_lines.append(cur_line)
                    i += 1
            continue

        new_lines.append(line)
        i += 1

    result = '\n'.join(new_lines) + '\n'
    
    # Fix multiple consecutive blank lines (> 2) to 1 blank line
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

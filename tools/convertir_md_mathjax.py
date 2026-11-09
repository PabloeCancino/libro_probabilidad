r"""Convierte un .md escrito con $...$ / $$...$$ al formato MathJax de mdBook del libro.

Reglas de conversión:
- $$...$$  ->  \\[ ... \\]  (en renglones propios)
- $...$    ->  \\( ... \\)
- Dentro de la matemática: duplica la barra ante puntuación ASCII (\{ -> \\{, \, -> \\,),
  convierte el salto de renglón \\ en \\\\, y escapa _ y * (\_, \*), para que
  CommonMark entregue a MathJax el LaTeX intacto.
- Ajusta los enlaces ../src/... -> ../... (el archivo destino vive dentro de src/).

Uso (desde la raíz del repositorio):
    python tools/convertir_md_mathjax.py
        Regenera src/evaluacion/autoexamen-semestral.md a partir de
        Auto-evaluaciones/autoexamen-semestral.md.

    python tools/convertir_md_mathjax.py ORIGEN.md DESTINO.md [--verificar]
        --verificar escribe además DESTINO.md.maths con el LaTeX original de cada
        expresión, útil para comparar contra el HTML renderizado.
"""
import re
import sys

BS = "\\"
PUNCT = re.compile(BS * 2 + r"([!-/:-@\[-`{-~])")


def esc(m):
    m = PUNCT.sub(lambda g: BS * 4 if g.group(1) == BS else BS * 2 + g.group(1), m)
    return m.replace("_", BS + "_").replace("*", BS + "*")


def convertir(texto):
    maths = []

    def disp(g):
        body = g.group(1).strip()
        maths.append(body)
        return BS * 2 + "[\n" + esc(body) + "\n" + BS * 2 + "]"

    def inl(g):
        maths.append(g.group(1))
        return BS * 2 + "(" + esc(g.group(1)) + BS * 2 + ")"

    t = texto.rstrip("\n") + "\n"
    t = re.sub(r"\$\$(.+?)\$\$", disp, t, flags=re.S)
    t = re.sub(r"(?<![\\$])\$([^$\n]+?)\$", inl, t)
    restantes = [l for l in t.splitlines() if "$" in l]
    if restantes:
        raise ValueError("Quedaron signos $ sin convertir:\n" + "\n".join(restantes[:5]))
    t = t.replace("](../src/", "](../")
    return t, maths


def main(argv):
    verificar = "--verificar" in argv
    args = [a for a in argv if a != "--verificar"]
    if not args:
        args = ["Auto-evaluaciones/autoexamen-semestral.md",
                "src/evaluacion/autoexamen-semestral.md"]
    if len(args) != 2:
        sys.exit(__doc__)
    src, dst = args
    with open(src, encoding="utf-8") as f:
        t, maths = convertir(f.read())
    with open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    if verificar:
        with open(dst + ".maths", "w", encoding="utf-8") as f:
            f.write("\n\x00\n".join(maths))
    print(f"{len(maths)} expresiones convertidas: {src} -> {dst}")


if __name__ == "__main__":
    main(sys.argv[1:])

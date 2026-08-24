# Apéndice A. Elementos de teoría de la medida e integración

Este apéndice sintetiza los teoremas fundamentales del análisis real y la teoría de la medida de Lebesgue que sustentan el cálculo riguroso de probabilidades y el paso al límite bajo el operador de integración/esperanza.

---

## A.1 Los Lemas de Borel-Cantelli

Sean \\((A\_n)\_{n=1}^\infty\\) una sucesión infinita de eventos en un espacio de probabilidad \\((\Omega, \mathcal{F}, \mathbb{P})\\).  
El evento *"\\(A\_n\\) ocurre para infinitos índices \\(n\\)"* se define mediante el límite superior de conjuntos:

\\[
\limsup\_{n \to \infty} A\_n = \{A\_n \text{ infinitas veces (i.v.)}\} = \bigcap\_{n=1}^\infty \bigcup\_{k=n}^\infty A\_k.
\\]

**Teorema A.1 (Primer Lema de Borel-Cantelli).** *Si la serie de probabilidades de los eventos converge:*

\\[
\sum\_{n=1}^\infty \mathbb{P}(A\_n) < \infty,
\\]

*entonces la probabilidad de que los eventos ocurran infinitas veces es cero:*

\\[
\mathbb{P}(A\_n \text{ i.v.}) = \mathbb{P}\left(\limsup\_{n \to \infty} A\_n\right) = 0.
\\]

*Demostración.*  
Definamos \\(E\_n = \bigcup\_{k=n}^\infty A\_k\\). La sucesión \\(E\_n\\) es decreciente: \\(E\_n \downarrow \limsup\_{k\to\infty} A\_k\\).  
Por la desigualdad de Boole (subaditividad numerable):

\\[
\mathbb{P}(E\_n) = \mathbb{P}\left(\bigcup\_{k=n}^\infty A\_k\right) \le \sum\_{k=n}^\infty \mathbb{P}(A\_k).
\\]

Como la serie \\(\sum\_{k=1}^\infty \mathbb{P}(A\_k)\\) es convergente, su cola residual tiende a cero: \\(\lim\_{n \to \infty} \sum\_{k=n}^\infty \mathbb{P}(A\_k) = 0\\).  
Por la continuidad de la medida de probabilidad desde arriba (Teorema 1.29):

\\[
\mathbb{P}\left(\limsup\_{n \to \infty} A\_n\right) = \lim\_{n \to \infty} \mathbb{P}(E\_n) \le \lim\_{n \to \infty} \sum\_{k=n}^\infty \mathbb{P}(A\_k) = 0. \quad \blacksquare
\\]

**Teorema A.2 (Segundo Lema de Borel-Cantelli).** *Si los eventos \\((A\_n)\_{n=1}^\infty\\) son **mutuamente independientes** y la serie de probabilidades diverge:*

\\[
\sum\_{n=1}^\infty \mathbb{P}(A\_n) = \infty,
\\]

*entonces la probabilidad de que ocurran infinitas veces es uno:*

\\[
\mathbb{P}(A\_n \text{ i.v.}) = \mathbb{P}\left(\limsup\_{n \to \infty} A\_n\right) = 1.
\\]

*Demostración.*  
El complemento del evento límite es:

\\[
\left(\limsup\_{n \to \infty} A\_n\right)^c = \left(\bigcap\_{n=1}^\infty \bigcup\_{k=n}^\infty A\_k\right)^c = \bigcup\_{n=1}^\infty \bigcap\_{k=n}^\infty A\_k^c.
\\]

Para cualquier \\(n \ge 1\\) fijo y cualquier \\(m > n\\), por la independencia de los eventos \\(A\_k\\) (y de sus complementos):

\\[
\mathbb{P}\left(\bigcap\_{k=n}^m A\_k^c\right) = \prod\_{k=n}^m \mathbb{P}(A\_k^c) = \prod\_{k=n}^m (1 - \mathbb{P}(A\_k)).
\\]

Usando la desigualdad elemental \\(1 - x \le e^{-x}\\) para todo \\(x \in \mathbb{R}\\):

\\[
\prod\_{k=n}^m (1 - \mathbb{P}(A\_k)) \le \prod\_{k=n}^m \exp(-\mathbb{P}(A\_k)) = \exp\left(-\sum\_{k=n}^m \mathbb{P}(A\_k)\right).
\\]

Haciendo \\(m \to \infty\\), como \\(\sum\_{k=n}^\infty \mathbb{P}(A\_k) = \infty\\), la exponencial tiende a \\(e^{-\infty} = 0\\).  
Por tanto, \\(\mathbb{P}\left(\bigcap\_{k=n}^\infty A\_k^c\right) = 0\\) para todo \\(n\\).  
Por la subaditividad de la probabilidad:

\\[
\mathbb{P}\left(\left(\limsup\_{n \to \infty} A\_n\right)^c\right) \le \sum\_{n=1}^\infty \mathbb{P}\left(\bigcap\_{k=n}^\infty A\_k^c\right) = \sum\_{n=1}^\infty 0 = 0.
\\]

Por la regla del complemento, \\(\mathbb{P}\left(\limsup\_{n \to \infty} A\_n\right) = 1 - 0 = 1\\). \\(\blacksquare\\)

---

## A.2 Teoremas de paso al límite bajo el operador esperanza

**Teorema A.3 (Teorema de Convergencia Monótona de Lebesgue / Beppo Levi).** *Sea \\((X\_n)\_{n=1}^\infty\\) una sucesión monótona no decreciente de variables aleatorias no negativas:*

\\[
0 \le X\_1 \le X\_2 \le X\_3 \le \dots \quad \text{con } X\_n \xrightarrow{\text{c.s.}} X.
\\]

*Entonces la esperanza del límite es el límite de las esperanzas:*

\\[
\lim\_{n \to \infty} \mathbb{E}[X\_n] = \mathbb{E}\left[\lim\_{n \to \infty} X\_n\right] = \mathbb{E}[X].
\\]

**Teorema A.4 (Teorema de Convergencia Dominada de Lebesgue).** *Sea \\((X\_n)\_{n=1}^\infty\\) una sucesión de variables aleatorias tales que \\(X\_n \xrightarrow{\text{c.s.}} X\\). Si existe una variable aleatoria no negativa \\(Y\\) (el dominador) con \\(\mathbb{E}[Y] < \infty\\) tal que:*

\\[
|X\_n(\omega)| \le Y(\omega) \quad \text{casi seguramente para todo } n \ge 1,
\\]

*entonces \\(X\\) es integrable y:*

\\[
\lim\_{n \to \infty} \mathbb{E}[X\_n] = \mathbb{E}[X], \qquad \text{y además } X\_n \xrightarrow{L^1} X \quad (\lim\_{n \to \infty} \mathbb{E}[|X\_n - X|] = 0).
\\]

**Lema A.5 (Lema de Fatou).** *Para cualquier sucesión de variables aleatorias no negativas \\(X\_n \ge 0\\):*

\\[
\mathbb{E}\left[\liminf\_{n \to \infty} X\_n\right] \le \liminf\_{n \to \infty} \mathbb{E}[X\_n].
\\]

---

## A.3 Teorema de Fubini-Tonelli para integrales conjuntas

**Teorema A.6 (Fubini-Tonelli).** *Sea \\(f: \mathbb{R}^2 \to \mathbb{R}\\) una función medible de Borel.*
1. **(Tonelli):** Si \\(f(x, y) \ge 0\\) es no negativa, entonces las integrales iteradas son iguales (pudiendo ambas ser \\(+\infty\\)):

   \\[
   \int\_{-\infty}^\infty \left(\int\_{-\infty}^\infty f(x, y) \, dy\right) dx = \int\_{-\infty}^\infty \left(\int\_{-\infty}^\infty f(x, y) \, dx\right) dy = \iint\_{\mathbb{R}^2} f(x, y) \, dx \, dy.
   \\]

2. **(Fubini):** Si \\(\iint\_{\mathbb{R}^2} |f(x, y)| \, dx \, dy < \infty\\), entonces el orden de integración puede intercambiarse libremente dando el mismo valor numérico finito.
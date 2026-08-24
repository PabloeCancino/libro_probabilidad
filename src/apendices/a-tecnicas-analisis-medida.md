# Apéndice A. Elementos de teoría de la medida e integración

Este apéndice sintetiza los teoremas fundamentales del análisis real y la teoría de la medida de Lebesgue que sustentan el cálculo riguroso de probabilidades y el paso al límite bajo el operador de integración/esperanza.

---

## A.1 Los Lemas de Borel-Cantelli

Sean \\((A_n)_{n=1}^\infty\\) una sucesión infinita de eventos en un espacio de probabilidad \\((\Omega, \mathcal{F}, \mathbb{P})\\).  
El evento *"\\(A_n\\) ocurre para infinitos índices \\(n\\)"* se define mediante el límite superior de conjuntos:

\\[
\limsup_{n \to \infty} A_n = \{A_n \text{ infinitas veces (i.v.)}\} = \bigcap_{n=1}^\infty \bigcup_{k=n}^\infty A_k.
\\]

**Teorema A.1 (Primer Lema de Borel-Cantelli).** *Si la serie de probabilidades de los eventos converge:*

\\[
\sum_{n=1}^\infty \mathbb{P}(A_n) < \infty,
\\]

*entonces la probabilidad de que los eventos ocurran infinitas veces es cero:*

\\[
\mathbb{P}(A_n \text{ i.v.}) = \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 0.
\\]

*Demostración.*  
Definamos \\(E_n = \bigcup_{k=n}^\infty A_k\\). La sucesión \\(E_n\\) es decreciente: \\(E_n \downarrow \limsup_{k\to\infty} A_k\\).  
Por la desigualdad de Boole (subaditividad numerable):

\\[
\mathbb{P}(E_n) = \mathbb{P}\left(\bigcup_{k=n}^\infty A_k\right) \le \sum_{k=n}^\infty \mathbb{P}(A_k).
\\]

Como la serie \\(\sum_{k=1}^\infty \mathbb{P}(A_k)\\) es convergente, su cola residual tiende a cero: \\(\lim_{n \to \infty} \sum_{k=n}^\infty \mathbb{P}(A_k) = 0\\).  
Por la continuidad de la medida de probabilidad desde arriba (Teorema 1.29):

\\[
\mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = \lim_{n \to \infty} \mathbb{P}(E_n) \le \lim_{n \to \infty} \sum_{k=n}^\infty \mathbb{P}(A_k) = 0. \quad \blacksquare
\\]

**Teorema A.2 (Segundo Lema de Borel-Cantelli).** *Si los eventos \\((A_n)_{n=1}^\infty\\) son **mutuamente independientes** y la serie de probabilidades diverge:*

\\[
\sum_{n=1}^\infty \mathbb{P}(A_n) = \infty,
\\]

*entonces la probabilidad de que ocurran infinitas veces es uno:*

\\[
\mathbb{P}(A_n \text{ i.v.}) = \mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 1.
\\]

*Demostración.*  
El complemento del evento límite es:

\\[
\left(\limsup_{n \to \infty} A_n\right)^c = \left(\bigcap_{n=1}^\infty \bigcup_{k=n}^\infty A_k\right)^c = \bigcup_{n=1}^\infty \bigcap_{k=n}^\infty A_k^c.
\\]

Para cualquier \\(n \ge 1\\) fijo y cualquier \\(m > n\\), por la independencia de los eventos \\(A_k\\) (y de sus complementos):

\\[
\mathbb{P}\left(\bigcap_{k=n}^m A_k^c\right) = \prod_{k=n}^m \mathbb{P}(A_k^c) = \prod_{k=n}^m (1 - \mathbb{P}(A_k)).
\\]

Usando la desigualdad elemental \\(1 - x \le e^{-x}\\) para todo \\(x \in \mathbb{R}\\):

\\[
\prod_{k=n}^m (1 - \mathbb{P}(A_k)) \le \prod_{k=n}^m \exp(-\mathbb{P}(A_k)) = \exp\left(-\sum_{k=n}^m \mathbb{P}(A_k)\right).
\\]

Haciendo \\(m \to \infty\\), como \\(\sum_{k=n}^\infty \mathbb{P}(A_k) = \infty\\), la exponencial tiende a \\(e^{-\infty} = 0\\).  
Por tanto, \\(\mathbb{P}\left(\bigcap_{k=n}^\infty A_k^c\right) = 0\\) para todo \\(n\\).  
Por la subaditividad de la probabilidad:

\\[
\mathbb{P}\left(\left(\limsup_{n \to \infty} A_n\right)^c\right) \le \sum_{n=1}^\infty \mathbb{P}\left(\bigcap_{k=n}^\infty A_k^c\right) = \sum_{n=1}^\infty 0 = 0.
\\]

Por la regla del complemento, \\(\mathbb{P}\left(\limsup_{n \to \infty} A_n\right) = 1 - 0 = 1\\). \\(\blacksquare\\)

---

## A.2 Teoremas de paso al límite bajo el operador esperanza

**Teorema A.3 (Teorema de Convergencia Monótona de Lebesgue / Beppo Levi).** *Sea \\((X_n)_{n=1}^\infty\\) una sucesión monótona no decreciente de variables aleatorias no negativas:*

\\[
0 \le X_1 \le X_2 \le X_3 \le \dots \quad \text{con } X_n \xrightarrow{\text{c.s.}} X.
\\]

*Entonces la esperanza del límite es el límite de las esperanzas:*

\\[
\lim_{n \to \infty} \mathbb{E}[X_n] = \mathbb{E}\left[\lim_{n \to \infty} X_n\right] = \mathbb{E}[X].
\\]

**Teorema A.4 (Teorema de Convergencia Dominada de Lebesgue).** *Sea \\((X_n)_{n=1}^\infty\\) una sucesión de variables aleatorias tales que \\(X_n \xrightarrow{\text{c.s.}} X\\). Si existe una variable aleatoria no negativa \\(Y\\) (el dominador) con \\(\mathbb{E}[Y] < \infty\\) tal que:*

\\[
|X_n(\omega)| \le Y(\omega) \quad \text{casi seguramente para todo } n \ge 1,
\\]

*entonces \\(X\\) es integrable y:*

\\[
\lim_{n \to \infty} \mathbb{E}[X_n] = \mathbb{E}[X], \qquad \text{y además } X_n \xrightarrow{L^1} X \quad (\lim_{n \to \infty} \mathbb{E}[|X_n - X|] = 0).
\\]

**Lema A.5 (Lema de Fatou).** *Para cualquier sucesión de variables aleatorias no negativas \\(X_n \ge 0\\):*

\\[
\mathbb{E}\left[\liminf_{n \to \infty} X_n\right] \le \liminf_{n \to \infty} \mathbb{E}[X_n].
\\]

---

## A.3 Teorema de Fubini-Tonelli para integrales conjuntas

**Teorema A.6 (Fubini-Tonelli).** *Sea \\(f: \mathbb{R}^2 \to \mathbb{R}\\) una función medible de Borel.*
1. **(Tonelli):** Si \\(f(x, y) \ge 0\\) es no negativa, entonces las integrales iteradas son iguales (pudiendo ambas ser \\(+\infty\\)):

   \\[
   \int_{-\infty}^\infty \left(\int_{-\infty}^\infty f(x, y) \, dy\right) dx = \int_{-\infty}^\infty \left(\int_{-\infty}^\infty f(x, y) \, dx\right) dy = \iint_{\mathbb{R}^2} f(x, y) \, dx \, dy.
   \\]

2. **(Fubini):** Si \\(\iint_{\mathbb{R}^2} |f(x, y)| \, dx \, dy < \infty\\), entonces el orden de integración puede intercambiarse libremente dando el mismo valor numérico finito.

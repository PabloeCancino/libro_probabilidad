# 4.1 Esperanza matemática, valor esperado y linealidad

## 4.1.1 Definición formal de esperanza matemática

La **esperanza matemática** (o valor esperado) de una variable aleatoria es el centro de masa o promedio ponderado de todos los valores posibles que puede tomar la variable, ponderados por sus respectivas probabilidades.

En el marco riguroso de la teoría de la medida de Lebesgue, si \\(X: \Omega \to \mathbb{R}\\) es una variable aleatoria en \\((\Omega, \mathcal{F}, \mathbb{P})\\), la esperanza se define como la integral abstracta:

\\[
\mathbb{E}[X] = \int\_\Omega X(\omega) \, d\mathbb{P}(\omega) = \int\_{-\infty}^\infty x \, dF\_X(x).
\\]

**Condición de existencia absoluta:** Decimos que la esperanza \\(\mathbb{E}[X]\\) **existe** y es finita si y solo si \\(X\\) es absolutamente integrable respecto a la medida de probabilidad:

\\[
\mathbb{E}[|X|] < \infty.
\\]

(Si \\(\mathbb{E}[|X|] = \infty\\), la esperanza no está definida o diverge, como en la distribución de Cauchy).

### Definición operativa por casos

**Definición 4.1 (Esperanza en los casos discreto y continuo).**
1. **Caso discreto:** Si \\(X\\) es una v.a. discreta con soporte \\(S\_X\\) y PMF \\(p\_X(x)\\):

   \\[
   \mathbb{E}[X] = \sum\_{x \in S\_X} x \cdot p\_X(x), \quad \text{siempre que } \sum\_{x \in S\_X} |x| \cdot p\_X(x) < \infty.
   \\]

2. **Caso continuo:** Si \\(X\\) es una v.a. continua con PDF \\(f\_X(x)\\):

   \\[
   \mathbb{E}[X] = \int\_{-\infty}^{\infty} x \cdot f\_X(x) \, dx, \quad \text{siempre que } \int\_{-\infty}^{\infty} |x| \cdot f\_X(x) \, dx < \infty.
   \\]

---

## 4.1.2 El Teorema del Cambio de Variable (LOTUS)

Para calcular la esperanza de una función de una variable aleatoria \\(Y = g(X)\\), no es necesario determinar primero la distribución de \\(Y\\); basta con integrar la función \\(g\\) ponderada por la distribución original de \\(X\\).

**Teorema 4.2 (Ley del Estadístico Inconsciente - LOTUS).** *Sea \\(X\\) una variable aleatoria y sea \\(g: \mathbb{R} \to \mathbb{R}\\) una función medible de Borel. Entonces:*
1. **Caso discreto:**

   \\[
   \mathbb{E}[g(X)] = \sum\_{x \in S\_X} g(x) \cdot p\_X(x).
   \\]

2. **Caso continuo:**

   \\[
   \mathbb{E}[g(X)] = \int\_{-\infty}^{\infty} g(x) \cdot f\_X(x) \, dx.
   \\]

*en ambos casos siempre que \\(\mathbb{E}[|g(X)|] < \infty\\).*

Para el caso bivariado \\(Z = g(X, Y)\\):

\\[
\mathbb{E}[g(X, Y)] = \iint\_{\mathbb{R}^2} g(x, y) f\_{X,Y}(x, y) \, dx \, dy \quad \left(\text{o } \sum\_{x}\sum\_{y} g(x, y) p\_{X,Y}(x, y)\right).
\\]

---

## 4.1.3 Linealidad del operador esperanza

La propiedad más poderosa y operativa de la esperanza matemática es su **linealidad absoluta**, la cual se cumple **sin importar si las variables son independientes o dependientes**.

**Teorema 4.3 (Linealidad de la esperanza).** *Sean \\(X\\) e \\(Y\\) dos variables aleatorias en el mismo espacio de probabilidad con esperanzas finitas, y sean \\(a, b, c \in \mathbb{R}\\). Entonces:*

\\[
\mathbb{E}[aX + bY + c] = a\mathbb{E}[X] + b\mathbb{E}[Y] + c.
\\]

*Demostración (caso continuo bivariado).*  
Aplicando el Teorema 4.2 con \\(g(x, y) = ax + by + c\\):

\\[
\begin{aligned}
\mathbb{E}[aX + bY + c] &= \int\_{-\infty}^\infty \int\_{-\infty}^\infty (ax + by + c) f\_{X,Y}(x, y) \, dx \, dy \\\\
&= a \int\_{-\infty}^\infty x \left[\int\_{-\infty}^\infty f\_{X,Y}(x, y) dy\right] dx + b \int\_{-\infty}^\infty y \left[\int\_{-\infty}^\infty f\_{X,Y}(x, y) dx\right] dy \\\\
&\quad + c \int\_{-\infty}^\infty \int\_{-\infty}^\infty f\_{X,Y}(x, y) \, dx \, dy \\\\
&= a \int\_{-\infty}^\infty x f\_X(x) \, dx + b \int\_{-\infty}^\infty y f\_Y(y) \, dy + c \cdot 1 \\\\
&= a\mathbb{E}[X] + b\mathbb{E}[Y] + c. \quad \blacksquare
\end{aligned}
\\]

---

## 4.1.4 Propiedades adicionales fundamentales de la esperanza

**Proposición 4.4.**
1. **Constante:** Si \\(c \in \mathbb{R}\\), entonces \\(\mathbb{E}[c] = c\\).
2. **Función indicadora:** Si \\(A \in \mathcal{F}\\) y \\(\mathbb{I}\_A\\) es su función indicadora, entonces \\(\mathbb{E}[\mathbb{I}\_A] = 1 \cdot \mathbb{P}(A) + 0 \cdot \mathbb{P}(A^c) = \mathbb{P}(A)\\).
3. **Monotonía:** Si \\(X \le Y\\) casi seguramente (es decir, \\(\mathbb{P}(X \le Y) = 1\\)), entonces:

   \\[
   \mathbb{E}[X] \le \mathbb{E}[Y].
   \\]

4. **Desigualdad del valor absoluto:**

   \\[
   |\mathbb{E}[X]| \le \mathbb{E}[|X|].
   \\]

**Teorema 4.5 (Producto de variables independientes).** *Si \\(X\\) e \\(Y\\) son variables aleatorias independientes con esperanzas finitas, entonces:*

\\[
\mathbb{E}[XY] = \mathbb{E}[X] \cdot \mathbb{E}[Y].
\\]

*Demostración (caso continuo).*  
Dado que \\(X \perp Y\\), la densidad conjunta factoriza: \\(f\_{X,Y}(x, y) = f\_X(x) f\_Y(y)\\). Por el Teorema de Fubini:

\\[
\begin{aligned}
\mathbb{E}[XY] &= \int\_{-\infty}^\infty \int\_{-\infty}^\infty (xy) f\_{X,Y}(x, y) \, dx \, dy \\\\
&= \int\_{-\infty}^\infty \int\_{-\infty}^\infty (xy) f\_X(x) f\_Y(y) \, dx \, dy \\\\
&= \left(\int\_{-\infty}^\infty x f\_X(x) \, dx\right) \left(\int\_{-\infty}^\infty y f\_Y(y) \, dy\right) = \mathbb{E}[X] \cdot \mathbb{E}[Y]. \quad \blacksquare
\end{aligned}
\\]

---

## 4.1.5 Fórmula de la integral de la cola (Tail Sum Formula)

Para variables aleatorias no negativas, la esperanza puede calcularse directamente integrando su función de supervivencia.

**Teorema 4.6 (Fórmula de la cola).** *Sea \\(X \ge 0\\) una variable aleatoria no negativa.*
1. **Caso continuo:**

   \\[
   \mathbb{E}[X] = \int\_0^\infty \mathbb{P}(X > x) \, dx = \int\_0^\infty (1 - F\_X(x)) \, dx.
   \\]

2. **Caso discreto en \\(\mathbb{N}\\):**

   \\[
   \mathbb{E}[X] = \sum\_{k=0}^\infty \mathbb{P}(X > k).
   \\]

*Demostración (caso continuo).*  
Por la definición y cambiando el orden de integración (Fubini):

\\[
\int\_0^\infty \mathbb{P}(X > x) \, dx = \int\_0^\infty \left(\int\_x^\infty f\_X(t) \, dt\right) dx = \int\_0^\infty f\_X(t) \left(\int\_0^t dx\right) dt = \int\_0^\infty t f\_X(t) \, dt = \mathbb{E}[X]. \quad \blacksquare
\\]
# 4.3 Esperanza condicional y ley de varianza total

## 4.3.1 Esperanza condicional como función y como variable aleatoria

La esperanza condicional es una de las herramientas más sofisticadas y útiles de la teoría moderna de probabilidades, sirviendo como fundamento de las martingalas, el filtrado estocástico y la inferencia predictiva.

**Definición 4.16 (Esperanza condicional dado un valor numérico).** Sea \\((X, Y)\\) un vector aleatorio con esperanza \\(\mathbb{E}[|X|] < \infty\\).
1. **Caso discreto:** Para cualquier \\(y\\) con \\(p_Y(y) > 0\\):

   \\[
   \mathbb{E}[X \mid Y = y] = \sum_{x} x \cdot p_{X \mid Y}(x \mid y) = \sum_{x} x \frac{p_{X,Y}(x, y)}{p_Y(y)}.
   \\]

2. **Caso continuo:** Para cualquier \\(y\\) con \\(f_Y(y) > 0\\):

   \\[
   \mathbb{E}[X \mid Y = y] = \int_{-\infty}^{\infty} x \cdot f_{X \mid Y}(x \mid y) \, dx = \int_{-\infty}^{\infty} x \frac{f_{X,Y}(x, y)}{f_Y(y)} \, dx.
   \\]

Observemos que \\(\mathbb{E}[X \mid Y = y] = g(y)\\) es una función determinista ordinaria del valor \\(y\\).

**Definición 4.17 (Esperanza condicional como variable aleatoria).** La **esperanza condicional de \\(X\\) dado \\(Y\\)**, denotada \\(\mathbb{E}[X \mid Y]\\), es la variable aleatoria:

\\[
\mathbb{E}[X \mid Y] = g(Y).
\\]

Es decir, \\(\mathbb{E}[X \mid Y]\\) es una función medible de la variable aleatoria \\(Y\\) que toma el valor \\(g(y)\\) cuando \\(Y(\omega) = y\\).

---

## 4.3.2 Propiedades fundamentales y la Ley de las Esperanzas Iteradas (Propiedad de la Torre)

**Teorema 4.18 (Ley de las Esperanzas Iteradas / Propiedad de la Torre).** *Para cualquier variable aleatoria \\(X\\) con \\(\mathbb{E}[|X|] < \infty\\):*

\\[
\mathbb{E}[\mathbb{E}[X \mid Y]] = \mathbb{E}[X].
\\]

*Demostración (caso continuo).*  
Sea \\(g(y) = \mathbb{E}[X \mid Y = y] = \int_{-\infty}^\infty x \frac{f_{X,Y}(x, y)}{f_Y(y)} dx\\).  
Por LOTUS (Teorema 4.2), la esperanza de la variable aleatoria \\(g(Y)\\) es:

\\[
\begin{aligned}
\mathbb{E}[\mathbb{E}[X \mid Y]] &= \mathbb{E}[g(Y)] = \int_{-\infty}^\infty g(y) f_Y(y) \, dy \\\\
&= \int_{-\infty}^\infty \left(\int_{-\infty}^\infty x \frac{f_{X,Y}(x, y)}{f_Y(y)} \, dx\right) f_Y(y) \, dy \\\\
&= \int_{-\infty}^\infty \int_{-\infty}^\infty x f_{X,Y}(x, y) \, dx \, dy = \mathbb{E}[X]. \quad \blacksquare
\end{aligned}
\\]

### Propiedades algebraicas de la esperanza condicional
1. **Linealidad:** \\(\mathbb{E}[a X_1 + b X_2 + c \mid Y] = a \mathbb{E}[X_1 \mid Y] + b \mathbb{E}[X_2 \mid Y] + c\\).
2. **"Sacar lo que es conocido":** Si \\(h(Y)\\) es una función medible de \\(Y\\):

   \\[
   \mathbb{E}[h(Y) X \mid Y] = h(Y) \cdot \mathbb{E}[X \mid Y].
   \\]

   En particular, \\(\mathbb{E}[h(Y) \mid Y] = h(Y)\\).
3. **Independencia:** Si \\(X \perp Y\\), entonces:

   \\[
   \mathbb{E}[X \mid Y] = \mathbb{E}[X] \quad \text{(una constante casi seguramente)}.
   \\]

---

## 4.3.3 La Esperanza Condicional como el Mejor Predictor en Media Cuadrática

**Teorema 4.19 (Ortogonalidad y predicción óptima).** *Entre todas las funciones medibles \\(h(Y)\\) con segundo momento finito, la esperanza condicional \\(g(Y) = \mathbb{E}[X \mid Y]\\) es el estimador que minimiza el error cuadrático medio:*

\\[
\min_{h} \mathbb{E}[(X - h(Y))^2] = \mathbb{E}[(X - \mathbb{E}[X \mid Y])^2].
\\]

*Demostración.*  
Para cualquier función predictora \\(h(Y)\\), sumamos y restamos \\(\mathbb{E}[X \mid Y]\\):

\\[
X - h(Y) = (X - \mathbb{E}[X \mid Y]) + (\mathbb{E}[X \mid Y] - h(Y)).
\\]

Elevando al cuadrado y tomando esperanza:

\\[
\mathbb{E}[(X - h(Y))^2] = \mathbb{E}[(X - \mathbb{E}[X \mid Y])^2] + \mathbb{E}[(\mathbb{E}[X \mid Y] - h(Y))^2] + 2 \mathbb{E}[(X - \mathbb{E}[X \mid Y])(\mathbb{E}[X \mid Y] - h(Y))].
\\]

Por la ley de esperanzas iteradas y sacando la función de \\(Y\\):

\\[
\mathbb{E}[(X - \mathbb{E}[X \mid Y])(\mathbb{E}[X \mid Y] - h(Y))] = \mathbb{E}\Big[(\mathbb{E}[X \mid Y] - h(Y)) \cdot \underbrace{\mathbb{E}[X - \mathbb{E}[X \mid Y] \mid Y]}_{= \mathbb{E}[X \mid Y] - \mathbb{E}[X \mid Y] = 0}\Big] = 0.
\\]

Por tanto:

\\[
\mathbb{E}[(X - h(Y))^2] = \mathbb{E}[(X - \mathbb{E}[X \mid Y])^2] + \underbrace{\mathbb{E}[(\mathbb{E}[X \mid Y] - h(Y))^2]}_{\ge 0}.
\\]

La expresión se minimiza de forma única cuando el segundo término no negativo se anula, es decir, cuando \\(h(Y) = \mathbb{E}[X \mid Y]\\) casi seguramente. \\(\blacksquare\\)

---

## 4.3.4 Varianza condicional y Ley de la Varianza Total (Ley de Eva)

**Definición 4.20 (Varianza condicional).** La **varianza condicional** de \\(X\\) dado \\(Y\\) es la variable aleatoria:

\\[
\text{Var}(X \mid Y) = \mathbb{E}[(X - \mathbb{E}[X \mid Y])^2 \mid Y] = \mathbb{E}[X^2 \mid Y] - (\mathbb{E}[X \mid Y])^2.
\\]

**Teorema 4.21 (Ley de la Varianza Total / Descomposición ANOVA).** *Para cualquier variable aleatoria \\(X\\) con varianza finita:*

\\[
\text{Var}(X) = \mathbb{E}[\text{Var}(X \mid Y)] + \text{Var}(\mathbb{E}[X \mid Y]).
\\]

*Demostración analítica.*  
Por la definición de varianza condicional:

\\[
\text{Var}(X \mid Y) = \mathbb{E}[X^2 \mid Y] - (\mathbb{E}[X \mid Y])^2.
\\]

Tomando esperanza en ambos lados y aplicando la Ley de la Torre (Teorema 4.18):

\\[
\mathbb{E}[\text{Var}(X \mid Y)] = \mathbb{E}[\mathbb{E}[X^2 \mid Y]] - \mathbb{E}[(\mathbb{E}[X \mid Y])^2] = \mathbb{E}[X^2] - \mathbb{E}[(\mathbb{E}[X \mid Y])^2]. \quad \text{(Ecuación 1)}
\\]

Por otro lado, la varianza de la variable aleatoria \\(\mathbb{E}[X \mid Y]\\) es:

\\[
\text{Var}(\mathbb{E}[X \mid Y]) = \mathbb{E}[(\mathbb{E}[X \mid Y])^2] - (\mathbb{E}[\mathbb{E}[X \mid Y]])^2 = \mathbb{E}[(\mathbb{E}[X \mid Y])^2] - (\mathbb{E}[X])^2. \quad \text{(Ecuación 2)}
\\]

Sumando la Ecuación 1 y la Ecuación 2:

\\[
\mathbb{E}[\text{Var}(X \mid Y)] + \text{Var}(\mathbb{E}[X \mid Y]) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = \text{Var}(X). \quad \blacksquare
\\]

### Interpretación conceptual
- \\(\mathbb{E}[\text{Var}(X \mid Y)]\\): **Varianza no explicada** (variabilidad intrínseca intra-grupos).
- \\(\text{Var}(\mathbb{E}[X \mid Y])\\): **Varianza explicada** por la variable \\(Y\\) (variabilidad inter-grupos).

**Ejemplo 4.22 (Suma aleatoria de variables aleatorias: Proceso Compuesto de Poisson).**  
Sea \\(N \sim \text{Poisson}(\lambda)\\) el número de reclamos a una aseguradora en un mes, y sean \\(X_1, X_2, \dots \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(\beta)\\) los montos individuales de cada reclamo, independientes de \\(N\\).  
Sea \\(S_N = \sum_{i=1}^N X_i\\) el monto total reclamado (con \\(S_0 = 0\\)).
1. **Esperanza total:**

   \\[
   \mathbb{E}[S_N \mid N] = \mathbb{E}\left[\sum_{i=1}^N X_i \;\middle|\; N\right] = N \mathbb{E}[X] \implies \mathbb{E}[S_N] = \mathbb{E}[N \mathbb{E}[X]] = \mathbb{E}[N] \mathbb{E}[X] = \lambda \cdot \frac{1}{\beta}.
   \\]

2. **Varianza total:**

   \\[
   \text{Var}(S_N \mid N) = N \text{Var}(X).
   \\]

   Por la Ley de la Varianza Total:

   \\[
   \begin{aligned}
   \text{Var}(S_N) &= \mathbb{E}[\text{Var}(S_N \mid N)] + \text{Var}(\mathbb{E}[S_N \mid N]) = \mathbb{E}[N \text{Var}(X)] + \text{Var}(N \mathbb{E}[X]) \\\\
   &= \text{Var}(X)\mathbb{E}[N] + (\mathbb{E}[X])^2 \text{Var}(N) = \frac{1}{\beta^2} \lambda + \frac{1}{\beta^2} \lambda = \frac{2\lambda}{\beta^2}.
   \end{aligned}
   \\]

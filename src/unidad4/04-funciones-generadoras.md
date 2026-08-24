# 4.4 Funciones generadoras de momentos y función característica

## 4.4.1 Función Generadora de Momentos (MGF)

La **función generadora de momentos** transforma una distribución de probabilidad en una función analítica real en el dominio de Laplace, codificando todos los momentos de la variable en una única expresión compacta y facilitando enormemente el análisis de sumas de variables independientes.

**Definición 4.23 (Función Generadora de Momentos - MGF).** La **función generadora de momentos** de una variable aleatoria \\(X\\), denotada \\(M\_X(t)\\), es la función:

\\[
M\_X(t) = \mathbb{E}[e^{tX}], \quad t \in \mathbb{R},
\\]

definida para todos los valores de \\(t\\) para los cuales la esperanza converge absolutamente. Decimos que la MGF **existe** si existe algún \\(h > 0\\) tal que \\(M\_X(t) < \infty\\) para todo \\(t \in (-h, h)\\).

- **Caso discreto:** \\(M\_X(t) = \sum\_{x \in S\_X} e^{tx} p\_X(x)\\).
- **Caso continuo:** \\(M\_X(t) = \int\_{-\infty}^{\infty} e^{tx} f\_X(x) \, dx\\) (la transformada bilateral de Laplace de \\(f\_X\\)).

---

## 4.4.2 Obtención de momentos a partir de la MGF

**Teorema 4.24 (Diferenciación bajo el signo de esperanza).** *Si \\(M\_X(t)\\) existe en un entorno \\((-h, h)\\) de cero, entonces \\(M\_X(t)\\) es infinitamente diferenciable en \\(t = 0\\), y el momento ordinario de orden \\(k\\) se obtiene evaluando la \\(k\\)-ésima derivada en cero:*

\\[
M\_X^{(k)}(0) = \left. \frac{d^k}{dt^k} M\_X(t) \right|\_{t=0} = \mathbb{E}[X^k].
\\]

*Demostración.*  
Expandiendo la función exponencial en su serie de Maclaurin en potencias de \\(t\\):

\\[
e^{tX} = \sum\_{k=0}^{\infty} \frac{(tX)^k}{k!} = 1 + tX + \frac{t^2 X^2}{2!} + \frac{t^3 X^3}{3!} + \dots + \frac{t^k X^k}{k!} + \dots
\\]

Tomando esperanza término a término (justificado por el Teorema de Convergencia Dominada dentro del radio de convergencia):

\\[
M\_X(t) = \mathbb{E}[e^{tX}] = \sum\_{k=0}^{\infty} \frac{t^k}{k!} \mathbb{E}[X^k] = 1 + t\mathbb{E}[X] + \frac{t^2}{2!}\mathbb{E}[X^2] + \dots + \frac{t^k}{k!}\mathbb{E}[X^k] + \dots
\\]

Derivando \\(k\\) veces respecto a \\(t\\) y evaluando en \\(t = 0\\), todos los términos con potencias de \\(t\\) se anulan salvo el término constante \\(\mathbb{E}[X^k]\\). \\(\blacksquare\\)

En particular:

\\[
\mathbb{E}[X] = M\_X'(0), \qquad \mathbb{E}[X^2] = M\_X''(0) \implies \text{Var}(X) = M\_X''(0) - [M\_X'(0)]^2.
\\]

---

## 4.4.3 Propiedades algebraicas fundamentales de la MGF

**Teorema 4.25.**
1. **Evaluación en cero:** \\(M\_X(0) = \mathbb{E}[e^0] = \mathbb{E}[1] = 1\\).
2. **Transformación lineal:** Si \\(Y = aX + b\\), entonces:

   \\[
   M\_{aX+b}(t) = \mathbb{E}[e^{t(aX+b)}] = e^{bt} \mathbb{E}[e^{(at)X}] = e^{bt} M\_X(at).
   \\]

3. **Suma de variables independientes:** Si \\(X\_1, X\_2, \dots, X\_n\\) son variables aleatorias mutuamente independientes:

   \\[
   M\_{\sum\_{i=1}^n X\_i}(t) = \mathbb{E}\left[e^{t\sum\_{i=1}^n X\_i}\right] = \mathbb{E}\left[\prod\_{i=1}^n e^{t X\_i}\right] = \prod\_{i=1}^n \mathbb{E}[e^{t X\_i}] = \prod\_{i=1}^n M\_{X\_i}(t).
   \\]

   *(La MGF de la suma de variables independientes es el producto de sus MGF individuales).*

**Teorema 4.26 (Teorema de Unicidad de la MGF).** *Si dos variables aleatorias \\(X\\) e \\(Y\\) tienen funciones generadoras de momentos \\(M\_X(t)\\) y \\(M\_Y(t)\\) que existen y coinciden en un intervalo abierto \\((-h, h)\\) alrededor de cero:*

\\[
M\_X(t) = M\_Y(t), \quad \forall t \in (-h, h),
\\]

*entonces \\(X\\) e \\(Y\\) tienen exactamente la misma función de distribución acumulada para todo punto:*

\\[
F\_X(x) = F\_Y(x), \quad \forall x \in \mathbb{R}.
\\]

---

## 4.4.4 Función Generadora de Probabilidad (PGF)

Para variables aleatorias discretas no negativas con soporte en \\(\mathbb{N} = \{0, 1, 2, \dots\}\\), la **función generadora de probabilidad** proporciona un marco analítico en series de potencias complejas.

**Definición 4.27 (PGF).** La **PGF** de una variable discreta entera \\(X \ge 0\\) es:

\\[
G\_X(s) = \mathbb{E}[s^X] = \sum\_{k=0}^{\infty} p\_X(k) s^k, \quad |s| \le 1.
\\]

- **Relación con MGF:** \\(G\_X(e^t) = M\_X(t)\\).
- **Recuperación de probabilidades:** \\(p\_X(k) = \mathbb{P}(X = k) = \frac{1}{k!} G\_X^{(k)}(0)\\).
- **Momentos factoriales:** \\(G\_X'(1) = \mathbb{E}[X]\\), y \\(G\_X''(1) = \mathbb{E}[X(X-1)] \implies \text{Var}(X) = G\_X''(1) + G\_X'(1) - [G\_X'(1)]^2\\).

---

## 4.4.5 Función Característica

Cuando una distribución no posee momentos finitos (como la distribución de Cauchy o Pareto con colas pesadas), la MGF diverge para todo \\(t \neq 0\\). Para garantizar la existencia universal, se utiliza la **función característica** en el plano complejo (la transformada de Fourier de la medida).

**Definición 4.28 (Función Característica).** La **función característica** de una variable aleatoria \\(X\\) es la función \\(\varphi\_X : \mathbb{R} \to \mathbb{C}\\) definida por:

\\[
\varphi\_X(t) = \mathbb{E}[e^{itX}] = \mathbb{E}[\cos(tX)] + i \mathbb{E}[\sin(tX)], \quad \text{donde } i = \sqrt{-1}.
\\]

**Teorema 4.29 (Existencia y acotamiento universal).** *Para **toda** variable aleatoria \\(X\\), la función característica \\(\varphi\_X(t)\\) existe y es uniformemente continua para todo \\(t \in \mathbb{R}\\), con:*

\\[
|\varphi\_X(t)| \le \mathbb{E}[|e^{itX}|] = \mathbb{E}[1] = 1, \qquad \varphi\_X(0) = 1.
\\]

---

## 4.4.6 Tabla Maestra de Funciones Generadoras de Momentos (MGF)

| Distribución | Parámetros | Soporte | MGF: \\(M\_X(t)\\) | Dominio de convergencia |
|---|---|---|---|---|
| **Bernoulli** | \\(p \in [0, 1]\\) | \\(\{0, 1\}\\) | \\((1 - p) + p e^t\\) | \\(t \in \mathbb{R}\\) |
| **Binomial** | \\(n, p\\) | \\(\{0, 1, \dots, n\}\\) | \\([(1 - p) + p e^t]^n\\) | \\(t \in \mathbb{R}\\) |
| **Geométrica** | \\(p \in (0, 1]\\) | \\(\{1, 2, \dots\}\\) | \\(\dfrac{p e^t}{1 - (1 - p) e^t}\\) | \\(t < -\ln(1 - p)\\) |
| **Binomial Negativa** | \\(r, p\\) | \\(\{r, r+1, \dots\}\\) | \\(\left[\dfrac{p e^t}{1 - (1 - p)e^t}\right]^r\\) | \\(t < -\ln(1 - p)\\) |
| **Poisson** | \\(\lambda > 0\\) | \\(\{0, 1, 2, \dots\}\\) | \\(\exp(\lambda(e^t - 1))\\) | \\(t \in \mathbb{R}\\) |
| **Uniforme** | \\(a < b\\) | \\([a, b]\\) | \\(\dfrac{e^{tb} - e^{ta}}{t(b - a)}\\) (con \\(M(0)=1\\)) | \\(t \in \mathbb{R}\\) |
| **Exponencial** | \\(\lambda > 0\\) | \\([0, \infty)\\) | \\(\dfrac{\lambda}{\lambda - t} = \left(1 - \frac{t}{\lambda}\right)^{-1}\\) | \\(t < \lambda\\) |
| **Gamma** | \\(\alpha, \beta\\) | \\((0, \infty)\\) | \\(\left(\dfrac{\beta}{\beta - t}\right)^\alpha = \left(1 - \frac{t}{\beta}\right)^{-\alpha}\\) | \\(t < \beta\\) |
| **Chi-cuadrada** | \\(k \in \mathbb{Z}^+\\) | \\((0, \infty)\\) | \\((1 - 2t)^{-k/2}\\) | \\(t < 1/2\\) |
| **Normal** | \\(\mu, \sigma^2\\) | \\(\mathbb{R}\\) | \\(\exp\left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\\) | \\(t \in \mathbb{R}\\) |
| **Laplace** | \\(\mu, b\\) | \\(\mathbb{R}\\) | \\(\dfrac{e^{\mu t}}{1 - b^2 t^2}\\) | \\(\|t\| < 1/b\\) |
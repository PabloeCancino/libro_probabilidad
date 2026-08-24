# 4.2 Momentos, varianza, covarianza y correlación

## 4.2.1 Momentos ordinarios y momentos centrales

Los momentos son medidas numéricas descriptivas que caracterizan completamente la forma, localización, dispersión y colas de la distribución de probabilidad de una variable aleatoria.

**Definición 4.7 (Momentos de orden $k$).** Sea \\(X\\) una variable aleatoria y sea \\(k \in \mathbb{Z}^+\\).
1. El **momento ordinario (alrededor del origen) de orden \\(k\\)** es:

   \\[
   \alpha\_k = \mathbb{E}[X^k].
   \\]

   (En particular, \\(\alpha\_1 = \mathbb{E}[X] = \mu\\) es la media poblacional).
2. El **momento central de orden \\(k\\)** es:

   \\[
   \mu\_k = \mathbb{E}[(X - \mu)^k].
   \\]

   (Se cumple siempre \\(\mu\_1 = \mathbb{E}[X - \mu] = \mu - \mu = 0\\)).

**Teorema 4.8 (Existencia de momentos inferiores).** *Si \\(\mathbb{E}[|X|^k] < \infty\\) para algún \\(k \ge 1\\), entonces \\(\mathbb{E}[|X|^j] < \infty\\) para todo \\(1 \le j \le k\\).*

*Demostración.*  
Para cualquier \\(x \in \mathbb{R}\\), se tiene \\(|x|^j \le 1 + |x|^k\\) (si \\(|x| \le 1\\), \\(|x|^j \le 1\\); si \\(|x| > 1\\), \\(|x|^j \le |x|^k\\)).  
Por monotonía y linealidad de la esperanza:

\\[
\mathbb{E}[|X|^j] \le \mathbb{E}[1 + |X|^k] = 1 + \mathbb{E}[|X|^k] < \infty. \quad \blacksquare
\\]

---

## 4.2.2 Varianza y desviación estándar

El segundo momento central mide el grado de dispersión o concentración de la masa de probabilidad alrededor de su media \\(\mu\\).

**Definición 4.9 (Varianza y desviación estándar).**
1. La **varianza** de \\(X\\), denotada \\(\text{Var}(X)\\) o \\(\sigma\_X^2\\) o \\(\sigma^2\\), es:

   \\[
   \text{Var}(X) = \mathbb{E}[(X - \mu)^2].
   \\]

2. La **desviación estándar** es la raíz cuadrada no negativa de la varianza:

   \\[
   \sigma\_X = \sqrt{\text{Var}(X)}.
   \\]

**Teorema 4.10 (Fórmula computacional y propiedades operativas de la varianza).**
1. **Fórmula computacional:**

   \\[
   \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2.
   \\]

2. **No negatividad:** \\(\text{Var}(X) \ge 0\\), y \\(\text{Var}(X) = 0 \iff \mathbb{P}(X = c) = 1\\) (la variable es constante casi seguramente).
3. **Invarianza bajo traslaciones y escalamiento:** Para cualesquiera constantes \\(a, b \in \mathbb{R}\\):

   \\[
   \text{Var}(aX + b) = a^2 \text{Var}(X), \qquad \sigma\_{aX + b} = |a| \sigma\_X.
   \\]

*Demostración.*
1. Expandiendo el binomio cuadrático y aplicando la linealidad de la esperanza:

   \\[
   \begin{aligned}
   \text{Var}(X) &= \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2 - 2\mu X + \mu^2] \\\\
   &= \mathbb{E}[X^2] - 2\mu\mathbb{E}[X] + \mu^2 = \mathbb{E}[X^2] - 2\mu^2 + \mu^2 = \mathbb{E}[X^2] - \mu^2.
   \end{aligned}
   \\]

2. \\((X - \mu)^2 \ge 0\\), luego su esperanza es no negativa.
3. \\(\mathbb{E}[aX + b] = a\mu + b\\). Por tanto:

   \\[
   \text{Var}(aX + b) = \mathbb{E}[((aX + b) - (a\mu + b))^2] = \mathbb{E}[(a(X - \mu))^2] = a^2 \mathbb{E}[(X - \mu)^2] = a^2 \text{Var}(X). \quad \blacksquare
   \\]

---

## 4.2.3 Covarianza y varianza de combinaciones lineales

**Definición 4.11 (Covarianza).** La **covarianza** entre dos variables aleatorias \\(X\\) e \\(Y\\), denotada \\(\text{Cov}(X, Y)\\) o \\(\sigma\_{XY}\\), es:

\\[
\text{Cov}(X, Y) = \mathbb{E}[(X - \mu\_X)(Y - \mu\_Y)] = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y].
\\]

### Propiedades algebraicas de la covarianza
1. **Simetría:** \\(\text{Cov}(X, Y) = \text{Cov}(Y, X)\\).
2. **Autocovarianza:** \\(\text{Cov}(X, X) = \text{Var}(X)\\).
3. **Bilinealidad:** Para constantes \\(a, b, c, d \in \mathbb{R}\\):

   \\[
   \text{Cov}(aX + b, \ cY + d) = ac \cdot \text{Cov}(X, Y).
   \\]

4. **Distributividad general:**

   \\[
   \text{Cov}\left(\sum\_{i=1}^n a\_i X\_i, \ \sum\_{j=1}^m b\_j Y\_j\right) = \sum\_{i=1}^n \sum\_{j=1}^m a\_i b\_j \text{Cov}(X\_i, Y\_j).
   \\]

5. **Independencia implica covarianza nula:** Si \\(X \perp Y\\), entonces \\(\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]\\), lo que implica:

   \\[
   \text{Cov}(X, Y) = 0.
   \\]

   *(El recíproco es falso en general: covarianza cero no implica independencia).*

**Teorema 4.12 (Varianza de una combinación lineal).** *Para cualquier colección de variables aleatorias \\(X\_1, \dots, X\_n\\) y constantes \\(a\_1, \dots, a\_n \in \mathbb{R}\\):*

\\[
\text{Var}\left(\sum\_{i=1}^n a\_i X\_i\right) = \sum\_{i=1}^n a\_i^2 \text{Var}(X\_i) + 2 \sum\_{1 \le i < j \le n} a\_i a\_j \text{Cov}(X\_i, X\_j).
\\]

En particular, si las variables son independientes dos a dos (o simplemente no correlacionadas):

\\[
\text{Var}\left(\sum\_{i=1}^n a\_i X\_i\right) = \sum\_{i=1}^n a\_i^2 \text{Var}(X\_i).
\\]

---

## 4.2.4 Coeficiente de correlación lineal de Pearson

**Definición 4.13 (Coeficiente de correlación de Pearson).** Para variables aleatorias \\(X, Y\\) con varianzas positivas finitas \\(\sigma\_X^2, \sigma\_Y^2 > 0\\), el **coeficiente de correlación lineal** es:

\\[
\rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sigma\_X \sigma\_Y} = \frac{\mathbb{E}[(X - \mu\_X)(Y - \mu\_Y)]}{\sqrt{\mathbb{E}[(X-\mu\_X)^2]\mathbb{E}[(Y-\mu\_Y)^2]}}.
\\]

**Teorema 4.14 (Desigualdad de Cauchy-Schwarz para variables aleatorias).** *Para cualesquiera variables aleatorias \\(U, V\\) con segundo momento finito:*

\\[
(\mathbb{E}[UV])^2 \le \mathbb{E}[U^2] \cdot \mathbb{E}[V^2],
\\]

*alcanzándose la igualdad si y solo si existen constantes no ambas nulas tales que \\(\mathbb{P}(aU + bV = 0) = 1\\).*

*Demostración.*  
Para cualquier parámetro real \\(t \in \mathbb{R}\\), la variable aleatoria \\((t U + V)^2 \ge 0\\) casi seguramente.  
Tomando la esperanza y expandiendo por linealidad:

\\[
g(t) = \mathbb{E}[(t U + V)^2] = \mathbb{E}[t^2 U^2 + 2t UV + V^2] = t^2 \mathbb{E}[U^2] + 2t \mathbb{E}[UV] + \mathbb{E}[V^2] \ge 0.
\\]

Como \\(g(t) = A t^2 + B t + C \ge 0\\) es un polinomio cuadrático en \\(t\\) que nunca toma valores negativos, su discriminante \\(\Delta = B^2 - 4AC\\) debe ser menor o igual a cero:

\\[
\Delta = (2\mathbb{E}[UV])^2 - 4 \mathbb{E}[U^2] \mathbb{E}[V^2] \le 0 \implies 4(\mathbb{E}[UV])^2 \le 4\mathbb{E}[U^2]\mathbb{E}[V^2],
\\]

lo que concluye la desigualdad de Cauchy-Schwarz. \\(\blacksquare\\)

**Corolario 4.15 (Propiedades de la correlación de Pearson).**
1. **Acotamiento:** \\(-1 \le \rho(X, Y) \le 1\\).
2. **Relación lineal perfecta:**
   - \\(\rho(X, Y) = 1 \iff Y = aX + b\\) con \\(a > 0\\) casi seguramente (relación lineal creciente perfecta).
   - \\(\rho(X, Y) = -1 \iff Y = aX + b\\) con \\(a < 0\\) casi seguramente (relación lineal decreciente perfecta).
3. **Invarianza de escala:** \\(\rho(aX + b, \ cY + d) = \text{signo}(ac) \cdot \rho(X, Y)\\).

---

## 4.2.5 Momentos de orden superior: Asimetría y Curtosis

1. **Coeficiente de Asimetría (Skewness - \\(\gamma\_1\\)):**

   \\[
   \gamma\_1 = \frac{\mu\_3}{\sigma^3} = \frac{\mathbb{E}[(X - \mu)^3]}{\sigma^3}.
   \\]

   - \\(\gamma\_1 = 0\\): Distribución simétrica (como la Normal o Uniforme).
   - \\(\gamma\_1 > 0\\): Asimetría positiva (cola larga a la derecha, como la Exponencial).
   - \\(\gamma\_1 < 0\\): Asimetría negativa (cola larga a la izquierda).

2. **Coeficiente de Curtosis (Exceso de curtosis - \\(\gamma\_2\\)):**

   \\[
   \gamma\_2 = \frac{\mu\_4}{\sigma^4} - 3 = \frac{\mathbb{E}[(X - \mu)^4]}{\sigma^4} - 3.
   \\]

   - \\(\gamma\_2 = 0\\): Mesocúrtica (idéntica a la Normal).
   - \\(\gamma\_2 > 0\\): Leptocúrtica (colas pesadas, pico agudo, como la \\(t\\)-Student y Laplace).
   - \\(\gamma\_2 < 0\\): Platicúrtica (colas ligeras, más aplanada, como la Uniforme).
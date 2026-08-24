# 3.4 Familias de distribuciones discretas fundamentales

Presentamos el tratamiento matemático formal de las familias de distribuciones de probabilidad discretas estándar, deduciendo para cada una de ellas su soporte, función de masa (PMF), parámetros, media, varianza e interpretación estocástica.

---

## 3.4.1 Distribución Uniforme Discreta

Modela un experimento con \\(k\\) resultados posibles que tienen exactamente la misma probabilidad de ocurrir.

- **Parámetros:** Enteros \\(a, b \in \mathbb{Z}\\) con \\(a \le b\\), donde \\(k = b - a + 1\\).
- **Notación:** \\(X \sim \mathcal{U}\{a, b\}\\).
- **Soporte:** \\(S\_X = \{a, a+1, \dots, b\}\\).
- **Función de masa (PMF):**

  \\[
  p\_X(x) = \frac{1}{b - a + 1} = \frac{1}{k}, \quad \forall x \in S\_X.
  \\]

- **Esperanza y Varianza:**

  \\[
  \mathbb{E}[X] = \frac{a + b}{2}, \qquad \text{Var}(X) = \frac{(b - a + 1)^2 - 1}{12} = \frac{k^2 - 1}{12}.
  \\]

---

## 3.4.2 Distribución Bernoulli

Modela un ensayo dicotómico único con dos resultados posibles: "Éxito" (\\(X=1\\)) con probabilidad \\(p\\), y "Fracaso" (\\(X=0\\)) con probabilidad \\(q = 1 - p\\).

- **Parámetro:** Probabilidad de éxito \\(p \in [0, 1]\\).
- **Notación:** \\(X \sim \text{Bernoulli}(p)\\).
- **Soporte:** \\(S\_X = \{0, 1\}\\).
- **Función de masa (PMF):**

  \\[
  p\_X(x) = p^x (1 - p)^{1 - x}, \quad x \in \{0, 1\}.
  \\]

- **Esperanza y Varianza:**

  \\[
  \mathbb{E}[X] = 0 \cdot (1-p) + 1 \cdot p = p,
  \\]

  \\[
  \mathbb{E}[X^2] = 0^2(1-p) + 1^2 p = p \implies \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 = p - p^2 = p(1 - p).
  \\]

---

## 3.4.3 Distribución Binomial

Modela el número total de éxitos obtenidos en una secuencia de \\(n\\) ensayos Bernoulli idénticos e **independientes**, cada uno con probabilidad constante de éxito \\(p\\).

- **Parámetros:** \\(n \in \mathbb{Z}^+\\) (número de ensayos), \\(p \in [0, 1]\\) (probabilidad de éxito).
- **Notación:** \\(X \sim \text{Binomial}(n, p)\\).
- **Soporte:** \\(S\_X = \{0, 1, 2, \dots, n\}\\).
- **Función de masa (PMF):**

  \\[
  p\_X(k) = \mathbb{P}(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k \in \{0, 1, \dots, n\}.
  \\]

**Verificación de la normalización:** Por el Teorema del Binomio de Newton:

\\[
\sum\_{k=0}^n p\_X(k) = \sum\_{k=0}^n \binom{n}{k} p^k (1-p)^{n-k} = (p + (1 - p))^n = 1^n = 1.
\\]

**Deducción de la Esperanza y Varianza:**  
Dado que \\(X = \sum\_{i=1}^n Y\_i\\), donde \\(Y\_i \stackrel{\text{i.i.d.}}{\sim} \text{Bernoulli}(p)\\):

\\[
\mathbb{E}[X] = \mathbb{E}\left[\sum\_{i=1}^n Y\_i\right] = \sum\_{i=1}^n \mathbb{E}[Y\_i] = \sum\_{i=1}^n p = np.
\\]

Por independencia de los ensayos:

\\[
\text{Var}(X) = \text{Var}\left(\sum\_{i=1}^n Y\_i\right) = \sum\_{i=1}^n \text{Var}(Y\_i) = \sum\_{i=1}^n p(1-p) = np(1 - p).
\\]

---

## 3.4.4 Distribución Geométrica

Modela el número de ensayos Bernoulli independientes requeridos hasta observar el **primer éxito**.

- **Parámetro:** \\(p \in (0, 1]\\).
- **Notación:** \\(X \sim \text{Geométrica}(p)\\).
- **Soporte:** \\(S\_X = \{1, 2, 3, \dots\}\\) (versión que cuenta el número de intentos totales).
- **Función de masa (PMF):**

  \\[
  p\_X(k) = (1 - p)^{k - 1} p, \quad k \in \{1, 2, 3, \dots\}.
  \\]

- **Función de distribución acumulada (CDF):**

  \\[
  F\_X(k) = \mathbb{P}(X \le k) = 1 - \mathbb{P}(X > k) = 1 - (1 - p)^k, \quad k \ge 1.
  \\]

- **Esperanza y Varianza:**

  \\[
  \mathbb{E}[X] = \frac{1}{p}, \qquad \text{Var}(X) = \frac{1 - p}{p^2}.
  \\]

**Teorema 3.21 (Falta de memoria discreta).** *La distribución geométrica es la única distribución discreta con soporte en \\(\mathbb{Z}^+\\) que satisface la propiedad de falta de memoria:*

\\[
\mathbb{P}(X > m + n \mid X > m) = \mathbb{P}(X > n), \quad \forall m, n \in \mathbb{Z}^+.
\\]

*Demostración.*

\\[
\mathbb{P}(X > m + n \mid X > m) = \frac{\mathbb{P}(X > m + n \text{ y } X > m)}{\mathbb{P}(X > m)} = \frac{\mathbb{P}(X > m + n)}{\mathbb{P}(X > m)} = \frac{(1 - p)^{m + n}}{(1 - p)^m} = (1 - p)^n = \mathbb{P}(X > n). \quad \blacksquare
\\]

---

## 3.4.5 Distribución Binomial Negativa (Pascal)

Modela el número de ensayos Bernoulli independientes \\(X\\) necesarios para acumular exactamente \\(r\\) éxitos.

- **Parámetros:** \\(r \in \mathbb{Z}^+\\) (éxitos requeridos), \\(p \in (0, 1]\\).
- **Notación:** \\(X \sim \text{BN}(r, p)\\).
- **Soporte:** \\(S\_X = \{r, r+1, r+2, \dots\}\\).
- **Función de masa (PMF):**  
  Para que el \\(r\\)-ésimo éxito ocurra en el intento \\(k\\), debe haber exactamente \\(r-1\\) éxitos en los primeros \\(k-1\\) intentos y un éxito en el intento \\(k\\):

  \\[
  p\_X(k) = \binom{k - 1}{r - 1} p^r (1 - p)^{k - r}, \quad k \ge r.
  \\]

- **Esperanza y Varianza:** (Como suma de \\(r\\) variables geométricas independientes):

  \\[
  \mathbb{E}[X] = \frac{r}{p}, \qquad \text{Var}(X) = \frac{r(1 - p)}{p^2}.
  \\]

---

## 3.4.6 Distribución Hipergeométrica

Modela el número de éxitos \\(k\\) obtenidos en una muestra de tamaño \\(n\\) extraída **sin reemplazo** de una población finita de tamaño \\(N\\) que contiene exactamente \\(K\\) elementos con la característica de éxito.

- **Parámetros:** \\(N \in \mathbb{Z}^+\\) (tamaño poblacional), \\(K \in \{0, 1, \dots, N\}\\) (éxitos en la población), \\(n \in \{1, \dots, N\}\\) (tamaño muestral).
- **Notación:** \\(X \sim \text{Hipergeométrica}(N, K, n)\\).
- **Soporte:** \\(S\_X = \{\max(0, n - (N - K)), \dots, \min(n, K)\}\\).
- **Función de masa (PMF):**

  \\[
  p\_X(k) = \frac{\binom{K}{k}\binom{N - K}{n - k}}{\binom{N}{n}}.
  \\]

- **Esperanza y Varianza:**

  \\[
  \mathbb{E}[X] = n \frac{K}{N} = n p, \qquad \text{donde } p = \frac{K}{N},
  \\]

  \\[
  \text{Var}(X) = n p (1 - p) \left(\frac{N - n}{N - 1}\right).
  \\]

  (El factor \\(\frac{N - n}{N - 1}\\) se denomina **factor de corrección por población finita**; cuando \\(N \to \infty\\), la distribución Hipergeométrica converge a la Binomial).

---

## 3.4.7 Distribución de Poisson

Modela el número de eventos raros que ocurren en un intervalo continuo fijo (tiempo, área o volumen), bajo una tasa media constante de ocurrencia \\(\lambda > 0\\).

- **Parámetro:** Tasa media \\(\lambda > 0\\).
- **Notación:** \\(X \sim \text{Poisson}(\lambda)\\).
- **Soporte:** \\(S\_X = \{0, 1, 2, \dots\} = \mathbb{N}\\).
- **Función de masa (PMF):**

  \\[
  p\_X(k) = \frac{e^{-\lambda} \lambda^k}{k!}, \quad k \in \mathbb{N}.
  \\]

**Verificación de la normalización:**

\\[
\sum\_{k=0}^\infty \frac{e^{-\lambda} \lambda^k}{k!} = e^{-\lambda} \sum\_{k=0}^\infty \frac{\lambda^k}{k!} = e^{-\lambda} e^\lambda = 1.
\\]

**Teorema 3.22 (Ley de eventos raros de Poisson).** *Si \\(X\_n \sim \text{Binomial}(n, p\_n)\\) donde \\(n \to \infty\\) y \\(p\_n \to 0\\) de forma tal que \\(n p\_n \to \lambda > 0\\), entonces para todo \\(k \in \mathbb{N}\\) fijo:*

\\[
\lim\_{n \to \infty} \mathbb{P}(X\_n = k) = \frac{e^{-\lambda} \lambda^k}{k!}.
\\]

*Demostración analítica.*  
Escribiendo la PMF binomial con \\(p = \frac{\lambda}{n}\\):

\\[
\begin{aligned}
\mathbb{P}(X\_n = k) &= \frac{n(n-1)\cdots(n-k+1)}{k!} \left(\frac{\lambda}{n}\right)^k \left(1 - \frac{\lambda}{n}\right)^{n-k} \\\\
&= \frac{\lambda^k}{k!} \left[\frac{n(n-1)\cdots(n-k+1)}{n^k}\right] \left(1 - \frac{\lambda}{n}\right)^n \left(1 - \frac{\lambda}{n}\right)^{-k}.
\end{aligned}
\\]

Tomando el límite cuando \\(n \to \infty\\) para \\(k\\) fijo:
- \\(\lim\_{n \to \infty} \frac{n(n-1)\cdots(n-k+1)}{n^k} = 1\\).
- \\(\lim\_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^n = e^{-\lambda}\\) (límite clásico de Euler).
- \\(\lim\_{n \to \infty} \left(1 - \frac{\lambda}{n}\right)^{-k} = 1^{-k} = 1\\).

Multiplicando los límites:

\\[
\lim\_{n \to \infty} \mathbb{P}(X\_n = k) = \frac{\lambda^k}{k!} \cdot 1 \cdot e^{-\lambda} \cdot 1 = \frac{e^{-\lambda}\lambda^k}{k!}. \quad \blacksquare
\\]

**Esperanza y Varianza de Poisson:**

\\[
\mathbb{E}[X] = \sum\_{k=0}^\infty k \frac{e^{-\lambda} \lambda^k}{k!} = \lambda e^{-\lambda} \sum\_{k=1}^\infty \frac{\lambda^{k-1}}{(k-1)!} = \lambda e^{-\lambda} e^\lambda = \lambda.
\\]

\\[
\mathbb{E}[X(X-1)] = \sum\_{k=2}^\infty k(k-1)\frac{e^{-\lambda}\lambda^k}{k!} = \lambda^2 e^{-\lambda}\sum\_{k=2}^\infty \frac{\lambda^{k-2}}{(k-2)!} = \lambda^2.
\\]

\\[
\text{Var}(X) = \mathbb{E}[X(X-1)] + \mathbb{E}[X] - (\mathbb{E}[X])^2 = \lambda^2 + \lambda - \lambda^2 = \lambda.
\\]

(Propiedad distintiva: para la distribución Poisson, **media y varianza son exactamente iguales a \\(\lambda\\)**).

---

## 3.4.8 Distribución Multinomial

Generalización multivariada de la distribución Binomial a \\(k\\) posibles categorías excluyentes con probabilidades \\(\mathbf{p} = (p\_1, \dots, p\_k)\\) tales que \\(\sum\_{i=1}^k p\_i = 1\\) en \\(n\\) ensayos independientes.

- **PMF Conjunta:** Para \\(\mathbf{x} = (x\_1, \dots, x\_k)\\) con \\(x\_i \in \mathbb{N}\\) y \\(\sum\_{i=1}^k x\_i = n\\):

  \\[
  p\_{\mathbf{X}}(x\_1, \dots, x\_k) = \frac{n!}{x\_1! x\_2! \cdots x\_k!} p\_1^{x\_1} p\_2^{x\_2} \cdots p\_k^{x\_k}.
  \\]

- **Marginales:** Cada componente individual es binomial: \\(X\_i \sim \text{Binomial}(n, p\_i)\\).
- **Covarianza entre categorías:** \\(\text{Cov}(X\_i, X\_j) = -n p\_i p\_j\\) para \\(i \neq j\\).
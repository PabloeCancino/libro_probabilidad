# 5.3 Ley Débil y Fuerte de los Grandes Números

## 5.3.1 La media muestral y el promedio de variables aleatorias

Sea \\((X\_n)\_{n=1}^\infty\\) una sucesión de variables aleatorias independientes e idénticamente distribuidas (**i.i.d.**) en un espacio de probabilidad \\((\Omega, \mathcal{F}, \mathbb{P})\\), con media común \\(\mathbb{E}[X\_i] = \mu\\).

**Definición 5.15 (Media muestral).** La **media muestral** de las primeras \\(n\\) observaciones es el promedio aritmético:

\\[
\bar{X}\_n = \frac{1}{n} \sum\_{i=1}^n X\_i = \frac{S\_n}{n}.
\\]

Por la linealidad de la esperanza:

\\[
\mathbb{E}[\bar{X}\_n] = \frac{1}{n} \sum\_{i=1}^n \mathbb{E}[X\_i] = \frac{n\mu}{n} = \mu.
\\]

Si además las variables tienen varianza común finita \\(\text{Var}(X\_i) = \sigma^2 < \infty\\), por la independencia de los ensayos:

\\[
\text{Var}(\bar{X}\_n) = \text{Var}\left(\frac{1}{n}\sum\_{i=1}^n X\_i\right) = \frac{1}{n^2} \sum\_{i=1}^n \text{Var}(X\_i) = \frac{n\sigma^2}{n^2} = \frac{\sigma^2}{n}.
\\]

Nótese que la varianza de la media muestral decae a cero como \\(\mathcal{O}(1/n)\\), lo que anticipa la concentración asintótica de \\(\bar{X}\_n\\) alrededor de \\(\mu\\).

---

## 5.3.2 La Ley Débil de los Grandes Números (WLLN)

La Ley Débil establece que la probabilidad de observar cualquier desviación entre el promedio empírico \\(\bar{X}\_n\\) y la media teórica \\(\mu\\) se anula cuando el tamaño muestral \\(n\\) tiende a infinito.

**Teorema 5.16 (Ley Débil de los Grandes Números - Versión de Chebyshev con varianza finita).** *Sea \\((X\_n)\_{n=1}^\infty\\) una sucesión de variables aleatorias independientes e idénticamente distribuidas con media \\(\mu\\) y varianza finita \\(\sigma^2 < \infty\\). Entonces \\(\bar{X}\_n\\) converge en probabilidad a \\(\mu\\):*

\\[
\bar{X}\_n \xrightarrow{P} \mu, \quad \text{es decir, } \lim\_{n \to \infty} \mathbb{P}(|\bar{X}\_n - \mu| > \epsilon) = 0, \quad \forall \epsilon > 0.
\\]

*Demostración analítica.*  
Aplicamos la desigualdad de Chebyshev (Teorema 5.2) a la variable \\(\bar{X}\_n\\), cuya media es \\(\mu\\) y cuya varianza es \\(\sigma^2 / n\\):

\\[
\mathbb{P}(|\bar{X}\_n - \mu| \ge \epsilon) \le \frac{\text{Var}(\bar{X}\_n)}{\epsilon^2} = \frac{\sigma^2}{n \epsilon^2}.
\\]

Tomando el límite cuando \\(n \to \infty\\) para cualquier \\(\epsilon > 0\\) constante fijo:

\\[
0 \le \lim\_{n \to \infty} \mathbb{P}(|\bar{X}\_n - \mu| \ge \epsilon) \le \lim\_{n \to \infty} \frac{\sigma^2}{n \epsilon^2} = 0.
\\]

Por el teorema del sándwich, \\(\lim\_{n \to \infty} \mathbb{P}(|\bar{X}\_n - \mu| > \epsilon) = 0\\), lo que concluye que \\(\bar{X}\_n \xrightarrow{P} \mu\\). \\(\blacksquare\\)

**Teorema 5.17 (Ley Débil de Khinchin).** *Si \\((X\_n)\_{n=1}^\infty\\) son i.i.d. con \\(\mathbb{E}[|X\_i|] < \infty\\) y media \\(\mu\\) (sin requerir varianza finita), entonces \\(\bar{X}\_n \xrightarrow{P} \mu\\).*

*Demostración.* Se deduce mediante la expansión de Taylor de la función característica \\(\varphi\_X(t) = 1 + i\mu t + o(t)\\) y el Teorema de Continuidad de Lévy. \\(\blacksquare\\)

---

## 5.3.3 La Ley Fuerte de los Grandes Números (SLLN)

La Ley Fuerte es un resultado mucho más profundo y contundente: afirma que con probabilidad 1, la trayectoria empírica de promedios \\(\bar{X}\_n(\omega)\\) converge punto a punto a \\(\mu\\).

**Teorema 5.18 (Ley Fuerte de los Grandes Números - Teorema de Kolmogórov, 1930).** *Sea \\((X\_n)\_{n=1}^\infty\\) una sucesión de variables aleatorias independientes e idénticamente distribuidas. La existencia de una constante \\(\mu\\) tal que:*

\\[
\bar{X}\_n \xrightarrow{\text{c.s.}} \mu \quad \left(\mathbb{P}\left(\lim\_{n \to \infty} \frac{1}{n}\sum\_{i=1}^n X\_i = \mu\right) = 1\right),
\\]

*es posible si y solo si \\(\mathbb{E}[|X\_1|] < \infty\\), en cuyo caso \\(\mu = \mathbb{E}[X\_1]\\).*

*Demostración (para el caso con cuarto momento finito \\(\mathbb{E}[X\_i^4] < \infty\\)).*  
Sin pérdida de generalidad supongamos \\(\mu = 0\\).  
Expandiendo \\(S\_n^4 = \left(\sum\_{i=1}^n X\_i\right)^4\\) y tomando esperanza:

\\[
\mathbb{E}[S\_n^4] = \sum\_{i=1}^n \mathbb{E}[X\_i^4] + 6 \sum\_{1 \le i < j \le n} \mathbb{E}[X\_i^2 X\_j^2] = n \mathbb{E}[X\_1^4] + 6 \binom{n}{2} (\sigma^2)^2 \le C n^2.
\\]

Por tanto:

\\[
\mathbb{E}[\bar{X}\_n^4] = \frac{\mathbb{E}[S\_n^4]}{n^4} \le \frac{C n^2}{n^4} = \frac{C}{n^2}.
\\]

Por la desigualdad de Márkov:

\\[
\mathbb{P}(|\bar{X}\_n| > \epsilon) = \mathbb{P}(\bar{X}\_n^4 > \epsilon^4) \le \frac{\mathbb{E}[\bar{X}\_n^4]}{\epsilon^4} \le \frac{C}{\epsilon^4 n^2}.
\\]

Como la serie numérica \\(\sum\_{n=1}^\infty \frac{1}{n^2} < \infty\\) converge, se tiene:

\\[
\sum\_{n=1}^\infty \mathbb{P}(|\bar{X}\_n| > \epsilon) < \infty.
\\]

Por el **Primer Lema de Borel-Cantelli** (Apéndice A), la probabilidad de que \\(|\bar{X}\_n| > \epsilon\\) ocurra infinitas veces es 0. Por ende, \\(\bar{X}\_n \xrightarrow{\text{c.s.}} 0\\). \\(\blacksquare\\)

---

## 5.3.4 Fundamentación de la interpretación frecuentista y Métodos de Monte Carlo

Sea \\(A \in \mathcal{F}\\) un evento arbitrario con probabilidad \\(p = \mathbb{P}(A)\\).  
Consideremos una sucesión de repeticiones independientes del experimento y definamos las variables indicadoras \\(I\_n = \mathbb{I}\_A^{(n)} \stackrel{\text{i.i.d.}}{\sim} \text{Bernoulli}(p)\\).  
La **frecuencia relativa** observada del evento \\(A\\) en las primeras \\(n\\) repeticiones es:

\\[
f\_n(A) = \frac{n\_A}{n} = \frac{1}{n}\sum\_{i=1}^n I\_i.
\\]

Por la Ley Fuerte de los Grandes Números (Teorema 5.18):

\\[
f\_n(A) \xrightarrow{\text{c.s.}} \mathbb{E}[I\_1] = \mathbb{P}(A).
\\]

> **Trascendencia filosófica y metodológica:** La definición intuitiva frecuentista de la probabilidad como el límite de las frecuencias relativas ya no es un postulado informal ad-hoc, sino un **teorema matemático rigurosamente demostrado** a partir de los axiomas de Kolmogórov.

---

## 5.3.5 Laboratorio en Python: Visualización de la Ley Fuerte
```python
import numpy as np
import matplotlib.pyplot as plt

def simular_ley_grandes_numeros(n_ensayos=10_000, n_trayectorias=5):
    """Simula trayectorias de la media muestral para ilustrar la SLLN."""
    np.random.seed(42)
    # Ensayos con distribucion Exponencial(lambda=0.5) -> Media mu = 2.0
    mu_teorica = 2.0
    
    plt.figure(figsize=(10, 5))
    for tray in range(n_trayectorias):
        muestras = np.random.exponential(scale=mu_teorica, size=n_ensayos)
        medias_acumuladas = np.cumsum(muestras) / np.arange(1, n_ensayos + 1)
        plt.plot(medias_acumuladas, lw=1.2, alpha=0.8, label=f'Trayectoria {tray+1}' if tray==0 else "")
        
    plt.axhline(mu_teorica, color='red', linestyle='--', lw=2, label=r'Media teórica $\mu = 2.0$')
    plt.title('Ley Fuerte de los Grandes Números (SLLN): Convergencia de $\\bar{X}_n \\xrightarrow{c.s.} \\mu$')
    plt.xlabel('Número de observaciones ($n$)')
    plt.ylabel('Media muestral $\\bar{X}_n$')
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.show()

# simular_ley_grandes_numeros()
```
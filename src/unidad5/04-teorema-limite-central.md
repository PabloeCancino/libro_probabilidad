# 5.4 El Teorema del Límite Central

## 5.4.1 Enunciado del Teorema del Límite Central (Lindeberg-Lévy)

El **Teorema del Límite Central (TLC)** es considerado el resultado cumbre de la probabilidad clásica y uno de los mayores logros del análisis matemático: explica por qué la distribución Normal (Gaussiana) emerge de manera omnipresente en la naturaleza, la física, la biología, las ciencias sociales y la ingeniería cada vez que un fenómeno es el resultado agregado de una multitud de pequeñas fluctuaciones aleatorias independientes.

Mientras que la Ley de los Grandes Números nos dice que la masa de \\(\bar{X}_n\\) colapsa en el punto \\(\mu\\), el Teorema del Límite Central describe la **forma geométrica exacta** de las fluctuaciones estocásticas a escala \\(1/\sqrt{n}\\).

**Teorema 5.19 (Teorema del Límite Central de Lindeberg-Lévy, 1920).** *Sea \\((X_n)_{n=1}^\infty\\) una sucesión de variables aleatorias independientes e idénticamente distribuidas (i.i.d.) con media común \\(\mathbb{E}[X_i] = \mu\\) y varianza común finita \\(0 < \text{Var}(X_i) = \sigma^2 < \infty\\).*  
*Definamos la variable estandarizada de la suma \\(S_n = \sum_{i=1}^n X_i\\) (o de la media muestral \\(\bar{X}_n = S_n / n\\)):*
\\[ Z_n = \frac{S_n - n\mu}{\sigma \sqrt{n}} = \frac{\bar{X}_n - \mu}{\sigma / \sqrt{n}}. \\]
*Entonces \\(Z_n\\) converge en distribución a una variable Normal estándar \\(\mathcal{N}(0, 1)\\):*
\\[ Z_n \xrightarrow{d} \mathcal{N}(0, 1), \\]
*es decir, para todo \\(z \in \mathbb{R}\\):*
\\[ \lim_{n \to \infty} \mathbb{P}(Z_n \le z) = \Phi(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-u^2 / 2} \, du. \\]

---

## 5.4.2 Demostración analítica rigurosa del TLC mediante MGF

*Demostración.*  
Sin pérdida de generalidad, consideremos las variables centradas \\(Y_i = \frac{X_i - \mu}{\sigma}\\).  
Entonces las \\(Y_i\\) son i.i.d. con:
\\[ \mathbb{E}[Y_i] = 0, \qquad \text{Var}(Y_i) = \mathbb{E}[Y_i^2] = 1. \\]
La variable normalizada \\(Z_n\\) se expresa como:
\\[ Z_n = \frac{1}{\sqrt{n}} \sum_{i=1}^n Y_i. \\]
Supongamos que la MGF común \\(M_Y(t)\\) existe en un entorno de cero \\((-h, h)\\).  
Por el Teorema de Taylor, la expansión de Maclaurin de \\(M_Y(t)\\) hasta segundo orden es:
\\[ M_Y(t) = M_Y(0) + M_Y'(0) t + \frac{1}{2!} M_Y''(0) t^2 + o(t^2) = 1 + 0 \cdot t + \frac{1}{2}(1) t^2 + o(t^2) = 1 + \frac{t^2}{2} + o(t^2). \\]
Por las propiedades de la MGF de sumas de variables independientes y escalamiento (Teorema 4.25):
\\[ M_{Z_n}(t) = M_{\sum_{i=1}^n Y_i / \sqrt{n}}(t) = \left[ M_Y\left(\frac{t}{\sqrt{n}}\right) \right]^n. \\]
Sustituyendo el desarrollo de Taylor en \\(t/\sqrt{n}\\):
\\[ M_{Z_n}(t) = \left[ 1 + \frac{(t/\sqrt{n})^2}{2} + o\left(\frac{t^2}{n}\right) \right]^n = \left[ 1 + \frac{t^2 / 2 + n \cdot o(t^2 / n)}{n} \right]^n. \\]
Tomando el límite cuando \\(n \to \infty\\) para cualquier \\(t \in \mathbb{R}\\) fijo, y recordando el límite clásico \\(\lim_{n \to \infty} (1 + a_n / n)^n = e^a\\) si \\(a_n \to a\\):
\\[ \lim_{n \to \infty} M_{Z_n}(t) = \lim_{n \to \infty} \left(1 + \frac{t^2 / 2}{n}\right)^n = \exp\left(\frac{t^2}{2}\right). \\]
Observemos que \\(\exp(t^2/2)\\) es precisamente la **función generadora de momentos de la distribución Normal estándar \\(\mathcal{N}(0, 1)\\)**.  
Por el **Teorema de Continuidad y Unicidad de Lévy-Cramér**, la convergencia de las funciones generadoras implica la convergencia en distribución de las funciones de distribución acumulada:
\\[ Z_n \xrightarrow{d} \mathcal{N}(0, 1). \quad \blacksquare \\]

*(Nota técnica: Cuando la MGF no existe en un entorno real, la misma demostración se realiza de manera idéntica utilizando la función característica \\(\varphi_Y(t) = 1 - \frac{t^2}{2} + o(t^2)\\), garantizando la validez universal del teorema para cualquier distribución con segundo momento finito).*

---

## 5.4.3 Generalizaciones: Condiciones de Lyapunov y Lindeberg

Cuando las variables \\(X_i\\) son independientes pero **no idénticamente distribuidas** (con medias \\(\mu_i\\) y varianzas \\(\sigma_i^2\\)), sea \\(s_n^2 = \sum_{i=1}^n \sigma_i^2\\).

**Teorema 5.20 (Condición de Lindeberg).** *Si para todo \\(\epsilon > 0\\):*
\\[ \lim_{n \to \infty} \frac{1}{s_n^2} \sum_{i=1}^n \mathbb{E}\left[(X_i - \mu_i)^2 \cdot \mathbb{I}_{(|X_i - \mu_i| > \epsilon s_n)}\right] = 0, \\]
*entonces:*
\\[ \frac{\sum_{i=1}^n (X_i - \mu_i)}{s_n} \xrightarrow{d} \mathcal{N}(0, 1). \\]

---

## 5.4.4 Aplicaciones prácticas fundamentales del TLC

### 1. Aproximación Normal a la Binomial (Teorema de De Moivre-Laplace)
Si \\(X \sim \text{Binomial}(n, p)\\), como \\(X = \sum_{i=1}^n Y_i\\) con \\(Y_i \stackrel{\text{i.i.d.}}{\sim} \text{Bernoulli}(p)\\), para \\(n\\) grande (típicamente \\(np \ge 5\\) y \\(n(1-p) \ge 5\\)):
\\[ X \approx \mathcal{N}(\mu = np, \ \sigma^2 = np(1-p)). \\]

**Corrección por continuidad (de Yates):** Dado que aproximamos una variable discreta entera mediante una densidad continua, la probabilidad puntual \\(\mathbb{P}(X = k)\\) se aproxima por el intervalo continuo \\([k - 0.5, k + 0.5]\\):
\\[ \mathbb{P}(a \le X \le b) \approx \mathbb{P}\left(\frac{(a - 0.5) - np}{\sqrt{np(1-p)}} \le Z \le \frac{(b + 0.5) - np}{\sqrt{np(1-p)}}\right). \\]

### 2. Aproximación Normal a la distribución de Poisson
Si \\(X \sim \text{Poisson}(\lambda)\\), para \\(\lambda \ge 15\\):
\\[ X \approx \mathcal{N}(\mu = \lambda, \ \sigma^2 = \lambda). \\]

---

## 5.4.5 Laboratorio en Python: Verificación empírica del TLC con distribuciones sesgadas

```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

def demostrar_tlc(distribucion='exponencial', tamanios_n=[1, 2, 5, 30, 100], n_sims=50_000):
    """Ilustra el Teorema del Limite Central a partir de poblaciones asimetricas."""
    plt.figure(figsize=(14, 8))
    
    for idx, n in enumerate(tamanios_n, 1):
        if distribucion == 'exponencial':
            # Poblacion Exponencial(lambda=1): muy asimetrica
            muestras = np.random.exponential(scale=1.0, size=(n_sims, n))
            mu, sigma = 1.0, 1.0
        elif distribucion == 'uniforme':
            muestras = np.random.uniform(0, 1, size=(n_sims, n))
            mu, sigma = 0.5, np.sqrt(1/12)
            
        medias = np.mean(muestras, axis=1)
        z_scores = (medias - mu) / (sigma / np.sqrt(n))
        
        plt.subplot(2, 3, idx)
        plt.hist(z_scores, bins=60, density=True, alpha=0.6, color='steelblue', edgecolor='black', lw=0.5)
        
        # Curva Normal Estandar teorica N(0,1)
        x_grid = np.linspace(-4, 4, 200)
        plt.plot(x_grid, stats.norm.pdf(x_grid), 'r-', lw=2, label=r'$\mathcal{N}(0,1)$')
        plt.title(f'$n = {n}$ observaciones')
        plt.xlabel(r'$Z_n$')
        plt.xlim(-4, 4)
        if idx == 1:
            plt.legend()
            
    plt.suptitle(f'Convergencia del Teorema del Límite Central (Base: {distribucion.capitalize()})', fontsize=14)
    plt.tight_layout()
    plt.show()

# demostrar_tlc('exponencial')
```

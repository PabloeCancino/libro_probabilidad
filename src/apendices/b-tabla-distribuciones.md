# Apéndice B. Tabla sinóptica de distribuciones de probabilidad

## B.1 Distribuciones Discretas

| Distribución | Notación y Parámetros | Soporte \\(S_X\\) | PMF: \\(p_X(k) = \mathbb{P}(X = k)\\) | Esperanza \\(\mathbb{E}[X]\\) | Varianza \\(\text{Var}(X)\\) | Función Generadora \\(M_X(t)\\) |
|---|---|---|---|---|---|---|
| **Uniforme discreta** | \\(\mathcal{U}\{a, b\}\\), \\(k = b - a + 1\\) | \\(\{a, a+1, \dots, b\}\\) | \\(\dfrac{1}{k}\\) | \\(\dfrac{a + b}{2}\\) | \\(\dfrac{k^2 - 1}{12}\\) | \\(\dfrac{e^{at}(1 - e^{kt})}{k(1 - e^t)}\\) |
| **Bernoulli** | \\(\text{Bernoulli}(p)\\), \\(p \in [0, 1]\\) | \\(\{0, 1\}\\) | \\(p^k (1 - p)^{1 - k}\\) | \\(p\\) | \\(p(1 - p)\\) | \\((1 - p) + p e^t\\) |
| **Binomial** | \\(\text{Binomial}(n, p)\\), \\(n \in \mathbb{Z}^+, \ p \in [0,1]\\) | \\(\{0, 1, \dots, n\}\\) | \\(\dbinom{n}{k} p^k (1 - p)^{n - k}\\) | \\(np\\) | \\(np(1 - p)\\) | \\([(1 - p) + p e^t]^n\\) |
| **Geométrica** | \\(\text{Geométrica}(p)\\), \\(p \in (0, 1]\\) | \\(\{1, 2, 3, \dots\}\\) | \\((1 - p)^{k - 1} p\\) | \\(\dfrac{1}{p}\\) | \\(\dfrac{1 - p}{p^2}\\) | \\(\dfrac{p e^t}{1 - (1 - p)e^t}\\) |
| **Binomial Negativa** | \\(\text{BN}(r, p)\\), \\(r \in \mathbb{Z}^+, \ p \in (0,1]\\) | \\(\{r, r+1, \dots\}\\) | \\(\dbinom{k - 1}{r - 1} p^r (1 - p)^{k - r}\\) | \\(\dfrac{r}{p}\\) | \\(\dfrac{r(1 - p)}{p^2}\\) | \\(\left[\dfrac{p e^t}{1 - (1 - p)e^t}\right]^r\\) |
| **Hipergeométrica** | \\(\text{Hiper}(N, K, n)\\) | \\(\{\max(0, n-N+K), \dots, \min(n,K)\}\\) | \\(\dfrac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}\\) | \\(n \dfrac{K}{N}\\) | \\(n \dfrac{K}{N}\left(1 - \dfrac{K}{N}\right)\left(\dfrac{N-n}{N-1}\right)\\) | *(Forma hipergeométrica)* |
| **Poisson** | \\(\text{Poisson}(\lambda)\\), \\(\lambda > 0\\) | \\(\{0, 1, 2, \dots\}\\) | \\(\dfrac{e^{-\lambda} \lambda^k}{k!}\\) | \\(\lambda\\) | \\(\lambda\\) | \\(\exp(\lambda(e^t - 1))\\) |

---

## B.2 Distribuciones Continuas

| Distribución | Notación y Parámetros | Soporte \\(S_X\\) | PDF: \\(f_X(x)\\) | Esperanza \\(\mathbb{E}[X]\\) | Varianza \\(\text{Var}(X)\\) | Función Generadora \\(M_X(t)\\) |
|---|---|---|---|---|---|---|
| **Uniforme continua** | \\(\mathcal{U}(a, b)\\), \\(a < b\\) | \\([a, b]\\) | \\(\dfrac{1}{b - a}\\) | \\(\dfrac{a + b}{2}\\) | \\(\dfrac{(b - a)^2}{12}\\) | \\(\dfrac{e^{tb} - e^{ta}}{t(b - a)}\\) |
| **Normal (Gauss)** | \\(\mathcal{N}(\mu, \sigma^2)\\), \\(\mu \in \mathbb{R}, \ \sigma > 0\\) | \\(\mathbb{R}\\) | \\(\dfrac{1}{\sigma\sqrt{2\pi}} e^{-(x-\mu)^2 / (2\sigma^2)}\\) | \\(\mu\\) | \\(\sigma^2\\) | \\(\exp\left(\mu t + \frac{1}{2}\sigma^2 t^2\right)\\) |
| **Exponencial** | \\(\text{Exp}(\lambda)\\), \\(\lambda > 0\\) | \\([0, \infty)\\) | \\(\lambda e^{-\lambda x}\\) | \\(\dfrac{1}{\lambda}\\) | \\(\dfrac{1}{\lambda^2}\\) | \\(\left(1 - \dfrac{t}{\lambda}\right)^{-1}, \ t < \lambda\\) |
| **Gamma** | \\(\text{Gamma}(\alpha, \beta)\\), \\(\alpha, \beta > 0\\) | \\((0, \infty)\\) | \\(\dfrac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}\\) | \\(\dfrac{\alpha}{\beta}\\) | \\(\dfrac{\alpha}{\beta^2}\\) | \\(\left(1 - \dfrac{t}{\beta}\right)^{-\alpha}, \ t < \beta\\) |
| **Beta** | \\(\text{Beta}(\alpha, \beta)\\), \\(\alpha, \beta > 0\\) | \\((0, 1)\\) | \\(\dfrac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1}\\) | \\(\dfrac{\alpha}{\alpha + \beta}\\) | \\(\dfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}\\) | \\(1 + \sum_{k=1}^\infty \left(\prod_{r=0}^{k-1} \frac{\alpha+r}{\alpha+\beta+r}\right) \frac{t^k}{k!}\\) |
| **Chi-cuadrada** | \\(\chi^2(k)\\), \\(k \in \mathbb{Z}^+\\) | \\((0, \infty)\\) | \\(\dfrac{1}{2^{k/2}\Gamma(k/2)} x^{k/2 - 1} e^{-x/2}\\) | \\(k\\) | \\(2k\\) | \\((1 - 2t)^{-k/2}, \ t < 1/2\\) |
| **$t$-Student** | \\(t(k)\\), \\(k > 0\\) | \\(\mathbb{R}\\) | \\(\dfrac{\Gamma((k+1)/2)}{\sqrt{k\pi}\Gamma(k/2)} \left(1 + \dfrac{x^2}{k}\right)^{-(k+1)/2}\\) | \\(0 \ (k > 1)\\) | \\(\dfrac{k}{k - 2} \ (k > 2)\\) | *(No existe para \\(t \neq 0\\))* |
| **$F$ Fisher** | \\(F(d_1, d_2)\\), \\(d_1, d_2 \in \mathbb{Z}^+\\) | \\((0, \infty)\\) | \\(\dfrac{\sqrt{\frac{(d_1 x)^{d_1} d_2^{d_2}}{(d_1 x + d_2)^{d_1+d_2}}}}{x B(d_1/2, d_2/2)}\\) | \\(\dfrac{d_2}{d_2 - 2} \ (d_2 > 2)\\) | \\(\dfrac{2d_2^2(d_1 + d_2 - 2)}{d_1(d_2 - 2)^2(d_2 - 4)}\\) | *(No existe para \\(t > 0\\))* |
| **Cauchy** | \\(\text{Cauchy}(x_0, \gamma)\\) | \\(\mathbb{R}\\) | \\(\dfrac{1}{\pi \gamma \left[1 + \left(\frac{x - x_0}{\gamma}\right)^2\right]}\\) | *No existe* | *No existe* | *(No existe; \\(\varphi(t)=e^{ix_0 t - \gamma \|t\|}\\))* |
| **Laplace** | \\(\text{Laplace}(\mu, b)\\), \\(b > 0\\) | \\(\mathbb{R}\\) | \\(\dfrac{1}{2b} \exp\left(-\dfrac{\|x - \mu\|}{b}\right)\\) | \\(\mu\\) | \\(2b^2\\) | \\(\dfrac{e^{\mu t}}{1 - b^2 t^2}, \ \|t\| < 1/b\\) |
| **Pareto** | \\(\text{Pareto}(x_m, \alpha)\\), \\(\alpha > 0\\) | \\([x_m, \infty)\\) | \\(\dfrac{\alpha x_m^\alpha}{x^{\alpha + 1}}\\) | \\(\dfrac{\alpha x_m}{\alpha - 1} \ (\alpha > 1)\\) | \\(\dfrac{\alpha x_m^2}{(\alpha - 1)^2 (\alpha - 2)} \ (\alpha > 2)\\) | *(No existe para \\(t > 0\\))* |
| **Weibull** | \\(\text{Weibull}(\lambda, k)\\), \\(\lambda, k > 0\\) | \\([0, \infty)\\) | \\(\dfrac{k}{\lambda} \left(\dfrac{x}{\lambda}\right)^{k-1} e^{-(x/\lambda)^k}\\) | \\(\lambda \Gamma\left(1 + \dfrac{1}{k}\right)\\) | \\(\lambda^2 \left[\Gamma\left(1 + \dfrac{2}{k}\right) - \left(\Gamma\left(1 + \dfrac{1}{k}\right)\right)^2\right]\\) | *(Serie infinita)* |

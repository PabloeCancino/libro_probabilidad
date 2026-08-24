# 3.5 Familias de distribuciones continuas fundamentales

Presentamos el catálogo formal y analítico de las familias continuas estándar, deduciendo para cada modelo su soporte, función de densidad (PDF), función de distribución acumulada (CDF), parámetros, media, varianza e interrelaciones teóricas.

---

## 3.5.1 Distribución Uniforme Continua

Modela la probabilidad homogénea en un intervalo continuo acotado \\([a, b]\\).

- **Parámetros:** \\(a < b\\) con \\(a, b \in \mathbb{R}\\).
- **Notación:** \\(X \sim \mathcal{U}(a, b)\\).
- **Soporte:** \\(S_X = [a, b]\\).
- **PDF y CDF:**
  \\[ f_X(x) = \begin{cases} \dfrac{1}{b - a}, & a \le x \le b, \\ 0, & \text{en otro caso.} \end{cases} \qquad F_X(x) = \begin{cases} 0, & x < a, \\ \dfrac{x - a}{b - a}, & a \le x \le b, \\ 1, & x > b. \end{cases} \\]
- **Esperanza y Varianza:**
  \\[ \mathbb{E}[X] = \int_a^b \frac{x}{b-a} \, dx = \frac{b^2 - a^2}{2(b-a)} = \frac{a + b}{2}. \\]
  \\[ \mathbb{E}[X^2] = \int_a^b \frac{x^2}{b-a} \, dx = \frac{b^3 - a^3}{3(b-a)} = \frac{a^2 + ab + b^2}{3} \implies \text{Var}(X) = \frac{(b - a)^2}{12}. \\]

---

## 3.5.2 Distribución Normal (Gaussiana)

Es la distribución continua más importante de toda la teoría estadística y probabilística, debido a su papel central en el Teorema del Límite Central.

- **Parámetros:** Media \\(\mu \in \mathbb{R}\\), varianza \\(\sigma^2 > 0\\) (o desviación estándar \\(\sigma > 0\\)).
- **Notación:** \\(X \sim \mathcal{N}(\mu, \sigma^2)\\).
- **Soporte:** \\(S_X = (-\infty, \infty) = \mathbb{R}\\).
- **PDF:**
  \\[ f_X(x) = \frac{1}{\sigma \sqrt{2\pi}} \exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right), \quad x \in \mathbb{R}. \\]

**Lema 3.23 (Integral Gaussiana).**
\\[ \int_{-\infty}^{\infty} e^{-z^2 / 2} \, dz = \sqrt{2\pi}. \\]
*Demostración.* Sea \\(I = \int_{-\infty}^{\infty} e^{-z^2/2} \, dz\\). Elevando al cuadrado y transformando a coordenadas polares en \\(\mathbb{R}^2\\):
\\[ I^2 = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} e^{-(x^2 + y^2)/2} \, dx \, dy = \int_0^{2\pi} d\theta \int_0^{\infty} r e^{-r^2/2} \, dr = 2\pi [-e^{-r^2/2}]_0^{\infty} = 2\pi (0 - (-1)) = 2\pi. \\]
Por ende, \\(I = \sqrt{2\pi}\\). Esto demuestra que \\(\int_{-\infty}^\infty f_X(x) \, dx = 1\\). \\(\blacksquare\\)

### La Normal Estándar y la transformación $Z$
Si \\(X \sim \mathcal{N}(\mu, \sigma^2)\\), la variable tipificada (estandarizada):
\\[ Z = \frac{X - \mu}{\sigma} \sim \mathcal{N}(0, 1). \\]
Su PDF se denota por \\(\phi(z) = \frac{1}{\sqrt{2\pi}} e^{-z^2/2}\\) y su CDF por \\(\Phi(z) = \int_{-\infty}^z \phi(t) \, dt\\).  
Por la simetría par de la curva campana respecto a cero:
\\[ \Phi(-z) = 1 - \Phi(z), \quad \forall z \in \mathbb{R}. \\]
- **Regla empírica 68-95-99.7:**
  - \\(\mathbb{P}(\mu - \sigma \le X \le \mu + \sigma) = \Phi(1) - \Phi(-1) \approx 0.6827\\) (68.27%).
  - \\(\mathbb{P}(\mu - 2\sigma \le X \le \mu + 2\sigma) = \Phi(2) - \Phi(-2) \approx 0.9545\\) (95.45%).
  - \\(\mathbb{P}(\mu - 3\sigma \le X \le \mu + 3\sigma) = \Phi(3) - \Phi(-3) \approx 0.9973\\) (99.73%).
- **Esperanza y Varianza:**
  \\[ \mathbb{E}[X] = \mu, \qquad \text{Var}(X) = \sigma^2. \\]

---

## 3.5.3 Distribución Exponencial

Modela el tiempo continuo de espera hasta la ocurrencia del primer evento en un proceso de Poisson con tasa \\(\lambda > 0\\).

- **Parámetro:** Tasa \\(\lambda > 0\\) (o escala \\(\beta = 1/\lambda\\)).
- **Notación:** \\(X \sim \text{Exp}(\lambda)\\).
- **Soporte:** \\(S_X = [0, \infty)\\).
- **PDF y CDF:**
  \\[ f_X(x) = \begin{cases} \lambda e^{-\lambda x}, & x \ge 0, \\ 0, & x < 0. \end{cases} \qquad F_X(x) = \begin{cases} 1 - e^{-\lambda x}, & x \ge 0, \\ 0, & x < 0. \end{cases} \\]
- **Función de Supervivencia / Confiabilidad:** \\(S_X(x) = \mathbb{P}(X > x) = e^{-\lambda x}\\).
- **Esperanza y Varianza:**
  \\[ \mathbb{E}[X] = \frac{1}{\lambda}, \qquad \text{Var}(X) = \frac{1}{\lambda^2}. \\]

**Teorema 3.24 (Falta de memoria continua).** *La distribución exponencial es la única distribución continua con soporte en \\([0, \infty)\\) que satisface:*
\\[ \mathbb{P}(X > s + t \mid X > s) = \mathbb{P}(X > t), \quad \forall s, t > 0. \\]
*Demostración.*
\\[ \mathbb{P}(X > s + t \mid X > s) = \frac{\mathbb{P}(X > s + t)}{\mathbb{P}(X > s)} = \frac{e^{-\lambda(s+t)}}{e^{-\lambda s}} = e^{-\lambda t} = \mathbb{P}(X > t). \quad \blacksquare \\]

---

## 3.5.4 Distribución Gamma

Generaliza la distribución exponencial para modelar el tiempo total de espera hasta acumular \\(\alpha\\) eventos independientes de Poisson.

- **Definición de la función Gamma de Euler:**
  \\[ \Gamma(\alpha) = \int_0^\infty t^{\alpha - 1} e^{-t} \, dt, \quad \text{con } \Gamma(\alpha + 1) = \alpha \Gamma(\alpha), \ \Gamma(n) = (n-1)!, \ \Gamma(1/2) = \sqrt{\pi}. \\]
- **Parámetros:** Forma \\(\alpha > 0\\), tasa \\(\beta > 0\\) (o escala \\(\theta = 1/\beta\\)).
- **Notación:** \\(X \sim \text{Gamma}(\alpha, \beta)\\).
- **Soporte:** \\(S_X = (0, \infty)\\).
- **PDF:**
  \\[ f_X(x) = \frac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha - 1} e^{-\beta x}, \quad x > 0. \\]
- **Esperanza y Varianza:**
  \\[ \mathbb{E}[X] = \frac{\alpha}{\beta}, \qquad \text{Var}(X) = \frac{\alpha}{\beta^2}. \\]
- **Casos particulares:**
  - \\(\alpha = 1 \implies \text{Gamma}(1, \beta) = \text{Exp}(\beta)\\).
  - \\(\alpha = k/2, \ \beta = 1/2 \implies \text{Gamma}(k/2, 1/2) = \chi^2(k)\\) (Chi-cuadrada con \\(k\\) grados de libertad).

---

## 3.5.5 Distribución Beta

Modela variables continuas acotadas en el intervalo unitario \\((0, 1)\\), ampliamente utilizada en estadística bayesiana como distribución a priori conjugada para proporciones binomiales.

- **Función Beta:** \\(B(\alpha, \beta) = \int_0^1 x^{\alpha - 1} (1 - x)^{\beta - 1} \, dx = \frac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha + \beta)}\\).
- **Parámetros:** Formas \\(\alpha > 0, \ \beta > 0\\).
- **Soporte:** \\(S_X = (0, 1)\\).
- **PDF:**
  \\[ f_X(x) = \frac{1}{B(\alpha, \beta)} x^{\alpha - 1} (1 - x)^{\beta - 1}, \quad x \in (0, 1). \\]
- **Esperanza y Varianza:**
  \\[ \mathbb{E}[X] = \frac{\alpha}{\alpha + \beta}, \qquad \text{Var}(X) = \frac{\alpha \beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}. \\]

---

## 3.5.6 Otras distribuciones continuas fundamentales

### 1. Distribución Chi-cuadrada (χ²)
Si \\(Z_1, \dots, Z_k \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0,1)\\), la suma de sus cuadrados \\(X = \sum_{i=1}^k Z_i^2 \sim \chi^2(k)\\) sigue una Chi-cuadrada con \\(k\\) grados de libertad.
- **PDF:** \\(f(x) = \frac{1}{2^{k/2}\Gamma(k/2)} x^{k/2 - 1} e^{-x/2}\\) para \\(x > 0\\).
- **Esperanza y Varianza:** \\(\mathbb{E}[X] = k\\), \\(\text{Var}(X) = 2k\\).

### 2. Distribución t-Student
Si \\(Z \sim \mathcal{N}(0,1)\\) y \\(V \sim \chi^2(k)\\) son independientes:
\\[ T = \frac{Z}{\sqrt{V / k}} \sim t(k). \\]
- **PDF:** \\(f(t) = \frac{\Gamma((k+1)/2)}{\sqrt{k\pi}\Gamma(k/2)} \left(1 + \frac{t^2}{k}\right)^{-(k+1)/2}\\) para \\(t \in \mathbb{R}\\).
- Posee colas más pesadas que la Normal; cuando \\(k \to \infty\\), \\(t(k) \xrightarrow{d} \mathcal{N}(0,1)\\).
- \\(\mathbb{E}[T] = 0\\) (para \\(k > 1\\)), \\(\text{Var}(T) = \frac{k}{k-2}\\) (para \\(k > 2\\)).

### 3. Distribución F de Fisher-Snedecor
Si \\(U \sim \chi^2(d_1)\\) y \\(V \sim \chi^2(d_2)\\) son independientes:
\\[ X = \frac{U / d_1}{V / d_2} \sim F(d_1, d_2). \\]
- **Esperanza:** \\(\mathbb{E}[X] = \frac{d_2}{d_2 - 2}\\) para \\(d_2 > 2\\).

### 4. Distribución de Cauchy
- **PDF:** \\(f(x) = \frac{1}{\pi (1 + x^2)}\\) para \\(x \in \mathbb{R}\\).
- **Propiedad patológica fundamental:** Las colas son tan pesadas (\\(\mathcal{O}(1/x^2)\\)) que la integral \\(\int_{-\infty}^\infty |x| f(x) dx = \infty\\). Por tanto, **la distribución de Cauchy no posee esperanza matemática, ni varianza, ni momentos de ningún orden**.

### 5. Distribución de Laplace (Doble Exponencial)
- **PDF:** \\(f(x) = \frac{1}{2b} \exp\left(-\frac{|x - \mu|}{b}\right)\\) para \\(x \in \mathbb{R}\\).
- **Esperanza y Varianza:** \\(\mathbb{E}[X] = \mu\\), \\(\text{Var}(X) = 2b^2\\).

### 6. Distribución de Pareto (Leyes de potencias)
- **PDF:** \\(f(x) = \frac{\alpha x_m^\alpha}{x^{\alpha + 1}}\\) para \\(x \ge x_m > 0\\).
- **Esperanza:** \\(\mathbb{E}[X] = \frac{\alpha x_m}{\alpha - 1}\\) (para \\(\alpha > 1\\)).

### 7. Distribución de Weibull
- **PDF:** \\(f(x) = \frac{k}{\lambda} \left(\frac{x}{\lambda}\right)^{k-1} e^{-(x/\lambda)^k}\\) para \\(x \ge 0\\).
- Fundamental en confiabilidad e ingeniería de materiales (tasas de falla crecientes, constantes o decrecientes).

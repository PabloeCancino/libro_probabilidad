# Ejercicios y proyectos de la Unidad 6

## Bloque A: Cadenas de Markov a tiempo discreto

1. **La caminata aleatoria con barreras absorbentes (Ruina del jugador):**
   - Considere una cadena de Markov con estados \\(S = \{0, 1, 2, 3, 4\}\\), donde los estados 0 y 4 son absorbentes (\\(p_{00}=1, \ p_{44}=1\\)), y para \\(i \in \{1, 2, 3\}\\), la transición es \\(p_{i, i+1} = p\\) y \\(p_{i, i-1} = 1 - p = q\\).
   - (a) Escriba la matriz de transición en forma canónica por bloques: \\(\mathbf{P} = \begin{pmatrix} \mathbf{Q} & \mathbf{R} \\ \mathbf{0} & \mathbf{I} \end{pmatrix}\\).
   - (b) Calcule la matriz fundamental \\(\mathbf{N} = (\mathbf{I} - \mathbf{Q})^{-1}\\) e interprete sus entradas como el número esperado de visitas a cada estado transitorio antes de la absorción.
   - (c) Calcule la matriz de probabilidades de absorción \\(\mathbf{B} = \mathbf{N}\mathbf{R}\\) para el caso simétrico \\(p = 0.5\\).

2. **El modelo de urnas de Ehrenfest:**
   - Hay \\(N = 4\\) moléculas distribuidas entre dos cámaras comunicadas \\(A\\) y \\(B\\). En cada paso se elige una molécula al azar y se traslada a la otra cámara.
   - Sea \\(X_n\\) el número de moléculas en la cámara \\(A\\) en el paso \\(n\\) (con \\(S = \{0, 1, 2, 3, 4\}\\)).
   - (a) Escriba la matriz de transición \\(\mathbf{P}\\).
   - (b) Demuestre que la cadena es irreducible con periodo \\(d = 2\\).
   - (c) Calcule la distribución estacionaria \\(\boldsymbol{\pi}\\) y demuestre que corresponde a la distribución Binomial \\(\text{Binomial}(N, 1/2)\\).

---

## Bloque B: Simulación de Monte Carlo y Métodos Inversos

3. **Generador para la distribución de Cauchy:**
   - La CDF de la distribución de Cauchy estándar es \\(F(x) = \frac{1}{2} + \frac{1}{\pi} \arctan(x)\\) para \\(x \in \mathbb{R}\\).
   - (a) Deduzca analíticamente la fórmula de la transformada inversa \\(X = F^{-1}(U)\\).
   - (b) Implemente una función en Python para generar 100\,000 muestras de Cauchy y grafique el histograma comparado con la PDF teórica.

4. **Estimación del volumen de una hiperesfera en dimensión $d$:**
   - El volumen teórico de una esfera unitaria en \\(\mathbb{R}^d\\) es \\(V_d = \frac{\pi^{d/2}}{\Gamma(d/2 + 1)}\\).
   - Escriba un script en Python que estime \\(V_d\\) mediante integración de Monte Carlo para \\(d = 2, 3, 4, 5, 10\\) y analice cómo evoluciona la eficiencia muestral al aumentar la dimensión.

---

## Bloque C: Proyecto de Laboratorio Computacional

5. **Proyecto Integrador: Ajuste distribucional sobre datos meteorológicos o financieros:**
   - Seleccione un conjunto de datos reales (por ejemplo, velocidad del viento, precipitaciones diarias o retornos logarítmicos financieros).
   - (a) Ajuste por Máxima Verosimilitud al menos tres familias continuas rivales (ej. Normal, Log-Normal, Weibull o Gamma) utilizando `scipy.stats`.
   - (b) Construya los gráficos de diagnóstico Q-Q correspondientes.
   - (c) Aplique la prueba formal de Kolmogorov-Smirnov y seleccione el mejor modelo probabilístico justificando con los valores \\(p\\) obtenidos.

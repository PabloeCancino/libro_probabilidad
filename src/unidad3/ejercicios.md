# Ejercicios de la Unidad 3

## Bloque A: Variables aleatorias y funciones de distribución

1. **Constante de normalización y CDF:** Sea la función:

   \\[
   f_X(x) = \begin{cases} c(1 - x^2), & -1 \le x \le 1, \\\\ 0, & \text{en otro caso.} \end{cases}
   \\]

   - (a) Determine el valor exacto de la constante \\(c\\) para que \\(f_X\\) sea una PDF legítima.
   - (b) Obtenga la función de distribución acumulada \\(F_X(x)\\) para todo \\(x \in \mathbb{R}\\).
   - (c) Calcule \\(\mathbb{P}(-0.5 \le X \le 0.5)\\) y la mediana de \\(X\\).

2. **Propiedades de la CDF:** Sea la función de distribución:

   \\[
   F(x) = \begin{cases} 0, & x < 0, \\\\ \frac{1}{2} x, & 0 \le x < 1, \\\\ 1 - \frac{1}{4} e^{-(x-1)}, & x \ge 1. \end{cases}
   \\]

   - (a) Demuestre que \\(F\\) cumple las 4 propiedades de una CDF.
   - (b) Calcule \\(\mathbb{P}(X = 1)\\), \\(\mathbb{P}(0.5 < X \le 2)\\) y determine si \\(X\\) es continua, discreta o mixta.

---

## Bloque B: Vectores aleatorios y transformaciones bivariadas

3. **Densidad conjunta y condicional:** Sean \\(X\\) e \\(Y\\) con densidad conjunta:

   \\[
   f_{X,Y}(x, y) = \begin{cases} 8xy, & 0 \le y \le x \le 1, \\\\ 0, & \text{en otro caso.} \end{cases}
   \\]

   - (a) Calcule las densidades marginales \\(f_X(x)\\) y \\(f_Y(y)\\).
   - (b) ¿Son \\(X\\) e \\(Y\\) variables aleatorias independientes? Justifique analíticamente.
   - (c) Obtenga la densidad condicional \\(f_{Y \mid X}(y \mid x)\\) y calcule \\(\mathbb{P}(Y \le 0.5 \mid X = 0.8)\\).

4. **Transformación por el método del Jacobiano:**
   - Sean \\(X, Y \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, 1)\\). Definamos la transformación a coordenadas polares \\(R = \sqrt{X^2 + Y^2}\\) y \\(\Theta = \arctan(Y/X)\\).
   - Demuestre que \\(R^2 \sim \text{Exp}(1/2) = \chi^2(2)\\) y \\(\Theta \sim \mathcal{U}(0, 2\pi)\\), y que son variables aleatorias independientes (generador de Box-Muller para números normales).

---

## Bloque C: Modelado con familias de distribuciones

5. **Distribución Binomial y Poisson:**
   - Un servidor web recibe en promedio 300 peticiones por minuto.
   - (a) Modele el número de peticiones por segundo mediante una distribución de Poisson adecuada.
   - (b) Calcule la probabilidad de que en un segundo determinado lleguen exactamente 4 peticiones.
   - (c) Calcule la probabilidad de que transcurran más de 2 segundos sin ninguna petición (utilizando la relación entre Poisson y Exponencial).

6. **Distribución Normal y puntuaciones $Z$:**
   - La estatura de una población de adultos se distribuye normalmente con media \\(\mu = 170\text{ cm}\\) y desviación estándar \\(\sigma = 8\text{ cm}\\).
   - (a) Calcule la proporción de adultos con estatura superior a 186 cm.
   - (b) Encuentre el percentil 90 de la estatura.

---

## Bloque D: Banco de reactivos institucionales (PALMAT)

7. **Reactivo PR-U2-01 (Esperanza Binomial):**  
   Si \\(X \sim \text{Binomial}(n = 10, p = 0.3)\\), calcule \\(\mathbb{E}[X]\\) y \\(\text{Var}(X)\\) deduciendo el procedimiento a partir de las variables indicadoras Bernoulli.

8. **Reactivo PR-U3-01 (Distribución Exponencial y Supervivencia):**  
   Sea \\(X \sim \text{Exp}(\lambda)\\) con media \\(\mathbb{E}[X] = 1/\lambda = 2\\). Calcule el valor analítico exacto de \\(\mathbb{P}(X > 3)\\).

9. **Reactivo PR-U4-01 (Criterio de Independencia de V.A.):**  
   Enuncie la condición necesaria y suficiente para que dos variables aleatorias continuas \\(X\\) e \\(Y\\) sean independientes en términos de sus funciones de densidad, y demuestre por qué la condición \\(\text{Cov}(X,Y) = 0\\) no es suficiente para asegurar la independencia en general.

# Ejercicios de la Unidad 5

## Bloque A: Desigualdades de probabilidad y concentración

1. **Comparación de cotas de concentración:**
   - Sea \\(X \sim \text{Poisson}(\lambda = 100)\\). Se desea estimar una cota superior para la probabilidad \\(\mathbb{P}(X \ge 150)\\).
   - (a) Calcule la cota exacta mediante la desigualdad de Márkov.
   - (b) Calcule la cota mediante la desigualdad de Chebyshev.
   - (c) Calcule la cota mediante la desigualdad de Cantelli.
   - (d) Obtenga la cota de Chernoff óptima optimizando \\(t > 0\\) y compare todas las cotas con el valor exacto de la distribución acumulada.

2. **Aplicación de la desigualdad de Jensen:**
   - Sea \\(X > 0\\) una variable aleatoria continua con media \\(\mu = 4\\). Demuestre que:

     \\[
     \mathbb{E}\left[\frac{1}{X}\right] \ge \frac{1}{4} \qquad \text{y} \qquad \mathbb{E}[\sqrt{X}] \le 2.
     \\]

---

## Bloque B: Modos de convergencia estocástica

3. **Convergencia de variables uniformes:**
   - Sea \\(X\_n \sim \mathcal{U}\left(0, \frac{1}{n}\right)\\) para \\(n \ge 1\\).
   - (a) Demuestre que \\(X\_n \xrightarrow{\text{c.s.}} 0\\).
   - (b) Demuestre que \\(X\_n \xrightarrow{L^2} 0\\).

4. **El máximo de variables exponenciales independientes:**
   - Sean \\(X\_1, X\_2, \dots, X\_n \stackrel{\text{i.i.d.}}{\sim} \text{Exp}(1)\\). Sea \\(M\_n = \max(X\_1, \dots, X\_n)\\).
   - Demuestre que la variable normalizada \\(Y\_n = M\_n - \ln n\\) converge en distribución a la distribución de Gumbel (valor extremo tipo I):

     \\[
     F\_Y(y) = e^{-e^{-y}}, \quad \forall y \in \mathbb{R}.
     \\]

---

## Bloque C: Ley de los Grandes Números y Teorema del Límite Central

5. **Diseño de tamaño muestral por Chebyshev:**
   - Una fábrica produce resistencias cuyo valor nominal es \\(100\,\Omega\\) con desviación estándar \\(\sigma = 5\,\Omega\\).
   - ¿Cuántas resistencias \\(n\\) deben medirse como mínimo para garantizar con al menos un 95% de confianza que la media muestral \\(\bar{X}\_n\\) no difiera de \\(100\,\Omega\\) en más de \\(0.5\,\Omega\\)?
   - Compare el tamaño muestral obtenido por Chebyshev con el obtenido utilizando el Teorema del Límite Central.

6. **Aproximación Normal a la Binomial con corrección por continuidad:**
   - Se lanza una moneda equilibrada 10\,000 veces.
   - Calcule mediante el Teorema de De Moivre-Laplace con corrección por continuidad la probabilidad de obtener entre 4\,950 y 5\,050 caras inclusive.

7. **Suma de variables continuas independientes:**
   - Un elevador tiene una capacidad máxima de carga de 2\,000 kg. Se sabe que el peso de los usuarios es una variable aleatoria con media \\(\mu = 75\text{ kg}\\) y desviación estándar \\(\sigma = 12\text{ kg}\\).
   - Si 25 personas suben al elevador, calcule la probabilidad aproximada mediante el TLC de que se supere la capacidad máxima de carga.
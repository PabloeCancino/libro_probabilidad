# 3.2 Funciones de masa, densidad y distribución acumulada

## 3.2.1 Función de masa de probabilidad (PMF) para variables discretas

Para una variable aleatoria discreta \\(X\\) con soporte \\(S_X = \{x_1, x_2, \dots\}\\), toda la información probabilística se concentra en la asignación puntual de probabilidades.

**Definición 3.5 (Función de masa de probabilidad - PMF).** La **función de masa de probabilidad** (o función de probabilidad) de una v.a. discreta \\(X\\) es la función \\(p_X : \mathbb{R} \to [0, 1]\\) dada por:
\\[ p_X(x) = \mathbb{P}(X = x) = \mathbb{P}(\{\omega \in \Omega : X(\omega) = x\}). \\]

**Teorema 3.6 (Condiciones necesarias y suficientes para una PMF).** *Una función \\(p: \mathbb{R} \to \mathbb{R}\\) es la PMF de alguna variable aleatoria discreta si y solo si satisface:*
1. **No negatividad:** \\(p(x) \ge 0\\) para todo \\(x \in \mathbb{R}\\).
2. **Soporte a lo más numerable:** El conjunto \\(S = \{x \in \mathbb{R} : p(x) > 0\}\\) es finito o infinito numerable.
3. **Condición de normalización:**
   \\[ \sum_{x \in S} p(x) = 1. \\]

Para cualquier subconjunto \\(B \subseteq \mathbb{R}\\), la probabilidad del evento \\((X \in B)\\) se calcula mediante la suma:
\\[ \mathbb{P}(X \in B) = \sum_{x \in B \cap S} p_X(x). \\]

---

## 3.2.2 Función de densidad de probabilidad (PDF) para variables continuas

Para una variable aleatoria continua, la probabilidad de cualquier punto individual es cero (\\(\mathbb{P}(X = x) = 0\\)). La distribución de probabilidad se describe mediante la densidad local de probabilidad por unidad de longitud.

**Definición 3.7 (Función de densidad de probabilidad - PDF).** La **función de densidad de probabilidad** de una variable aleatoria continua \\(X\\) es una función medible no negativa \\(f_X : \mathbb{R} \to [0, \infty)\\) tal que para todo intervalo \\([a, b] \subset \mathbb{R}\\):
\\[ \mathbb{P}(a \le X \le b) = \int_a^b f_X(x) \, dx. \\]

**Teorema 3.8 (Condiciones necesarias y suficientes para una PDF).** *Una función integrable \\(f: \mathbb{R} \to \mathbb{R}\\) es la PDF de una variable aleatoria continua si y solo si satisface:*
1. **No negatividad casi en todas partes:** \\(f(x) \ge 0\\) para todo \\(x \in \mathbb{R}\\).
2. **Normalización del área total:**
   \\[ \int_{-\infty}^{\infty} f(x) \, dx = 1. \\]

### Interpretación física de la densidad
Para un incremento infinitesimal \\(dx > 0\\):
\\[ \mathbb{P}(x \le X \le x + dx) = \int_x^{x+dx} f_X(u) \, du \approx f_X(x) \, dx. \\]
Por ende, \\(f_X(x)\\) no representa una probabilidad directa (puede ser mayor que 1, e incluso no estar acotada, como en \\(f(x) = \frac{1}{2\sqrt{x}}\\) para \\(x \in (0,1)\\)), sino una densidad de probabilidad por unidad de medida.

---

## 3.2.3 Función de distribución acumulada (CDF)

La función de distribución acumulada es la herramienta unificadora del cálculo de probabilidades: está definida de manera universal e idéntica tanto para variables discretas, continuas como mixtas.

**Definición 3.9 (Función de distribución acumulada - CDF).** La **función de distribución acumulada** de una variable aleatoria \\(X\\) (discreta, continua o mixta) es la función \\(F_X : \mathbb{R} \to [0, 1]\\) definida por:
\\[ F_X(x) = \mathbb{P}(X \le x) = \mathbb{P}(X \in (-\infty, x]), \quad \forall x \in \mathbb{R}. \\]

- **Para variables discretas:** \\(F_X(x) = \sum_{t \le x, \, t \in S_X} p_X(t)\\) (función escalonada, constante a trozos con saltos en cada átomo).
- **Para variables continuas:** \\(F_X(x) = \int_{-\infty}^x f_X(t) \, dt\\) (función continua no decreciente).

Por el Teorema Fundamental del Cálculo, si \\(F_X\\) es diferenciable en \\(x\\):
\\[ f_X(x) = \frac{d}{dx} F_X(x) = F_X'(x). \\]

---

## 3.2.4 Teorema de caracterización de la CDF: Las cuatro propiedades fundamentales

**Teorema 3.10 (Propiedades cardinales de la CDF).** *Toda función de distribución acumulada \\(F_X: \mathbb{R} \to [0, 1]\\) satisface las siguientes cuatro propiedades analíticas fundamentales:*

> 1. **Monotonía no decreciente:** Si \\(x_1 < x_2\\), entonces \\(F_X(x_1) \le F_X(x_2)\\).
> 2. **Límite inferior:** \\(\lim_{x \to -\infty} F_X(x) = 0\\).
> 3. **Límite superior:** \\(\lim_{x \to +\infty} F_X(x) = 1\\).
> 4. **Continuidad por la derecha:** Para todo \\(x \in \mathbb{R}\\), \\(\lim_{h \to 0^+} F_X(x + h) = F_X(x)\\) (es decir, \\(F_X(x^+) = F_X(x)\\)).

*Demostración analítica rigurosa.*
1. **Monotonía:** Sean \\(x_1 < x_2\\). El rayo \\((-\infty, x_1] \subseteq (-\infty, x_2]\\).  
   Por el Teorema de monotonía de la medida de probabilidad (Teorema 1.24):
   \\[ \mathbb{P}(X \in (-\infty, x_1]) \le \mathbb{P}(X \in (-\infty, x_2]) \implies F_X(x_1) \le F_X(x_2). \\]
   Además, se deduce la regla fundamental para el cálculo en intervalos semiabiertos:
   \\[ \mathbb{P}(x_1 < X \le x_2) = F_X(x_2) - F_X(x_1). \\]

2. **Límite en \\(-\infty\\):** Sea \\(\{x_n\}_{n=1}^\infty\\) una sucesión monótona estrictamente decreciente tal que \\(x_n \downarrow -\infty\\).  
   Definamos los eventos \\(A_n = (X \le x_n)\\). Entonces \\(A_n \downarrow \bigcap_{n=1}^\infty A_n = \emptyset\\).  
   Por el Teorema de continuidad de la probabilidad desde arriba (Teorema 1.29):
   \\[ \lim_{n \to \infty} F_X(x_n) = \lim_{n \to \infty} \mathbb{P}(A_n) = \mathbb{P}(\emptyset) = 0. \\]

3. **Límite en \\(+\infty\\):** Sea \\(\{x_n\}_{n=1}^\infty\\) una sucesión creciente con \\(x_n \uparrow +\infty\\).  
   Los eventos \\(B_n = (X \le x_n)\\) forman una sucesión creciente \\(B_n \uparrow \bigcup_{n=1}^\infty B_n = \Omega\\).  
   Por el Teorema de continuidad desde abajo (Teorema 1.29):
   \\[ \lim_{n \to \infty} F_X(x_n) = \lim_{n \to \infty} \mathbb{P}(B_n) = \mathbb{P}(\Omega) = 1. \\]

4. **Continuidad por la derecha:** Sea \\(x \in \mathbb{R}\\) fijo y consideremos una sucesión decreciente \\(h_n > 0\\) tal que \\(h_n \downarrow 0\\).  
   Los eventos \\(C_n = (X \le x + h_n)\\) forman una sucesión decreciente cuya intersección es:

   \\[
   \bigcap_{n=1}^\infty C_n = \bigcap_{n=1}^\infty \left\\{\omega : X(\omega) \le x + h_n\right\\} = \left\\{\omega : X(\omega) \le x\right\\} = (X \le x).
   \\]

   Por la continuidad de la probabilidad desde arriba:
   \\[ \lim_{n \to \infty} F_X(x + h_n) = \lim_{n \to \infty} \mathbb{P}(C_n) = \mathbb{P}(X \le x) = F_X(x). \quad \blacksquare \\]

---

## 3.2.5 Discontinuidades y masa puntual (Límite por la izquierda)

**Proposición 3.11 (Probabilidad de un punto individual).** *Para cualquier \\(x \in \mathbb{R}\\), denotando por \\(F_X(x^-) = \lim_{h \to 0^+} F_X(x - h)\\) el límite por la izquierda de la CDF en \\(x\\):*
\\[ \mathbb{P}(X = x) = F_X(x) - F_X(x^-). \\]

*Demostración.*  
El evento puntual \\((X = x)\\) se escribe como la intersección de intervalos semiabiertos decrecientes:

\\[
(X = x) = \bigcap_{n=1}^\infty \left(x - \frac{1}{n} < X \le x\right).
\\]

Por continuidad de la probabilidad:
\\[ \mathbb{P}(X = x) = \lim_{n \to \infty} \mathbb{P}\left(x - \frac{1}{n} < X \le x\right) = \lim_{n \to \infty} \left[F_X(x) - F_X\left(x - \frac{1}{n}\right)\right] = F_X(x) - F_X(x^-). \quad \blacksquare \\]

### Consecuencias para el cálculo de intervalos
- \\(\mathbb{P}(a < X \le b) = F_X(b) - F_X(a)\\).
- \\(\mathbb{P}(a \le X \le b) = F_X(b) - F_X(a^-) = F_X(b) - F_X(a) + \mathbb{P}(X = a)\\).
- \\(\mathbb{P}(a < X < b) = F_X(b^-) - F_X(a) = F_X(b) - F_X(a) - \mathbb{P}(X = b)\\).
- \\(\mathbb{P}(X > a) = 1 - F_X(a)\\).

---

## 3.2.6 Cuantiles y función cuantil (Inversa generalizada)

**Definición 3.12 (Función cuantil / Inversa generalizada).** Para cualquier \\(p \in (0, 1)\\), el **cuantil de orden \\(p\\)** (o percentil \\(100p\%\\)) de la variable aleatoria \\(X\\) se define como:
\\[ x_p = F_X^{-1}(p) = \inf \{x \in \mathbb{R} : F_X(x) \ge p\}. \\]

- **Mediana:** \\(m = x_{0.5} = F_X^{-1}(0.5)\\) (el valor central que divide la probabilidad acumulada en dos mitades del 50%).
- **Primer cuartil (Q1):** \\(q_1 = x_{0.25}\\); **Tercer cuartil (Q3):** \\(q_3 = x_{0.75}\\).
- **Rango intercuartílico:** \\(\text{IQR} = Q_3 - Q_1\\).

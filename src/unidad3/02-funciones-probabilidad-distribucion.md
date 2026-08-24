# 3.2 Funciones de masa, densidad y distribución acumulada

## 3.2.1 Función de masa de probabilidad (PMF) para variables discretas

Para una variable aleatoria discreta \\(X\\) con soporte \\(S\_X = \{x\_1, x\_2, \dots\}\\), toda la información probabilística se concentra en la asignación puntual de probabilidades.

**Definición 3.5 (Función de masa de probabilidad - PMF).** La **función de masa de probabilidad** (o función de probabilidad) de una v.a. discreta \\(X\\) es la función \\(p\_X : \mathbb{R} \to [0, 1]\\) dada por:

\\[
p\_X(x) = \mathbb{P}(X = x) = \mathbb{P}(\{\omega \in \Omega : X(\omega) = x\}).
\\]

**Teorema 3.6 (Condiciones necesarias y suficientes para una PMF).** *Una función \\(p: \mathbb{R} \to \mathbb{R}\\) es la PMF de alguna variable aleatoria discreta si y solo si satisface:*
1. **No negatividad:** \\(p(x) \ge 0\\) para todo \\(x \in \mathbb{R}\\).
2. **Soporte a lo más numerable:** El conjunto \\(S = \{x \in \mathbb{R} : p(x) > 0\}\\) es finito o infinito numerable.
3. **Condición de normalización:**

   \\[
   \sum\_{x \in S} p(x) = 1.
   \\]

Para cualquier subconjunto \\(B \subseteq \mathbb{R}\\), la probabilidad del evento \\((X \in B)\\) se calcula mediante la suma:

\\[
\mathbb{P}(X \in B) = \sum\_{x \in B \cap S} p\_X(x).
\\]

---

## 3.2.2 Función de densidad de probabilidad (PDF) para variables continuas

Para una variable aleatoria continua, la probabilidad de cualquier punto individual es cero (\\(\mathbb{P}(X = x) = 0\\)). La distribución de probabilidad se describe mediante la densidad local de probabilidad por unidad de longitud.

**Definición 3.7 (Función de densidad de probabilidad - PDF).** La **función de densidad de probabilidad** de una variable aleatoria continua \\(X\\) es una función medible no negativa \\(f\_X : \mathbb{R} \to [0, \infty)\\) tal que para todo intervalo \\([a, b] \subset \mathbb{R}\\):

\\[
\mathbb{P}(a \le X \le b) = \int\_a^b f\_X(x) \, dx.
\\]

**Teorema 3.8 (Condiciones necesarias y suficientes para una PDF).** *Una función integrable \\(f: \mathbb{R} \to \mathbb{R}\\) es la PDF de una variable aleatoria continua si y solo si satisface:*
1. **No negatividad casi en todas partes:** \\(f(x) \ge 0\\) para todo \\(x \in \mathbb{R}\\).
2. **Normalización del área total:**

   \\[
   \int\_{-\infty}^{\infty} f(x) \, dx = 1.
   \\]

### Interpretación física de la densidad
Para un incremento infinitesimal \\(dx > 0\\):

\\[
\mathbb{P}(x \le X \le x + dx) = \int\_x^{x+dx} f\_X(u) \, du \approx f\_X(x) \, dx.
\\]

Por ende, \\(f\_X(x)\\) no representa una probabilidad directa (puede ser mayor que 1, e incluso no estar acotada, como en \\(f(x) = \frac{1}{2\sqrt{x}}\\) para \\(x \in (0,1)\\)), sino una densidad de probabilidad por unidad de medida.

---

## 3.2.3 Función de distribución acumulada (CDF)

La función de distribución acumulada es la herramienta unificadora del cálculo de probabilidades: está definida de manera universal e idéntica tanto para variables discretas, continuas como mixtas.

**Definición 3.9 (Función de distribución acumulada - CDF).** La **función de distribución acumulada** de una variable aleatoria \\(X\\) (discreta, continua o mixta) es la función \\(F\_X : \mathbb{R} \to [0, 1]\\) definida por:

\\[
F\_X(x) = \mathbb{P}(X \le x) = \mathbb{P}(X \in (-\infty, x]), \quad \forall x \in \mathbb{R}.
\\]

- **Para variables discretas:** \\(F\_X(x) = \sum\_{t \le x, \, t \in S\_X} p\_X(t)\\) (función escalonada, constante a trozos con saltos en cada átomo).
- **Para variables continuas:** \\(F\_X(x) = \int\_{-\infty}^x f\_X(t) \, dt\\) (función continua no decreciente).

Por el Teorema Fundamental del Cálculo, si \\(F\_X\\) es diferenciable en \\(x\\):

\\[
f\_X(x) = \frac{d}{dx} F\_X(x) = F\_X'(x).
\\]

---

## 3.2.4 Teorema de caracterización de la CDF: Las cuatro propiedades fundamentales

**Teorema 3.10 (Propiedades cardinales de la CDF).** *Toda función de distribución acumulada \\(F\_X: \mathbb{R} \to [0, 1]\\) satisface las siguientes cuatro propiedades analíticas fundamentales:*

> 1. **Monotonía no decreciente:** Si \\(x\_1 < x\_2\\), entonces \\(F\_X(x\_1) \le F\_X(x\_2)\\).
> 2. **Límite inferior:** \\(\lim\_{x \to -\infty} F\_X(x) = 0\\).
> 3. **Límite superior:** \\(\lim\_{x \to +\infty} F\_X(x) = 1\\).
> 4. **Continuidad por la derecha:** Para todo \\(x \in \mathbb{R}\\), \\(\lim\_{h \to 0^+} F\_X(x + h) = F\_X(x)\\) (es decir, \\(F\_X(x^+) = F\_X(x)\\)).

*Demostración analítica rigurosa.*
1. **Monotonía:** Sean \\(x\_1 < x\_2\\). El rayo \\((-\infty, x\_1] \subseteq (-\infty, x\_2]\\).  
   Por el Teorema de monotonía de la medida de probabilidad (Teorema 1.24):

   \\[
   \mathbb{P}(X \in (-\infty, x\_1]) \le \mathbb{P}(X \in (-\infty, x\_2]) \implies F\_X(x\_1) \le F\_X(x\_2).
   \\]

   Además, se deduce la regla fundamental para el cálculo en intervalos semiabiertos:

   \\[
   \mathbb{P}(x\_1 < X \le x\_2) = F\_X(x\_2) - F\_X(x\_1).
   \\]

2. **Límite en \\(-\infty\\):** Sea \\(\{x\_n\}\_{n=1}^\infty\\) una sucesión monótona estrictamente decreciente tal que \\(x\_n \downarrow -\infty\\).  
   Definamos los eventos \\(A\_n = (X \le x\_n)\\). Entonces \\(A\_n \downarrow \bigcap\_{n=1}^\infty A\_n = \emptyset\\).  
   Por el Teorema de continuidad de la probabilidad desde arriba (Teorema 1.29):

   \\[
   \lim\_{n \to \infty} F\_X(x\_n) = \lim\_{n \to \infty} \mathbb{P}(A\_n) = \mathbb{P}(\emptyset) = 0.
   \\]

3. **Límite en \\(+\infty\\):** Sea \\(\{x\_n\}\_{n=1}^\infty\\) una sucesión creciente con \\(x\_n \uparrow +\infty\\).  
   Los eventos \\(B\_n = (X \le x\_n)\\) forman una sucesión creciente \\(B\_n \uparrow \bigcup\_{n=1}^\infty B\_n = \Omega\\).  
   Por el Teorema de continuidad desde abajo (Teorema 1.29):

   \\[
   \lim\_{n \to \infty} F\_X(x\_n) = \lim\_{n \to \infty} \mathbb{P}(B\_n) = \mathbb{P}(\Omega) = 1.
   \\]

4. **Continuidad por la derecha:** Sea \\(x \in \mathbb{R}\\) fijo y consideremos una sucesión decreciente \\(h\_n > 0\\) tal que \\(h\_n \downarrow 0\\).  
   Los eventos \\(C\_n = (X \le x + h\_n)\\) forman una sucesión decreciente cuya intersección es:

   \\[
   \bigcap\_{n=1}^\infty C\_n = \bigcap\_{n=1}^\infty \left\\{\omega : X(\omega) \le x + h\_n\right\\} = \left\\{\omega : X(\omega) \le x\right\\} = (X \le x).
   \\]

   Por la continuidad de la probabilidad desde arriba:

   \\[
   \lim\_{n \to \infty} F\_X(x + h\_n) = \lim\_{n \to \infty} \mathbb{P}(C\_n) = \mathbb{P}(X \le x) = F\_X(x). \quad \blacksquare
   \\]

---

## 3.2.5 Discontinuidades y masa puntual (Límite por la izquierda)

**Proposición 3.11 (Probabilidad de un punto individual).** *Para cualquier \\(x \in \mathbb{R}\\), denotando por \\(F\_X(x^-) = \lim\_{h \to 0^+} F\_X(x - h)\\) el límite por la izquierda de la CDF en \\(x\\):*

\\[
\mathbb{P}(X = x) = F\_X(x) - F\_X(x^-).
\\]

*Demostración.*  
El evento puntual \\((X = x)\\) se escribe como la intersección de intervalos semiabiertos decrecientes:

\\[
(X = x) = \bigcap\_{n=1}^\infty \left(x - \frac{1}{n} < X \le x\right).
\\]

Por continuidad de la probabilidad:

\\[
\mathbb{P}(X = x) = \lim\_{n \to \infty} \mathbb{P}\left(x - \frac{1}{n} < X \le x\right) = \lim\_{n \to \infty} \left[F\_X(x) - F\_X\left(x - \frac{1}{n}\right)\right] = F\_X(x) - F\_X(x^-). \quad \blacksquare
\\]

### Consecuencias para el cálculo de intervalos
- \\(\mathbb{P}(a < X \le b) = F\_X(b) - F\_X(a)\\).
- \\(\mathbb{P}(a \le X \le b) = F\_X(b) - F\_X(a^-) = F\_X(b) - F\_X(a) + \mathbb{P}(X = a)\\).
- \\(\mathbb{P}(a < X < b) = F\_X(b^-) - F\_X(a) = F\_X(b) - F\_X(a) - \mathbb{P}(X = b)\\).
- \\(\mathbb{P}(X > a) = 1 - F\_X(a)\\).

---

## 3.2.6 Cuantiles y función cuantil (Inversa generalizada)

**Definición 3.12 (Función cuantil / Inversa generalizada).** Para cualquier \\(p \in (0, 1)\\), el **cuantil de orden \\(p\\)** (o percentil \\(100p\%\\)) de la variable aleatoria \\(X\\) se define como:

\\[
x\_p = F\_X^{-1}(p) = \inf \{x \in \mathbb{R} : F\_X(x) \ge p\}.
\\]

- **Mediana:** \\(m = x\_{0.5} = F\_X^{-1}(0.5)\\) (el valor central que divide la probabilidad acumulada en dos mitades del 50%).
- **Primer cuartil (Q1):** \\(q\_1 = x\_{0.25}\\); **Tercer cuartil (Q3):** \\(q\_3 = x\_{0.75}\\).
- **Rango intercuartílico:** \\(\text{IQR} = Q\_3 - Q\_1\\).
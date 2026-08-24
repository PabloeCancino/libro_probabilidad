# 1.4 Probabilidad geométrica y problemas clásicos

## 1.4.1 Fundamentos de la probabilidad geométrica

Cuando un experimento aleatorio posee un espacio muestral continuo no numerable \\(\Omega \subset \mathbb{R}^n\\) (con \\(n \in \{1, 2, 3\}\\)) que tiene medida de Lebesgue finita y estrictamente positiva \\(0 < \mu(\Omega) < \infty\\) (donde \\(\mu\\) representa longitud, área o volumen), y se postula que el punto se elige "al azar" de manera uniforme en \\(\Omega\\), la probabilidad de que el resultado caiga dentro de una región medible de Borel \\(A \subseteq \Omega\\) se define geométricamente.

**Definición 1.31 (Probabilidad geométrica).** Si \\(\Omega \subset \mathbb{R}^n\\) es una región con medida \\(\mu(\Omega) > 0\\), la probabilidad geométrica de cualquier evento boreliano \\(A \in \mathcal{B}(\Omega)\\) es:

\\[
\mathbb{P}(A) = \frac{\mu(A)}{\mu(\Omega)} = \frac{\int_A d\mathbf{x}}{\int_\Omega d\mathbf{x}}.
\\]

- **En \\(\mathbb{R}\\) (Longitud):** \\(\mathbb{P}(A) = \frac{\text{Longitud}(A)}{\text{Longitud}(\Omega)}\\).
- **En \\(\mathbb{R}^2\\) (Área):** \\(\mathbb{P}(A) = \frac{\text{Área}(A)}{\text{Área}(\Omega)}\\).
- **En \\(\mathbb{R}^3\\) (Volumen):** \\(\mathbb{P}(A) = \frac{\text{Volumen}(A)}{\text{Volumen}(\Omega)}\\).

**Observación importante (Conjuntos de medida cero):** Para cualquier punto individual \\(\mathbf{x}_0 \in \Omega\\), \\(\mu(\{\mathbf{x}_0\}) = 0\\), lo que implica:

\\[
\mathbb{P}(\{\mathbf{x}_0\}) = 0.
\\]

En un espacio de probabilidad continuo, un evento con probabilidad cero **no es necesariamente imposible** (el experimento necesariamente arrojará algún punto individual de probabilidad cero). De igual forma, un evento con probabilidad 1 no es necesariamente el espacio seguro \\(\Omega\\), sino que se dice que ocurre **casi con certeza** o **casi seguramente (c.s.)**.

---

## 1.4.2 El problema del encuentro

**Ejemplo 1.32 (Cita al azar).**  
Dos personas acuerdan encontrarse en una cafetería entre las 12:00 y las 13:00 horas (un intervalo de 60 minutos). Cada una llega de manera independiente y uniforme en cualquier instante dentro de esa hora, y esperará a la otra persona como máximo 15 minutos. Si la otra persona no llega en ese lapso de 15 minutos, se retira. ¿Cuál es la probabilidad de que logren encontrarse?

*Solución analítica:*  
Sean \\(X\\) e \\(Y\\) los tiempos de llegada (en minutos después de las 12:00) de la primera y segunda persona, respectivamente.  
El espacio muestral es el cuadrado unitario en el plano:

\\[
\Omega = \{(x, y) \in \mathbb{R}^2 : 0 \le x \le 60, \ 0 \le y \le 60\}, \quad \text{con Área}(\Omega) = 60 \times 60 = 3\,600.
\\]

Las dos personas se encuentran si y solo si la diferencia absoluta de sus tiempos de llegada no supera los 15 minutos:

\\[
A = \{(x, y) \in \Omega : |x - y| \le 15\} = \{(x, y) \in \Omega : x - 15 \le y \le x + 15\}.
\\]

El evento complementario \\(A^c = \{(x, y) \in \Omega : |x - y| > 15\}\\) corresponde a dos triángulos rectángulos idénticos en las esquinas superior izquierda (\\(y - x > 15\\)) e inferior derecha (\\(x - y > 15\\)).  
La base y altura de cada triángulo complementario miden \\(60 - 15 = 45\\) minutos. Por tanto:

\\[
\text{Área}(A^c) = 2 \times \left(\frac{1}{2} \times 45 \times 45\right) = 45^2 = 2\,025.
\\]

El área de la región favorable \\(A\\) es:

\\[
\text{Área}(A) = \text{Área}(\Omega) - \text{Área}(A^c) = 3\,600 - 2\,025 = 1\,575.
\\]

Por la fórmula de probabilidad geométrica:

\\[
\mathbb{P}(A) = \frac{\text{Área}(A)}{\text{Área}(\Omega)} = \frac{1\,575}{3\,600} = \frac{7}{16} = 0.4375 \quad (43.75\%).
\\]

---

## 1.4.3 El problema clásico de la aguja de Buffon

Propuesto por Georges-Louis Leclerc, conde de Buffon en 1777, este problema constituye el primer ejemplo documentado de simulación geométrica de Monte Carlo para aproximar constantes matemáticas fundamentales como \\(\pi\\).

**Teorema 1.33 (Problema de la aguja de Buffon).** *Se tiene un piso con líneas paralelas separadas por una distancia \\(D\\). Se deja caer al azar una aguja de longitud \\(L\\) con \\(L \le D\\). La probabilidad de que la aguja cruce alguna de las líneas paralelas es:*

\\[
\mathbb{P}(\text{Cruce}) = \frac{2L}{\pi D}.
\\]

*Demostración analítica.*  
La posición de la aguja queda unívocamente determinada por dos variables aleatorias independientes:
1. \\(X\\): La distancia desde el centro de la aguja hasta la línea paralela más cercana. Como las líneas distan \\(D\\), la distancia al centro varía uniformemente en el intervalo \\([0, D/2]\\).
2. \\(\Theta\\): El ángulo agudo que forma la aguja con la dirección de las líneas paralelas, que varía uniformemente en \\([0, \pi/2]\\).

El espacio muestral en el plano \\((x, \theta)\\) es el rectángulo:

\\[
\Omega = \left\\{(x, \theta) : 0 \le x \le \frac{D}{2}, \ 0 \le \theta \le \frac{\pi}{2}\right\\}, \quad \text{con } \text{Área}(\Omega) = \frac{D}{2} \times \frac{\pi}{2} = \frac{\pi D}{4}.
\\]

Por trigonometría elemental, la proyección del semicuerpo de la aguja perpendicular a las líneas es \\(\frac{L}{2} \sin \theta\\).  
La aguja cruza una línea si y solo si la distancia \\(X\\) del centro a la línea es menor o igual a dicha proyección:

\\[
X \le \frac{L}{2} \sin \theta.
\\]

La región favorable \\(A\\) es el conjunto de puntos \\((x, \theta) \in \Omega\\) bajo la curva \\(x = \frac{L}{2} \sin \theta\\). Su área se calcula mediante la integral definida:

\\[
\text{Área}(A) = \int_0^{\pi/2} \left(\frac{L}{2} \sin \theta\right) d\theta = \frac{L}{2} [-\cos \theta]_0^{\pi/2} = \frac{L}{2} (0 - (-1)) = \frac{L}{2}.
\\]

Aplicando la definición de probabilidad geométrica:

\\[
\mathbb{P}(\text{Cruce}) = \frac{\text{Área}(A)}{\text{Área}(\Omega)} = \frac{L/2}{\pi D / 4} = \frac{2L}{\pi D}. \quad \blacksquare
\\]

**Estimación de π vía Monte Carlo:** Si se arroja la aguja \\(N\\) veces y se observan \\(N_{\text{cruces}}\\) cruces, la frecuencia relativa converge a la probabilidad teórica:

\\[
\frac{N_{\text{cruces}}}{N} \approx \frac{2L}{\pi D} \implies \hat{\pi} = \frac{2L \cdot N}{D \cdot N_{\text{cruces}}}.
\\]

---

## 1.4.4 La paradoja de Bertrand y la importancia de la medida invariante

En 1889, Joseph Bertrand planteó la siguiente pregunta: *"Se traza una cuerda al azar en una circunferencia. ¿Cuál es la probabilidad de que la longitud de la cuerda sea mayor que el lado del triángulo equilátero inscrito?"*

Si el radio de la circunferencia es \\(R\\), el lado del triángulo equilátero inscrito mide \\(L = R\sqrt{3}\\), y su distancia al centro es \\(d = R/2\\).

Bertrand propuso tres métodos aparentemente legítimos que conducen a tres respuestas distintas:

1. **Método 1 (Extremos al azar):**  
   Fijamos un extremo \\(A\\) del triángulo. El segundo extremo \\(B\\) se elige uniformemente sobre la circunferencia. Para que la cuerda sea mayor que \\(R\sqrt{3}\\), el punto \\(B\\) debe caer en el arco opuesto que subtiende \\(120^\circ\\) de los \\(360^\circ\\) totales.  

   \\[
   \mathbb{P}_1 = \frac{120^\circ}{360^\circ} = \frac{1}{3}.
   \\]

2. **Método 2 (Radio al azar):**  
   Fijamos un radio perpendicular a la cuerda. El punto medio de la cuerda se elige uniformemente sobre el radio de longitud \\(R\\). La cuerda mide más de \\(R\sqrt{3}\\) si su distancia al centro es menor que \\(R/2\\).  

   \\[
   \mathbb{P}_2 = \frac{R/2}{R} = \frac{1}{2}.
   \\]

3. **Método 3 (Punto medio en el círculo):**  
   El punto medio de la cuerda se elige uniformemente en el interior del círculo de radio \\(R\\) (área \\(\pi R^2\\)). Para que la cuerda sea mayor que \\(R\sqrt{3}\\), el punto medio debe caer dentro de un círculo concéntrico de radio \\(R/2\\) (área \\(\pi (R/2)^2 = \frac{1}{4}\pi R^2\\)).  

   \\[
   \mathbb{P}_3 = \frac{\pi (R/2)^2}{\pi R^2} = \frac{1}{4}.
   \\]

### Resolución matemática de la paradoja

La aparente paradoja radica en que la frase *"trazar una cuerda al azar"* está **mal definida** hasta que se especifique unívocamente la medida de probabilidad en el espacio de cuerdas. Cada método define un espacio de probabilidad \\((\Omega_i, \mathcal{F}_i, \mathbb{P}_i)\\) distinto con un grupo de simetrías diferente.

Edwin Jaynes (1973) demostró mediante el principio de máxima ignorancia que si se impone invariancia bajo rotaciones y traslaciones en el plano (invariancia euclidiana completa), el único modelo físicamente consistente con el lanzamiento de cuerdas reales es el **Método 2**, cuya probabilidad es \\(1/2\\).

---

## 1.4.5 Laboratorio en Python: Aguja de Buffon y Bertrand

```python
import numpy as np

def estimar_pi_buffon(L=1.0, D=2.0, N=1_000_000):
    """Simula la aguja de Buffon para estimar el valor de pi."""
    # Posicion x uniforme en [0, D/2]
    x = np.random.uniform(0, D / 2.0, size=N)
    # Angulo theta uniforme en [0, pi/2]
    theta = np.random.uniform(0, np.pi / 2.0, size=N)
    
    # Condicion de cruce
    cruces = x <= (L / 2.0) * np.sin(theta)
    n_cruces = np.sum(cruces)
    
    p_estimada = n_cruces / N
    pi_estimado = (2.0 * L) / (D * p_estimada) if n_cruces > 0 else 0
    return p_estimada, pi_estimado

p_obs, pi_calc = estimar_pi_buffon(L=1.0, D=2.0, N=1_000_000)
print(f"Probabilidad de cruce observada: {p_obs:.5f} (Teorica: {1/np.pi:.5f})")
print(f"Valor estimado de pi: {pi_calc:.5f} (Error absoluto: {abs(pi_calc - np.pi):.5f})")
```

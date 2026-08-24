# 1.1 Pensamiento probabilístico, desarrollo histórico y combinatoria

## 1.1.1 El pensamiento probabilístico vs. el determinismo

En la historia de la ciencia, el paradigma clásico newtoniano concibió al universo como un sistema determinista regido por leyes exactas: conocido el estado inicial completo de un sistema físico y las ecuaciones dinámicas que gobiernan su evolución, el futuro puede determinarse con absoluta precisión (*determinismo de Laplace*).

Sin embargo, la complejidad inherente a sistemas con incontables grados de libertad (como la mecánica estadística de Boltzmann y Maxwell), las limitaciones físicas en la precisión de medición, y finalmente la naturaleza intrínsecamente indeterminista de la mecánica cuántica (el principio de incertidumbre de Heisenberg), demostraron que el **pensamiento probabilístico** no es una simple renuncia ante la ignorancia, sino el lenguaje natural y riguroso para modelar, cuantificar y tomar decisiones racionales bajo condiciones de **incertidumbre**.

Un **experimento aleatorio** es cualquier proceso de observación o medición que satisface las siguientes tres condiciones:
1. Todos los resultados posibles son conocidos de antemano.
2. No es posible predecir con certeza el resultado particular de una realización individual del experimento.
3. El experimento puede repetirse, al menos conceptualmente, un número arbitrario de veces bajo condiciones esencialmente idénticas.

## 1.1.2 Breve perspectiva histórica

- **Siglo XVII (1654):** Pierre de Fermat y Blaise Pascal, motivados por las consultas del caballero de Méré sobre el reparto equitativo de apuestas en juegos de azar interrumpidos (*problema de los puntos*), establecen las primeras bases del cálculo de probabilidades.
- **Siglo XVIII (1713 - 1738):** Jakob Bernoulli publica *Ars Conjectandi*, introduciendo la primera formulación de la Ley Débil de los Grandes Números. Abraham de Moivre introduce en *The Doctrine of Chances* la aproximación de la distribución binomial mediante la curva normal.
- **Siglo XIX (1812):** Pierre-Simon Laplace publica *Théorie analytique des probabilités*, formalizando el principio de razón insuficiente y la definición clásica de probabilidad.
- **Siglo XX (1933):** Andréi N. Kolmogórov publica su monografía fundacional *Grundbegriffe der Wahrscheinlichkeitsrechnung* (Fundamentos de la teoría de probabilidades), asentando la disciplina de manera definitiva sobre la teoría axiomática de la medida y la integración.

---

## 1.1.3 Principios fundamentales del conteo

El cálculo de probabilidades en espacios muestrales finitos equiprobables descansa sobre el análisis combinatorio.

### Principio de adición (regla de la suma)

**Proposición 1.1 (Principio de adición).** *Si una tarea puede realizarse de \\(m\\) formas distintas, mientras que una segunda tarea puede realizarse de \\(n\\) formas distintas, y ambas tareas son mutuamente excluyentes (no pueden realizarse simultáneamente), entonces realizar una u otra tarea puede hacerse de \\(m + n\\) formas distintas.*

En términos de teoría de conjuntos, si \\(A\\) y \\(B\\) son conjuntos finitos y disjuntos (\\(A \cap B = \emptyset\\)), entonces:
\\[ |A \cup B| = |A| + |B|. \\]
Generalizando para una familia de conjuntos finitos disjuntos dos a dos \\(A_1, A_2, \dots, A_k\\):
\\[ \left|\bigcup_{i=1}^k A_i\right| = \sum_{i=1}^k |A_i|. \\]

### Principio de multiplicación (regla del producto)

**Proposición 1.2 (Principio de multiplicación).** *Si un procedimiento se compone de \\(k\\) etapas secuenciales, donde la primera etapa puede realizarse de \\(n_1\\) formas, la segunda de \\(n_2\\) formas (independientemente del resultado de la primera), y en general la etapa \\(i\\)-ésima puede realizarse de \\(n_i\\) formas, entonces el número total de formas en que puede completarse el procedimiento completo es:*
\\[ N = n_1 \cdot n_2 \cdots n_k = \prod_{i=1}^k n_i. \\]

En términos de conjuntos, si \\(A_1, \dots, A_k\\) son conjuntos finitos, el cardinal del producto cartesiano satisface:
\\[ |A_1 \times A_2 \times \dots \times A_k| = |A_1| \cdot |A_2| \cdots |A_k|. \\]

---

## 1.1.4 Permutaciones, variaciones y combinaciones

Sea \\(S\\) un conjunto finito con \\(n\\) elementos distintos: \\(|S| = n\\).

### 1. Permutaciones simples (sin repetición)

Una **permutación** de \\(S\\) es una ordenación biyectiva de los \\(n\\) elementos.

**Teorema 1.3.** *El número de permutaciones de \\(n\\) elementos distintos es:*
\\[ P_n = n! = n \cdot (n-1) \cdot (n-2) \cdots 2 \cdot 1, \quad \text{con } 0! = 1. \\]

*Demostración.* Hay \\(n\\) opciones para la primera posición, \\(n-1\\) para la segunda, \\(n-2\\) para la tercera, y así sucesivamente hasta \\(1\\) opción para la última posición. Por el principio de multiplicación, el total es \\(n!\\). \\(\blacksquare\\)

### 2. Variaciones (ordenaciones de \\(r\\) elementos tomados de \\(n\\))

Una **variación** o \\(r\\)-permutación es una selección ordenada de \\(r\\) elementos distintos de un conjunto de \\(n\\) elementos (donde \\(0 \le r \le n\\)).

**Teorema 1.4.** *El número de ordenaciones de \\(r\\) elementos tomados de \\(n\\) elementos distintos sin repetición es:*
\\[ P(n, r) = V_n^r = \frac{n!}{(n-r)!} = n(n-1)\cdots(n-r+1). \\]

*Demostración.* La primera posición puede llenarse de \\(n\\) formas, la segunda de \\(n-1\\), ..., y la posición \\(r\\)-ésima de \\(n - (r-1) = n - r + 1\\) formas. Multiplicando y completando el factorial:
\\[ n(n-1)\cdots(n-r+1) = \frac{n(n-1)\cdots(n-r+1)(n-r)\cdots 1}{(n-r)\cdots 1} = \frac{n!}{(n-r)!}. \quad \blacksquare \\]

Si se permite repetición (cada elemento puede elegirse más de una vez en las \\(r\\) posiciones), el número de variaciones con repetición es:
\\[ VR_n^r = n^r. \\]

### 3. Combinaciones simples

Una **combinación** de \\(r\\) elementos tomados de \\(n\\) es un subconjunto de tamaño \\(r\\) de \\(S\\) (donde el orden no importa).

**Teorema 1.5.** *El número de combinaciones de \\(r\\) elementos tomados de \\(n\\) elementos distintos es el coeficiente binomial:*
\\[ \binom{n}{r} = C(n, r) = \frac{n!}{r!(n-r)!}. \\]

*Demostración.* Cada subconjunto de tamaño \\(r\\) puede ordenarse internamente de \\(r!\\) maneras distintas para producir una variación ordenada de \\(r\\) elementos. Por tanto:
\\[ P(n, r) = \binom{n}{r} \cdot r! \implies \binom{n}{r} = \frac{P(n, r)}{r!} = \frac{n!}{r!(n-r)!}. \quad \blacksquare \\]

**Propiedades fundamentales del coeficiente binomial:**
1. **Simetría:** \\(\binom{n}{r} = \binom{n}{n-r}\\).
2. **Identidad de Pascal:** \\(\binom{n}{r} = \binom{n-1}{r-1} + \binom{n-1}{r}\\) para \\(1 \le r \le n-1\\).
3. **Teorema del Binomio:** Para cualesquiera \\(x, y \in \mathbb{R}\\) y \\(n \in \mathbb{N}\\):
   \\[ (x + y)^n = \sum_{r=0}^n \binom{n}{r} x^{n-r} y^r. \\]
4. **Suma de coeficientes:** \\(\sum_{r=0}^n \binom{n}{r} = 2^n\\) (el cardinal del conjunto potencia \\(|\mathcal{P}(S)|\\)).

### 4. Permutaciones con repetición y particiones ordenadas

Si se tienen \\(n\\) objetos donde \\(n_1\\) son de tipo 1 (indistinguibles entre sí), \\(n_2\\) de tipo 2, ..., y \\(n_k\\) de tipo \\(k\\), con \\(n_1 + n_2 + \dots + n_k = n\\):

**Teorema 1.6 (Coeficiente Multinomial).** *El número de permutaciones distinguibles de estos \\(n\\) objetos es:*
\\[ \binom{n}{n_1, n_2, \dots, n_k} = \frac{n!}{n_1! n_2! \cdots n_k!}. \\]

*Demostración.* De las \\(n\\) posiciones, elegimos \\(n_1\\) para los objetos del tipo 1 de \\(\binom{n}{n_1}\\) formas; de las \\(n - n_1\\) restantes, elegimos \\(n_2\\) para los del tipo 2 de \\(\binom{n-n_1}{n_2}\\) formas, y así sucesivamente. Multiplicando:
\\[ \binom{n}{n_1}\binom{n-n_1}{n_2}\cdots\binom{n_k}{n_k} = \frac{n!}{n_1!(n-n_1)!}\frac{(n-n_1)!}{n_2!(n-n_1-n_2)!}\cdots\frac{n_k!}{n_k!0!} = \frac{n!}{n_1! n_2! \cdots n_k!}. \quad \blacksquare \\]

### 5. Combinaciones con repetición

El número de formas de seleccionar \\(r\\) objetos de un conjunto de \\(n\\) tipos con reemplazo (donde el orden no importa pero un tipo puede elegirse varias veces) equivale al número de soluciones enteras no negativas a la ecuación \\(x_1 + x_2 + \dots + x_n = r\\) (con \\(x_i \ge 0\\)).

**Teorema 1.7 (Estrellas y barras).**
\\[ CR_n^r = \binom{n + r - 1}{r} = \binom{n + r - 1}{n - 1}. \\]

---

## 1.1.5 La regla clásica de Laplace

Cuando un experimento aleatorio tiene un espacio muestral finito \\(\Omega = \{\omega_1, \omega_2, \dots, \omega_N\}\\) y no existe ninguna razón asimétrica para favorecer un resultado elemental sobre otro (*principio de razón suficiente o indiferencia*), todos los eventos elementales son **equiprobables**:
\\[ \mathbb{P}(\{\omega_i\}) = \frac{1}{N}, \quad \forall i = 1, \dots, N. \\]

**Definición 1.8 (Regla de Laplace).** Para cualquier evento \\(A \subseteq \Omega\\), la probabilidad de ocurrencia de \\(A\\) es la razón entre el número de casos favorables a \\(A\\) y el número total de casos posibles:
\\[ \mathbb{P}(A) = \frac{|A|}{|\Omega|} = \frac{\text{Número de casos favorables a } A}{\text{Número total de casos posibles en } \Omega}. \\]

### Ejemplos resueltos

**Ejemplo 1.9 (El problema del cumpleaños).**  
¿Cuál es la probabilidad de que en un grupo de \\(k\\) personas al menos dos cumplan años el mismo día? (Supóngase un año no bisiesto de 365 días equiprobables e nacimientos independientes).

*Solución:*  
El espacio muestral de secuencias de cumpleaños de las \\(k\\) personas tiene cardinal:
\\[ |\Omega| = 365^k. \\]
Sea \\(A\\) el evento "al menos dos personas comparten cumpleaños". Su complemento \\(A^c\\) es "todas las \\(k\\) personas tienen cumpleaños en días estrictamente distintos".  
El número de formas en que \\(k\\) personas tienen cumpleaños distintos es la variación sin repetición:
\\[ |A^c| = P(365, k) = 365 \cdot 364 \cdot 363 \cdots (365 - k + 1). \\]
Por la regla de Laplace y la propiedad del complemento:
\\[ \mathbb{P}(A^c) = \frac{|A^c|}{|\Omega|} = \frac{365 \cdot 364 \cdots (365 - k + 1)}{365^k} = \prod_{i=0}^{k-1} \left(1 - \frac{i}{365}\right). \\]
Por consiguiente:
\\[ \mathbb{P}(A) = 1 - \prod_{i=0}^{k-1} \left(1 - \frac{i}{365}\right). \\]
Evaluando para valores representativos:
- Para \\(k = 23\\): \\(\mathbb{P}(A) \approx 0.5073\\) (más del 50% de probabilidad con solo 23 personas).
- Para \\(k = 50\\): \\(\mathbb{P}(A) \approx 0.9704\\).
- Para \\(k = 70\\): \\(\mathbb{P}(A) \approx 0.9992\\).

**Ejemplo 1.10 (Póker: Probabilidad de Full House).**  
En una baraja inglesa estándar de 52 cartas (4 palos de 13 cartas cada uno), se reparten 5 cartas al azar. ¿Cuál es la probabilidad de obtener un *Full House* (tres cartas del mismo valor y dos cartas de otro valor distinto)?

*Solución:*  
El número total de manos posibles de 5 cartas es:
\\[ |\Omega| = \binom{52}{5} = \frac{52 \cdot 51 \cdot 50 \cdot 49 \cdot 48}{120} = 2\,598\,960. \\]
Para formar un Full House:
1. Elegimos el valor del trío: \\(\binom{13}{1} = 13\\) opciones.
2. Elegimos 3 de los 4 palos disponibles para ese valor: \\(\binom{4}{3} = 4\\) formas.
3. De los 12 valores restantes, elegimos el valor de la pareja: \\(\binom{12}{1} = 12\\) opciones.
4. Elegimos 2 de los 4 palos disponibles para la pareja: \\(\binom{4}{2} = 6\\) formas.

Por el principio de multiplicación, el número de casos favorables es:
\\[ |A| = \binom{13}{1}\binom{4}{3}\binom{12}{1}\binom{4}{2} = 13 \times 4 \times 12 \times 6 = 3\,744. \\]
Por la regla de Laplace:
\\[ \mathbb{P}(\text{Full House}) = \frac{3\,744}{2\,598\,960} = \frac{6}{4\,165} \approx 0.001441 \quad (0.1441\%). \\]

---

## 1.1.6 Implementación en Python: Verificación combinatoria y simulación

```python
import math
import numpy as np

def prob_cumpleanos(k):
    """Calcula la probabilidad teorica analitica del problema del cumpleanos."""
    if k > 365:
        return 1.0
    p_distintos = 1.0
    for i in range(k):
        p_distintos *= (365 - i) / 365.0
    return 1.0 - p_distintos

def simular_cumpleanos(k, n_simulaciones=100_000):
    """Simula empiricamente el problema del cumpleanos mediante Monte Carlo."""
    # Genera matrices de dias de cumpleanos aleatorios (1 a 365)
    cumples = np.random.randint(1, 366, size=(n_simulaciones, k))
    # Cuenta cuantas simulaciones tienen al menos un duplicado
    coincidencias = [len(np.unique(fila)) < k for fila in cumples]
    return np.mean(coincidencias)

# Evaluacion comparativa
k_test = 23
p_teorica = prob_cumpleanos(k_test)
p_simulada = simular_cumpleanos(k_test)

print(f"Para k = {k_test} personas:")
print(f"Probabilidad teorica : {p_teorica:.5f}")
print(f"Probabilidad simulada: {p_simulada:.5f}")
```

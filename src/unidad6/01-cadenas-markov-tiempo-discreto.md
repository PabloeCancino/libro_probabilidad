# 6.1 Cadenas de Markov a tiempo discreto

## 6.1.1 Introducción a los procesos estocásticos y la propiedad de Márkov

Un **proceso estocástico** es una familia indexada de variables aleatorias \\((X_t)_{t \in T}\\) definidas sobre un espacio de probabilidad común \\((\Omega, \mathcal{F}, \mathbb{P})\\), donde el índice \\(t \in T\\) representa usualmente el tiempo.
- Si \\(T = \mathbb{N}_0 = \{0, 1, 2, \dots\}\\), el proceso es a **tiempo discreto**.
- Si \\(T = [0, \infty)\\), el proceso es a **tiempo continuo**.

El conjunto de todos los valores posibles que pueden tomar las variables \\(X_t\\) se denomina el **espacio de estados** \\(S\\). En esta sección nos enfocaremos en espacios de estados finitos o numerables \\(S = \{1, 2, \dots, N\}\\).

**Definición 6.1 (Propiedad de Márkov a tiempo discreto).** Un proceso estocástico a tiempo discreto \\((X_n)_{n=0}^\infty\\) con espacio de estados \\(S\\) es una **Cadena de Markov a tiempo discreto (DTMC)** si satisface la **propiedad de pérdida de memoria estocástica (propiedad de Márkov)**: la probabilidad condicional de la transición hacia el estado futuro \\(X_{n+1}\\) depende únicamente del estado presente actual \\(X_n\\), siendo completamente independiente de toda la trayectoria histórica pasada:
\\[ \mathbb{P}(X_{n+1} = j \mid X_n = i, \ X_{n-1} = i_{n-1}, \dots, X_0 = i_0) = \mathbb{P}(X_{n+1} = j \mid X_n = i), \\]
para todo \\(n \ge 0\\) y para cualesquiera estados \\(i, j, i_0, \dots, i_{n-1} \in S\\).

Decimos que la cadena es **homogénea en el tiempo** si las probabilidades de transición no dependen del paso temporal \\(n\\):
\\[ p_{ij} = \mathbb{P}(X_{n+1} = j \mid X_n = i) = \mathbb{P}(X_1 = j \mid X_0 = i). \\]

---

## 6.1.2 Matriz de transición de un paso y Ecuaciones de Chapman-Kolmogórov

**Definición 6.2 (Matriz estocástica de transición).** Para una cadena homogénea con \\(N\\) estados, la **matriz de transición en un paso** es la matriz cuadrada \\(\mathbf{P} = (p_{ij}) \in \mathbb{R}^{N \times N}\\):
\\[ \mathbf{P} = \begin{pmatrix} p_{11} & p_{12} & \dots & p_{1N} \\ p_{21} & p_{22} & \dots & p_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ p_{N1} & p_{N2} & \dots & p_{NN} \end{pmatrix}. \\]
Toda matriz de transición es una **matriz estocástica por filas**:
1. \\(p_{ij} \ge 0\\) para todo \\(i, j \in S\\).
2. Cada fila suma exactamente 1: \\(\sum_{j=1}^N p_{ij} = 1\\) para todo \\(i \in S\\).

**Definición 6.3 (Probabilidades de transición en $n$ pasos).**
\\[ p_{ij}^{(n)} = \mathbb{P}(X_{n+m} = j \mid X_m = i) = \mathbb{P}(X_n = j \mid X_0 = i). \\]

**Teorema 6.4 (Ecuaciones de Chapman-Kolmogórov).** *Para cualesquiera enteros \\(n, m \ge 0\\) y estados \\(i, j \in S\\):*
\\[ p_{ij}^{(n+m)} = \sum_{k \in S} p_{ik}^{(n)} p_{kj}^{(m)}. \\]
*En notación matricial, la matriz de transición en \\(n\\) pasos es simplemente la \\(n\\)-ésima potencia algebraica de la matriz \\(\mathbf{P}\\):*
\\[ \mathbf{P}^{(n)} = \mathbf{P}^n = \underbrace{\mathbf{P} \cdot \mathbf{P} \cdots \mathbf{P}}_{n \text{ veces}}. \\]

*Demostración.*  
Aplicando la Ley de la Probabilidad Total condicionando sobre el estado intermedio \\(X_n = k\\) y la propiedad de Márkov:

\\[
\begin{aligned}
p_{ij}^{(n+m)} &= \mathbb{P}(X_{n+m} = j \mid X_0 = i) = \sum_{k \in S} \mathbb{P}(X_{n+m} = j, X_n = k \mid X_0 = i) \\\\
&= \sum_{k \in S} \mathbb{P}(X_n = k \mid X_0 = i) \mathbb{P}(X_{n+m} = j \mid X_n = k, X_0 = i) \\\\
&= \sum_{k \in S} p_{ik}^{(n)} p_{kj}^{(m)}.
\end{aligned}
\\]
Esto coincide exactamente con la regla del producto de matrices para \\(\mathbf{P}^{n+m} = \mathbf{P}^n \mathbf{P}^m\\). \\(\blacksquare\\)

Si el vector de probabilidades iniciales es \\(\boldsymbol{\pi}^{(0)} = (\mathbb{P}(X_0=1), \dots, \mathbb{P}(X_0=N))\\), la distribución de probabilidad marginal en el paso \\(n\\) es:
\\[ \boldsymbol{\pi}^{(n)} = \boldsymbol{\pi}^{(0)} \mathbf{P}^n. \\]

---

## 6.1.3 Clasificación de estados y propiedades estructurales

1. **Accesibilidad y Comunicación:**  
   - El estado \\(j\\) es accesible desde \\(i\\) (\\(i \to j\\)) si existe algún \\(n \ge 0\\) tal que \\(p_{ij}^{(n)} > 0\\).
   - Dos estados **comunican** (\\(i \leftrightarrow j\\)) si \\(i \to j\\) y \\(j \to i\\). La comunicación es una relación de equivalencia que particiona a \\(S\\) en clases comunicantes disjuntas.
2. **Irreducibilidad:** Una cadena es **irreducible** si todos sus estados comunican entre sí (hay una única clase que abarca todo \\(S\\)).
3. **Periodicidad:** El **periodo** de un estado \\(i\\) es \\(d(i) = \text{mcd}\{n \ge 1 : p_{ii}^{(n)} > 0\}\\). Si \\(d(i) = 1\\), el estado es **aperiódico**.
4. **Recurrencia y Transitoriedad:**  
   Sea \\(f_{ii} = \mathbb{P}(\text{la cadena eventualmente regresa al estado } i \mid X_0 = i)\\).
   - El estado \\(i\\) es **recurrente** si \\(f_{ii} = 1\\) (se visita infinitas veces casi seguramente).
   - El estado \\(i\\) es **transitorio** si \\(f_{ii} < 1\\) (se visita solo un número finito de veces).
   - Un estado \\(i\\) es **absorbente** si \\(p_{ii} = 1\\) (una vez que entra, nunca sale).

---

## 6.1.4 Distribución estacionaria y convergencia al equilibrio

**Definición 6.5 (Distribución estacionaria o invariante).** Un vector de probabilidad por filas \\(\boldsymbol{\pi} = (\pi_1, \dots, \pi_N)\\) es una **distribución estacionaria** para la cadena de Markov con matriz \\(\mathbf{P}\\) si satisface:
\\[ \boldsymbol{\pi} \mathbf{P} = \boldsymbol{\pi}, \qquad \text{con } \pi_i \ge 0 \quad \text{y} \quad \sum_{i=1}^N \pi_i = 1. \\]
(Es decir, \\(\boldsymbol{\pi}\\) es un vector propio por la izquierda asociado al valor propio \\(\lambda = 1\\)).

**Teorema 6.6 (Teorema Ergódico Fundamental de Markov).** *Si una cadena de Markov con espacio de estados finito es **irreducible y aperiódica**, entonces:*
1. *Existe una **única** distribución estacionaria \\(\boldsymbol{\pi}\\) estrictamente positiva (\\(\pi_i > 0\\) para todo \\(i\\)).*
2. *Para cualquier distribución inicial \\(\boldsymbol{\pi}^{(0)}\\), la cadena converge asintóticamente al equilibrio:*

   \\[
   \lim_{n \to \infty} \mathbf{P}^n = \begin{pmatrix} \boldsymbol{\pi} \\\\ \boldsymbol{\pi} \\\\ \vdots \\\\ \boldsymbol{\pi} \end{pmatrix}, \qquad \lim_{n \to \infty} \boldsymbol{\pi}^{(n)} = \boldsymbol{\pi}.
   \\]
3. *El tiempo medio de recurrencia al estado \\(i\\) es \\(\mu_{ii} = \frac{1}{\pi_i}\\).*

---

## 6.1.5 Ejemplo: Modelo climatológico y cálculo en Python

Consideremos un modelo simplificado del clima con dos estados: Soleado (1) y Lluvioso (2).
- Si hoy está soleado, mañana estará soleado con probabilidad 0.8 y lluvioso con 0.2.
- Si hoy llueve, mañana estará soleado con probabilidad 0.4 y lluvioso con 0.6.

La matriz de transición es:

\\[
\mathbf{P} = \begin{pmatrix} 0.8 & 0.2 \\\\ 0.4 & 0.6 \end{pmatrix}.
\\]

Para encontrar la distribución estacionaria \\(\boldsymbol{\pi} = (\pi_1, \pi_2)\\):

\\[
(\pi_1, \pi_2) \begin{pmatrix} 0.8 & 0.2 \\\\ 0.4 & 0.6 \end{pmatrix} = (\pi_1, \pi_2) \implies \begin{cases} 0.8\pi_1 + 0.4\pi_2 = \pi_1 \\\\ 0.2\pi_1 + 0.6\pi_2 = \pi_2 \\\\ \pi_1 + \pi_2 = 1 \end{cases} \implies 0.4\pi_2 = 0.2\pi_1 \implies \pi_1 = 2\pi_2.
\\]

Sustituyendo en \\(\pi_1 + \pi_2 = 1\\):
\\[ 2\pi_2 + \pi_2 = 1 \implies \pi_2 = \frac{1}{3}, \quad \pi_1 = \frac{2}{3}. \\]
A largo plazo, el 66.67% de los días serán soleados y el 33.33% serán lluviosos, independientemente del clima en el día inicial.

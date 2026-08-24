# 6.1 Cadenas de Markov a tiempo discreto

## 6.1.1 Introducción a los procesos estocásticos y la propiedad de Márkov

Un **proceso estocástico** es una familia indexada de variables aleatorias \\((X\_t)\_{t \in T}\\) definidas sobre un espacio de probabilidad común \\((\Omega, \mathcal{F}, \mathbb{P})\\), donde el índice \\(t \in T\\) representa usualmente el tiempo.
- Si \\(T = \mathbb{N}\_0 = \{0, 1, 2, \dots\}\\), el proceso es a **tiempo discreto**.
- Si \\(T = [0, \infty)\\), el proceso es a **tiempo continuo**.

El conjunto de todos los valores posibles que pueden tomar las variables \\(X\_t\\) se denomina el **espacio de estados** \\(S\\). En esta sección nos enfocaremos en espacios de estados finitos o numerables \\(S = \{1, 2, \dots, N\}\\).

**Definición 6.1 (Propiedad de Márkov a tiempo discreto).** Un proceso estocástico a tiempo discreto \\((X\_n)\_{n=0}^\infty\\) con espacio de estados \\(S\\) es una **Cadena de Markov a tiempo discreto (DTMC)** si satisface la **propiedad de pérdida de memoria estocástica (propiedad de Márkov)**: la probabilidad condicional de la transición hacia el estado futuro \\(X\_{n+1}\\) depende únicamente del estado presente actual \\(X\_n\\), siendo completamente independiente de toda la trayectoria histórica pasada:

\\[
\mathbb{P}(X\_{n+1} = j \mid X\_n = i, \ X\_{n-1} = i\_{n-1}, \dots, X\_0 = i\_0) = \mathbb{P}(X\_{n+1} = j \mid X\_n = i),
\\]

para todo \\(n \ge 0\\) y para cualesquiera estados \\(i, j, i\_0, \dots, i\_{n-1} \in S\\).

Decimos que la cadena es **homogénea en el tiempo** si las probabilidades de transición no dependen del paso temporal \\(n\\):

\\[
p\_{ij} = \mathbb{P}(X\_{n+1} = j \mid X\_n = i) = \mathbb{P}(X\_1 = j \mid X\_0 = i).
\\]

---

## 6.1.2 Matriz de transición de un paso y Ecuaciones de Chapman-Kolmogórov

**Definición 6.2 (Matriz estocástica de transición).** Para una cadena homogénea con \\(N\\) estados, la **matriz de transición en un paso** es la matriz cuadrada \\(\mathbf{P} = (p\_{ij}) \in \mathbb{R}^{N \times N}\\):

\\[
\mathbf{P} = \begin{pmatrix} p\_{11} & p\_{12} & \dots & p\_{1N} \\ p\_{21} & p\_{22} & \dots & p\_{2N} \\ \vdots & \vdots & \ddots & \vdots \\ p\_{N1} & p\_{N2} & \dots & p\_{NN} \end{pmatrix}.
\\]

Toda matriz de transición es una **matriz estocástica por filas**:
1. \\(p\_{ij} \ge 0\\) para todo \\(i, j \in S\\).
2. Cada fila suma exactamente 1: \\(\sum\_{j=1}^N p\_{ij} = 1\\) para todo \\(i \in S\\).

**Definición 6.3 (Probabilidades de transición en $n$ pasos).**

\\[
p\_{ij}^{(n)} = \mathbb{P}(X\_{n+m} = j \mid X\_m = i) = \mathbb{P}(X\_n = j \mid X\_0 = i).
\\]

**Teorema 6.4 (Ecuaciones de Chapman-Kolmogórov).** *Para cualesquiera enteros \\(n, m \ge 0\\) y estados \\(i, j \in S\\):*

\\[
p\_{ij}^{(n+m)} = \sum\_{k \in S} p\_{ik}^{(n)} p\_{kj}^{(m)}.
\\]

*En notación matricial, la matriz de transición en \\(n\\) pasos es simplemente la \\(n\\)-ésima potencia algebraica de la matriz \\(\mathbf{P}\\):*

\\[
\mathbf{P}^{(n)} = \mathbf{P}^n = \underbrace{\mathbf{P} \cdot \mathbf{P} \cdots \mathbf{P}}\_{n \text{ veces}}.
\\]

*Demostración.*  
Aplicando la Ley de la Probabilidad Total condicionando sobre el estado intermedio \\(X\_n = k\\) y la propiedad de Márkov:

\\[
\begin{aligned}
p\_{ij}^{(n+m)} &= \mathbb{P}(X\_{n+m} = j \mid X\_0 = i) = \sum\_{k \in S} \mathbb{P}(X\_{n+m} = j, X\_n = k \mid X\_0 = i) \\\\
&= \sum\_{k \in S} \mathbb{P}(X\_n = k \mid X\_0 = i) \mathbb{P}(X\_{n+m} = j \mid X\_n = k, X\_0 = i) \\\\
&= \sum\_{k \in S} p\_{ik}^{(n)} p\_{kj}^{(m)}.
\end{aligned}
\\]

Esto coincide exactamente con la regla del producto de matrices para \\(\mathbf{P}^{n+m} = \mathbf{P}^n \mathbf{P}^m\\). \\(\blacksquare\\)

Si el vector de probabilidades iniciales es \\(\boldsymbol{\pi}^{(0)} = (\mathbb{P}(X\_0=1), \dots, \mathbb{P}(X\_0=N))\\), la distribución de probabilidad marginal en el paso \\(n\\) es:

\\[
\boldsymbol{\pi}^{(n)} = \boldsymbol{\pi}^{(0)} \mathbf{P}^n.
\\]

---

## 6.1.3 Clasificación de estados y propiedades estructurales

1. **Accesibilidad y Comunicación:**  
   - El estado \\(j\\) es accesible desde \\(i\\) (\\(i \to j\\)) si existe algún \\(n \ge 0\\) tal que \\(p\_{ij}^{(n)} > 0\\).
   - Dos estados **comunican** (\\(i \leftrightarrow j\\)) si \\(i \to j\\) y \\(j \to i\\). La comunicación es una relación de equivalencia que particiona a \\(S\\) en clases comunicantes disjuntas.
2. **Irreducibilidad:** Una cadena es **irreducible** si todos sus estados comunican entre sí (hay una única clase que abarca todo \\(S\\)).
3. **Periodicidad:** El **periodo** de un estado \\(i\\) es \\(d(i) = \text{mcd}\{n \ge 1 : p\_{ii}^{(n)} > 0\}\\). Si \\(d(i) = 1\\), el estado es **aperiódico**.
4. **Recurrencia y Transitoriedad:**  
   Sea \\(f\_{ii} = \mathbb{P}(\text{la cadena eventualmente regresa al estado } i \mid X\_0 = i)\\).
   - El estado \\(i\\) es **recurrente** si \\(f\_{ii} = 1\\) (se visita infinitas veces casi seguramente).
   - El estado \\(i\\) es **transitorio** si \\(f\_{ii} < 1\\) (se visita solo un número finito de veces).
   - Un estado \\(i\\) es **absorbente** si \\(p\_{ii} = 1\\) (una vez que entra, nunca sale).

---

## 6.1.4 Distribución estacionaria y convergencia al equilibrio

**Definición 6.5 (Distribución estacionaria o invariante).** Un vector de probabilidad por filas \\(\boldsymbol{\pi} = (\pi\_1, \dots, \pi\_N)\\) es una **distribución estacionaria** para la cadena de Markov con matriz \\(\mathbf{P}\\) si satisface:

\\[
\boldsymbol{\pi} \mathbf{P} = \boldsymbol{\pi}, \qquad \text{con } \pi\_i \ge 0 \quad \text{y} \quad \sum\_{i=1}^N \pi\_i = 1.
\\]

(Es decir, \\(\boldsymbol{\pi}\\) es un vector propio por la izquierda asociado al valor propio \\(\lambda = 1\\)).

**Teorema 6.6 (Teorema Ergódico Fundamental de Markov).** *Si una cadena de Markov con espacio de estados finito es **irreducible y aperiódica**, entonces:*
1. *Existe una **única** distribución estacionaria \\(\boldsymbol{\pi}\\) estrictamente positiva (\\(\pi\_i > 0\\) para todo \\(i\\)).*
2. *Para cualquier distribución inicial \\(\boldsymbol{\pi}^{(0)}\\), la cadena converge asintóticamente al equilibrio:*

   \\[
   \lim\_{n \to \infty} \mathbf{P}^n = \begin{pmatrix} \boldsymbol{\pi} \\\\ \boldsymbol{\pi} \\\\ \vdots \\\\ \boldsymbol{\pi} \end{pmatrix}, \qquad \lim\_{n \to \infty} \boldsymbol{\pi}^{(n)} = \boldsymbol{\pi}.
   \\]

3. *El tiempo medio de recurrencia al estado \\(i\\) es \\(\mu\_{ii} = \frac{1}{\pi\_i}\\).*

---

## 6.1.5 Ejemplo: Modelo climatológico y cálculo en Python

Consideremos un modelo simplificado del clima con dos estados: Soleado (1) y Lluvioso (2).
- Si hoy está soleado, mañana estará soleado con probabilidad 0.8 y lluvioso con 0.2.
- Si hoy llueve, mañana estará soleado con probabilidad 0.4 y lluvioso con 0.6.

La matriz de transición es:

\\[
\mathbf{P} = \begin{pmatrix} 0.8 & 0.2 \\\\ 0.4 & 0.6 \end{pmatrix}.
\\]

Para encontrar la distribución estacionaria \\(\boldsymbol{\pi} = (\pi\_1, \pi\_2)\\):

\\[
(\pi\_1, \pi\_2) \begin{pmatrix} 0.8 & 0.2 \\\\ 0.4 & 0.6 \end{pmatrix} = (\pi\_1, \pi\_2) \implies \begin{cases} 0.8\pi\_1 + 0.4\pi\_2 = \pi\_1 \\\\ 0.2\pi\_1 + 0.6\pi\_2 = \pi\_2 \\\\ \pi\_1 + \pi\_2 = 1 \end{cases} \implies 0.4\pi\_2 = 0.2\pi\_1 \implies \pi\_1 = 2\pi\_2.
\\]

Sustituyendo en \\(\pi\_1 + \pi\_2 = 1\\):

\\[
2\pi\_2 + \pi\_2 = 1 \implies \pi\_2 = \frac{1}{3}, \quad \pi\_1 = \frac{2}{3}.
\\]

A largo plazo, el 66.67% de los días serán soleados y el 33.33% serán lluviosos, independientemente del clima en el día inicial.
# Apéndice C. Banco de reactivos institucionales resueltos (PALMAT 2024)

Este apéndice presenta la resolución analítica exhaustiva, justificación paso a paso y retroalimentación pedagógica del **Banco Institucional de Reactivos de Probabilidad (CBIMAT-234)** del Plan de Estudios 2024 de la Licenciatura en Matemáticas (PALMAT) de la Universidad Autónoma de Nayarit.

---

## C.1 Reactivo PR-U1-01: Eventos mutuamente excluyentes

**Enunciado institucional:**  
Sean \\(A\\) y \\(B\\) dos eventos en un espacio de probabilidad \\((\Omega, \mathcal{F}, \mathbb{P})\\) con \\(\mathbb{P}(A) = 0.3\\) y \\(\mathbb{P}(B) = 0.4\\). Si \\(A\\) y \\(B\\) son **mutuamente excluyentes**, ¿cuánto es \\(\mathbb{P}(A \cup B)\\)?

- **A) \\(0.70\\)** *(Opción Correcta)*
- B) \\(0.12\\)
- C) \\(0.58\\)
- D) \\(1.00\\)

### Solución analítica y justificación formal
Por definición, dos eventos son **mutuamente excluyentes** si su intersección es el evento imposible:

\\[
A \cap B = \emptyset \implies \mathbb{P}(A \cap B) = \mathbb{P}(\emptyset) = 0.
\\]

Aplicando la regla general de adición de Kolmogórov (Teorema 1.25):

\\[
\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B) = 0.3 + 0.4 - 0 = 0.70.
\\]

### Análisis pedagógico de distractores
- **Distractor B (\\(0.12\\)):** Es el producto \\(\mathbb{P}(A)\mathbb{P}(B) = 0.3 \times 0.4 = 0.12\\). Este cálculo corresponde a la probabilidad de la *intersección* \\(\mathbb{P}(A \cap B)\\) bajo la hipótesis de *independencia*, no a la unión de eventos excluyentes.
- **Distractor C (\\(0.58\\)):** Resultado de calcular \\(\mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A)\mathbb{P}(B) = 0.70 - 0.12 = 0.58\\), que corresponde a la unión bajo *independencia*, confundiendo exclusión con independencia.
- **Distractor D (\\(1.00\\)):** Asume erróneamente que los eventos forman una partición exhaustiva de \\(\Omega\\).

*Referencia bibliográfica:* Wackerly, D., Mendenhall, W. & Scheaffer, R. L. (2010). *Estadística Matemática con Aplicaciones* (7a ed.). Cengage Learning.

---

## C.2 Reactivo PR-U1-02: Probabilidad condicional en conjuntos

**Enunciado institucional:**  
En un grupo estudiantil, el 60% tiene competencia en inglés (\\(I\\)), el 40% en francés (\\(F\\)) y el 20% domina ambos idiomas simultáneamente. ¿Cuál es la probabilidad condicional de que un estudiante domine el francés dado que domina el inglés (\\(\mathbb{P}(F \mid I)\\))?

- **A) \\(1/3 \approx 0.3333\\)** *(Opción Correcta)*
- B) \\(0.40\\)
- C) \\(0.20\\)
- D) \\(0.50\\)

### Solución analítica y justificación formal
Identificamos los datos proporcionados:

\\[
\mathbb{P}(I) = 0.60, \qquad \mathbb{P}(F) = 0.40, \qquad \mathbb{P}(I \cap F) = 0.20.
\\]

Por la definición formal de probabilidad condicional (Definición 2.1) sobre el espacio muestral reducido \\(I\\):

\\[
\mathbb{P}(F \mid I) = \frac{\mathbb{P}(F \cap I)}{\mathbb{P}(I)} = \frac{0.20}{0.60} = \frac{2}{6} = \frac{1}{3} \approx 0.3333 \quad (33.33\%).
\\]

### Análisis pedagógico de distractores
- **Distractor B (\\(0.40\\)):** Corresponde a la probabilidad marginal \\(\mathbb{P}(F)\\), ignorando el condicionamiento sobre el subgrupo que habla inglés.
- **Distractor C (\\(0.20\\)):** Corresponde a la probabilidad conjunta \\(\mathbb{P}(F \cap I)\\).
- **Distractor D (\\(0.50\\)):** Resultado de invertir erróneamente el evento condicionante: \\(\mathbb{P}(I \mid F) = \frac{\mathbb{P}(I \cap F)}{\mathbb{P}(F)} = \frac{0.20}{0.40} = 0.50\\).

*Referencia bibliográfica:* DeGroot, M. H. & Schervish, M. J. (2012). *Probability and Statistics* (4th ed.). Pearson.

---

## C.3 Reactivo PR-U2-01: Esperanza matemática de la distribución Binomial

**Enunciado institucional:**  
Sea \\(X \sim \text{Binomial}(n = 10, p = 0.3)\\). ¿Cuál es el valor esperado \\(\mathbb{E}[X]\\)?

- **A) \\(3.0\\)** *(Opción Correcta)*
- B) \\(0.3\\)
- C) \\(10.0\\)
- D) \\(2.1\\)

### Solución analítica y justificación formal
Toda variable binomial \\(X \sim \text{Binomial}(n, p)\\) se descompone como la suma de \\(n\\) variables indicadoras independientes \\(Y_1, \dots, Y_n \stackrel{\text{i.i.d.}}{\sim} \text{Bernoulli}(p)\\), donde \\(\mathbb{E}[Y_i] = 1 \cdot p + 0 \cdot (1-p) = p\\).  
Por la linealidad del operador esperanza (Teorema 4.3):

\\[
\mathbb{E}[X] = \mathbb{E}\left[\sum_{i=1}^{10} Y_i\right] = \sum_{i=1}^{10} \mathbb{E}[Y_i] = 10 \cdot p = 10 \times 0.3 = 3.0.
\\]

### Análisis pedagógico de distractores
- **Distractor B (\\(0.3\\)):** Es únicamente el parámetro de probabilidad individual \\(p\\).
- **Distractor C (\\(10.0\\)):** Es el número total de ensayos \\(n\\).
- **Distractor D (\\(2.1\\)):** Es la **varianza** \\(\text{Var}(X) = n p (1 - p) = 10 \times 0.3 \times 0.7 = 2.1\\), no la esperanza.

*Referencia bibliográfica:* Wackerly, D., Mendenhall, W. & Scheaffer, R. L. (2010). *Estadística Matemática con Aplicaciones*. Cengage Learning.

---

## C.4 Reactivo PR-U3-01: Distribución Exponencial y supervivencia

**Enunciado institucional:**  
Sea \\(X \sim \text{Exp}(\lambda)\\) una variable aleatoria continua con media \\(\mathbb{E}[X] = 1/\lambda = 2\\). ¿Cuánto es \\(\mathbb{P}(X > 3)\\)?

- **A) \\(e^{-3/2} \approx 0.2231\\)** *(Opción Correcta)*
- B) \\(1 - e^{-3/2}\\)
- C) \\(e^{-3}\\)
- D) \\(0.50\\)

### Solución analítica y justificación formal
Dado que \\(\mathbb{E}[X] = 1/\lambda = 2\\), el parámetro de tasa es \\(\lambda = 1/2 = 0.5\\).  
La función de densidad es \\(f_X(x) = \frac{1}{2} e^{-x/2}\\) para \\(x \ge 0\\).  
La probabilidad de la cola de supervivencia es:

\\[
\mathbb{P}(X > 3) = \int_3^\infty \frac{1}{2} e^{-x/2} \, dx = \left[-e^{-x/2}\right]_3^\infty = 0 - (-e^{-3/2}) = e^{-3/2} = e^{-1.5} \approx 0.22313.
\\]

### Análisis pedagógico de distractores
- **Distractor B (\\(1 - e^{-3/2}\\)):** Es la probabilidad acumulada \\(\mathbb{P}(X \le 3) = F_X(3)\\).
- **Distractor C (\\(e^{-3}\\)):** Corresponde a asumir erróneamente \\(\lambda = 1\\) en lugar de \\(\lambda = 1/2\\).
- **Distractor D (\\(0.50\\)):** Asume erróneamente un decaimiento lineal.

*Referencia bibliográfica:* DeGroot, M. H. & Schervish, M. J. (2012). *Probability and Statistics*. Pearson.

---

## C.5 Reactivo PR-U4-01: Criterio de independencia de variables continuas

**Enunciado institucional:**  
Dos variables aleatorias continuas \\(X\\) e \\(Y\\) son estocásticamente independientes si y solo si:

- **A) \\(f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y)\\) para todo \\((x, y) \in \mathbb{R}^2\\)** *(Opción Correcta)*
- B) \\(\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]\\)
- C) \\(\text{Cov}(X, Y) = 0\\)
- D) \\(\mathbb{P}(X > a) = \mathbb{P}(Y > a)\\) para todo \\(a \in \mathbb{R}\\)

### Solución analítica y justificación formal
La independencia estocástica exige que la medida de probabilidad conjunta en el plano factorice como el producto tensorial de las medidas marginales, lo que en el caso absolutamente continuo equivale a la **factorización puntual de la función de densidad conjunta en el producto de las densidades marginales** para casi todo \\((x, y)\\) (Teorema 3.17).

### Análisis pedagógico de distractores
- **Distractor B y C:** La no correlación (\\(\text{Cov}(X,Y)=0 \iff \mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]\\)) es una **consecuencia necesaria pero NO suficiente** de la independencia (existen variables no correlacionadas con fuerte dependencia no lineal, como \\(X \sim \mathcal{U}(-1,1)\\) e \\(Y = X^2\\)).
- **Distractor D:** Afirma que las variables tienen la misma distribución marginal (ser idénticamente distribuidas), lo cual no guarda ninguna relación lógica con la independencia.

*Referencia bibliográfica:* Wackerly, D. et al. (2010). *Estadística Matemática con Aplicaciones*. Cengage Learning.

# 3.3 Vectores aleatorios, distribuciones conjuntas e independencia

## 3.3.1 Vectores aleatorios bivariados

Frecuentemente, el análisis de un experimento aleatorio requiere observar simultáneamente múltiples características numéricas asociadas al mismo resultado \\(\omega \in \Omega\\).

**Definición 3.13 (Vector aleatorio bivariado).** Un **vector aleatorio bivariado** es una función medible \\(\mathbf{X} = (X, Y) : \Omega \to \mathbb{R}^2\\), donde cada componente \\(X: \Omega \to \mathbb{R}\\) e \\(Y: \Omega \to \mathbb{R}\\) es una variable aleatoria real ordinaria.

---

## 3.3.2 Función de distribución acumulada conjunta

**Definición 3.14 (CDF conjunta).** La **función de distribución acumulada conjunta** de \\((X, Y)\\) es la función \\(F_{X,Y} : \mathbb{R}^2 \to [0, 1]\\) definida por:
\\[ F_{X,Y}(x, y) = \mathbb{P}(X \le x, \ Y \le y) = \mathbb{P}(\{\omega \in \Omega : X(\omega) \le x \text{ y } Y(\omega) \le y\}). \\]

### Propiedades fundamentales de la CDF conjunta
1. **Monotonía por componentes:** Si \\(x_1 \le x_2\\) e \\(y_1 \le y_2\\), entonces \\(F_{X,Y}(x_1, y_1) \le F_{X,Y}(x_2, y_2)\\).
2. **Límites en el infinito:**
   \\[ \lim_{x \to -\infty} F_{X,Y}(x, y) = 0, \quad \lim_{y \to -\infty} F_{X,Y}(x, y) = 0, \quad \lim_{x, y \to +\infty} F_{X,Y}(x, y) = 1. \\]
3. **Distribuciones marginales:**
   \\[ F_X(x) = \lim_{y \to +\infty} F_{X,Y}(x, y), \qquad F_Y(y) = \lim_{x \to +\infty} F_{X,Y}(x, y). \\]
4. **Probabilidad de rectángulos (No negatividad de la medida 2D):**  
   Para cualesquiera \\(a_1 < a_2\\) y \\(b_1 < b_2\\):
   \\[ \mathbb{P}(a_1 < X \le a_2, \ b_1 < Y \le b_2) = F_{X,Y}(a_2, b_2) - F_{X,Y}(a_1, b_2) - F_{X,Y}(a_2, b_1) + F_{X,Y}(a_1, b_1) \ge 0. \\]

---

## 3.3.3 Distribuciones conjuntas discretas y continuas

### Caso discreto: PMF conjunta
Si \\((X, Y)\\) toma valores en un conjunto a lo más numerable \\(S_{X,Y} \subset \mathbb{R}^2\\), su **función de masa conjunta** es:
\\[ p_{X,Y}(x, y) = \mathbb{P}(X = x, \ Y = y), \quad \text{con } p_{X,Y}(x, y) \ge 0 \quad \text{y} \quad \sum_{(x,y)} p_{X,Y}(x, y) = 1. \\]
- **PMF Marginales:**
  \\[ p_X(x) = \sum_{y} p_{X,Y}(x, y), \qquad p_Y(y) = \sum_{x} p_{X,Y}(x, y). \\]

### Caso continuo: PDF conjunta
Si existe una función no negativa integrable \\(f_{X,Y} : \mathbb{R}^2 \to [0, \infty)\\) tal que para toda región boreliana \\(A \subseteq \mathbb{R}^2\\):
\\[ \mathbb{P}((X, Y) \in A) = \iint_A f_{X,Y}(x, y) \, dx \, dy, \quad \text{con } \int_{-\infty}^\infty \int_{-\infty}^\infty f_{X,Y}(x, y) \, dx \, dy = 1. \\]
Por el Teorema Fundamental del Cálculo en varias variables:
\\[ f_{X,Y}(x, y) = \frac{\partial^2}{\partial x \partial y} F_{X,Y}(x, y). \\]
- **PDF Marginales:**
  \\[ f_X(x) = \int_{-\infty}^\infty f_{X,Y}(x, y) \, dy, \qquad f_Y(y) = \int_{-\infty}^\infty f_{X,Y}(x, y) \, dx. \\]

---

## 3.3.4 Distribuciones condicionales

**Definición 3.15 (Distribución condicional).**
1. **Caso discreto:** Para cualquier valor \\(y\\) tal que \\(p_Y(y) > 0\\), la **PMF condicional** de \\(X\\) dado \\(Y = y\\) es:
   \\[ p_{X \mid Y}(x \mid y) = \mathbb{P}(X = x \mid Y = y) = \frac{p_{X,Y}(x, y)}{p_Y(y)}. \\]
2. **Caso continuo:** Para cualquier valor \\(y\\) tal que \\(f_Y(y) > 0\\), la **PDF condicional** de \\(X\\) dado \\(Y = y\\) es:
   \\[ f_{X \mid Y}(x \mid y) = \frac{f_{X,Y}(x, y)}{f_Y(y)}. \\]

Es directo verificar que \\(\int_{-\infty}^\infty f_{X \mid Y}(x \mid y) \, dx = \frac{\int_{-\infty}^\infty f_{X,Y}(x,y) dx}{f_Y(y)} = \frac{f_Y(y)}{f_Y(y)} = 1\\), por lo que \\(f_{X \mid Y}(\cdot \mid y)\\) es una genuina densidad de probabilidad univariada sobre \\(\mathbb{R}\\).

---

## 3.3.5 Independencia estocástica de variables aleatorias

**Definición 3.16 (Independencia de variables aleatorias).** Dos variables aleatorias \\(X\\) e \\(Y\\) son **estocásticamente independientes** (denotado \\(X \perp Y\\)) si para cualesquiera conjuntos borelianos \\(A, B \in \mathcal{B}(\mathbb{R})\\):
\\[ \mathbb{P}(X \in A, \ Y \in B) = \mathbb{P}(X \in A) \cdot \mathbb{P}(Y \in B). \\]

**Teorema 3.17 (Criterios equivalentes de independencia).** *Las siguientes proposiciones son lógicamente equivalentes:*
1. \\(X\\) e \\(Y\\) son independientes.
2. Para todo \\((x, y) \in \mathbb{R}^2\\), la CDF conjunta factoriza en el producto de las CDF marginales:
   \\[ F_{X,Y}(x, y) = F_X(x) \cdot F_Y(y). \\]
3. En el caso continuo, la densidad conjunta factoriza para todo \\((x, y)\\):
   \\[ f_{X,Y}(x, y) = f_X(x) \cdot f_Y(y). \\]
4. En el caso discreto, la masa conjunta factoriza para todo \\((x, y)\\):
   \\[ p_{X,Y}(x, y) = p_X(x) \cdot p_Y(y). \\]
5. Para todo \\(y\\) con \\(f_Y(y) > 0\\), la densidad condicional coincide con la marginal:
   \\[ f_{X \mid Y}(x \mid y) = f_X(x). \\]

---

## 3.3.6 Transformaciones bivariadas y el método del Jacobiano

Sean \\(X, Y\\) variables aleatorias continuas conjuntas con PDF \\(f_{X,Y}(x, y)\\) y soporte \\(S \subseteq \mathbb{R}^2\\).  
Consideremos la transformación invertible (difeomorfismo) \\((U, V) = \mathbf{g}(X, Y) = (g_1(X, Y), g_2(X, Y))\\), con transformación inversa única:
\\[ X = h_1(U, V), \qquad Y = h_2(U, V). \\]

**Definición 3.18 (Matriz Jacobiana y Jacobiano de la transformación).** La matriz jacobiana de la transformación inversa es:
\\[ J = \begin{pmatrix} \dfrac{\partial x}{\partial u} & \dfrac{\partial x}{\partial v} \\ \dfrac{\partial y}{\partial u} & \dfrac{\partial y}{\partial v} \end{pmatrix}, \qquad \det(J) = \frac{\partial x}{\partial u}\frac{\partial y}{\partial v} - \frac{\partial x}{\partial v}\frac{\partial y}{\partial u}. \\]

**Teorema 3.19 (Cambio de variables bivariado).** *Si la transformación \\(\mathbf{g}\\) es biyectiva y diferenciable con continuidad con \\(\det(J) \neq 0\\), la PDF conjunta del nuevo vector \\((U, V)\\) es:*
\\[ f_{U,V}(u, v) = f_{X,Y}(h_1(u, v), h_2(u, v)) \cdot |\det(J)|. \\]

### Aplicación fundamental: Distribución de la suma $U = X + Y$ (Convolución)

Sea \\(U = X + Y\\) y definamos una variable auxiliar \\(V = Y\\).  
La transformación inversa es \\(X = U - V\\), \\(Y = V\\).  
La matriz jacobiana es:
\\[ J = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix} \implies |\det(J)| = |(1)(1) - (-1)(0)| = 1. \\]
La PDF conjunta es \\(f_{U,V}(u, v) = f_{X,Y}(u - v, v)\\). Integrando respecto a \\(v\\) para obtener la marginal de \\(U\\):

**Teorema 3.20 (Fórmula de Convolución).** *Si \\(X\\) e \\(Y\\) son variables aleatorias continuas e independientes con densidades \\(f_X\\) y \\(f_Y\\), la PDF de su suma \\(U = X + Y\\) es la convolución de sus densidades:*
\\[ f_{X+Y}(u) = (f_X * f_Y)(u) = \int_{-\infty}^\infty f_X(u - v) f_Y(v) \, dv = \int_{-\infty}^\infty f_X(x) f_Y(u - x) \, dx. \\]

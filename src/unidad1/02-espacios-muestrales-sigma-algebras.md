# 1.2 Espacios muestrales, álgebra de eventos y σ-álgebras

## 1.2.1 Espacios muestrales

Para construir una teoría matemática rigurosa de la probabilidad, es indispensable definir con precisión el conjunto de todos los desenlaces posibles de un experimento aleatorio.

**Definición 1.11 (Espacio muestral).** El **espacio muestral**, denotado usualmente por \\(\Omega\\) (o \\(S\\)), es el conjunto no vacío cuyos elementos individuales \\(\omega \in \Omega\\) representan todos los resultados elementales posibles y mutuamente excluyentes de un experimento aleatorio.

Los espacios muestrales se clasifican según su cardinalidad:
1. **Espacios muestrales finitos:** \\(|\Omega| = n < \infty\\).  
   *Ejemplo:* El lanzamiento de un dado de seis caras: \\(\Omega = \{1, 2, 3, 4, 5, 6\}\\).
2. **Espacios muestrales infinitos numerables:** \\(|\Omega| = \aleph_0\\) (existe una biyección con \\(\mathbb{N}\\)).  
   *Ejemplo:* Lanzar una moneda hasta obtener la primera cara: \\(\Omega = \{C, SC, SSC, SSSC, \dots\} \cong \mathbb{N}\\).
3. **Espacios muestrales continuos (no numerables):** \\(|\Omega| = 2^{\aleph_0} = \mathfrak{c}\\).  
   *Ejemplo:* El tiempo de vida útil \\(T\\) de un componente electrónico: \\(\Omega = [0, \infty) \subset \mathbb{R}\\); o las coordenadas \\((x, y)\\) del impacto de un dardo en un círculo unitario: \\(\Omega = \{(x,y) \in \mathbb{R}^2 : x^2 + y^2 \le 1\}\\).

---

## 1.2.2 Álgebra de eventos

Un **evento** o suceso es una afirmación o proposición lógica sobre el resultado del experimento que puede verificarse empíricamente. Matemáticamente, un evento se modela como un subconjunto \\(A \subseteq \Omega\\). Decimos que el evento \\(A\\) **ocurre** si el resultado elemental observado \\(\omega\\) pertenece a \\(A\\) (es decir, \\(\omega \in A\\)).

### Operaciones con eventos

Sean \\(A, B \subseteq \Omega\\) dos eventos:
- **Evento seguro (universal):** \\(\Omega\\) (siempre ocurre).
- **Evento imposible (nulo):** \\(\emptyset\\) (nunca ocurre).
- **Complemento (negación):** \\(A^c = \Omega \setminus A = \{\omega \in \Omega : \omega \notin A\}\\). Ocurre si y solo si \\(A\\) no ocurre.
- **Unión (disyunción lógica):** \\(A \cup B = \{\omega \in \Omega : \omega \in A \text{ o } \omega \in B\}\\). Ocurre si al menos uno de los dos eventos ocurre.
- **Intersección (conjunción lógica):** \\(A \cap B = \{\omega \in \Omega : \omega \in A \text{ y } \omega \in B\}\\). Ocurre si ambos eventos ocurren simultáneamente.
- **Diferencia relativa:** \\(A \setminus B = A \cap B^c = \{\omega \in \Omega : \omega \in A \text{ y } \omega \notin B\}\\). Ocurre si ocurre \\(A\\) pero no \\(B\\).
- **Diferencia simétrica (disyunción exclusiva):** \\(A \mathbin{\Delta} B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)\\).
- **Eventos mutuamente excluyentes (disjuntos):** \\(A \cap B = \emptyset\\). No pueden ocurrir simultáneamente.
- **Inclusión (implicación):** \\(A \subseteq B\\). La ocurrencia de \\(A\\) garantiza necesariamente la ocurrencia de \\(B\\).

**Leyes de De Morgan:** Para cualquier familia arbitraria (finita, numerable o no numerable) de eventos \\(\{A_i\}_{i \in I}\\):
\\[ \left(\bigcup_{i \in I} A_i\right)^c = \bigcap_{i \in I} A_i^c, \qquad \left(\bigcap_{i \in I} A_i\right)^c = \bigcup_{i \in I} A_i^c. \\]

---

## 1.2.3 Álgebras y σ-álgebras de eventos

En espacios finitos podemos considerar que *cualquier* subconjunto de \\(\Omega\\) es un evento legítimo, es decir, la familia de eventos es el conjunto potencia \\(\mathcal{P}(\Omega)\\). Sin embargo, cuando \\(\Omega\\) es un espacio continuo (como \\(\mathbb{R}\\) o \\(\mathbb{R}^n\\)), la paradoja de Banach-Tarski y la existencia de conjuntos no medibles de Vitali demuestran que es matemáticamente imposible asignar una medida de probabilidad coherente a *todos* los subconjuntos de \\(\mathcal{P}(\Omega)\\). Por ello, debemos restringir los eventos admisibles a una estructura algebraica adecuada: una **σ-álgebra**.

**Definición 1.12 (Álgebra de conjuntos).** Sea \\(\Omega\\) un conjunto no vacío. Una familia \\(\mathcal{A} \subseteq \mathcal{P}(\Omega)\\) es un **álgebra** (o campo) sobre \\(\Omega\\) si satisface:
1. \\(\Omega \in \mathcal{A}\\).
2. Si \\(A \in \mathcal{A}\\), entonces \\(A^c \in \mathcal{A}\\) (cerradura bajo complementos).
3. Si \\(A, B \in \mathcal{A}\\), entonces \\(A \cup B \in \mathcal{A}\\) (cerradura bajo uniones finitas).

**Definición 1.13 (σ-álgebra).** Sea \\(\Omega\\) un conjunto no vacío. Una familia \\(\mathcal{F} \subseteq \mathcal{P}(\Omega)\\) es una **σ-álgebra** (o campo de Borel) sobre \\(\Omega\\) si satisface:
1. \\(\Omega \in \mathcal{F}\\).
2. Si \\(A \in \mathcal{F}\\), entonces \\(A^c \in \mathcal{F}\\) (cerradura bajo complementos).
3. Si \\(\{A_n\}_{n=1}^{\infty} \subseteq \mathcal{F}\\) es una sucesión numerable de conjuntos en \\(\mathcal{F}\\), entonces:
   \\[ \bigcup_{n=1}^{\infty} A_n \in \mathcal{F} \quad \text{(cerradura bajo uniones numerables)}. \\]

El par \\((\Omega, \mathcal{F})\\) recibe el nombre de **espacio medible**, y los elementos de \\(\mathcal{F}\\) se denominan **conjuntos medibles** o **eventos**.

**Proposición 1.14 (Propiedades elementales de una σ-álgebra).** *Sea \\(\mathcal{F}\\) una σ-álgebra sobre \\(\Omega\\). Entonces:*
1. \\(\emptyset \in \mathcal{F}\\).
2. Si \\(A_1, \dots, A_k \in \mathcal{F}\\), entonces \\(\bigcup_{i=1}^k A_i \in \mathcal{F}\\) (cerradura finita).
3. Si \\(\{A_n\}_{n=1}^{\infty} \subseteq \mathcal{F}\\), entonces \\(\bigcap_{n=1}^{\infty} A_n \in \mathcal{F}\\) (cerradura bajo intersecciones numerables).
4. Si \\(A, B \in \mathcal{F}\\), entonces \\(A \setminus B \in \mathcal{F}\\) y \\(A \mathbin{\Delta} B \in \mathcal{F}\\).

*Demostración.*
1. Por el axioma 1, \\(\Omega \in \mathcal{F}\\). Por el axioma 2, \\(\Omega^c = \emptyset \in \mathcal{F}\\).
2. Tomando la sucesión \\(A_1, A_2, \dots, A_k, \emptyset, \emptyset, \dots\\), su unión infinita coincide con \\(\bigcup_{i=1}^k A_i\\), que pertenece a \\(\mathcal{F}\\) por el axioma 3.
3. Por las leyes de De Morgan:
   \\[ \bigcap_{n=1}^{\infty} A_n = \left(\bigcup_{n=1}^{\infty} A_n^c\right)^c. \\]
   Como cada \\(A_n \in \mathcal{F}\\), su complemento \\(A_n^c \in \mathcal{F}\\). Por cerradura bajo uniones numerables, \\(\bigcup_{n=1}^{\infty} A_n^c \in \mathcal{F}\\), y su complemento final pertenece a \\(\mathcal{F}\\).
4. Como \\(A \setminus B = A \cap B^c\\), al ser \\(B^c \in \mathcal{F}\\), la intersección finita pertenece a \\(\mathcal{F}\\). Análogamente, \\(A \mathbin{\Delta} B = (A \setminus B) \cup (B \setminus A) \in \mathcal{F}\\). \\(\blacksquare\\)

### Ejemplos notables de σ-álgebras

1. **σ-álgebra trivial (mínima):** \\(\mathcal{F}_{\text{min}} = \{\emptyset, \Omega\}\\).
2. **σ-álgebra discreta (máxima):** \\(\mathcal{F}_{\text{max}} = \mathcal{P}(\Omega)\\).
3. **σ-álgebra generada por un evento \\(A \subseteq \Omega\\):** \\(\mathcal{F}_A = \{\emptyset, A, A^c, \Omega\}\\).
4. **σ-álgebra de una partición finita:** Si \\(\Omega = \bigcup_{i=1}^k B_i\\) con \\(B_i \cap B_j = \emptyset\\) para \\(i \neq j\\), la σ-álgebra generada por la partición consiste en todas las uniones de elementos de la partición (incluyendo la unión vacía \\(\emptyset\\)), conteniendo exactamente \\(2^k\\) eventos.

---

## 1.2.4 σ-álgebra generada y la σ-álgebra de Borel

**Teorema 1.15.** *La intersección arbitraria de cualquier colección de σ-álgebras sobre \\(\Omega\\) es también una σ-álgebra sobre \\(\Omega\\).*

*Demostración.* Sea \\(\{\mathcal{F}_i\}_{i \in I}\\) una familia no vacía de σ-álgebras sobre \\(\Omega\\), y definamos \\(\mathcal{F} = \bigcap_{i \in I} \mathcal{F}_i\\).
1. Como \\(\Omega \in \mathcal{F}_i\\) para todo \\(i \in I\\), se tiene \\(\Omega \in \mathcal{F}\\).
2. Si \\(A \in \mathcal{F}\\), entonces \\(A \in \mathcal{F}_i\\) para todo \\(i\\). Como cada \\(\mathcal{F}_i\\) es σ-álgebra, \\(A^c \in \mathcal{F}_i\\) para todo \\(i\\), luego \\(A^c \in \mathcal{F}\\).
3. Si \\(\{A_n\}_{n=1}^{\infty} \subseteq \mathcal{F}\\), entonces \\(\{A_n\}_{n=1}^{\infty} \subseteq \mathcal{F}_i\\) para todo \\(i\\). Por cerradura en cada \\(\mathcal{F}_i\\), \\(\bigcup_{n=1}^{\infty} A_n \in \mathcal{F}_i\\) para todo \\(i\\), por ende \\(\bigcup_{n=1}^{\infty} A_n \in \mathcal{F}\\). \\(\blacksquare\\)

**Definición 1.16 (σ-álgebra generada).** Sea \\(\mathcal{C} \subseteq \mathcal{P}(\Omega)\\) una clase arbitraria de subconjuntos de \\(\Omega\\). La **σ-álgebra generada por \\(\mathcal{C}\\)**, denotada por \\(\sigma(\mathcal{C})\\), es la menor σ-álgebra sobre \\(\Omega\\) que contiene a \\(\mathcal{C}\\):
\\[ \sigma(\mathcal{C}) = \bigcap \{\mathcal{G} \subseteq \mathcal{P}(\Omega) : \mathcal{G} \text{ es una } \sigma\text{-álgebra y } \mathcal{C} \subseteq \mathcal{G}\}. \\]

### La σ-álgebra de Borel sobre la recta real y espacios euclidianos

Cuando el espacio muestral es la recta real \\(\mathbb{R}\\), la topología usual (generada por los intervalos abiertos) nos proporciona la estructura natural.

**Definición 1.17 (σ-álgebra de Borel en ℝ).** La **σ-álgebra de Borel** sobre \\(\mathbb{R}\\), denotada por \\(\mathcal{B}(\mathbb{R})\\) o simplemente \\(\mathcal{B}\\), es la σ-álgebra generada por la clase de todos los conjuntos abiertos de \\(\mathbb{R}\\):
\\[ \mathcal{B}(\mathbb{R}) = \sigma(\{\text{abiertos de } \mathbb{R}\}). \\]
A los elementos de \\(\mathcal{B}(\mathbb{R})\\) se les llama **conjuntos borelianos**.

**Proposición 1.18.** *La \\(\sigma\\)-álgebra de Borel \\(\mathcal{B}(\mathbb{R})\\) puede ser generada equivalentemente por cualquiera de las siguientes familias de intervalos:*
1. \\(\mathcal{C}_1 = \{(a, b) : a < b, a, b \in \mathbb{R}\}\\) (intervalos abiertos).
2. \\(\mathcal{C}_2 = \{[a, b] : a \le b, a, b \in \mathbb{R}\}\\) (intervalos cerrados).
3. \\(\mathcal{C}_3 = \{(-\infty, x] : x \in \mathbb{R}\}\\) (rayos izquierdos cerrados).
4. \\(\mathcal{C}_4 = \{(-\infty, x) : x \in \mathbb{R}\}\\) (rayos izquierdos abiertos).

*Demostración (caso \\(\mathcal{C}_3\\)).*
- Todo rayo abierto \\((-\infty, x)\\) se escribe como la unión numerable de rayos cerrados:
  \\[ (-\infty, x) = \bigcup_{n=1}^{\infty} \left(-\infty, x - \frac{1}{n}\right]. \\]
  Por tanto, \\(\sigma(\mathcal{C}_4) \subseteq \sigma(\mathcal{C}_3)\\).
- Cualquier intervalo semiabierto \\((a, b]\\) se expresa como diferencia de rayos:
  \\[ (a, b] = (-\infty, b] \setminus (-\infty, a] \in \sigma(\mathcal{C}_3). \\]
- Cualquier intervalo abierto \\((a, b)\\) se obtiene como unión numerable:
  \\[ (a, b) = \bigcup_{n=1}^{\infty} \left(a, b - \frac{1}{n}\right] \in \sigma(\mathcal{C}_3). \\]
- Como todo conjunto abierto en \\(\mathbb{R}\\) es la unión numerable disjunta de intervalos abiertos racionales, todo abierto pertenece a \\(\sigma(\mathcal{C}_3)\\). En consecuencia, \\(\mathcal{B}(\mathbb{R}) = \sigma(\mathcal{C}_3)\\). \\(\blacksquare\\)

Esta propiedad es crucial en probabilidad: garantiza que para definir rigurosamente una variable aleatoria o una función de distribución acumulada \\(F(x) = \mathbb{P}(X \le x) = \mathbb{P}(X \in (-\infty, x])\\), basta con especificar las probabilidades sobre los rayos \\((-\infty, x]\\).

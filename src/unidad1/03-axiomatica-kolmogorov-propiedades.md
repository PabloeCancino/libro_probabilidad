# 1.3 Axiomática de Kolmogórov y propiedades fundamentales

## 1.3.1 La terna axiomática de Kolmogórov

En 1933, Andréi N. Kolmogórov formuló la fundamentación axiomática definitiva de la probabilidad como una rama de la teoría de la medida.

**Definición 1.19 (Espacio de probabilidad de Kolmogórov).** Un **espacio de probabilidad** es una terna \\((\Omega, \mathcal{F}, \mathbb{P})\\), donde:
1. \\(\Omega\\) es el espacio muestral (conjunto no vacío).
2. \\(\mathcal{F}\\) es una \\(\sigma\\)-álgebra de subconjuntos de \\(\Omega\\) (los eventos medibles).
3. \\(\mathbb{P} : \mathcal{F} \to [0, 1]\\) es una función de conjunto, denominada **medida de probabilidad**, que satisface los tres **Axiomas de Kolmogórov**:

> **Axioma 1 (No negatividad):** Para todo evento \\(A \in \mathcal{F}\\):
> \\[ \mathbb{P}(A) \ge 0. \\]
>
> **Axioma 2 (Normalización / Certidumbre):** La probabilidad del evento seguro es 1:
> \\[ \mathbb{P}(\Omega) = 1. \\]
>
> **Axioma 3 (σ-aditividad o aditividad numerable):** Para cualquier sucesión infinita de eventos disjuntos dos a dos en \\(\mathcal{F}\\) (es decir, \\(A_i \cap A_j = \emptyset\\) para todo \\(i \neq j\\)):
> \\[ \mathbb{P}\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mathbb{P}(A_n). \\]

---

## 1.3.2 Teoremas y propiedades fundamentales deducidas

A partir de los tres axiomas de Kolmogórov, demostramos sistemáticamente todas las propiedades operativas del cálculo de probabilidades.

### 1. Probabilidad del evento imposible

**Teorema 1.20.** *La probabilidad del evento imposible \\(\emptyset\\) es cero:*
\\[ \mathbb{P}(\emptyset) = 0. \\]

*Demostración.* Consideremos la sucesión de eventos \\(A_1 = \Omega\\), y \\(A_n = \emptyset\\) para todo \\(n \ge 2\\). Como \\(\Omega \cap \emptyset = \emptyset\\) y \\(\emptyset \cap \emptyset = \emptyset\\), los eventos son disjuntos dos a dos. Su unión es:
\\[ \bigcup_{n=1}^{\infty} A_n = \Omega \cup \emptyset \cup \emptyset \cup \dots = \Omega. \\]
Aplicando el Axioma 3:
\\[ \mathbb{P}(\Omega) = \mathbb{P}\left(\bigcup_{n=1}^{\infty} A_n\right) = \mathbb{P}(\Omega) + \sum_{n=2}^{\infty} \mathbb{P}(\emptyset). \\]
Por el Axioma 2, \\(\mathbb{P}(\Omega) = 1\\), luego:
\\[ 1 = 1 + \sum_{n=2}^{\infty} \mathbb{P}(\emptyset) \implies \sum_{n=2}^{\infty} \mathbb{P}(\emptyset) = 0. \\]
Dado que por el Axioma 1 \\(\mathbb{P}(\emptyset) \ge 0\\), una serie infinita de términos no negativos solo puede sumar cero si cada término es idénticamente cero. Por tanto, \\(\mathbb{P}(\emptyset) = 0\\). \\(\blacksquare\\)

### 2. Aditividad finita

**Corolario 1.21.** *Si \\(A_1, A_2, \dots, A_k \in \mathcal{F}\\) son eventos disjuntos dos a dos (\\(A_i \cap A_j = \emptyset\\) para \\(i \neq j\\)), entonces:*
\\[ \mathbb{P}\left(\bigcup_{i=1}^k A_i\right) = \sum_{i=1}^k \mathbb{P}(A_i). \\]

*Demostración.* Definamos la sucesión infinita \\(B_n\\) tal que \\(B_i = A_i\\) para \\(i = 1, \dots, k\\) y \\(B_n = \emptyset\\) para todo \\(n > k\\). Como los \\(B_n\\) son disjuntos dos a dos, por el Axioma 3 y el Teorema 1.20:
\\[ \mathbb{P}\left(\bigcup_{i=1}^k A_i\right) = \mathbb{P}\left(\bigcup_{n=1}^{\infty} B_n\right) = \sum_{i=1}^k \mathbb{P}(A_i) + \sum_{n=k+1}^{\infty} \mathbb{P}(\emptyset) = \sum_{i=1}^k \mathbb{P}(A_i) + 0 = \sum_{i=1}^k \mathbb{P}(A_i). \quad \blacksquare \\]

### 3. Regla del complemento

**Teorema 1.22.** *Para cualquier evento \\(A \in \mathcal{F}\\):*
\\[ \mathbb{P}(A^c) = 1 - \mathbb{P}(A). \\]

*Demostración.* Como \\(A \cup A^c = \Omega\\) y \\(A \cap A^c = \emptyset\\), por aditividad finita (Corolario 1.21):
\\[ \mathbb{P}(\Omega) = \mathbb{P}(A \cup A^c) = \mathbb{P}(A) + \mathbb{P}(A^c). \\]
Como \\(\mathbb{P}(\Omega) = 1\\), tenemos \\(1 = \mathbb{P}(A) + \mathbb{P}(A^c)\\), lo que implica \\(\mathbb{P}(A^c) = 1 - \mathbb{P}(A)\\). \\(\blacksquare\\)

### 4. Probabilidad de la diferencia relativa

**Teorema 1.23.** *Para cualesquiera eventos \\(A, B \in \mathcal{F}\\):*
\\[ \mathbb{P}(A \setminus B) = \mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B). \\]

*Demostración.* El evento \\(A\\) puede descomponerse en la unión de dos eventos disjuntos:
\\[ A = (A \setminus B) \cup (A \cap B), \quad \text{con } (A \setminus B) \cap (A \cap B) = \emptyset. \\]
Por aditividad finita:
\\[ \mathbb{P}(A) = \mathbb{P}(A \setminus B) + \mathbb{P}(A \cap B) \implies \mathbb{P}(A \setminus B) = \mathbb{P}(A) - \mathbb{P}(A \cap B). \quad \blacksquare \\]

### 5. Monotonía de la medida de probabilidad

**Teorema 1.24 (Monotonía).** *Si \\(A, B \in \mathcal{F}\\) con \\(A \subseteq B\\), entonces:*
1. \\(\mathbb{P}(A) \le \mathbb{P}(B)\\).
2. \\(\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A)\\).

*Demostración.* Como \\(A \subseteq B\\), se tiene \\(A \cap B = A\\). Por el Teorema 1.23:
\\[ \mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A \cap B) = \mathbb{P}(B) - \mathbb{P}(A). \\]
Dado que por el Axioma 1 \\(\mathbb{P}(B \setminus A) \ge 0\\), se sigue que \\(\mathbb{P}(B) - \mathbb{P}(A) \ge 0 \implies \mathbb{P}(A) \le \mathbb{P}(B)\\). \\(\blacksquare\\)

Como consecuencia inmediata, para cualquier evento \\(A \in \mathcal{F}\\), como \\(\emptyset \subseteq A \subseteq \Omega\\), se tiene:
\\[ 0 \le \mathbb{P}(A) \le 1. \\]

### 6. Regla de adición para dos eventos

**Teorema 1.25 (Regla de la suma general).** *Para cualesquiera eventos \\(A, B \in \mathcal{F}\\):*
\\[ \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B). \\]

*Demostración.* Podemos escribir \\(A \cup B\\) como la unión disjunta de dos conjuntos:
\\[ A \cup B = A \cup (B \setminus A), \quad \text{donde } A \cap (B \setminus A) = \emptyset. \\]
Por aditividad finita y aplicando el Teorema 1.23:
\\[ \mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B \setminus A) = \mathbb{P}(A) + [\mathbb{P}(B) - \mathbb{P}(A \cap B)] = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B). \quad \blacksquare \\]

---

## 1.3.3 Principio de inclusión-exclusión general

El Teorema 1.25 se generaliza para la unión de cualquier número finito \\(n\\) de eventos.

**Teorema 1.26 (Principio de inclusión-exclusión de Poincaré).** *Para cualquier colección finita de eventos \\(A_1, A_2, \dots, A_n \in \mathcal{F}\\):*
\\[ \mathbb{P}\left(\bigcup_{i=1}^n A_i\right) = \sum_{k=1}^n (-1)^{k-1} \sum_{1 \le i_1 < i_2 < \dots < i_k \le n} \mathbb{P}(A_{i_1} \cap A_{i_2} \cap \dots \cap A_{i_k}). \\]
En particular, para \\(n = 3\\):
\\[ \begin{aligned} \mathbb{P}(A_1 \cup A_2 \cup A_3) = &\ \mathbb{P}(A_1) + \mathbb{P}(A_2) + \mathbb{P}(A_3) \\ &- [\mathbb{P}(A_1 \cap A_2) + \mathbb{P}(A_1 \cap A_3) + \mathbb{P}(A_2 \cap A_3)] \\ &+ \mathbb{P}(A_1 \cap A_2 \cap A_3). \end{aligned} \\]

*Demostración (por funciones indicadoras).*  
Recordemos que la función indicadora \\(\mathbb{I}_A(\omega)\\) vale 1 si \\(\omega \in A\\) y 0 si \\(\omega \notin A\\), y cumple \\(\mathbb{E}[\mathbb{I}_A] = \mathbb{P}(A)\\).  
Para \\(A = \bigcup_{i=1}^n A_i\\), su complemento es \\(A^c = \bigcap_{i=1}^n A_i^c\\). Por tanto:
\\[ 1 - \mathbb{I}_A(\omega) = \mathbb{I}_{A^c}(\omega) = \prod_{i=1}^n (1 - \mathbb{I}_{A_i}(\omega)). \\]
Expandiendo el producto algebraico:
\\[ \prod_{i=1}^n (1 - \mathbb{I}_{A_i}(\omega)) = 1 - \sum_{i=1}^n \mathbb{I}_{A_i}(\omega) + \sum_{1 \le i < j \le n} \mathbb{I}_{A_i \cap A_j}(\omega) - \dots + (-1)^n \mathbb{I}_{A_1 \cap \dots \cap A_n}(\omega). \\]
Despejando \\(\mathbb{I}_A(\omega)\\) y tomando esperanza (o integrando respecto a la medida \\(\mathbb{P}\\)), obtenemos la fórmula exacta de inclusión-exclusión. \\(\blacksquare\\)

### Subaditividad (Desigualdad de Boole)

**Teorema 1.27 (Desigualdad de Boole).** *Para cualquier sucesión finita o numerable de eventos \\(\{A_n\}_{n=1}^{\infty} \subseteq \mathcal{F}\\):*
\\[ \mathbb{P}\left(\bigcup_{n=1}^{\infty} A_n\right) \le \sum_{n=1}^{\infty} \mathbb{P}(A_n). \\]

*Demostración.* Definamos una sucesión disjunta \\(B_n\\) mediante la técnica de disyuntivación estándar:
\\[ B_1 = A_1, \quad B_n = A_n \setminus \left(\bigcup_{k=1}^{n-1} A_k\right) = A_n \cap A_1^c \cap \dots \cap A_{n-1}^c \quad \text{para } n \ge 2. \\]
Por construcción, los \\(B_n\\) son disjuntos dos a dos, \\(B_n \subseteq A_n\\) para todo \\(n\\), y \\(\bigcup_{n=1}^{\infty} B_n = \bigcup_{n=1}^{\infty} A_n\\).  
Aplicando el Axioma 3 y la monotonía (Teorema 1.24):
\\[ \mathbb{P}\left(\bigcup_{n=1}^{\infty} A_n\right) = \mathbb{P}\left(\bigcup_{n=1}^{\infty} B_n\right) = \sum_{n=1}^{\infty} \mathbb{P}(B_n) \le \sum_{n=1}^{\infty} \mathbb{P}(A_n). \quad \blacksquare \\]

---

## 1.3.4 Continuidad de la medida de probabilidad

Una de las propiedades más poderosas de la \\(\sigma\\)-aditividad es que permite intercambiar el operador de probabilidad con el paso al límite de sucesiones monótonas de eventos.

**Definición 1.28 (Sucesiones monótonas de eventos).**
1. Una sucesión \\(\{A_n\}_{n=1}^{\infty}\\) es **creciente** (o monótona no decreciente), denotada \\(A_n \uparrow A\\), si \\(A_1 \subseteq A_2 \subseteq A_3 \subseteq \dots\\) y \\(A = \bigcup_{n=1}^{\infty} A_n\\).
2. Una sucesión \\(\{A_n\}_{n=1}^{\infty}\\) es **decreciente** (o monótona no creciente), denotada \\(A_n \downarrow A\\), si \\(A_1 \supseteq A_2 \supseteq A_3 \supseteq \dots\\) y \\(A = \bigcap_{n=1}^{\infty} A_n\\).

**Teorema 1.29 (Continuidad de la probabilidad).**
1. **(Continuidad desde abajo):** Si \\(A_n \uparrow A\\), entonces:
   \\[ \lim_{n \to \infty} \mathbb{P}(A_n) = \mathbb{P}(A) = \mathbb{P}\left(\bigcup_{n=1}^{\infty} A_n\right). \\]
2. **(Continuidad desde arriba):** Si \\(A_n \downarrow A\\), entonces:
   \\[ \lim_{n \to \infty} \mathbb{P}(A_n) = \mathbb{P}(A) = \mathbb{P}\left(\bigcap_{n=1}^{\infty} A_n\right). \\]

*Demostración.*
1. Sea \\(A_n \uparrow A\\). Definamos la sucesión disjunta \\(B_1 = A_1\\) y \\(B_n = A_n \setminus A_{n-1}\\) para \\(n \ge 2\\).  
   Como \\(A_k \subseteq A_{k+1}\\), se verifica \\(A_n = \bigcup_{k=1}^n B_k\\) (unión disjunta finita), de modo que \\(\mathbb{P}(A_n) = \sum_{k=1}^n \mathbb{P}(B_k)\\).  
   Asimismo, \\(A = \bigcup_{n=1}^{\infty} A_n = \bigcup_{k=1}^{\infty} B_k\\). Por el Axioma 3:
   \\[ \mathbb{P}(A) = \sum_{k=1}^{\infty} \mathbb{P}(B_k) = \lim_{n \to \infty} \sum_{k=1}^n \mathbb{P}(B_k) = \lim_{n \to \infty} \mathbb{P}(A_n). \\]
2. Sea \\(A_n \downarrow A\\). Entonces los complementos forman una sucesión creciente: \\(A_n^c \uparrow A^c\\). Por la parte 1 y la regla del complemento:
   \\[ \lim_{n \to \infty} \mathbb{P}(A_n^c) = \mathbb{P}(A^c) \implies \lim_{n \to \infty} (1 - \mathbb{P}(A_n)) = 1 - \mathbb{P}(A) \implies \lim_{n \to \infty} \mathbb{P}(A_n) = \mathbb{P}(A). \quad \blacksquare \\]

**Teorema 1.30 (Equivalencia de la σ-aditividad).** *Sobre un álgebra de conjuntos \\(\mathcal{A}\\), una función aditiva finita \\(\mathbb{P}\\) con \\(\mathbb{P}(\Omega) = 1\\) es \\(\sigma\\)-aditiva si y solo si es continua en \\(\emptyset\\) (es decir, \\(A_n \downarrow \emptyset \implies \lim_{n \to \infty} \mathbb{P}(A_n) = 0\\)).*

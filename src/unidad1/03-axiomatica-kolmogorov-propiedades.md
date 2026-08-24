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
> **Axioma 3 (σ-aditividad o aditividad numerable):** Para cualquier sucesión infinita de eventos disjuntos dos a dos en \\(\mathcal{F}\\) (es decir, \\(A\_i \cap A\_j = \emptyset\\) para todo \\(i \neq j\\)):
> \\[ \mathbb{P}\left(\bigcup_{n=1}^{\infty} A_n\right) = \sum_{n=1}^{\infty} \mathbb{P}(A_n). \\]

---

## 1.3.2 Teoremas y propiedades fundamentales deducidas

A partir de los tres axiomas de Kolmogórov, demostramos sistemáticamente todas las propiedades operativas del cálculo de probabilidades.

### 1. Probabilidad del evento imposible

**Teorema 1.20.** *La probabilidad del evento imposible \\(\emptyset\\) es cero:*

\\[
\mathbb{P}(\emptyset) = 0.
\\]

*Demostración.* Consideremos la sucesión de eventos \\(A\_1 = \Omega\\), y \\(A\_n = \emptyset\\) para todo \\(n \ge 2\\). Como \\(\Omega \cap \emptyset = \emptyset\\) y \\(\emptyset \cap \emptyset = \emptyset\\), los eventos son disjuntos dos a dos. Su unión es:

\\[
\bigcup\_{n=1}^{\infty} A\_n = \Omega \cup \emptyset \cup \emptyset \cup \dots = \Omega.
\\]

Aplicando el Axioma 3:

\\[
\mathbb{P}(\Omega) = \mathbb{P}\left(\bigcup\_{n=1}^{\infty} A\_n\right) = \mathbb{P}(\Omega) + \sum\_{n=2}^{\infty} \mathbb{P}(\emptyset).
\\]

Por el Axioma 2, \\(\mathbb{P}(\Omega) = 1\\), luego:

\\[
1 = 1 + \sum\_{n=2}^{\infty} \mathbb{P}(\emptyset) \implies \sum\_{n=2}^{\infty} \mathbb{P}(\emptyset) = 0.
\\]

Dado que por el Axioma 1 \\(\mathbb{P}(\emptyset) \ge 0\\), una serie infinita de términos no negativos solo puede sumar cero si cada término es idénticamente cero. Por tanto, \\(\mathbb{P}(\emptyset) = 0\\). \\(\blacksquare\\)

### 2. Aditividad finita

**Corolario 1.21.** *Si \\(A\_1, A\_2, \dots, A\_k \in \mathcal{F}\\) son eventos disjuntos dos a dos (\\(A\_i \cap A\_j = \emptyset\\) para \\(i \neq j\\)), entonces:*

\\[
\mathbb{P}\left(\bigcup\_{i=1}^k A\_i\right) = \sum\_{i=1}^k \mathbb{P}(A\_i).
\\]

*Demostración.* Definamos la sucesión infinita \\(B\_n\\) tal que \\(B\_i = A\_i\\) para \\(i = 1, \dots, k\\) y \\(B\_n = \emptyset\\) para todo \\(n > k\\). Como los \\(B\_n\\) son disjuntos dos a dos, por el Axioma 3 y el Teorema 1.20:

\\[
\mathbb{P}\left(\bigcup\_{i=1}^k A\_i\right) = \mathbb{P}\left(\bigcup\_{n=1}^{\infty} B\_n\right) = \sum\_{i=1}^k \mathbb{P}(A\_i) + \sum\_{n=k+1}^{\infty} \mathbb{P}(\emptyset) = \sum\_{i=1}^k \mathbb{P}(A\_i) + 0 = \sum\_{i=1}^k \mathbb{P}(A\_i). \quad \blacksquare
\\]

### 3. Regla del complemento

**Teorema 1.22.** *Para cualquier evento \\(A \in \mathcal{F}\\):*

\\[
\mathbb{P}(A^c) = 1 - \mathbb{P}(A).
\\]

*Demostración.* Como \\(A \cup A^c = \Omega\\) y \\(A \cap A^c = \emptyset\\), por aditividad finita (Corolario 1.21):

\\[
\mathbb{P}(\Omega) = \mathbb{P}(A \cup A^c) = \mathbb{P}(A) + \mathbb{P}(A^c).
\\]

Como \\(\mathbb{P}(\Omega) = 1\\), tenemos \\(1 = \mathbb{P}(A) + \mathbb{P}(A^c)\\), lo que implica \\(\mathbb{P}(A^c) = 1 - \mathbb{P}(A)\\). \\(\blacksquare\\)

### 4. Probabilidad de la diferencia relativa

**Teorema 1.23.** *Para cualesquiera eventos \\(A, B \in \mathcal{F}\\):*

\\[
\mathbb{P}(A \setminus B) = \mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B).
\\]

*Demostración.* El evento \\(A\\) puede descomponerse en la unión de dos eventos disjuntos:

\\[
A = (A \setminus B) \cup (A \cap B), \quad \text{con } (A \setminus B) \cap (A \cap B) = \emptyset.
\\]

Por aditividad finita:

\\[
\mathbb{P}(A) = \mathbb{P}(A \setminus B) + \mathbb{P}(A \cap B) \implies \mathbb{P}(A \setminus B) = \mathbb{P}(A) - \mathbb{P}(A \cap B). \quad \blacksquare
\\]

### 5. Monotonía de la medida de probabilidad

**Teorema 1.24 (Monotonía).** *Si \\(A, B \in \mathcal{F}\\) con \\(A \subseteq B\\), entonces:*
1. \\(\mathbb{P}(A) \le \mathbb{P}(B)\\).
2. \\(\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A)\\).

*Demostración.* Como \\(A \subseteq B\\), se tiene \\(A \cap B = A\\). Por el Teorema 1.23:

\\[
\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A \cap B) = \mathbb{P}(B) - \mathbb{P}(A).
\\]

Dado que por el Axioma 1 \\(\mathbb{P}(B \setminus A) \ge 0\\), se sigue que \\(\mathbb{P}(B) - \mathbb{P}(A) \ge 0 \implies \mathbb{P}(A) \le \mathbb{P}(B)\\). \\(\blacksquare\\)

Como consecuencia inmediata, para cualquier evento \\(A \in \mathcal{F}\\), como \\(\emptyset \subseteq A \subseteq \Omega\\), se tiene:

\\[
0 \le \mathbb{P}(A) \le 1.
\\]

### 6. Regla de adición para dos eventos

**Teorema 1.25 (Regla de la suma general).** *Para cualesquiera eventos \\(A, B \in \mathcal{F}\\):*

\\[
\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B).
\\]

*Demostración.* Podemos escribir \\(A \cup B\\) como la unión disjunta de dos conjuntos:

\\[
A \cup B = A \cup (B \setminus A), \quad \text{donde } A \cap (B \setminus A) = \emptyset.
\\]

Por aditividad finita y aplicando el Teorema 1.23:

\\[
\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B \setminus A) = \mathbb{P}(A) + [\mathbb{P}(B) - \mathbb{P}(A \cap B)] = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B). \quad \blacksquare
\\]

---

## 1.3.3 Principio de inclusión-exclusión general

El Teorema 1.25 se generaliza para la unión de cualquier número finito \\(n\\) de eventos.

**Teorema 1.26 (Principio de inclusión-exclusión de Poincaré).** *Para cualquier colección finita de eventos \\(A\_1, A\_2, \dots, A\_n \in \mathcal{F}\\):*

\\[
\mathbb{P}\left(\bigcup\_{i=1}^n A\_i\right) = \sum\_{k=1}^n (-1)^{k-1} \sum\_{1 \le i\_1 < i\_2 < \dots < i\_k \le n} \mathbb{P}(A\_{i\_1} \cap A\_{i\_2} \cap \dots \cap A\_{i\_k}).
\\]

En particular, para \\(n = 3\\):

\\[
\begin{aligned}
\mathbb{P}(A\_1 \cup A\_2 \cup A\_3) &= \mathbb{P}(A\_1) + \mathbb{P}(A\_2) + \mathbb{P}(A\_3) \\\\
&\quad - [\mathbb{P}(A\_1 \cap A\_2) + \mathbb{P}(A\_1 \cap A\_3) + \mathbb{P}(A\_2 \cap A\_3)] \\\\
&\quad + \mathbb{P}(A\_1 \cap A\_2 \cap A\_3).
\end{aligned}
\\]

*Demostración (por funciones indicadoras).*  
Recordemos que la función indicadora \\(\mathbb{I}\_A(\omega)\\) vale 1 si \\(\omega \in A\\) y 0 si \\(\omega \notin A\\), y cumple \\(\mathbb{E}[\mathbb{I}\_A] = \mathbb{P}(A)\\).  
Para \\(A = \bigcup\_{i=1}^n A\_i\\), su complemento es \\(A^c = \bigcap\_{i=1}^n A\_i^c\\). Por tanto:

\\[
1 - \mathbb{I}\_A(\omega) = \mathbb{I}\_{A^c}(\omega) = \prod\_{i=1}^n (1 - \mathbb{I}\_{A\_i}(\omega)).
\\]

Expandiendo el producto algebraico:

\\[
\prod\_{i=1}^n (1 - \mathbb{I}\_{A\_i}(\omega)) = 1 - \sum\_{i=1}^n \mathbb{I}\_{A\_i}(\omega) + \sum\_{1 \le i < j \le n} \mathbb{I}\_{A\_i \cap A\_j}(\omega) - \dots + (-1)^n \mathbb{I}\_{A\_1 \cap \dots \cap A\_n}(\omega).
\\]

Despejando \\(\mathbb{I}\_A(\omega)\\) y tomando esperanza (o integrando respecto a la medida \\(\mathbb{P}\\)), obtenemos la fórmula exacta de inclusión-exclusión. \\(\blacksquare\\)

### Subaditividad (Desigualdad de Boole)

**Teorema 1.27 (Desigualdad de Boole).** *Para cualquier sucesión finita o numerable de eventos \\((A\_n)\_{n=1}^{\infty} \subseteq \mathcal{F}\\):*

\\[
\mathbb{P}\left(\bigcup\_{n=1}^{\infty} A\_n\right) \le \sum\_{n=1}^{\infty} \mathbb{P}(A\_n).
\\]

*Demostración.* Definamos una sucesión disjunta \\(B\_n\\) mediante la técnica de disyuntivación estándar:

\\[
B\_1 = A\_1, \quad B\_n = A\_n \setminus \left(\bigcup\_{k=1}^{n-1} A\_k\right) = A\_n \cap A\_1^c \cap \dots \cap A\_{n-1}^c \quad \text{para } n \ge 2.
\\]

Por construcción, los \\(B\_n\\) son disjuntos dos a dos, \\(B\_n \subseteq A\_n\\) para todo \\(n\\), y \\(\bigcup\_{n=1}^{\infty} B\_n = \bigcup\_{n=1}^{\infty} A\_n\\).  
Aplicando el Axioma 3 y la monotonía (Teorema 1.24):

\\[
\mathbb{P}\left(\bigcup\_{n=1}^{\infty} A\_n\right) = \mathbb{P}\left(\bigcup\_{n=1}^{\infty} B\_n\right) = \sum\_{n=1}^{\infty} \mathbb{P}(B\_n) \le \sum\_{n=1}^{\infty} \mathbb{P}(A\_n). \quad \blacksquare
\\]

---

## 1.3.4 Continuidad de la medida de probabilidad

Una de las propiedades más poderosas de la σ-aditividad es que permite intercambiar el operador de probabilidad con el paso al límite de sucesiones monótonas de eventos.

**Definición 1.28 (Sucesiones monótonas de eventos).**
1. Una sucesión \\((A\_n)\_{n=1}^{\infty}\\) es **creciente** (o monótona no decreciente), denotada \\(A\_n \uparrow A\\), si \\(A\_1 \subseteq A\_2 \subseteq A\_3 \subseteq \dots\\) y \\(A = \bigcup\_{n=1}^{\infty} A\_n\\).
2. Una sucesión \\((A\_n)\_{n=1}^{\infty}\\) es **decreciente** (o monótona no creciente), denotada \\(A\_n \downarrow A\\), si \\(A\_1 \supseteq A\_2 \supseteq A\_3 \supseteq \dots\\) y \\(A = \bigcap\_{n=1}^{\infty} A\_n\\).

**Teorema 1.29 (Continuidad de la probabilidad).**
1. **(Continuidad desde abajo):** Si \\(A\_n \uparrow A\\), entonces:

   \\[
   \lim\_{n \to \infty} \mathbb{P}(A\_n) = \mathbb{P}(A) = \mathbb{P}\left(\bigcup\_{n=1}^{\infty} A\_n\right).
   \\]

2. **(Continuidad desde arriba):** Si \\(A\_n \downarrow A\\), entonces:

   \\[
   \lim\_{n \to \infty} \mathbb{P}(A\_n) = \mathbb{P}(A) = \mathbb{P}\left(\bigcap\_{n=1}^{\infty} A\_n\right).
   \\]

*Demostración.*
1. Sea \\(A\_n \uparrow A\\). Definamos la sucesión disjunta \\(B\_1 = A\_1\\) y \\(B\_n = A\_n \setminus A\_{n-1}\\) para \\(n \ge 2\\).  
   Como \\(A\_k \subseteq A\_{k+1}\\), se verifica \\(A\_n = \bigcup\_{k=1}^n B\_k\\) (unión disjunta finita), de modo que \\(\mathbb{P}(A\_n) = \sum\_{k=1}^n \mathbb{P}(B\_k)\\).  
   Asimismo, \\(A = \bigcup\_{n=1}^{\infty} A\_n = \bigcup\_{k=1}^{\infty} B\_k\\). Por el Axioma 3:

   \\[
   \mathbb{P}(A) = \sum\_{k=1}^{\infty} \mathbb{P}(B\_k) = \lim\_{n \to \infty} \sum\_{k=1}^n \mathbb{P}(B\_k) = \lim\_{n \to \infty} \mathbb{P}(A\_n).
   \\]

2. Sea \\(A\_n \downarrow A\\). Entonces los complementos forman una sucesión creciente: \\(A\_n^c \uparrow A^c\\). Por la parte 1 y la regla del complemento:

   \\[
   \lim\_{n \to \infty} \mathbb{P}(A\_n^c) = \mathbb{P}(A^c) \implies \lim\_{n \to \infty} (1 - \mathbb{P}(A\_n)) = 1 - \mathbb{P}(A) \implies \lim\_{n \to \infty} \mathbb{P}(A\_n) = \mathbb{P}(A). \quad \blacksquare
   \\]

**Teorema 1.30 (Equivalencia de la σ-aditividad).** *Sobre un álgebra de conjuntos \\(\mathcal{A}\\), una función aditiva finita \\(\mathbb{P}\\) con \\(\mathbb{P}(\Omega) = 1\\) es \\(\sigma\\)-aditiva si y solo si es continua en \\(\emptyset\\) (es decir, \\(A\_n \downarrow \emptyset \implies \lim\_{n \to \infty} \mathbb{P}(A\_n) = 0\\)).*
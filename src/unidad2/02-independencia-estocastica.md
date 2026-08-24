# 2.2 Eventos independientes y propiedades

## 2.2.1 Definición de independencia estocástica

Intuitivamente, dos eventos \\(A\\) y \\(B\\) son independientes si la ocurrencia de uno de ellos no proporciona ninguna información sobre la ocurrencia del otro, es decir, \\(\mathbb{P}(A \mid B) = \mathbb{P}(A)\\).

Sin embargo, para evitar requerir que \\(\mathbb{P}(B) > 0\\) y para que la definición sea perfectamente simétrica respecto a ambos eventos, se formula mediante el producto de sus probabilidades.

**Definición 2.5 (Independencia de dos eventos).** Dos eventos \\(A, B \in \mathcal{F}\\) son **estocásticamente independientes** (denotado \\(A \perp B\\)) si y solo si:

\\[
\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B).
\\]

**Proposición 2.6.** *Si \\(\mathbb{P}(B) > 0\\), entonces \\(A \perp B \iff \mathbb{P}(A \mid B) = \mathbb{P}(A)\\).*

*Demostración.*
- \\((\implies)\\) Si \\(A \perp B\\), entonces \\(\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)\\). Por tanto:

  \\[
  \mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)} = \frac{\mathbb{P}(A)\mathbb{P}(B)}{\mathbb{P}(B)} = \mathbb{P}(A).
  \\]

- \\((\impliedby)\\) Si \\(\mathbb{P}(A \mid B) = \mathbb{P}(A)\\), multiplicando por \\(\mathbb{P}(B)\\) se obtiene inmediatamente \\(\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)\\). \\(\blacksquare\\)

---

## 2.2.2 Propiedades algebraicas de la independencia

**Teorema 2.7 (Independencia de complementos).** *Si \\(A\\) y \\(B\\) son eventos independientes, entonces:*
1. \\(A\\) y \\(B^c\\) son independientes.
2. \\(A^c\\) y \\(B\\) son independientes.
3. \\(A^c\\) y \\(B^c\\) son independientes.

*Demostración.*
1. Descomponiendo \\(A = (A \cap B) \cup (A \cap B^c)\\) en dos conjuntos disjuntos:

   \\[
   \mathbb{P}(A) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap B^c).
   \\]

   Dado que \\(A\\) y \\(B\\) son independientes, \\(\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)\\). Sustituyendo:

   \\[
   \mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B) = \mathbb{P}(A)(1 - \mathbb{P}(B)) = \mathbb{P}(A)\mathbb{P}(B^c).
   \\]

   Esto demuestra que \\(A \perp B^c\\).
2. Se deduce de la parte (1) por la simetría de la independencia.
3. Aplicando el resultado de la parte (1) a los eventos \\(B^c\\) y \\(A\\): como \\(B^c \perp A\\), se tiene \\(B^c \perp A^c\\), es decir, \\(\mathbb{P}(A^c \cap B^c) = \mathbb{P}(A^c)\mathbb{P}(B^c)\\). \\(\blacksquare\\)

**Proposición 2.8 (Eventos de probabilidad 0 o 1).** *Si \\(A \in \mathcal{F}\\) cumple \\(\mathbb{P}(A) = 0\\) o \\(\mathbb{P}(A) = 1\\), entonces \\(A\\) es independiente de cualquier otro evento \\(B \in \mathcal{F}\\).*

*Demostración.*
- Si \\(\mathbb{P}(A) = 0\\): como \\(A \cap B \subseteq A\\), por monotonía \\(0 \le \mathbb{P}(A \cap B) \le \mathbb{P}(A) = 0\\), luego \\(\mathbb{P}(A \cap B) = 0\\). Por otro lado, \\(\mathbb{P}(A)\mathbb{P}(B) = 0 \cdot \mathbb{P}(B) = 0\\). Se cumple \\(\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)\\).
- Si \\(\mathbb{P}(A) = 1\\): entonces \\(\mathbb{P}(A^c) = 0\\), luego por la parte anterior \\(A^c \perp B\\). Por el Teorema 2.7, \\(A \perp B\\). \\(\blacksquare\\)

---

## 2.2.3 Independencia mutua vs. independencia 2 a 2

Para una colección de más de dos eventos, la independencia por pares (dos a dos) **no es suficiente** para garantizar la independencia conjunta (mutua).

**Definición 2.9 (Independencia mutua o colectiva).** Una familia de \\(n\\) eventos \\(A\_1, A\_2, \dots, A\_n \in \mathcal{F}\\) es **mutuamente independiente** si para todo subconjunto de índices \\(\{i\_1, i\_2, \dots, i\_k\} \subseteq \{1, 2, \dots, n\}\\) con \\(2 \le k \le n\\), se satisface:

\\[
\mathbb{P}\left(\bigcap\_{j=1}^k A\_{i\_j}\right) = \prod\_{j=1}^k \mathbb{P}(A\_{i\_j}).
\\]

(Esto requiere verificar un total de \\(2^n - n - 1\\) ecuaciones de producto).

**Definición 2.10 (Independencia dos a dos o por pares).** La familia \\(A\_1, \dots, A\_n\\) es **independiente dos a dos** si:

\\[
\mathbb{P}(A\_i \cap A\_j) = \mathbb{P}(A\_i) \mathbb{P}(A\_j) \quad \text{para todo } 1 \le i < j \le n.
\\]

### El contraejemplo clásico de Serguéi Bernstein (1927)

Consideremos un tetraedro regular cuyas cuatro caras están pintadas de la siguiente manera:
- Cara 1: Pintada de Rojo (\\(R\\)).
- Cara 2: Pintada de Verde (\\(V\\)).
- Cara 3: Pintada de Azul (\\(A\\)).
- Cara 4: Pintada con franjas de los tres colores Rojo, Verde y Azul (\\(R, V, A\\)).

Se lanza el tetraedro y se observa la cara que apoya en la mesa. Como las cuatro caras son simétricas y equiprobables:

\\[
\Omega = \{1, 2, 3, 4\}, \quad \mathbb{P}(\{i\}) = \frac{1}{4}, \ \forall i=1,2,3,4.
\\]

Definamos los eventos:
- \\(E\_R\\): "La cara resultante contiene el color Rojo" \\(= \{1, 4\}\\).
- \\(E\_V\\): "La cara resultante contiene el color Verde" \\(= \{2, 4\}\\).
- \\(E\_A\\): "La cara resultante contiene el color Azul" \\(= \{3, 4\}\\).

Calculamos sus probabilidades marginales:

\\[
\mathbb{P}(E\_R) = \frac{2}{4} = \frac{1}{2}, \quad \mathbb{P}(E\_V) = \frac{2}{4} = \frac{1}{2}, \quad \mathbb{P}(E\_A) = \frac{2}{4} = \frac{1}{2}.
\\]

Analicemos las intersecciones dos a dos:

\\[
E\_R \cap E\_V = \{4\} \implies \mathbb{P}(E\_R \cap E\_V) = \frac{1}{4} = \frac{1}{2} \times \frac{1}{2} = \mathbb{P}(E\_R)\mathbb{P}(E\_V).
\\]

\\[
E\_R \cap E\_A = \{4\} \implies \mathbb{P}(E\_R \cap E\_A) = \frac{1}{4} = \mathbb{P}(E\_R)\mathbb{P}(E\_A).
\\]

\\[
E\_V \cap E\_A = \{4\} \implies \mathbb{P}(E\_V \cap E\_A) = \frac{1}{4} = \mathbb{P}(E\_V)\mathbb{P}(E\_A).
\\]

Por consiguiente, los eventos \\(E\_R, E\_V, E\_A\\) son **independientes dos a dos**.

Ahora evaluemos la intersección triple simultánea:

\\[
E\_R \cap E\_V \cap E\_A = \{4\} \implies \mathbb{P}(E\_R \cap E\_V \cap E\_A) = \frac{1}{4}.
\\]

Sin embargo, el producto de las tres probabilidades individuales es:

\\[
\mathbb{P}(E\_R)\mathbb{P}(E\_V)\mathbb{P}(E\_A) = \frac{1}{2} \times \frac{1}{2} \times \frac{1}{2} = \frac{1}{8}.
\\]

Como \\(\frac{1}{4} \neq \frac{1}{8}\\), los tres eventos **no son mutuamente independientes**.

De hecho, si sabemos que ocurrieron \\(E\_R\\) y \\(E\_V\\), estamos con certeza en la cara 4, por lo que \\(\mathbb{P}(E\_A \mid E\_R \cap E\_V) = 1 \neq \mathbb{P}(E\_A) = 1/2\\).

---

## 2.2.4 Distinción crítica: Exclusión mutua vs. Independencia

Es un error conceptual frecuente confundir la exclusión mutua con la independencia.

| Concepto | Exclusión mutua (Disjuntos) | Independencia estocástica |
|---|---|---|
| **Definición formal** | \\(A \cap B = \emptyset\\) | \\(\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)\\) |
| **Naturaleza** | Relación de teoría de conjuntos (geométrica/espacial). | Propiedad de la medida de probabilidad \\(\mathbb{P}\\). |
| **Si \\(\mathbb{P}(A)>0\\) y \\(\mathbb{P}(B)>0\\)** | \\(\mathbb{P}(A \cap B) = 0\\). ¡**Nunca** pueden ser independientes! (la ocurrencia de uno prohíbe al otro: \\(\mathbb{P}(A \mid B) = 0 \neq \mathbb{P}(A)\\)). | \\(\mathbb{P}(A \cap B) > 0\\). Los eventos **deben tener intersección no vacía**. |
| **Unión** | \\(\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)\\) | \\(\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A)\mathbb{P}(B)\\) |

**Teorema 2.11.** *Sean \\(A, B \in \mathcal{F}\\) con \\(\mathbb{P}(A) > 0\\) y \\(\mathbb{P}(B) > 0\\). Si \\(A\\) y \\(B\\) son mutuamente excluyentes, entonces \\(A\\) y \\(B\\) son dependientes.*

*Demostración.* Si son excluyentes, \\(A \cap B = \emptyset \implies \mathbb{P}(A \cap B) = 0\\). Pero como \\(\mathbb{P}(A) > 0\\) y \\(\mathbb{P}(B) > 0\\), su producto es estrictamente positivo: \\(\mathbb{P}(A)\mathbb{P}(B) > 0\\). Por ende, \\(\mathbb{P}(A \cap B) \neq \mathbb{P}(A)\mathbb{P}(B)\\), lo que prueba que son dependientes. \\(\blacksquare\\)
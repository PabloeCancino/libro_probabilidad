# 2.1 Probabilidad condicional y regla de la multiplicación

## 2.1.1 Concepto y definición formal

En la práctica matemática y aplicada, la probabilidad asignada a un evento con frecuencia debe actualizarse ante la adquisición de **información parcial** sobre el desarrollo del experimento. Si sabemos con certeza que un evento \\(B\\) ha ocurrido (con \\(\mathbb{P}(B) > 0\\)), el espacio muestral relevante deja de ser el conjunto universal original \\(\Omega\\) y se contrae a un **espacio muestral reducido** \\(B\\).

**Definición 2.1 (Probabilidad condicional).** Sea \\((\Omega, \mathcal{F}, \mathbb{P})\\) un espacio de probabilidad y sean \\(A, B \in \mathcal{F}\\) dos eventos tales que \\(\mathbb{P}(B) > 0\\). La **probabilidad condicional** de \\(A\\) dado \\(B\\), denotada por \\(\mathbb{P}(A \mid B)\\), se define como el cociente:

\\[
\mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}.
\\]

### Interpretación intuitiva y geométrica
- En el caso equiprobable finito:

  \\[
  \mathbb{P}(A \mid B) = \frac{|A \cap B| / |\Omega|}{|B| / |\Omega|} = \frac{|A \cap B|}{|B|} = \frac{\text{Casos favorables en } A \text{ que están en } B}{\text{Total de casos en } B}.
  \\]

- El evento condicionante \\(B\\) actúa como el nuevo conjunto de referencia normalizado.

---

## 2.1.2 Teorema: La probabilidad condicional es una medida de probabilidad legítima

Un resultado fundamental es que, para cualquier evento fijo \\(B\\) con \\(\mathbb{P}(B) > 0\\), la función \\(\mathbb{Q}(\cdot) = \mathbb{P}(\cdot \mid B)\\) satisface estrictamente los tres axiomas de Kolmogórov.

**Teorema 2.2.** *Sea \\((\Omega, \mathcal{F}, \mathbb{P})\\) un espacio de probabilidad y sea \\(B \in \mathcal{F}\\) con \\(\mathbb{P}(B) > 0\\). La función \\(\mathbb{P}(\cdot \mid B) : \mathcal{F} \to [0, 1]\\) es una medida de probabilidad sobre \\((\Omega, \mathcal{F})\\).*

*Demostración.*
1. **Axioma 1 (No negatividad):** Para todo \\(A \in \mathcal{F}\\), como \\(A \cap B \in \mathcal{F}\\), por la no negatividad de \\(\mathbb{P}\\) se tiene \\(\mathbb{P}(A \cap B) \ge 0\\). Como \\(\mathbb{P}(B) > 0\\), el cociente cumple:

   \\[
   \mathbb{P}(A \mid B) = \frac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)} \ge 0.
   \\]

2. **Axioma 2 (Normalización):** Evaluando en \\(\Omega\\):

   \\[
   \mathbb{P}(\Omega \mid B) = \frac{\mathbb{P}(\Omega \cap B)}{\mathbb{P}(B)} = \frac{\mathbb{P}(B)}{\mathbb{P}(B)} = 1.
   \\]

3. **Axioma 3 (σ-aditividad):** Sea \\((A\_n)\_{n=1}^\infty \subseteq \mathcal{F}\\) una sucesión de eventos disjuntos dos a dos, es decir, \\(A\_i \cap A\_j = \emptyset\\) para todo \\(i \neq j\\).  
   Entonces los conjuntos \\(A\_n \cap B\\) son también mutuamente disjuntos dos a dos, puesto que:

   \\[
   (A\_i \cap B) \cap (A\_j \cap B) = (A\_i \cap A\_j) \cap B = \emptyset \cap B = \emptyset.
   \\]

   Por la distributividad de la intersección respecto a la unión numerable y la σ-aditividad de \\(\mathbb{P}\\):

   \\[
   \begin{aligned}
   \mathbb{P}\left(\bigcup\_{n=1}^\infty A\_n \;\middle|\; B\right) &= \frac{\mathbb{P}\left(\left(\bigcup\_{n=1}^\infty A\_n\right) \cap B\right)}{\mathbb{P}(B)} \\\\
   &= \frac{\mathbb{P}\left(\bigcup\_{n=1}^\infty (A\_n \cap B)\right)}{\mathbb{P}(B)} \\\\
   &= \frac{\sum\_{n=1}^\infty \mathbb{P}(A\_n \cap B)}{\mathbb{P}(B)} \\\\
   &= \sum\_{n=1}^\infty \frac{\mathbb{P}(A\_n \cap B)}{\mathbb{P}(B)} \\\\
   &= \sum\_{n=1}^\infty \mathbb{P}(A\_n \mid B).
   \end{aligned}
   \\]

   Por tanto, \\(\mathbb{P}(\cdot \mid B)\\) es una medida de probabilidad axiomática sobre \\((\Omega, \mathcal{F})\\). \\(\blacksquare\\)

### Consecuencias inmediatas
Dado que \\(\mathbb{P}(\cdot \mid B)\\) es una medida de probabilidad, hereda **todos** los teoremas demostrados en la Unidad 1:
- \\(\mathbb{P}(\emptyset \mid B) = 0\\).
- \\(\mathbb{P}(A^c \mid B) = 1 - \mathbb{P}(A \mid B)\\).
- Si \\(A\_1 \subseteq A\_2\\), entonces \\(\mathbb{P}(A\_1 \mid B) \le \mathbb{P}(A\_2 \mid B)\\).
- \\(\mathbb{P}(A\_1 \cup A\_2 \mid B) = \mathbb{P}(A\_1 \mid B) + \mathbb{P}(A\_2 \mid B) - \mathbb{P}(A\_1 \cap A\_2 \mid B)\\).

---

## 2.1.3 La regla de la multiplicación (regla de la cadena)

Despejando la probabilidad conjunta \\(\mathbb{P}(A \cap B)\\) de la definición de probabilidad condicional:

\\[
\mathbb{P}(A \cap B) = \mathbb{P}(B) \mathbb{P}(A \mid B) = \mathbb{P}(A) \mathbb{P}(B \mid A).
\\]

Este principio se extiende inductivamente a cualquier número finito de eventos.

**Teorema 2.3 (Regla general de la multiplicación).** *Sean \\(A\_1, A\_2, \dots, A\_n \in \mathcal{F}\\) eventos tales que \\(\mathbb{P}(A\_1 \cap A\_2 \cap \dots \cap A\_{n-1}) > 0\\). Entonces:*

\\[
\mathbb{P}\left(\bigcap\_{i=1}^n A\_i\right) = \mathbb{P}(A\_1) \mathbb{P}(A\_2 \mid A\_1) \mathbb{P}(A\_3 \mid A\_1 \cap A\_2) \cdots \mathbb{P}\left(A\_n \;\middle|\; \bigcap\_{i=1}^{n-1} A\_i\right).
\\]

*Demostración (por inducción matemática).*
- **Base (\\(n = 2\\)):** \\(\mathbb{P}(A\_1 \cap A\_2) = \mathbb{P}(A\_1)\mathbb{P}(A\_2 \mid A\_1)\\), que es la definición de probabilidad condicional.
- **Paso inductivo:** Supongamos que la fórmula es válida para \\(k-1\\) eventos.  
  Definamos el evento \\(B = \bigcap\_{i=1}^{k-1} A\_i\\). Entonces:

  \\[
  \mathbb{P}\left(\bigcap\_{i=1}^k A\_i\right) = \mathbb{P}(B \cap A\_k) = \mathbb{P}(B) \mathbb{P}(A\_k \mid B) = \mathbb{P}\left(\bigcap\_{i=1}^{k-1} A\_i\right) \mathbb{P}\left(A\_k \;\middle|\; \bigcap\_{i=1}^{k-1} A\_i\right).
  \\]

  Sustituyendo la hipótesis de inducción para \\(\mathbb{P}\left(\bigcap\_{i=1}^{k-1} A\_i\right)\\), se obtiene el resultado para \\(k\\) eventos. Por el principio de inducción, la fórmula es válida para todo \\(n \ge 2\\). \\(\blacksquare\\)

---

## 2.1.4 Ejemplos resueltos y diagramas de árbol

**Ejemplo 2.4 (Extracción secuencial sin reemplazo).**  
Una urna contiene 5 bolas rojas y 3 bolas verdes. Se extraen 3 bolas consecutivamente sin reemplazo. ¿Cuál es la probabilidad de que las tres bolas extraídas sean rojas?

*Solución:*  
Sean \\(R\_1, R\_2, R\_3\\) los eventos "la bola extraída en el turno 1, 2 y 3 es roja".
Por la regla de la multiplicación:

\\[
\mathbb{P}(R\_1 \cap R\_2 \cap R\_3) = \mathbb{P}(R\_1) \mathbb{P}(R\_2 \mid R\_1) \mathbb{P}(R\_3 \mid R\_1 \cap R\_2).
\\]

1. En la primera extracción hay 5 rojas de un total de 8: \\(\mathbb{P}(R\_1) = \frac{5}{8}\\).
2. Quedan 4 rojas de un total de 7: \\(\mathbb{P}(R\_2 \mid R\_1) = \frac{4}{7}\\).
3. Quedan 3 rojas de un total de 6: \\(\mathbb{P}(R\_3 \mid R\_1 \cap R\_2) = \frac{3}{6} = \frac{1}{2}\\).

Multiplicando las probabilidades condicionales:

\\[
\mathbb{P}(R\_1 \cap R\_2 \cap R\_3) = \frac{5}{8} \times \frac{4}{7} \times \frac{3}{6} = \frac{60}{336} = \frac{5}{28} \approx 0.17857 \quad (17.86\%).
\\]

(Nótese que por combinatoria directa mediante Laplace: \\(\frac{\binom{5}{3}}{\binom{8}{3}} = \frac{10}{56} = \frac{5}{28}\\), verificando la consistencia del modelo).
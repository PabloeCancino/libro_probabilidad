# 2.3 Particiones y Teorema de la Probabilidad Total

## 2.3.1 Particiones del espacio muestral

En muchas situaciones experimentales complejas, es difícil calcular la probabilidad de un evento \\(A\\) directamente. Sin embargo, el cálculo se simplifica drásticamente si condicionamos sobre un conjunto de hipótesis o escenarios exhaustivos y mutuamente excluyentes que fragmentan el espacio muestral.

**Definición 2.12 (Partición del espacio muestral).** Una colección finita o numerable de eventos \\(\{B_1, B_2, \dots, B_k, \dots\} \subseteq \mathcal{F}\\) es una **partición** de \\(\Omega\\) si satisface:
1. **Mutuamente excluyentes (disjuntos dos a dos):** \\(B_i \cap B_j = \emptyset\\) para todo \\(i \neq j\\).
2. **Exhaustivos (cubren todo el espacio):** \\(\bigcup_{i} B_i = \Omega\\).
3. **No nulos:** \\(\mathbb{P}(B_i) > 0\\) para todo \\(i\\).

El ejemplo más elemental de partición para cualquier evento \\(B\\) con \\(0 < \mathbb{P}(B) < 1\\) es el par formado por el evento y su complemento: \\(\{B, B^c\}\\).

---

## 2.3.2 El Teorema de la Probabilidad Total

**Teorema 2.13 (Ley de la Probabilidad Total).** *Sea \\(\{B_1, B_2, \dots, B_k\}\\) una partición finita del espacio muestral \\(\Omega\\) tal que \\(\mathbb{P}(B_i) > 0\\) para todo \\(i = 1, \dots, k\\). Para cualquier evento \\(A \in \mathcal{F}\\), se tiene:*

\\[
\mathbb{P}(A) = \sum_{i=1}^k \mathbb{P}(A \cap B_i) = \sum_{i=1}^k \mathbb{P}(B_i) \mathbb{P}(A \mid B_i).
\\]

*Demostración.*
Como \\(\bigcup_{i=1}^k B_i = \Omega\\), podemos expresar el evento \\(A\\) mediante la intersección con el espacio universal:

\\[
A = A \cap \Omega = A \cap \left(\bigcup_{i=1}^k B_i\right).
\\]

Por la propiedad distributiva de la teoría de conjuntos:

\\[
A = \bigcup_{i=1}^k (A \cap B_i).
\\]

Dado que los conjuntos \\(B_i\\) son disjuntos dos a dos, los eventos \\(A \cap B_i\\) también son disjuntos dos a dos:

\\[
(A \cap B_i) \cap (A \cap B_j) = A \cap (B_i \cap B_j) = A \cap \emptyset = \emptyset \quad \forall i \neq j.
\\]

Aplicando el axioma de aditividad finita (Corolario 1.21):

\\[
\mathbb{P}(A) = \sum_{i=1}^k \mathbb{P}(A \cap B_i).
\\]

Aplicando la definición de probabilidad condicional \\(\mathbb{P}(A \cap B_i) = \mathbb{P}(B_i)\mathbb{P}(A \mid B_i)\\) a cada término:

\\[
\mathbb{P}(A) = \sum_{i=1}^k \mathbb{P}(B_i) \mathbb{P}(A \mid B_i). \quad \blacksquare
\\]

### Versión para particiones numerables infinitas

**Corolario 2.14.** *Si \\(\{B_n\}_{n=1}^\infty\\) es una partición numerable de \\(\Omega\\), entonces para todo \\(A \in \mathcal{F}\\):*

\\[
\mathbb{P}(A) = \sum_{n=1}^\infty \mathbb{P}(B_n) \mathbb{P}(A \mid B_n).
\\]

*Demostración.* Sigue idéntico razonamiento aplicando directamente el Axioma 3 ($\sigma$-aditividad). \\(\blacksquare\\)

---

## 2.3.3 Ejemplos resueltos y aplicaciones

**Ejemplo 2.15 (Control de calidad en líneas de producción).**  
Una fábrica de microprocesadores tiene tres líneas de ensamble automatizadas:
- La línea \\(B_1\\) produce el 50% del total y tiene una tasa de defectos del 1% (\\(\mathbb{P}(D \mid B_1) = 0.01\\)).
- La línea \\(B_2\\) produce el 30% del total y tiene una tasa de defectos del 2% (\\(\mathbb{P}(D \mid B_2) = 0.02\\)).
- La línea \\(B_3\\) produce el 20% del total y tiene una tasa de defectos del 5% (\\(\mathbb{P}(D \mid B_3) = 0.05\\)).

Se selecciona un microprocesador al azar de la producción total. ¿Cuál es la probabilidad global de que esté defectuoso (\\(D\\))?

*Solución:*  
Las líneas \\(\{B_1, B_2, B_3\}\\) constituyen una partición del espacio muestral:
Por el Teorema de la Probabilidad Total:

\\[
\begin{aligned}
\mathbb{P}(D) &= \mathbb{P}(B_1)\mathbb{P}(D \mid B_1) + \mathbb{P}(B_2)\mathbb{P}(D \mid B_2) + \mathbb{P}(B_3)\mathbb{P}(D \mid B_3) \\\\
&= (0.50)(0.01) + (0.30)(0.02) + (0.20)(0.05) \\\\
&= 0.005 + 0.006 + 0.010 = 0.021 \quad (2.1\%).
\end{aligned}
\\]

**Ejemplo 2.16 (La ruina del jugador en un paso).**  
En un juego de azar, un participante gana \$1 con probabilidad \\(p\\) y pierde \$1 con probabilidad \\(q = 1 - p\\). Sea \\(u_k\\) la probabilidad de que el jugador eventualmente alcance una fortuna de \$N antes de arruinarse (llegar a \$0), partiendo de un capital inicial de \$k\\) (con \\(0 \le k \le N\\)).  
Condicionando sobre el resultado del primer juego (partición \\(\{G, P\}\\) donde \\(G\\) es ganar y \\(P\\) es perder):

\\[
u_k = \mathbb{P}(\text{Victoria} \mid G) \mathbb{P}(G) + \mathbb{P}(\text{Victoria} \mid P) \mathbb{P}(P) = p \cdot u_{k+1} + q \cdot u_{k-1}.
\\]

Esta es la clásica ecuación en diferencias de segundo orden homogénea:

\\[
p u_{k+1} - u_k + q u_{k-1} = 0, \quad \text{con condiciones de frontera } u_0 = 0, \ u_N = 1,
\\]

cuya deducción descansa enteramente en el Teorema de la Probabilidad Total.

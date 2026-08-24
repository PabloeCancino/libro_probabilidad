# Ejercicios de la Unidad 1

## Bloque A: Conteo, combinatoria y regla de Laplace

1. **Problema de las cartas:** De una baraja de 52 cartas se seleccionan 5 cartas al azar sin reemplazo.
   - (a) Calcule la probabilidad de obtener una *Escalera Real de Color* (10, J, Q, K, A del mismo palo).
   - (b) Calcule la probabilidad de obtener un *Póker* (4 cartas del mismo valor).
   - (c) Calcule la probabilidad de obtener un *Color* (5 cartas del mismo palo que no formen escalera consecutiva).

2. **Permutaciones circulares y collares:**
   - (a) ¿De cuántas formas pueden sentarse 8 matemáticos alrededor de una mesa redonda si dos de ellos no deben quedar juntos?
   - (b) Calcule la probabilidad de que al sentarse al azar queden completamente separados.

3. **Particiones y ocupación:** Se distribuyen al azar \\(n\\) bolas distinguibles en \\(k\\) celdas distinguibles (con \\(n \ge k\\)).
   - Calcule la probabilidad de que ninguna celda quede vacía utilizando el principio de inclusión-exclusión.

---

## Bloque B: $\sigma$-álgebras y axiomática de Kolmogórov

4. **$\sigma$-álgebra generada:** Sea \\(\Omega = \{1, 2, 3, 4, 5, 6\}\\) y consideremos los eventos \\(A = \{1, 2\}\\) y \\(B = \{2, 3, 4\}\\).
   - Determine explícitamente todos los elementos de la \\(\sigma\\)-álgebra \\(\sigma(\{A, B\})\\). ¿Cuántos eventos contiene?

5. **Demostración analítica de la diferencia simétrica:**
   - Demuestre rigurosamente a partir de los axiomas de Kolmogórov que para cualesquiera \\(A, B \in \mathcal{F}\\):
     \\[ \mathbb{P}(A \mathbin{\Delta} B) = \mathbb{P}(A) + \mathbb{P}(B) - 2\mathbb{P}(A \cap B). \\]

6. **Desigualdades de Bonferroni:**
   - Demuestre que para cualquier par de eventos \\(A, B \in \mathcal{F}\\):
     \\[ \mathbb{P}(A \cap B) \ge \mathbb{P}(A) + \mathbb{P}(B) - 1. \\]
   - Generalice por inducción matemática para demostrar que para \\(n\\) eventos \\(A_1, \dots, A_n\\):
     \\[ \mathbb{P}\left(\bigcap_{i=1}^n A_i\right) \ge \sum_{i=1}^n \mathbb{P}(A_i) - (n - 1). \\]

7. **Continuidad de la medida:** Sea \\((\Omega, \mathcal{F}, \mathbb{P})\\) un espacio de probabilidad y sea \\(\{A_n\}_{n=1}^\infty\\) una sucesión de eventos tales que \\(\mathbb{P}(A_n) = 1\\) para todo \\(n \ge 1\\).
   - Demuestre que \\(\mathbb{P}\left(\bigcap_{n=1}^\infty A_n\right) = 1\\).

---

## Bloque C: Probabilidad geométrica

8. **Ruptura de una varilla:** Se rompe una varilla de longitud \\(L = 1\\) al azar en dos puntos independientes distribuidos uniformemente.
   - Calcule la probabilidad de que los tres segmentos resultantes puedan formar un triángulo válido (aplicando la desigualdad triangular).

9. **El dardo en la diana:** Un dardo impacta en un círculo de radio \\(R\\) con distribución espacial uniforme.
   - (a) Calcule la probabilidad de que el impacto ocurra a una distancia menor o igual a \\(r\\) del centro (con \\(0 \le r \le R\\)).
   - (b) Deduzca la función de densidad de la distancia radial \\(r\\).

---

## Bloque D: Banco de reactivos institucionales (PALMAT)

10. **Reactivo PR-U1-01 (Eventos excluyentes):**  
    Sean \\(A, B\\) dos eventos en \\((\Omega, \mathcal{F}, \mathbb{P})\\) tales que \\(\mathbb{P}(A) = 0.3\\) y \\(\mathbb{P}(B) = 0.4\\). Si \\(A\\) y \\(B\\) son mutuamente excluyentes, calcule \\(\mathbb{P}(A \cup B)\\) e interprete por qué difiere del caso en que fueran independientes.

11. **Reactivo PR-U1-02 (Espacio muestral y condicionalidad básica):**  
    En una población estudiantil, el 60% tiene competencia en inglés (\\(I\\)), el 40% en francés (\\(F\\)) y el 20% domina ambos idiomas. Calcule la proporción de estudiantes que, sabiendo inglés, también dominan el francés (\\(\mathbb{P}(F \mid I)\\)).

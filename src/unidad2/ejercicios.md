# Ejercicios de la Unidad 2

## Bloque A: Probabilidad condicional y regla de la multiplicación

1. **Problema de Monty Hall (Las tres puertas):** En un concurso de televisión hay 3 puertas cerradas: detrás de una hay un automóvil de lujo y detrás de las otras dos hay cabras.
   - El concursante elige la Puerta 1.
   - El presentador (que sabe qué hay detrás de cada puerta) abre la Puerta 3, revelando una cabra.
   - El presentador le ofrece al concursante la opción de cambiar su elección a la Puerta 2.
   - (a) Modele el experimento definiendo los eventos pertinentes y aplique el Teorema de Bayes para calcular \\(\mathbb{P}(\text{Auto en Puerta 2} \mid \text{Presentador abre Puerta 3})\\).
   - (b) Demuestre rigurosamente por qué cambiar de puerta duplica la probabilidad de ganar de \\(1/3\\) a \\(2/3\\).

2. **Extracción sin reemplazo:** Una caja contiene 10 bombillas, de las cuales 3 están fundidas. Se prueban una a una sin reemplazo hasta encontrar la última bombilla defectuosa.
   - Calcule la probabilidad de que la búsqueda concluya exactamente en la quinta prueba.

---

## Bloque B: Independencia estocástica y contraejemplos

3. **Independencia y complementos generalizados:** Sean \\(A\_1, A\_2, \dots, A\_n\\) eventos mutuamente independientes con \\(\mathbb{P}(A\_i) = p\_i\\).
   - Demuestre que la probabilidad de que ocurra al menos uno de ellos es:

     \\[
     \mathbb{P}\left(\bigcup\_{i=1}^n A\_i\right) = 1 - \prod\_{i=1}^n (1 - p\_i).
     \\]

4. **Construcción de independencia condicional:**
   - Proporcione un ejemplo con un espacio muestral finito de tres eventos \\(A, B, C\\) tales que \\(A\\) y \\(B\\) sean condicionalmente independientes dado \\(C\\), pero sean marginalmente dependientes (es decir, \\(A \not\perp B\\)).

5. **El dado de tres caras coloreadas:** Considere el lanzamiento de dos dados equilibrados.
   - Sea \\(A\\): "El primer dado es par".
   - Sea \\(B\\): "El segundo dado es impar".
   - Sea \\(C\\): "La suma de ambos dados es impar".
   - Demuestre analíticamente que \\(A, B, C\\) son independientes dos a dos, pero determine si son mutuamente independientes.

---

## Bloque C: Probabilidad Total y Teorema de Bayes

6. **Filtro de correo no deseado (Spam filter):** Un clasificador bayesiano analiza correos electrónicos.
   - El 40% de todos los correos recibidos son *Spam* (\\(S\\)) y el 60% son legítimos (\\(S^c\\)).
   - La palabra "gratis" aparece en el 80% de los correos Spam y solo en el 5% de los correos legítimos.
   - Calcule la probabilidad de que un correo que contiene la palabra "gratis" sea realmente Spam.

7. **Pruebas diagnósticas en serie y en paralelo:**
   - Se aplican dos pruebas diagnósticas independientes \\(T\_1\\) y \\(T\_2\\) a un paciente para confirmar una enfermedad con prevalencia \\(\pi\_0 = 0.05\\).
   - La prueba 1 tiene sensibilidad \\(S\_{e1} = 0.90\\) y especificidad \\(S\_{p1} = 0.95\\).
   - La prueba 2 tiene sensibilidad \\(S\_{e2} = 0.85\\) y especificidad \\(S\_{p2} = 0.98\\).
   - (a) Calcule el VPP si ambas pruebas resultan positivas en el paciente.
   - (b) Calcule el VPN si ambas pruebas resultan negativas.

8. **La falacia del fiscal en genética forense:**
   - Un perfil de ADN coincide con una muestra en la escena del crimen con una probabilidad de falsa alarma de \\(10^{-6}\\) en una persona no culpable.
   - La ciudad donde ocurrió el crimen tiene 500\,000 habitantes adultos y no hay evidencia inicial previa contra el sospechoso.
   - Calcule la probabilidad real de culpabilidad del sospechoso asumiendo una distribución a priori uniforme en la población de la ciudad.

---

## Bloque D: Banco de reactivos institucionales (PALMAT)

9. **Reactivo PR-U1-02 (Probabilidad condicional directa):**  
   En una encuesta universitaria se determinó que el 60% de los estudiantes habla inglés (\\(I\\)), el 40% habla francés (\\(F\\)) y el 20% habla ambos idiomas.
   - Calcule \\(\mathbb{P}(F \mid I)\\).
   - Determine si el dominio del inglés y del francés son eventos independientes justificando con el producto de probabilidades.
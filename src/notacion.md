# Notación y convenciones

A lo largo del texto se emplea la siguiente notación estándar, salvo advertencia explícita en contrario:

| Símbolo | Significado matemático |
|---|---|
| \\(\Omega\\) | Espacio muestral (conjunto universal de todos los resultados elementales posibles). |
| \\(\omega \in \Omega\\) | Resultado elemental de un experimento aleatorio. |
| \\(\mathcal{F}\\) o \\(\mathcal{B}\\) | \\(\sigma\\)-álgebra de eventos asociados a \\(\Omega\\) (o \\(\sigma\\)-álgebra de Borel). |
| \\((\Omega, \mathcal{F}, \mathbb{P})\\) | Espacio de probabilidad axiomático de Kolmogórov. |
| \\(\mathbb{P}(A)\\) o \\(P(A)\\) | Medida de probabilidad del evento \\(A \in \mathcal{F}\\). |
| \\(A^c\\) o \\(A'\\) o \\(\Omega \setminus A\\) | Complemento del evento \\(A\\) respecto a \\(\Omega\\). |
| \\(A \cup B\\), \\(A \cap B\\) | Unión (ocurre \\(A\\) o \\(B\\)) e intersección (ocurre \\(A\\) y \\(B\\)). |
| \\(A \subseteq B\\) | Inclusión de eventos: si ocurre \\(A\\), necesariamente ocurre \\(B\\). |
| \\(\emptyset\\) | Evento imposible (conjunto vacío). |
| \\(\mathbb{P}(A \mid B)\\) | Probabilidad condicional del evento \\(A\\) dado que ha ocurrido \\(B\\). |
| \\(A \perp B\\) | Independencia estocástica de los eventos \\(A\\) y \\(B\\) (\\(\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)\\)). |
| \\(X, Y, Z\\) | Variables aleatorias (funciones medibles \\(X: \Omega \to \mathbb{R}\\)). |
| \\(\mathbf{X} = (X_1, \dots, X_n)\\) | Vector aleatorio \\(n\\)-dimensional. |
| \\(S_X\\) o \\(\text{sop}(X)\\) | Soporte de la variable aleatoria \\(X\\). |
| \\(p_X(x)\\) o \\(P(X = x)\\) | Función de masa de probabilidad (PMF) de una v.a. discreta. |
| \\(f_X(x)\\) | Función de densidad de probabilidad (PDF) de una v.a. continua. |
| \\(F_X(x) = \mathbb{P}(X \le x)\\) | Función de distribución acumulada (CDF). |
| \\(\mathbb{E}[X]\\) o \\(E[X]\\) | Esperanza matemática o valor esperado de \\(X\\). |
| \\(\text{Var}(X)\\) o \\(\sigma_X^2\\) | Varianza de la variable aleatoria \\(X\\). |
| \\(\sigma_X = \sqrt{\text{Var}(X)}\\) | Desviación estándar de \\(X\\). |
| \\(\text{Cov}(X, Y)\\) o \\(\sigma_{XY}\\) | Covarianza entre \\(X\\) e \\(Y\\). |
| \\(\rho(X, Y)\\) o \\(\text{Corr}(X, Y)\\) | Coeficiente de correlación lineal de Pearson. |
| \\(\mathbb{E}[X \mid Y]\\) | Esperanza condicional de \\(X\\) dado el valor de \\(Y\\). |
| \\(M_X(t) = \mathbb{E}[e^{tX}]\\) | Función generadora de momentos (MGF). |
| \\(G_X(s) = \mathbb{E}[s^X]\\) | Función generadora de probabilidad (PGF). |
| \\(\varphi_X(t) = \mathbb{E}[e^{itX}]\\) | Función característica de \\(X\\). |
| \\(X \sim \mathcal{D}(\boldsymbol{\theta})\\) | La v.a. \\(X\\) sigue la familia distribucional \\(\mathcal{D}\\) con vector de parámetros \\(\boldsymbol{\theta}\\). |
| \\(\mathcal{N}(\mu, \sigma^2)\\) | Distribución Normal (Gaussiana) con media \\(\mu\\) y varianza \\(\sigma^2\\). |
| \\(\Phi(z)\\) | Función de distribución acumulada de la Normal estándar \\(\mathcal{N}(0,1)\\). |
| \\(X_n \xrightarrow{\text{c.s.}} X\\) | Convergencia casi segura (con probabilidad 1). |
| \\(X_n \xrightarrow{P} X\\) | Convergencia en probabilidad. |
| \\(X_n \xrightarrow{L^p} X\\) | Convergencia en media de orden \\(p\\) (en particular \\(L^2\\) o media cuadrática). |
| \\(X_n \xrightarrow{d} X\\) | Convergencia en distribución (débil). |
| \\(\mathbb{I}_A(\omega)\\) o \\(\mathbf{1}_A\\) | Función indicadora del conjunto \\(A\\) (vale 1 si \\(\omega \in A\\) y 0 si \\(\omega \notin A\\)). |
| \\(\blacksquare\\) o "∎" | Cierre de demostración formal. |

---

## Estructura de Enunciados y Tipografía

- **Definiciones:** Se destacan con la cabecera **Definición** y establecen los objetos matemáticos de manera rigurosa.
- **Resultados:** Se jerarquizan como **Teorema**, **Proposición**, **Lema** o **Corolario**, y se acompañan obligatoriamente de su demostración completa salvo indicación expresa de referencia externa.
- **Ejemplos:** Se identifican como **Ejemplo** y desarrollan cálculos detallados, paso a paso, con interpretación conceptual.
- **Laboratorio Python:** Bloques de código ejecutables ilustran la simulación numérica, verificación de teoremas asintóticos y contrastes empíricos.

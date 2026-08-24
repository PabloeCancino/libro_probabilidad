# 2.4 Teorema de Bayes, pruebas diagnósticas y falacias condicionales

## 2.4.1 Enunciado y demostración del Teorema de Bayes

Publicado póstumamente en 1763 por Thomas Bayes y reformulado independientemente por Pierre-Simon Laplace en 1774, el **Teorema de Bayes** es la piedra angular del razonamiento condicional inverso: permite actualizar la probabilidad asignada a una hipótesis inicial (*a priori*) a la luz de una nueva evidencia observada (*a posteriori*).

**Teorema 2.17 (Teorema de Bayes).** *Sea \\(\{B_1, B_2, \dots, B_k\}\\) una partición del espacio muestral \\(\Omega\\) con \\(\mathbb{P}(B_i) > 0\\) para todo \\(i = 1, \dots, k\\). Sea \\(A \in \mathcal{F}\\) un evento con \\(\mathbb{P}(A) > 0\\). Entonces, para cualquier \\(j \in \{1, \dots, k\}\\):*
\\[ \mathbb{P}(B_j \mid A) = \frac{\mathbb{P}(B_j \cap A)}{\mathbb{P}(A)} = \frac{\mathbb{P}(B_j) \mathbb{P}(A \mid B_j)}{\sum_{i=1}^k \mathbb{P}(B_i) \mathbb{P}(A \mid B_i)}. \\]

*Demostración.*
Por la definición de probabilidad condicional:
\\[ \mathbb{P}(B_j \mid A) = \frac{\mathbb{P}(B_j \cap A)}{\mathbb{P}(A)}. \\]
Por la regla de la multiplicación en el numerador:
\\[ \mathbb{P}(B_j \cap A) = \mathbb{P}(B_j) \mathbb{P}(A \mid B_j). \\]
Sustituyendo en el denominador la descomposición del Teorema de la Probabilidad Total (Teorema 2.13):
\\[ \mathbb{P}(A) = \sum_{i=1}^k \mathbb{P}(B_i) \mathbb{P}(A \mid B_i). \\]
Dividiendo ambas expresiones se obtiene la fórmula de Bayes. \\(\blacksquare\\)

### Terminología bayesiana fundamental
- \\(\mathbb{P}(B_j)\\): **Probabilidad a priori (prior)** de la hipótesis \\(B_j\\) antes de observar la evidencia \\(A\\).
- \\(\mathbb{P}(A \mid B_j)\\): **Verosimilitud (likelihood)** de observar la evidencia \\(A\\) si la hipótesis \\(B_j\\) fuera cierta.
- \\(\mathbb{P}(A) = \sum_{i=1}^k \mathbb{P}(B_i) \mathbb{P}(A \mid B_i)\\): **Probabilidad marginal de la evidencia** (constante de normalización).
- \\(\mathbb{P}(B_j \mid A)\\): **Probabilidad a posteriori (posterior)** de la hipótesis \\(B_j\\) dada la evidencia observada \\(A\\).

---

## 2.4.2 Forma de Momios (Odds) y Razón de Verosimilitud

Para dos hipótesis rivales \\(H_0\\) y \\(H_1\\), definiendo los momios a priori como \\(\text{Odds}(H_1) = \frac{\mathbb{P}(H_1)}{\mathbb{P}(H_0)}\\), el Teorema de Bayes se expresa de forma compacta:
\\[ \frac{\mathbb{P}(H_1 \mid A)}{\mathbb{P}(H_0 \mid A)} = \frac{\mathbb{P}(H_1)}{\mathbb{P}(H_0)} \times \frac{\mathbb{P}(A \mid H_1)}{\mathbb{P}(A \mid H_0)}. \\]
\\[ \text{Odds a posteriori} = \text{Odds a priori} \times \text{Razón de Verosimilitudes (Bayes Factor)}. \\]

---

## 2.4.3 Aplicación crítica: Pruebas diagnósticas y epidemiología

Consideremos una prueba clínica para detectar una enfermedad \\(E\\).
- \\(E\\): El paciente padece la enfermedad (prevalencia poblacional \\(\mathbb{P}(E) = \pi_0\\)).
- \\(E^c\\): El paciente está sano (\\(\mathbb{P}(E^c) = 1 - \pi_0\\)).
- \\(T^+\\): La prueba diagnóstica resulta **positiva**.
- \\(T^-\\): La prueba diagnóstica resulta **negativa**.

### Parámetros intrínsecos de la prueba diagnóstica
1. **Sensibilidad (\\(S_e\\)):** Probabilidad de que la prueba sea positiva si el paciente está enfermo:
   \\[ S_e = \mathbb{P}(T^+ \mid E). \\]
   (La tasa de falsos negativos es \\(\mathbb{P}(T^- \mid E) = 1 - S_e\\)).
2. **Especificidad (\\(S_p\\)):** Probabilidad de que la prueba sea negativa si el paciente está sano:
   \\[ S_p = \mathbb{P}(T^- \mid E^c). \\]
   (La tasa de falsos positivos es \\(\mathbb{P}(T^+ \mid E^c) = 1 - S_p\\)).

### Valores predictivos (Inferencia a posteriori)
- **Valor Predictivo Positivo (VPP):** Probabilidad de estar realmente enfermo dado un resultado positivo en la prueba:
  \\[ \text{VPP} = \mathbb{P}(E \mid T^+) = \frac{\mathbb{P}(E)\mathbb{P}(T^+ \mid E)}{\mathbb{P}(E)\mathbb{P}(T^+ \mid E) + \mathbb{P}(E^c)\mathbb{P}(T^+ \mid E^c)} = \frac{\pi_0 \cdot S_e}{\pi_0 \cdot S_e + (1 - \pi_0)(1 - S_p)}. \\]
- **Valor Predictivo Negativo (VPN):** Probabilidad de estar sano dado un resultado negativo:
  \\[ \text{VPN} = \mathbb{P}(E^c \mid T^-) = \frac{(1 - \pi_0) S_p}{(1 - \pi_0) S_p + \pi_0 (1 - S_e)}. \\]

---

## 2.4.4 Falacias bayesianas y la paradoja del falso positivo

### 1. La paradoja del falso positivo (Olvido de la tasa base / Base Rate Fallacy)

**Ejemplo 2.18 (El cribado de una enfermedad rara).**  
Supongamos una enfermedad con una prevalencia de 1 en cada 1\,000 habitantes en la población general (\\(\pi_0 = 0.001\\)). Se desarrolla un test diagnóstico con alta precisión clínica:
- Sensibilidad: \\(S_e = 99\% = 0.99\\).
- Especificidad: \\(S_p = 95\% = 0.95\\) (tasa de falsos positivos \\(1 - S_p = 5\%\\)).

Una persona asintomática seleccionada al azar de la población se realiza el test y obtiene un resultado positivo (\\(T^+\\)). ¿Cuál es la probabilidad real de que padezca la enfermedad?

*Solución analítica:*  
Aplicando el Teorema de Bayes:
\\[ \begin{aligned} \mathbb{P}(E \mid T^+) &= \frac{(0.001)(0.99)}{(0.001)(0.99) + (0.999)(0.05)} \\ &= \frac{0.00099}{0.00099 + 0.04995} = \frac{0.00099}{0.05094} \approx 0.01943 \quad (1.94\%). \end{aligned} \\]

> **Conclusión contraintuitiva pero rigurosa:** A pesar de que la prueba tiene un 99% de sensibilidad y 95% de especificidad, una persona que da positivo **solo tiene un 1.94% de probabilidad real de estar enferma**. El 98.06% de los resultados positivos son en realidad falsos positivos.  
> **Explicación matemática:** En una población de 100\,000 personas:
> - Hay 100 enfermos; el test detecta a \\(100 \times 0.99 = 99\\) verdaderos positivos.
> - Hay 99\,900 sanos; el 5% de ellos da falso positivo: \\(99\,900 \times 0.05 = 4\,995\\) falsos positivos.
> - Total de positivos: \\(99 + 4\,995 = 5\,094\\). De ellos, solo 99 están realmente enfermos: \\(\frac{99}{5\,094} \approx 1.94\%\\).

### 2. La falacia del fiscal (Prosecutor's Fallacy)

Consiste en confundir la probabilidad condicional de la evidencia dada la inocencia con la probabilidad de inocencia dada la evidencia:
\\[ \mathbb{P}(\text{Evidencia coincidente} \mid \text{Inocente}) \neq \mathbb{P}(\text{Inocente} \mid \text{Evidencia coincidente}). \\]
En un juicio, si una prueba de ADN tiene una tasa de coincidencia fortuita de 1 en 100\,000 en personas inocentes (\\(\mathbb{P}(M \mid I) = 10^{-5}\\)), el fiscal erróneamente alega que *"la probabilidad de que el acusado sea inocente es de 1 en 100\,000"*.  
Si la población sospechosa es de 1\,000\,000 de personas, habrá unas 10 personas inocentes con coincidencia genética. La probabilidad a posteriori de inocencia sin otras pruebas incriminatorias es de \\(\frac{10}{11} \approx 90.9\%\\).

---

## 2.4.5 Laboratorio en Python: Calculadora e Inferencia Bayesiana

```python
import numpy as np
import matplotlib.pyplot as plt

def calcular_vpp(prevalencia, sensibilidad, especificidad):
    """Calcula el Valor Predictivo Positivo usando el Teorema de Bayes."""
    numerador = prevalencia * sensibilidad
    denominador = numerador + (1 - prevalencia) * (1 - especificidad)
    return numerador / denominador

# Variacion del VPP en funcion de la prevalencia para distintas especificidades
prevalencias = np.logspace(-4, -0.3, 500) # Desde 0.01% hasta 50%
sens = 0.99 # 99% de sensibilidad fija

especificidades = [0.90, 0.95, 0.99, 0.999]

print("Demostracion numerica del Teorema de Bayes:")
for sp in especificidades:
    vpp_ejemplo = calcular_vpp(0.001, sens, sp)
    print(f"Prevalencia = 0.1%, Sens = 99%, Espec = {sp*100:.1f}% -> VPP = {vpp_ejemplo*100:.2f}%")
```

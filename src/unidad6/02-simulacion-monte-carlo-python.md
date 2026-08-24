# 6.2 Simulación de Monte Carlo y método de la transformada inversa

## 6.2.1 El método de la transformada inversa

La **simulación estocástica** descansa sobre la capacidad de generar muestras numéricas de cualquier distribución de probabilidad a partir de un generador de números pseudoaleatorios uniformes \\(U \sim \mathcal{U}(0, 1)\\). El método más directo y elegante es el **método de la transformada inversa**.

**Teorema 6.7 (Teorema de la Transformada Inversa).** *Sea \\(F: \mathbb{R} \to [0, 1]\\) una función de distribución acumulada continua y estrictamente creciente con función inversa ordinaria \\(F^{-1}: (0, 1) \to \mathbb{R}\\). Si \\(U \sim \mathcal{U}(0, 1)\\), entonces la variable aleatoria transformada:*
\\[ X = F^{-1}(U) \\]
*tiene exactamente la función de distribución \\(F\\).*

*Demostración analítica.*  
Calculamos la función de distribución acumulada de la variable \\(X = F^{-1}(U)\\):
\\[ F_X(x) = \mathbb{P}(X \le x) = \mathbb{P}(F^{-1}(U) \le x). \\]
Dado que \\(F\\) es monótona estrictamente creciente, aplicar \\(F\\) en ambos lados de la desigualdad preserva la relación de orden:
\\[ \mathbb{P}(F^{-1}(U) \le x) = \mathbb{P}(F(F^{-1}(U)) \le F(x)) = \mathbb{P}(U \le F(x)). \\]
Como \\(U \sim \mathcal{U}(0, 1)\\), su CDF es \\(\mathbb{P}(U \le u) = u\\) para todo \\(u \in [0, 1]\\). Por tanto:
\\[ \mathbb{P}(U \le F(x)) = F(x). \\]
Esto demuestra que \\(F_X(x) = F(x)\\) para todo \\(x \in \mathbb{R}\\). \\(\blacksquare\\)

### Aplicación: Generación de la distribución Exponencial
Para \\(X \sim \text{Exp}(\lambda)\\), su CDF es \\(F(x) = 1 - e^{-\lambda x}\\) para \\(x \ge 0\\).  
Igualando a \\(u \in (0, 1)\\) y despejando \\(x\\):
\\[ 1 - e^{-\lambda x} = u \implies e^{-\lambda x} = 1 - u \implies -\lambda x = \ln(1 - u) \implies x = -\frac{1}{\lambda} \ln(1 - u). \\]
Dado que si \\(U \sim \mathcal{U}(0, 1)\\), entonces \\(1 - U \sim \mathcal{U}(0, 1)\\), el algoritmo de generación es simplemente:
\\[ X = -\frac{1}{\lambda} \ln(U). \\]

---

## 6.2.2 El método de Aceptación y Rechazo (von Neumann)

Cuando la función inversa \\(F^{-1}\\) no tiene forma analítica cerrada (como en la distribución Normal, Gamma o Beta), se utiliza el **método de aceptación y rechazo**.

Sea \\(f(x)\\) la densidad objetivo que deseamos simular, y sea \\(g(x)\\) una densidad propuesta (candidata) fácil de simular, tal que existe una constante \\(c \ge 1\\) con:
\\[ f(x) \le c \cdot g(x), \quad \forall x \in \mathbb{R}. \\]

**Algoritmo de Aceptación-Rechazo:**
1. Generar una muestra candidata \\(Y \sim g(y)\\).
2. Generar independientemente \\(U \sim \mathcal{U}(0, 1)\\).
3. Si \\(U \le \frac{f(Y)}{c \cdot g(Y)}\\), **aceptar** \\(X = Y\\). En caso contrario, **rechazar** \\(Y\\) y volver al paso 1.

**Teorema 6.8.** *La variable aceptada \\(X\\) tiene exactamente la densidad \\(f(x)\\), y el número de intentos hasta la primera aceptación sigue una distribución geométrica con probabilidad de éxito \\(p = 1/c\\).*

---

## 6.2.3 Integración de Monte Carlo y análisis de error

Deseamos aproximar el valor de una integral definida multidimensional compleja:
\\[ I = \int_D h(\mathbf{x}) \, d\mathbf{x}. \\]
Reescribiendo la integral como el valor esperado de una función respecto a una densidad uniforme \\(f(\mathbf{x}) = \frac{1}{\text{Vol}(D)}\\):
\\[ I = \text{Vol}(D) \int_D h(\mathbf{x}) \frac{1}{\text{Vol}(D)} \, d\mathbf{x} = \text{Vol}(D) \cdot \mathbb{E}[h(\mathbf{X})], \quad \text{donde } \mathbf{X} \sim \mathcal{U}(D). \\]
El **estimador de Monte Carlo** basado en \\(N\\) puntos independientes generados uniformemente en \\(D\\) es:
\\[ \hat{I}_N = \frac{\text{Vol}(D)}{N} \sum_{i=1}^N h(\mathbf{X}_i). \\]

**Propiedades del estimador de Monte Carlo:**
1. **Insesgamiento:** \\(\mathbb{E}[\hat{I}_N] = I\\).
2. **Convergencia casi segura:** Por la Ley Fuerte de los Grandes Números, \\(\hat{I}_N \xrightarrow{\text{c.s.}} I\\).
3. **Error estándar asintótico:** Por el Teorema del Límite Central:
   \\[ \text{Error} = |\hat{I}_N - I| \sim \mathcal{O}\left(\frac{\sigma_h}{\sqrt{N}}\right). \\]

> **Ventaja decisiva en alta dimensión:** Mientras que las reglas de cuadratura numéricas tradicionales (como Simpson o Gauss) sufren la *maldición de la dimensionalidad* (el error decae como \\(\mathcal{O}(N^{-k/d})\\), volviéndose inútiles para \\(d \ge 4\\)), **la tasa de convergencia de Monte Carlo \\(\mathcal{O}(N^{-1/2})\\) es completamente independiente de la dimensión \\(d\\)**.

---

## 6.2.4 Implementación en Python: Integración Monte Carlo y Transformada Inversa

```python
import numpy as np
import scipy.stats as stats

def integracion_monte_carlo(funcion, limites, N=1_000_000):
    """Calcula una integral definida en R^d mediante Monte Carlo."""
    # limites: lista de tuplas [(a1, b1), (a2, b2), ...]
    d = len(limites)
    volumen = np.prod([b - a for a, b in limites])
    
    # Genera puntos uniformes en la caja hiperrectangular
    puntos = np.zeros((N, d))
    for i, (a, b) in enumerate(limites):
        puntos[:, i] = np.random.uniform(a, b, size=N)
        
    evaluaciones = funcion(puntos)
    estimacion = volumen * np.mean(evaluaciones)
    error_estandar = volumen * (np.std(evaluaciones) / np.sqrt(N))
    
    return estimacion, error_estandar

# Ejemplo: Integral de Gauss en 3D en la esfera unitaria: \iiint exp(-(x^2+y^2+z^2)) dV
def f_gauss_3d(pts):
    radio_sq = np.sum(pts**2, axis=1)
    # Dentro de la esfera unitaria radio_sq <= 1, fuera vale 0
    return np.where(radio_sq <= 1.0, np.exp(-radio_sq), 0.0)

limites_cubo = [(-1, 1), (-1, 1), (-1, 1)]
I_est, err = integracion_monte_carlo(f_gauss_3d, limites_cubo, N=2_000_000)

print(f"Estimación de Monte Carlo: {I_est:.6f} +/- {1.96*err:.6f} (IC 95%)")
```

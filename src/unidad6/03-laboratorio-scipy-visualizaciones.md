# 6.3 Laboratorio computacional con SciPy y visualización de distribuciones

## 6.3.1 El ecosistema científico de Python (`scipy.stats`)

En el trabajo probabilístico y estadístico moderno, la biblioteca `scipy.stats` proporciona una interfaz unificada y orientada a objetos para más de 100 familias continuas y discretas.

### Métodos universales en objetos de distribución de `scipy.stats`
Para cualquier variable aleatoria continua `dist` (ej. `stats.norm`, `stats.expon`, `stats.gamma`) o discreta (ej. `stats.binom`, `stats.poisson`):

| Método | Significado probabilístico formal |
|---|---|
| `dist.rvs(params, size=N)` | Genera \\(N\\) realizaciones pseudoaleatorias independientes de la distribución. |
| `dist.pmf(k, params)` | Evalúa la función de masa de probabilidad \\(p(k) = \mathbb{P}(X = k)\\) (discreta). |
| `dist.pdf(x, params)` | Evalúa la función de densidad de probabilidad \\(f(x)\\) (continua). |
| `dist.cdf(x, params)` | Evalúa la función de distribución acumulada \\(F(x) = \mathbb{P}(X \le x)\\). |
| `dist.sf(x, params)` | Función de supervivencia \\(S(x) = 1 - F(x) = \mathbb{P}(X > x)\\). |
| `dist.ppf(q, params)` | Función cuantil / percentil \\(F^{-1}(q)\\) tal que \\(\mathbb{P}(X \le x\_q) = q\\). |
| `dist.stats(params, moments='mvsk')` | Devuelve la media (m), varianza (v), asimetría (s) y curtosis (k). |
| `dist.fit(datos)` | Estima los parámetros óptimos por **Máxima Verosimilitud (MLE)** a partir de datos. |

---

## 6.3.2 Guía de Implementación Práctica

### 1. Manipulación de distribuciones continuas
```python
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Configuracion de una distribucion Gamma(alpha=3.0, scale=theta=2.0 -> beta = 0.5)
dist_gamma = stats.gamma(a=3.0, scale=2.0)

# 1. Calculo de probabilidades
p_menor_4 = dist_gamma.cdf(4.0)       # P(X <= 4)
p_entre_2_6 = dist_gamma.cdf(6.0) - dist_gamma.cdf(2.0) # P(2 <= X <= 6)
cuantil_95 = dist_gamma.ppf(0.95)     # Valor x tal que P(X <= x) = 0.95

# 2. Momentos teoricos
media, varianza, sesgo, curt = dist_gamma.stats(moments='mvsk')

print(f"P(X <= 4.0): {p_menor_4:.4f}")
print(f"P(2.0 <= X <= 6.0): {p_entre_2_6:.4f}")
print(f"Percentil 95: {cuantil_95:.4f}")
print(f"Media: {media:.2f}, Varianza: {varianza:.2f}, Asimetría: {sesgo:.2f}")
```

---

## 6.3.3 Diagnóstico visual y contrastes de bondad de ajuste

Para evaluar si una muestra empírica \\(\{x\_1, \dots, x\_n\}\\) proviene de una distribución teórica postulada, se combinan gráficos de diagnóstico y pruebas formales:

1. **Histograma de densidad vs. PDF teórica superpuesta.**
2. **Gráfico Q-Q (Quantile-Quantile Plot):** Grafica los cuantiles empíricos muestrales frente a los cuantiles teóricos. Si los puntos se alinean perfectamente sobre la diagonal de 45 grados, los datos provienen de la distribución postulada.
3. **Prueba de Kolmogorov-Smirnov:** Contrasta la distancia suprema entre la CDF empírica \\(F\_n(x)\\) y la teórica \\(F(x)\\):

   \\[
   D\_n = \sup\_{x \in \mathbb{R}} |F\_n(x) - F(x)|.
   \\]
```python
def diagnostico_distribucional(datos, dist_nombre='norm'):
    """Genera panel completo de diagnostico grafico para una muestra de datos."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # 1. Histograma vs PDF ajustada por MLE
    dist_obj = getattr(stats, dist_nombre)
    parametros = dist_obj.fit(datos)
    
    x_vals = np.linspace(min(datos), max(datos), 300)
    pdf_ajustada = dist_obj.pdf(x_vals, *parametros)
    
    axes[0].hist(datos, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='navy')
    axes[0].plot(x_vals, pdf_ajustada, 'r-', lw=2, label=f'Ajuste MLE {dist_nombre}')
    axes[0].set_title('Histograma y Densidad Ajustada')
    axes[0].set_xlabel('Valor')
    axes[0].set_ylabel('Densidad')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # 2. Grafico Q-Q
    stats.probplot(datos, dist=dist_nombre, sparams=parametros[:-2] if len(parametros)>2 else (), plot=axes[1])
    axes[1].set_title('Gráfico Q-Q Normal / Teórico')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# Ejemplo con datos sinteticos
datos_test = np.random.normal(loc=10, scale=2.5, size=1000)
# diagnostico_distribucional(datos_test, 'norm')
```
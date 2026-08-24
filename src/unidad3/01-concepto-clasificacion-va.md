# 3.1 Concepto y clasificación formal de variables aleatorias

## 3.1.1 Definición formal de variable aleatoria

En muchos experimentos aleatorios, los resultados elementales \\(\omega \in \Omega\\) son de naturaleza cualitativa (por ejemplo, "cara o cruz", "cara roja o verde", "paciente recuperado o enfermo"). Para aplicar los métodos del cálculo diferencial e integral, el álgebra lineal y el análisis real, es necesario asociar a cada resultado elemental un valor numérico real.

No cualquier función arbitraria \\(X: \Omega \to \mathbb{R}\\) es admisible: para poder calcular la probabilidad de que \\(X\\) tome valores en un conjunto numérico \\(B \subseteq \mathbb{R}\\) (como un intervalo \\([a, b]\\)), la preimagen \\(X^{-1}(B)\\) debe ser un evento medible que pertenezca a la \\(\sigma\\)-álgebra \\(\mathcal{F}\\).

**Definición 3.1 (Variable aleatoria real).** Sea \\((\Omega, \mathcal{F}, \mathbb{P})\\) un espacio de probabilidad. Una **variable aleatoria (v.a.)** real es una función medible de Borel:
\\[ X : \Omega \to \mathbb{R}, \\]
tal que para todo conjunto boreliano \\(B \in \mathcal{B}(\mathbb{R})\\), la imagen inversa (preimagen) pertenece a \\(\mathcal{F}\\):
\\[ X^{-1}(B) = \{\omega \in \Omega : X(\omega) \in B\} \in \mathcal{F}. \\]

Por convención de notación probabilística, el evento \\(\{\omega \in \Omega : X(\omega) \in B\}\\) se abrevia simplemente como:
\\[ (X \in B) \quad \text{o} \quad \{X \in B\}. \\]

**Teorema 3.2 (Criterio de medibilidad por rayos).** *Una función \\(X: \Omega \to \mathbb{R}\\) es una variable aleatoria si y solo si para todo número real \\(x \in \mathbb{R}\\):*
\\[ X^{-1}((-\infty, x]) = \{\omega \in \Omega : X(\omega) \le x\} \in \mathcal{F}. \\]

*Demostración.*  
- \\((\implies)\\) Como los rayos \\((-\infty, x]\\) son conjuntos cerrados en \\(\mathbb{R}\\), pertenecen a la \\(\sigma\\)-álgebra de Borel \\(\mathcal{B}(\mathbb{R})\\). Si \\(X\\) es medible, \\(X^{-1}((-\infty, x]) \in \mathcal{F}\\) por definición.  
- \\((\impliedby)\\) Consideremos la clase de subconjuntos de \\(\mathbb{R}\\) cuyas preimágenes pertenecen a \\(\mathcal{F}\\):
  \\[ \mathcal{G} = \{B \subseteq \mathbb{R} : X^{-1}(B) \in \mathcal{F}\}. \\]
  Se verifica fácilmente que \\(\mathcal{G}\\) es una \\(\sigma\\)-álgebra sobre \\(\mathbb{R}\\) debido a las propiedades de la preimagen de conjuntos (preserva complementos, uniones e intersecciones numerables).  
  Como \\(\mathcal{G}\\) contiene a todos los rayos \\((-\infty, x]\\), y estos generan a \\(\mathcal{B}(\mathbb{R})\\) (Proposición 1.18), se concluye que \\(\mathcal{B}(\mathbb{R}) \subseteq \mathcal{G}\\), lo que demuestra que \\(X^{-1}(B) \in \mathcal{F}\\) para todo \\(B \in \mathcal{B}(\mathbb{R})\\). \\(\blacksquare\\)

---

## 3.1.2 Medida de probabilidad inducida y σ-álgebra generada

Toda variable aleatoria \\(X\\) transfiere la estructura probabilística del espacio abstracto original \\((\Omega, \mathcal{F}, \mathbb{P})\\) a la recta real \\((\mathbb{R}, \mathcal{B}(\mathbb{R}))\\).

**Definición 3.3 (Medida de probabilidad inducida / Distribución de X).** La **distribución de probabilidad inducida** por \\(X\\) en \\((\mathbb{R}, \mathcal{B}(\mathbb{R}))\\) es la función \\(\mathbb{P}_X : \mathcal{B}(\mathbb{R}) \to [0, 1]\\) definida por:
\\[ \mathbb{P}_X(B) = \mathbb{P}(X^{-1}(B)) = \mathbb{P}(X \in B), \quad \forall B \in \mathcal{B}(\mathbb{R}). \\]

**Definición 3.4 (σ-álgebra generada por una variable aleatoria).** La \\(\sigma\\)-álgebra generada por \\(X\\), denotada \\(\sigma(X)\\), es la menor sub-\\(\sigma\\)-álgebra de \\(\mathcal{F}\\) respecto a la cual \\(X\\) es medible:
\\[ \sigma(X) = \{X^{-1}(B) : B \in \mathcal{B}(\mathbb{R})\}. \\]
Intuitivamente, \\(\sigma(X)\\) representa toda la información experimental que puede obtenerse observando únicamente el valor numérico tomado por \\(X\\).

---

## 3.1.3 Clasificación rigurosa de las variables aleatorias

Sea \\(S_X = X(\Omega) = \{X(\omega) : \omega \in \Omega\} \subset \mathbb{R}\\) el **soporte** (o rango) de la variable aleatoria \\(X\\). Según la naturaleza matemática de su soporte y su medida inducida respecto a la medida de Lebesgue \\(\lambda\\), las variables aleatorias se clasifican en:

### 1. Variables aleatorias discretas
Una variable aleatoria \\(X\\) es **discreta** si su soporte \\(S_X\\) es un conjunto finito o infinito numerable:
\\[ S_X = \{x_1, x_2, \dots, x_n, \dots\} \subset \mathbb{R}, \quad \text{con } \sum_{x \in S_X} \mathbb{P}(X = x) = 1. \\]
La masa de probabilidad está concentrada en puntos aislados (átomos de probabilidad).

### 2. Variables aleatorias continuas (Absolutamente continuas)
Una variable aleatoria \\(X\\) es **(absolutamente) continua** si su medida inducida \\(\mathbb{P}_X\\) es absolutamente continua respecto a la medida de Lebesgue en \\(\mathbb{R}\\) (es decir, conjuntos de longitud de Lebesgue cero tienen probabilidad cero).  
Por el Teorema de Radon-Nikodym, esto equivale a la existencia de una función integrable no negativa \\(f_X: \mathbb{R} \to [0, \infty)\\) (la *función de densidad*) tal que para todo boreliano \\(B \in \mathcal{B}(\mathbb{R})\\):
\\[ \mathbb{P}(X \in B) = \int_B f_X(x) \, dx. \\]
Para cualquier punto individual \\(x_0 \in \mathbb{R}\\):
\\[ \mathbb{P}(X = x_0) = \int_{x_0}^{x_0} f_X(x) \, dx = 0. \\]

### 3. Variables aleatorias mixtas y singulares
- **Mixtas:** Su distribución posee tanto componentes discretos (átomos con probabilidad estrictamente positiva) como una componente continua integrada por una densidad.  
  *Ejemplo:* El tiempo de espera \\(T\\) en un semáforo: \\(\mathbb{P}(T = 0) = p > 0\\) (si el semáforo ya estaba en verde), y para \\(t > 0\\) el tiempo se distribuye con una densidad continua en \\((0, t_{\text{max}}]\\).
- **Singulares continuas:** Variables cuya función de distribución acumulada es continua en todo punto pero su derivada es cero casi en todas partes respecto a la medida de Lebesgue (por ejemplo, la distribución asociada al conjunto de Cantor).

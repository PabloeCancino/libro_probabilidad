# 5.2 Modos de convergencia estocástica

## 5.2.1 Las cuatro nociones de convergencia

En análisis real ordinario, una sucesión de números reales \\(\{x_n\}\\) converge a un límite \\(x\\) si la distancia \\(|x_n - x| \to 0\\). En probabilidad, las variables aleatorias \\(X_n: \Omega \to \mathbb{R}\\) son funciones medibles sobre un espacio abstracto de medida \\((\Omega, \mathcal{F}, \mathbb{P})\\), lo que da origen a distintos conceptos cualitativos y cuantitativos de aproximación asintótica.

---

### 1. Convergencia casi segura (Convergencia con probabilidad 1)

Es la noción más fuerte de convergencia estocástica y corresponde a la convergencia puntual del análisis funcional salvo en un conjunto de resultados de medida nula.

**Definición 5.7 (Convergencia casi segura).** Una sucesión de variables aleatorias \\(\{X_n\}_{n=1}^\infty\\) converge **casi seguramente (c.s.)** a la variable aleatoria \\(X\\) (denotado \\(X_n \xrightarrow{\text{c.s.}} X\\) o \\(X_n \xrightarrow{\text{a.s.}} X\\)) si:
\\[ \mathbb{P}\left(\left\{\omega \in \Omega : \lim_{n \to \infty} X_n(\omega) = X(\omega)\right\}\right) = 1. \\]
Equivalentemente:
\\[ \mathbb{P}\left(\limsup_{n \to \infty} |X_n - X| > \epsilon\right) = 0, \quad \forall \epsilon > 0. \\]

---

### 2. Convergencia en probabilidad

Evalúa si la masa de probabilidad de que \\(X_n\\) difiera de \\(X\\) en más de una tolerancia \\(\epsilon\\) se extingue cuando \\(n \to \infty\\).

**Definición 5.8 (Convergencia en probabilidad).** La sucesión \\(\{X_n\}\\) converge **en probabilidad** a \\(X\\) (denotado \\(X_n \xrightarrow{P} X\\) o \\(\text{plim}_{n\to\infty} X_n = X\\)) si para todo \\(\epsilon > 0\\):
\\[ \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) = 0 \iff \lim_{n \to \infty} \mathbb{P}(|X_n - X| \le \epsilon) = 1. \\]

---

### 3. Convergencia en media de orden p (Lᵖ)

**Definición 5.9 (Convergencia en Lᵖ).** Para \\(p \ge 1\\), la sucesión \\(\{X_n\}\\) converge a \\(X\\) en **media de orden \\(p\\)** (denotado \\(X_n \xrightarrow{L^p} X\\)) si \\(\mathbb{E}[|X_n|^p] < \infty\\) para todo \\(n\\) y:
\\[ \lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0. \\]
- Para \\(p = 1\\): **Convergencia en media** (\\(\lim_{n\to\infty} \mathbb{E}[|X_n - X|] = 0\\)).
- Para \\(p = 2\\): **Convergencia en media cuadrática** (\\(\lim_{n\to\infty} \mathbb{E}[(X_n - X)^2] = 0\\)), denotada \\(X_n \xrightarrow{\text{m.c.}} X\\).

---

### 4. Convergencia en distribución (Convergencia débil / en ley)

Es la noción más débil: no exige que las variables aleatorias estén definidas sobre el mismo espacio muestral \\(\Omega\\), pues solo concierne a sus funciones de distribución acumulada.

**Definición 5.10 (Convergencia en distribución).** La sucesión \\(\{X_n\}\\) converge **en distribución** (o en ley) a \\(X\\) (denotado \\(X_n \xrightarrow{d} X\\) o \\(X_n \xrightarrow{\mathcal{D}} X\\)) si:
\\[ \lim_{n \to \infty} F_{X_n}(x) = F_X(x), \\]
para todo punto \\(x \in \mathbb{R}\\) donde la función de distribución límite \\(F_X\\) es continua (puntos de continuidad \\(C(F_X)\\)).

---

## 5.2.2 Jerarquía y relaciones de implicación entre modos de convergencia

**Teorema 5.11 (Jerarquía de convergencias estocásticas).**
```
           X_n ──c.s.──> X
                │
                ▼
X_n ──L^p──> X ───> X_n ──P──> X ───> X_n ──d──> X
```

*Demostraciones formales de las implicaciones principales:*

### 1. Convergencia en Lᵖ ⟹ Convergencia en probabilidad
Aplicando la desigualdad de Márkov generalizada (Teorema 5.1) con \\(g(u) = u^p\\):
\\[ \mathbb{P}(|X_n - X| > \epsilon) \le \frac{\mathbb{E}[|X_n - X|^p]}{\epsilon^p}. \\]
Como \\(\lim_{n \to \infty} \mathbb{E}[|X_n - X|^p] = 0\\), para cualquier \\(\epsilon > 0\\) fijo:
\\[ 0 \le \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) \le \lim_{n \to \infty} \frac{\mathbb{E}[|X_n - X|^p]}{\epsilon^p} = 0 \implies X_n \xrightarrow{P} X. \quad \blacksquare \\]

### 2. Convergencia casi segura ⟹ Convergencia en probabilidad
Para cualquier \\(\epsilon > 0\\), definamos el conjunto \\(E_n = \bigcup_{k=n}^\infty (|X_k - X| > \epsilon)\\).  
La sucesión \\(E_n\\) es decreciente: \\(E_n \downarrow E = \limsup_{k\to\infty} (|X_k - X| > \epsilon)\\).  
Por la hipótesis de convergencia casi segura, \\(\mathbb{P}(E) = 0\\).  
Por continuidad de la probabilidad desde arriba (Teorema 1.29):
\\[ \lim_{n \to \infty} \mathbb{P}(E_n) = \mathbb{P}(E) = 0. \\]
Como \\((|X_n - X| > \epsilon) \subseteq E_n\\), por monotonía:
\\[ 0 \le \lim_{n \to \infty} \mathbb{P}(|X_n - X| > \epsilon) \le \lim_{n \to \infty} \mathbb{P}(E_n) = 0 \implies X_n \xrightarrow{P} X. \quad \blacksquare \\]

### 3. Convergencia en probabilidad ⟹ Convergencia en distribución
Para cualquier \\(\epsilon > 0\\) y \\(x \in \mathbb{R}\\):
\\[ F_{X_n}(x) = \mathbb{P}(X_n \le x) = \mathbb{P}(X_n \le x, |X_n - X| \le \epsilon) + \mathbb{P}(X_n \le x, |X_n - X| > \epsilon). \\]
Si \\(X_n \le x\\) y \\(|X_n - X| \le \epsilon\\), entonces \\(X \le X_n + \epsilon \le x + \epsilon\\). Por tanto:
\\[ F_{X_n}(x) \le \mathbb{P}(X \le x + \epsilon) + \mathbb{P}(|X_n - X| > \epsilon) = F_X(x + \epsilon) + \mathbb{P}(|X_n - X| > \epsilon). \\]
Tomando límite superior cuando \\(n \to \infty\\) (donde \\(\mathbb{P}(|X_n - X| > \epsilon) \to 0\\)):
\\[ \limsup_{n \to \infty} F_{X_n}(x) \le F_X(x + \epsilon). \\]
Análogamente, se demuestra que \\(\liminf_{n \to \infty} F_{X_n}(x) \ge F_X(x - \epsilon)\\).  
Haciendo \\(\epsilon \to 0^+\\) en un punto de continuidad de \\(F_X\\):
\\[ F_X(x) \le \liminf_{n \to \infty} F_{X_n}(x) \le \limsup_{n \to \infty} F_{X_n}(x) \le F_X(x) \implies \lim_{n \to \infty} F_{X_n}(x) = F_X(x). \quad \blacksquare \\]

**Teorema 5.12 (Equivalencia con constante).** *Si el límite \\(c \in \mathbb{R}\\) es una constante determinista, entonces:*
\\[ X_n \xrightarrow{d} c \iff X_n \xrightarrow{P} c. \\]

---

## 5.2.3 Contraejemplos clásicos de no reversibilidad

### Contraejemplo 1: Convergencia en probabilidad NO implica casi segura (La máquina de escribir deslizante)
Sea \\(\Omega = [0, 1)\\) con la medida de Lebesgue uniforme.  
Para cada entero \\(n \ge 1\\), escribimos \\(n = 2^k + j\\) de forma única con \\(k \ge 0\\) y \\(0 \le j < 2^k\\).  
Definamos la sucesión de intervalos viajantes \\(I_n = \left[\frac{j}{2^k}, \frac{j+1}{2^k}\right)\\) y las variables aleatorias indicadoras:
\\[ X_n(\omega) = \mathbb{I}_{I_n}(\omega) = \begin{cases} 1, & \omega \in I_n, \\ 0, & \omega \notin I_n. \end{cases} \\]
- **En probabilidad:** Para todo \\(\epsilon \in (0, 1)\\):
  \\[ \mathbb{P}(|X_n - 0| > \epsilon) = \mathbb{P}(X_n = 1) = \text{Longitud}(I_n) = \frac{1}{2^k} \to 0 \quad \text{cuando } n \to \infty \implies X_n \xrightarrow{P} 0. \\]
- **Casi seguramente:** Para **todo** \\(\omega \in [0, 1)\\), el punto \\(\omega\\) es cubierto infinitas veces por los intervalos \\(I_n\\) e ignorado infinitas veces. Por tanto, la sucesión numérica \\(X_n(\omega)\\) oscila eternamente entre 0 y 1:
  \\[ \limsup_{n \to \infty} X_n(\omega) = 1 \neq \liminf_{n \to \infty} X_n(\omega) = 0, \quad \forall \omega \in \Omega. \\]
  En consecuencia, \\(\mathbb{P}(\lim_{n \to \infty} X_n = 0) = 0\\), demostrando que \\(X_n\\) **no** converge casi seguramente.

### Contraejemplo 2: Convergencia en probabilidad NO implica convergencia en L¹
Sea \\(\Omega = (0, 1)\\) con probabilidad uniforme. Definamos:
\\[ X_n(\omega) = n^2 \cdot \mathbb{I}_{(0, 1/n)}(\omega). \\]
- Para todo \\(\epsilon > 0\\), \\(\mathbb{P}(|X_n| > \epsilon) = \mathbb{P}(\omega \in (0, 1/n)) = \frac{1}{n} \to 0 \implies X_n \xrightarrow{P} 0\\).
- Sin embargo, su valor esperado es \\(\mathbb{E}[|X_n|] = n^2 \cdot \frac{1}{n} = n \to \infty\\), por lo que **no** converge en \\(L^1\\).

---

## 5.2.4 Teorema de Slutsky y Teorema de Mapeo Continuo

**Teorema 5.13 (Teorema de Slutsky).** *Sean \\(\{X_n\}\\) e \\(\{Y_n\}\\) dos sucesiones de variables aleatorias tales que \\(X_n \xrightarrow{d} X\\) y \\(Y_n \xrightarrow{P} c\\) (donde \\(c\\) es una constante). Entonces:*
1. \\(X_n + Y_n \xrightarrow{d} X + c\\).
2. \\(X_n Y_n \xrightarrow{d} c X\\).
3. \\(\dfrac{X_n}{Y_n} \xrightarrow{d} \dfrac{X}{c}\\) (siempre que \\(c \neq 0\\)).

**Teorema 5.14 (Teorema del Mapeo Continuo / Mann-Wald).** *Sea \\(g: \mathbb{R} \to \mathbb{R}\\) una función continua. Entonces:*
1. \\(X_n \xrightarrow{\text{c.s.}} X \implies g(X_n) \xrightarrow{\text{c.s.}} g(X)\\).
2. \\(X_n \xrightarrow{P} X \implies g(X_n) \xrightarrow{P} g(X)\\).
3. \\(X_n \xrightarrow{d} X \implies g(X_n) \xrightarrow{d} g(X)\\).

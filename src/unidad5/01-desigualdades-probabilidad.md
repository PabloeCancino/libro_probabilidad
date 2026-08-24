# 5.1 Desigualdades de probabilidad y concentración

En muchas situaciones prácticas y teóricas, la función de distribución exacta de una variable aleatoria \\(X\\) es desconocida o intratable analíticamente. Las **desigualdades de probabilidad** proporcionan cotas superiores no paramétricas universales para la probabilidad de que una variable aleatoria se desvíe de su valor esperado, dependiendo únicamente del conocimiento de sus momentos básicos (esperanza, varianza o MGF).

---

## 5.1.1 Desigualdad de Márkov

Es la desigualdad fundamental a partir de la cual se deducen casi todas las demás cotas probabilísticas.

**Teorema 5.1 (Desigualdad de Márkov).** *Sea \\(X\\) una variable aleatoria no negativa (\\(X \ge 0\\)) con esperanza finita \\(\mathbb{E}[X] < \infty\\). Para cualquier constante real \\(a > 0\\):*
\\[ \mathbb{P}(X \ge a) \le \frac{\mathbb{E}[X]}{a}. \\]
*Más generalmente, para cualquier variable aleatoria \\(Y\\) y función no negativa estrictamente creciente \\(g: [0, \infty) \to [0, \infty)\\):*
\\[ \mathbb{P}(|Y| \ge a) \le \frac{\mathbb{E}[g(|Y|)]}{g(a)}. \\]

*Demostración analítica.*  
Para \\(a > 0\\), consideremos la función indicadora \\(\mathbb{I}_{(X \ge a)}\\).  
Para todo \\(\omega \in \Omega\\), se verifica la desigualdad puntual:
\\[ a \cdot \mathbb{I}_{(X \ge a)}(\omega) \le X(\omega). \\]
- Si \\(X(\omega) < a\\), el lado izquierdo es \\(a \cdot 0 = 0 \le X(\omega)\\) (pues \\(X \ge 0\\)).
- Si \\(X(\omega) \ge a\\), el lado izquierdo es \\(a \cdot 1 = a \le X(\omega)\\).

Tomando la esperanza matemática en ambos lados (preservada por monotonía y linealidad):
\\[ \mathbb{E}[a \cdot \mathbb{I}_{(X \ge a)}] \le \mathbb{E}[X] \implies a \mathbb{E}[\mathbb{I}_{(X \ge a)}] \le \mathbb{E}[X] \implies a \mathbb{P}(X \ge a) \le \mathbb{E}[X]. \\]
Dividiendo entre \\(a > 0\\) se obtiene la desigualdad de Márkov. \\(\blacksquare\\)

---

## 5.1.2 Desigualdad de Chebyshev

Publicada por Pafnuti Chebyshev en 1867, acota la probabilidad de que una variable aleatoria se aleje de su media poblacional en términos de su varianza.

**Teorema 5.2 (Desigualdad de Chebyshev / Bienaymé-Chebyshev).** *Sea \\(X\\) una variable aleatoria con media finita \\(\mu = \mathbb{E}[X]\\) y varianza finita \\(\sigma^2 = \text{Var}(X)\\). Para cualquier \\(\epsilon > 0\\):*
\\[ \mathbb{P}(|X - \mu| \ge \epsilon) \le \frac{\text{Var}(X)}{\epsilon^2}. \\]
*O equivalentemente, expresando la distancia en múltiplos de la desviación estándar \\(\epsilon = k\sigma\\) (con \\(k > 0\\)):*
\\[ \mathbb{P}(|X - \mu| \ge k\sigma) \le \frac{1}{k^2}. \\]

*Demostración.*  
Definamos la variable aleatoria no negativa \\(Y = (X - \mu)^2 \ge 0\\).  
El evento \\(\{|X - \mu| \ge \epsilon\}\\) es idéntico al evento \\(\{(X - \mu)^2 \ge \epsilon^2\}\\).  
Aplicando la desigualdad de Márkov (Teorema 5.1) a la variable \\(Y\\) con el valor \\(a = \epsilon^2 > 0\\):
\\[ \mathbb{P}(|X - \mu| \ge \epsilon) = \mathbb{P}((X - \mu)^2 \ge \epsilon^2) \le \frac{\mathbb{E}[(X - \mu)^2]}{\epsilon^2} = \frac{\text{Var}(X)}{\epsilon^2}. \quad \blacksquare \\]

### Regla universal de concentración
- Para \\(k = 2\\): \\(\mathbb{P}(|X - \mu| \ge 2\sigma) \le \frac{1}{4} = 0.25 \implies \mathbb{P}(|X - \mu| < 2\sigma) \ge 75\%\\).
- Para \\(k = 3\\): \\(\mathbb{P}(|X - \mu| \ge 3\sigma) \le \frac{1}{9} \approx 0.111 \implies \mathbb{P}(|X - \mu| < 3\sigma) \ge 88.89\%\\).
- Para \\(k = 5\\): \\(\mathbb{P}(|X - \mu| \ge 5\sigma) \le \frac{1}{25} = 0.04 \implies \mathbb{P}(|X - \mu| < 5\sigma) \ge 96\%\\).

*(Nótese que esta cota es válida para **cualquier** distribución con varianza finita, por muy asimétrica o extraña que sea).*

---

## 5.1.3 Desigualdad de Cantelli (Chebyshev unilateral)

Cuando solo se desea acotar una de las dos colas (por ejemplo, la desviación positiva \\(X - \mu \ge a\\)), la cota de Cantelli es más ajustada que la de Chebyshev.

**Teorema 5.3 (Desigualdad de Cantelli).** *Para cualquier \\(a > 0\\):*
\\[ \mathbb{P}(X - \mu \ge a) \le \frac{\sigma^2}{\sigma^2 + a^2} = \frac{1}{1 + (a/\sigma)^2}. \\]

*Demostración.*  
Para cualquier constante real \\(u > 0\\):
\\[ \mathbb{P}(X - \mu \ge a) = \mathbb{P}((X - \mu + u) \ge a + u) \le \mathbb{P}((X - \mu + u)^2 \ge (a + u)^2). \\]
Aplicando Márkov:
\\[ \mathbb{P}(X - \mu \ge a) \le \frac{\mathbb{E}[(X - \mu + u)^2]}{(a + u)^2} = \frac{\sigma^2 + u^2}{(a + u)^2}. \\]
Minimizando la función \\(h(u) = \frac{\sigma^2 + u^2}{(a + u)^2}\\) respecto a \\(u > 0\\) mediante cálculo diferencial ordinario, el mínimo global se alcanza en \\(u^* = \frac{\sigma^2}{a}\\). Sustituyendo este valor óptimo:
\\[ h\left(\frac{\sigma^2}{a}\right) = \frac{\sigma^2 + \sigma^4/a^2}{(a + \sigma^2/a)^2} = \frac{\sigma^2(1 + \sigma^2/a^2)}{a^2(1 + \sigma^2/a^2)^2} = \frac{\sigma^2}{a^2(1 + \sigma^2/a^2)} = \frac{\sigma^2}{a^2 + \sigma^2}. \quad \blacksquare \\]

---

## 5.1.4 Desigualdad de Jensen

**Definición 5.4 (Función convexa).** Una función \\(g: I \subseteq \mathbb{R} \to \mathbb{R}\\) es **convexa** si para cualesquiera \\(x, y \in I\\) y \\(\lambda \in [0, 1]\\):
\\[ g(\lambda x + (1 - \lambda)y) \le \lambda g(x) + (1 - \lambda) g(y). \\]
(Si \\(g\\) es dos veces diferenciable, \\(g''(x) \ge 0\\) en todo el intervalo).

**Teorema 5.5 (Desigualdad de Jensen).** *Sea \\(X\\) una variable aleatoria tal que \\(\mathbb{E}[|X|] < \infty\\) y sea \\(g: \mathbb{R} \to \mathbb{R}\\) una función convexa tal que \\(\mathbb{E}[|g(X)|] < \infty\\). Entonces:*
\\[ g(\mathbb{E}[X]) \le \mathbb{E}[g(X)]. \\]

*Demostración (mediante recta tangente de soporte).*  
Sea \\(\mu = \mathbb{E}[X]\\). Por ser \\(g\\) convexa, en el punto \\(\mu\\) existe una recta tangente de soporte con pendiente \\(m\\) tal que para todo \\(x \in \mathbb{R}\\):
\\[ g(x) \ge g(\mu) + m(x - \mu). \\]
Evaluando en la variable aleatoria \\(X\\):
\\[ g(X) \ge g(\mu) + m(X - \mu). \\]
Tomando la esperanza matemática en ambos lados por monotonía y linealidad:
\\[ \mathbb{E}[g(X)] \ge \mathbb{E}[g(\mu) + m(X - \mu)] = g(\mu) + m(\mathbb{E}[X] - \mu) = g(\mu) + m(\mu - \mu) = g(\mu) = g(\mathbb{E}[X]). \quad \blacksquare \\]

### Consecuencias clásicas
1. Para \\(g(x) = x^2\\) (convexa): \\((\mathbb{E}[X])^2 \le \mathbb{E}[X^2] \implies \text{Var}(X) = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 \ge 0\\).
2. Para \\(g(x) = -\ln x\\) en \\(x > 0\\) (convexa): \\(-\ln(\mathbb{E}[X]) \le \mathbb{E}[-\ln X] \implies \ln(\mathbb{E}[X]) \ge \mathbb{E}[\ln X]\\), lo que demuestra que la **media geométrica es siempre menor o igual a la media aritmética**.

---

## 5.1.5 Cotas de Chernoff y concentración de la medida

Para variables cuya MGF existe, las **cotas de Chernoff** proporcionan un decaimiento exponencial extremadamente rápido en las colas.

**Teorema 5.6 (Cota de Chernoff).** *Sea \\(X\\) una variable aleatoria con función generadora de momentos \\(M_X(t)\\) finita para \\(t > 0\\). Para cualquier \\(a \in \mathbb{R}\\):*
\\[ \mathbb{P}(X \ge a) \le \inf_{t > 0} e^{-ta} M_X(t). \\]
*Y análogamente para la cola izquierda:*
\\[ \mathbb{P}(X \le a) \le \inf_{t > 0} e^{ta} M_X(-t). \\]

*Demostración.*  
Para cualquier \\(t > 0\\) fijo, la función \\(x \mapsto e^{tx}\\) es monótona estrictamente creciente. Por tanto, el evento \\(\{X \ge a\}\\) es idéntico a \\(\{e^{tX} \ge e^{ta}\}\\).  
Aplicando la desigualdad de Márkov a la variable positiva \\(e^{tX}\\):
\\[ \mathbb{P}(X \ge a) = \mathbb{P}(e^{tX} \ge e^{ta}) \le \frac{\mathbb{E}[e^{tX}]}{e^{ta}} = e^{-ta} M_X(t). \\]
Dado que la desigualdad es válida para **todo** \\(t > 0\\), se toma el ínfimo sobre todos los valores posibles de \\(t > 0\\) para obtener la cota más ajustada. \\(\blacksquare\\)

# Auto-examen Semestral

Este auto-examen es un **simulacro del examen final** de Probabilidad (CBIMAT-234). Cubre las seis unidades del curso con la misma estructura y el mismo nivel de exigencia de un examen final: reactivos de opción múltiple, problemas de respuesta corta y cálculo, y demostraciones formales.

Su propósito no es asignarte una calificación, sino **mostrarte con precisión qué temas dominas y cuáles debes repasar** antes del examen verdadero. Por eso cada reactivo está vinculado a la sección del libro donde se estudia su contenido.

---

## 📋 Instrucciones de aplicación

1. **Momento recomendado:** resuélvelo entre dos y tres semanas antes del examen final. Así tendrás tiempo de repasar los temas débiles y, si lo deseas, de volver a intentar los reactivos que fallaste.
2. **Condiciones de examen real:** reserva **3 horas continuas**, sin apuntes, sin formulario, sin el libro y sin consultar las soluciones. Puedes usar una **calculadora científica no programable** y la **tabla de la Normal estándar** que aparece abajo. Escribe tus respuestas en hojas aparte.
3. **Distribución del tiempo sugerida:**

| Parte | Contenido | Reactivos | Puntos | Tiempo sugerido |
| :---: | :--- | :---: | :---: | :---: |
| I | Opción múltiple | 1 a 20 | 20 | 30 min |
| II | Respuesta corta y cálculo | 21 a 28 | 32 | 60 min |
| III | Demostraciones | 29 a 34 | 48 | 90 min |
| | **Total** | **34** | **100** | **3 h** |

4. **Al terminar:** califícate con la clave y las rúbricas del final de esta página. Sé estricto: en un cálculo, un resultado correcto sin planteamiento no recibe el puntaje completo, y en una demostración, una idea correcta mal justificada tampoco. Después llena la **tabla de diagnóstico** para decidir qué repasar.

### Tabla abreviada de la Normal estándar

Si $Z \sim \mathcal{N}(0, 1)$, la tabla da $\Phi(z) = \mathbb{P}(Z \le z)$. Para valores negativos usa $\Phi(-z) = 1 - \Phi(z)$.

| $z$ | 0.50 | 1.00 | 1.28 | 1.50 | 1.645 | 1.96 | 2.00 | 2.50 | 3.00 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $\Phi(z)$ | 0.6915 | 0.8413 | 0.8997 | 0.9332 | 0.9500 | 0.9750 | 0.9772 | 0.9938 | 0.9987 |

**Convenciones del libro:** $\mathcal{N}(\mu, \sigma^2)$ se escribe con la **varianza**; $\text{Exp}(\lambda)$ tiene densidad $\lambda e^{-\lambda x}$ y media $1/\lambda$; $\text{Geométrica}(p)$ cuenta el número de ensayos hasta el primer éxito, con soporte $\{1, 2, 3, \dots\}$; $\text{Gamma}(\alpha, \beta)$ tiene densidad proporcional a $x^{\alpha - 1} e^{-\beta x}$.

---

## 📝 Parte I. Opción múltiple (20 puntos, 1 punto cada reactivo)

Elige **una sola** respuesta en cada reactivo.

### Unidad 1. Espacios de probabilidad y combinatoria

**1.** ¿Cuántas palabras distinguibles (con o sin sentido) pueden formarse permutando todas las letras de la palabra PALMAT?

- A) 720
- B) 180
- C) 360
- D) 120

**2.** ¿Cuántas soluciones tiene la ecuación $x_1 + x_2 + x_3 + x_4 = 10$ con $x_1, x_2, x_3, x_4$ **enteros no negativos**?

- A) 286
- B) 84
- C) 715
- D) 1001

**3.** Sea $\Omega = \{1, 2, 3, 4, 5, 6\}$ y sean $A = \{1, 2\}$ y $B = \{1, 2, 3, 4\}$. ¿Cuántos eventos contiene la $\sigma$-álgebra generada $\sigma(\{A, B\})$?

- A) 4
- B) 8
- C) 16
- D) 64

**4.** Dos personas acuerdan encontrarse entre las 12:00 y las 13:00. Cada una llega en un instante uniformemente distribuido en esa hora, independientemente de la otra, y espera a la otra a lo sumo 20 minutos. ¿Cuál es la probabilidad de que se encuentren?

- A) $4/9$
- B) $1/3$
- C) $1/9$
- D) $5/9$

### Unidad 2. Probabilidad condicional, independencia y Teorema de Bayes

**5.** Sean $A$ y $B$ eventos con $\mathbb{P}(A) = 0.5$, $\mathbb{P}(B) = 0.4$ y $\mathbb{P}(A \cup B) = 0.7$. ¿Cuál de las siguientes afirmaciones es **verdadera**?

- A) $A$ y $B$ son independientes y $\mathbb{P}(A \mid B) = 0.5$.
- B) $A$ y $B$ son mutuamente excluyentes.
- C) $A$ y $B$ son dependientes, porque $\mathbb{P}(A \cap B) \neq 0$.
- D) $\mathbb{P}(A \mid B) = 0.4$.

**6.** Se lanzan dos monedas equilibradas. Sean $A$: «la primera cae águila», $B$: «la segunda cae águila» y $C$: «ambas monedas muestran la misma cara». Entonces $A$, $B$ y $C$ son:

- A) Mutuamente independientes.
- B) Independientes dos a dos, pero no mutuamente independientes.
- C) Tales que $A$ y $C$ son dependientes.
- D) Tales que $A \cap B \cap C = \emptyset$.

**7.** La urna I contiene 3 bolas blancas y 2 negras; la urna II contiene 1 blanca y 4 negras. Se lanza una moneda equilibrada para elegir la urna y se extrae una bola, que resulta **blanca**. ¿Cuál es la probabilidad de que provenga de la urna I?

- A) 0.60
- B) 0.40
- C) 0.75
- D) 0.30

**8.** Una enfermedad tiene prevalencia del 1 %. Una prueba tiene sensibilidad 0.99 y especificidad 0.95. Si una persona elegida al azar da **positivo**, la probabilidad de que esté enferma (valor predictivo positivo) es, aproximadamente:

- A) 0.99
- B) 0.17
- C) 0.95
- D) 0.01

### Unidad 3. Variables aleatorias y familias de distribuciones

**9.** La variable aleatoria $X$ tiene función de distribución acumulada

$$
F(x) = \begin{cases} 0, & x < 0, \\ x/4, & 0 \le x < 1, \\ 1/2, & 1 \le x < 2, \\ 1, & x \ge 2. \end{cases}
$$

¿Cuánto vale $\mathbb{P}(X = 1)$ y de qué tipo es $X$?

- A) $0$; continua.
- B) $1/2$; discreta.
- C) $1/4$; discreta.
- D) $1/4$; mixta.

**10.** El vector $(X, Y)$ tiene la función de masa conjunta dada en la tabla. ¿Cuánto vale $\mathbb{P}(Y = 1 \mid X = 1)$?

| | $Y = 0$ | $Y = 1$ |
| :---: | :---: | :---: |
| $X = 0$ | 0.1 | 0.3 |
| $X = 1$ | 0.2 | 0.4 |

- A) 0.4
- B) 0.7
- C) $2/3$
- D) $4/7$

**11.** Un servidor recibe en promedio 120 peticiones por hora, según un proceso de Poisson. ¿Cuál es la probabilidad de que en un minuto dado **no** llegue ninguna petición?

- A) $e^{-120}$
- B) $1 - e^{-2} \approx 0.8647$
- C) $2e^{-2} \approx 0.2707$
- D) $e^{-2} \approx 0.1353$

**12.** La vida útil de un componente sigue una distribución exponencial con media de 4 años. Si el componente ya funcionó 3 años, ¿cuál es la probabilidad de que funcione **al menos 2 años más**?

- A) $e^{-1/2} \approx 0.6065$
- B) $e^{-5/4} \approx 0.2865$
- C) $1 - e^{-1/2} \approx 0.3935$
- D) $e^{-3/4} \approx 0.4724$

### Unidad 4. Esperanza matemática, momentos y operadores lineales

**13.** Si $X \sim \mathcal{U}(0, 2)$, ¿cuánto vale $\mathbb{E}[X^2]$?

- A) 1
- B) $4/3$
- C) $1/3$
- D) 2

**14.** Si $\text{Var}(X) = 4$, $\text{Var}(Y) = 1$ y $\text{Cov}(X, Y) = -1$, ¿cuánto vale $\text{Var}(2X - 3Y + 1)$?

- A) 25
- B) 13
- C) 26
- D) 37

**15.** Si $X$ e $Y$ son variables aleatorias con varianza finita y $\text{Cov}(X, Y) = 0$, entonces **necesariamente**:

- A) $X$ e $Y$ son independientes.
- B) $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$.
- C) $\text{Var}(X - Y) = \text{Var}(X) - \text{Var}(Y)$.
- D) $Y$ no puede ser una función de $X$.

**16.** La función generadora de momentos de $X$ es $M_X(t) = (0.3 + 0.7e^t)^{10}$. Entonces:

- A) $X \sim \text{Binomial}(10, 0.3)$, con $\mathbb{E}[X] = 3$ y $\text{Var}(X) = 2.1$.
- B) $X \sim \text{Poisson}(7)$, con $\mathbb{E}[X] = \text{Var}(X) = 7$.
- C) $X \sim \text{Binomial}(10, 0.7)$, con $\mathbb{E}[X] = 7$ y $\text{Var}(X) = 7$.
- D) $X \sim \text{Binomial}(10, 0.7)$, con $\mathbb{E}[X] = 7$ y $\text{Var}(X) = 2.1$.

### Unidad 5. Teoremas límite y leyes asintóticas

**17.** Una variable aleatoria $X$, de distribución **desconocida**, tiene media 50 y desviación estándar 5. ¿Cuál es la mejor cota inferior que garantiza la desigualdad de Chebyshev para $\mathbb{P}(40 < X < 60)$?

- A) 0.25
- B) 0.9544
- C) 0.75
- D) 0.8889

**18.** ¿Cuál de las siguientes implicaciones entre modos de convergencia es **siempre** válida?

- A) $X_n \xrightarrow{\text{c.s.}} X \implies X_n \xrightarrow{P} X$
- B) $X_n \xrightarrow{P} X \implies X_n \xrightarrow{\text{c.s.}} X$
- C) $X_n \xrightarrow{d} X \implies X_n \xrightarrow{P} X$
- D) $X_n \xrightarrow{P} X \implies X_n \xrightarrow{L^2} X$

**19.** Un elevador soporta 2 592 kg. Suben 36 personas cuyos pesos son i.i.d. con media 70 kg y desviación estándar 12 kg. Según el Teorema del Límite Central, la probabilidad aproximada de que se **supere** la capacidad es:

- A) 0.1587
- B) 0.8413
- C) 0.0228
- D) 0.3413

### Unidad 6. Procesos estocásticos y laboratorio computacional

**20.** Una cadena de Markov con estados $\{1, 2\}$ tiene matriz de transición

$$
\mathbf{P} = \begin{pmatrix} 0.9 & 0.1 \\ 0.5 & 0.5 \end{pmatrix}.
$$

Su distribución estacionaria $\boldsymbol{\pi} = (\pi_1, \pi_2)$ es:

- A) $(1/2, 1/2)$
- B) $(0.9, 0.1)$
- C) $(5/6, 1/6)$
- D) $(1/6, 5/6)$

---

## 📝 Parte II. Respuesta corta y cálculo (32 puntos, 4 puntos cada reactivo)

Muestra tu procedimiento: define los eventos o variables, escribe la fórmula que usas y después sustituye. Una respuesta final sin justificación recibe a lo sumo 1 punto.

**21.** *(Inclusión-exclusión.)* Cuatro estudiantes dejan sus mochilas en la entrada y, al salir, se las devuelven completamente al azar.

- a) Usando el principio de inclusión-exclusión, calcula la probabilidad de que **ninguno** reciba su propia mochila.
- b) ¿Cuál es la probabilidad de que **al menos uno** reciba la suya?

**22.** *(Pruebas diagnósticas en serie.)* Una enfermedad tiene prevalencia del 2 %. La prueba $T_1$ tiene sensibilidad 0.90 y especificidad 0.90; la prueba $T_2$ tiene sensibilidad 0.80 y especificidad 0.95. Los resultados de ambas pruebas son condicionalmente independientes dado el estado del paciente.

- a) Calcula el valor predictivo positivo (VPP) si solo se aplica $T_1$ y resulta positiva.
- b) Calcula el VPP si se aplican ambas pruebas y **las dos** resultan positivas.
- c) Interpreta en una o dos oraciones por qué se recomienda confirmar un positivo con una segunda prueba.

**23.** *(Regla de la multiplicación.)* Una urna contiene 4 bolas rojas y 6 azules. Se extraen 3 bolas una tras otra **sin reemplazo**.

- a) Con la regla de la multiplicación, calcula la probabilidad de obtener roja, roja y azul, **en ese orden**.
- b) Calcula la probabilidad de obtener **exactamente 2** rojas, y verifica tu resultado con la distribución hipergeométrica.

**24.** *(Densidad y CDF.)* Sea

$$
f_X(x) = \begin{cases} c\,x(2 - x), & 0 \le x \le 2, \\ 0, & \text{en otro caso.} \end{cases}
$$

- a) Encuentra la constante $c$ que hace de $f_X$ una densidad.
- b) Obtén la función de distribución acumulada $F_X(x)$ para todo $x \in \mathbb{R}$.
- c) Calcula $\mathbb{P}(X \le 1/2)$ y la mediana de $X$.

**25.** *(Vector aleatorio continuo.)* El vector $(X, Y)$ tiene densidad conjunta $f_{X,Y}(x, y) = 2$ en el triángulo $0 \le y \le x \le 1$, y cero fuera de él.

- a) Calcula las densidades marginales $f_X$ y $f_Y$.
- b) ¿Son $X$ e $Y$ independientes? Justifica.
- c) Obtén la densidad condicional $f_{Y \mid X}(y \mid x)$ y deduce $\mathbb{E}[Y \mid X]$.
- d) Calcula $\mathbb{P}(X + Y \le 1)$.

**26.** *(Esperanza y varianza totales.)* El número de clientes que llega a una tienda en un día es $N \sim \text{Poisson}(4)$. Cada cliente gasta una cantidad $Y_i$ con media 100 pesos y desviación estándar 20 pesos; las $Y_i$ son i.i.d. e independientes de $N$. Sea $S = \sum_{i=1}^{N} Y_i$ el ingreso del día ($S = 0$ si $N = 0$).

- a) Usa la Ley de las Esperanzas Iteradas para calcular $\mathbb{E}[S]$.
- b) Usa la Ley de la Varianza Total para calcular $\text{Var}(S)$ y la desviación estándar de $S$.

**27.** *(Función generadora de momentos.)* La función generadora de momentos de $X$ es $M_X(t) = e^{2(e^t - 1)}$.

- a) Calcula $\mathbb{E}[X]$ y $\text{Var}(X)$ derivando $M_X(t)$.
- b) Identifica la distribución de $X$.
- c) Si $Y \sim \text{Poisson}(3)$ es independiente de $X$, identifica la distribución de $X + Y$ mediante la MGF y calcula $\mathbb{P}(X + Y = 0)$.

**28.** *(Tamaño de muestra: Chebyshev frente al TLC.)* Se mide repetidamente una magnitud con desviación estándar $\sigma = 2$ y media desconocida $\mu$. Se quiere que la media muestral $\bar{X}_n$ cumpla $\mathbb{P}(|\bar{X}_n - \mu| < 0.5) \ge 0.95$.

- a) Encuentra el menor $n$ que lo garantiza según la desigualdad de Chebyshev.
- b) Encuentra el menor $n$ que lo logra aproximadamente según el Teorema del Límite Central.
- c) Explica por qué los dos tamaños son tan diferentes.

---

## 📝 Parte III. Demostraciones (48 puntos, 8 puntos cada una)

Redacta cada demostración en prosa matemática completa: declara lo que supones y lo que quieres probar, justifica cada paso con un axioma, una definición o un resultado previo, y cierra con una conclusión explícita.

**29.** *(Axiomática de Kolmogórov.)* Sea $(\Omega, \mathcal{F}, \mathbb{P})$ un espacio de probabilidad y sean $A, B \in \mathcal{F}$. Puedes usar que $\mathbb{P}(\emptyset) = 0$ y la aditividad finita. Demuestra que:

- a) $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$.
- b) Si $A \subseteq B$, entonces $\mathbb{P}(A) \le \mathbb{P}(B)$.
- c) $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$.
- d) $\mathbb{P}(A \cap B) \ge \mathbb{P}(A) + \mathbb{P}(B) - 1$ (desigualdad de Bonferroni).

**30.** *(Independencia.)* Sean $A, B \in \mathcal{F}$.

- a) Demuestra que si $A$ y $B$ son independientes, entonces $A$ y $B^c$ también lo son.
- b) Deduce que $A^c$ y $B^c$ son independientes.
- c) Demuestra que si $A$ y $B$ son mutuamente excluyentes y $\mathbb{P}(A) > 0$, $\mathbb{P}(B) > 0$, entonces $A$ y $B$ **no** son independientes.

**31.** *(Falta de memoria y discretización.)* Sea $X \sim \text{Exp}(\lambda)$.

- a) Demuestra que $\mathbb{P}(X > s + t \mid X > s) = \mathbb{P}(X > t)$ para todo $s, t \ge 0$.
- b) Sea $Y = \lceil X \rceil$ (el menor entero mayor o igual que $X$). Demuestra que $Y \sim \text{Geométrica}(p)$ con $p = 1 - e^{-\lambda}$.

**32.** *(Varianza, covarianza e independencia.)* Sean $X$ e $Y$ variables aleatorias con segundo momento finito.

- a) Demuestra que $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\,\text{Cov}(X, Y)$.
- b) Usando que la independencia implica $\mathbb{E}[XY] = \mathbb{E}[X]\,\mathbb{E}[Y]$, concluye que si $X$ e $Y$ son independientes, la varianza de la suma es la suma de las varianzas.
- c) Sea $X$ uniforme en $\{-1, 0, 1\}$ y sea $Y = X^2$. Demuestra que $\text{Cov}(X, Y) = 0$, pero que $X$ e $Y$ **no** son independientes.

**33.** *(Funciones generadoras de momentos.)*

- a) Demuestra que si $X \sim \text{Exp}(\lambda)$, entonces $M_X(t) = \dfrac{\lambda}{\lambda - t}$ para $t < \lambda$.
- b) Sean $X_1, \dots, X_n$ i.i.d. con distribución $\text{Exp}(\lambda)$. Demuestra que $S_n = X_1 + \dots + X_n \sim \text{Gamma}(n, \lambda)$, sabiendo que la MGF de $\text{Gamma}(\alpha, \beta)$ es $\left(1 - t/\beta\right)^{-\alpha}$ para $t < \beta$. Indica qué teorema usas para concluir.
- c) A partir de la MGF de $S_n$, obtén $\mathbb{E}[S_n]$ y $\text{Var}(S_n)$.

**34.** *(Desigualdades y Ley Débil de los Grandes Números.)*

- a) Demuestra la desigualdad de Márkov: si $X \ge 0$ y $a > 0$, entonces $\mathbb{P}(X \ge a) \le \dfrac{\mathbb{E}[X]}{a}$.
- b) Deduce de ella la desigualdad de Chebyshev: $\mathbb{P}(|X - \mu| \ge \varepsilon) \le \dfrac{\sigma^2}{\varepsilon^2}$ para todo $\varepsilon > 0$.
- c) Sean $X_1, X_2, \dots$ i.i.d. con media $\mu$ y varianza $\sigma^2 < \infty$. Demuestra que $\bar{X}_n \xrightarrow{P} \mu$.

---

## 🔑 Clave de respuestas y soluciones

No abras estos bloques hasta haber terminado el examen completo.

<details>
<summary><strong>Mostrar / ocultar la clave de la Parte I</strong></summary>

| Reactivo | Respuesta | Justificación breve |
| :---: | :---: | :--- |
| 1 | C | Seis letras con la A repetida dos veces: $\frac{6!}{2!} = 360$. A ignora la repetición. |
| 2 | A | Estrellas y barras: $\binom{10 + 4 - 1}{4 - 1} = \binom{13}{3} = 286$. B cuenta soluciones **positivas**: $\binom{9}{3} = 84$. |
| 3 | B | Como $A \subseteq B$, los átomos son $\{1, 2\}$, $\{3, 4\}$ y $\{5, 6\}$. Con 3 átomos hay $2^3 = 8$ eventos. C supone 4 átomos sin revisar la inclusión. |
| 4 | D | En el cuadrado $[0, 60]^2$, la región $\lvert x - y \rvert \le 20$ tiene área $60^2 - 40^2$; la probabilidad es $1 - (40/60)^2 = 5/9$. A es $(40/60)^2$, la probabilidad de **no** encontrarse; B es $20/60$, un razonamiento en una sola dimensión. |
| 5 | A | $\mathbb{P}(A \cap B) = 0.5 + 0.4 - 0.7 = 0.2 = \mathbb{P}(A)\,\mathbb{P}(B)$; luego son independientes y $\mathbb{P}(A \mid B) = 0.2/0.4 = 0.5$. |
| 6 | B | $\mathbb{P}(A \cap C) = \mathbb{P}(\text{AA}) = 1/4 = \mathbb{P}(A)\,\mathbb{P}(C)$, y lo mismo para los otros pares; pero $\mathbb{P}(A \cap B \cap C) = 1/4 \neq 1/8$. |
| 7 | C | $\mathbb{P}(\text{blanca}) = 0.5(0.6) + 0.5(0.2) = 0.4$ y $\mathbb{P}(\text{I} \mid \text{blanca}) = 0.3/0.4 = 0.75$. A es $\mathbb{P}(\text{blanca} \mid \text{I})$, B es la probabilidad total y D la conjunta. |
| 8 | B | $\frac{0.01(0.99)}{0.01(0.99) + 0.99(0.05)} = \frac{0.0099}{0.0594} = \frac{1}{6} \approx 0.17$. A confunde el VPP con la sensibilidad (falacia del fiscal). |
| 9 | D | El salto en 1 es $F(1) - F(1^-) = 1/2 - 1/4 = 1/4$. Hay saltos (en 1 y en 2) y un tramo continuo en $[0, 1)$: la variable es mixta. |
| 10 | C | $\mathbb{P}(X = 1) = 0.6$ y $\mathbb{P}(Y = 1 \mid X = 1) = 0.4/0.6 = 2/3$. D es $\mathbb{P}(X = 1 \mid Y = 1)$. |
| 11 | D | Se ajusta la tasa al intervalo: $\lambda = 120/60 = 2$ por minuto, y $\mathbb{P}(N = 0) = e^{-2}$. A no ajusta la tasa y C es $\mathbb{P}(N = 1)$. |
| 12 | A | Por la falta de memoria, $\mathbb{P}(X > 5 \mid X > 3) = \mathbb{P}(X > 2) = e^{-2/4}$. B es $\mathbb{P}(X > 5)$, sin condicionar. |
| 13 | B | Por LOTUS, $\int_0^2 x^2 \cdot \frac{1}{2}\,dx = \frac{4}{3}$. A es $(\mathbb{E}[X])^2$ y C es $\text{Var}(X)$. |
| 14 | D | $2^2(4) + (-3)^2(1) + 2(2)(-3)(-1) = 16 + 9 + 12 = 37$. La constante no afecta. A ignora la covarianza y B usa mal su signo. |
| 15 | B | $\text{Cov}(X, Y) = \mathbb{E}[XY] - \mathbb{E}[X]\,\mathbb{E}[Y]$. No correlación no implica independencia (véase el reactivo 32). C es falsa: con covarianza nula, $\text{Var}(X - Y) = \text{Var}(X) + \text{Var}(Y)$, porque $\text{Var}(-Y) = \text{Var}(Y)$ y la covarianza es nula. |
| 16 | D | Es la MGF de $\text{Binomial}(n, p)$ con $1 - p = 0.3$: $n = 10$, $p = 0.7$; $np = 7$ y $np(1 - p) = 2.1$. A confunde $p$ con $1 - p$. |
| 17 | C | Con $k = 2$ desviaciones: $\mathbb{P}(\lvert X - 50 \rvert < 10) \ge 1 - 1/k^2 = 0.75$. B supone normalidad, que no se conoce. |
| 18 | A | La convergencia casi segura implica la convergencia en probabilidad; las otras tres implicaciones tienen contraejemplos clásicos. |
| 19 | A | $\mathbb{E}[S] = 36(70) = 2520$, $\sigma_S = 12\sqrt{36} = 72$, $z = (2592 - 2520)/72 = 1$ y $\mathbb{P}(Z > 1) = 0.1587$. B es el complemento. |
| 20 | C | $\pi_1 = 0.9\pi_1 + 0.5\pi_2$ da $0.1\pi_1 = 0.5\pi_2$; con $\pi_1 + \pi_2 = 1$ resulta $\boldsymbol{\pi} = (5/6, 1/6)$. |

</details>

<details>
<summary><strong>Mostrar / ocultar las soluciones de la Parte II</strong></summary>

**Reactivo 21.** Sea $A_i$ el evento «el estudiante $i$ recibe su mochila», $i = 1, \dots, 4$. Para $k$ índices fijos, $\mathbb{P}(A_{i_1} \cap \dots \cap A_{i_k}) = \frac{(4 - k)!}{4!}$, y hay $\binom{4}{k}$ elecciones de esos índices, de modo que cada suma de la fórmula vale $\binom{4}{k}\frac{(4-k)!}{4!} = \frac{1}{k!}$. Por inclusión-exclusión:

$$
\mathbb{P}\left(\bigcup_{i=1}^{4} A_i\right) = 1 - \frac{1}{2!} + \frac{1}{3!} - \frac{1}{4!} = \frac{24 - 12 + 4 - 1}{24} = \frac{15}{24} = \frac{5}{8}
$$

- a) Ninguno recibe la suya: $1 - \frac{5}{8} = \frac{3}{8} = 0.375$. (Equivalentemente, hay 9 desarreglos de 4 elementos entre $4! = 24$ permutaciones.)
- b) Al menos uno: $\frac{5}{8} = 0.625$.

*Puntaje:* 1 por definir los eventos y las intersecciones, 2 por la fórmula con signos correctos, 1 por ambas respuestas.

**Reactivo 22.** Sea $E$ el evento «estar enfermo».

- a) $\mathbb{P}(E \mid T_1^+) = \dfrac{0.02(0.90)}{0.02(0.90) + 0.98(0.10)} = \dfrac{0.018}{0.116} \approx 0.155$.
- b) Por la independencia condicional, $\mathbb{P}(T_1^+ \cap T_2^+ \mid E) = 0.90(0.80) = 0.72$ y $\mathbb{P}(T_1^+ \cap T_2^+ \mid E^c) = 0.10(0.05) = 0.005$. Luego:

$$
\mathbb{P}(E \mid T_1^+ \cap T_2^+) = \frac{0.02(0.72)}{0.02(0.72) + 0.98(0.005)} = \frac{0.0144}{0.0193} \approx 0.746
$$

- c) Con una prevalencia baja, la mayoría de los positivos de una sola prueba son falsos positivos (VPP de apenas 15.5 %). La segunda prueba actúa como una nueva evidencia que actualiza la probabilidad *a priori* 0.155 y la eleva hasta cerca de 75 %.

*Puntaje:* 1 por a), 2 por b) (incluyendo el uso explícito de la independencia condicional), 1 por c).

**Reactivo 23.**

- a) $\mathbb{P}(R_1 \cap R_2 \cap A_3) = \mathbb{P}(R_1)\,\mathbb{P}(R_2 \mid R_1)\,\mathbb{P}(A_3 \mid R_1 \cap R_2) = \frac{4}{10} \cdot \frac{3}{9} \cdot \frac{6}{8} = \frac{1}{10}$.
- b) Hay $\binom{3}{2} = 3$ órdenes posibles para las dos rojas (RRA, RAR, ARR) y cada uno tiene probabilidad $\frac{1}{10}$, así que la probabilidad es $\frac{3}{10}$. Con la hipergeométrica: $\dfrac{\binom{4}{2}\binom{6}{1}}{\binom{10}{3}} = \dfrac{6 \cdot 6}{120} = \dfrac{3}{10}$.

*Puntaje:* 2 por a) con la regla de la cadena escrita, 1 por b), 1 por la verificación.

**Reactivo 24.**

- a) $\int_0^2 (2x - x^2)\,dx = 4 - \frac{8}{3} = \frac{4}{3}$, luego $c = \frac{3}{4}$.
- b) Para $0 \le x \le 2$: $F_X(x) = \frac{3}{4}\int_0^x (2u - u^2)\,du = \frac{3}{4}\left(x^2 - \frac{x^3}{3}\right)$. Así,

$$
F_X(x) = \begin{cases} 0, & x < 0, \\ \frac{3}{4}x^2 - \frac{1}{4}x^3, & 0 \le x \le 2, \\ 1, & x > 2. \end{cases}
$$

- c) $\mathbb{P}(X \le 1/2) = \frac{3}{4}\left(\frac{1}{4} - \frac{1}{24}\right) = \frac{5}{32} \approx 0.156$. Como $F_X(1) = \frac{3}{4} - \frac{1}{4} = \frac{1}{2}$, la mediana es 1 (también se sigue de que $f_X$ es simétrica respecto de $x = 1$).

*Puntaje:* 1 por a), 1.5 por b) (incluyendo los tres tramos), 1.5 por c).

**Reactivo 25.**

- a) $f_X(x) = \int_0^x 2\,dy = 2x$ para $0 \le x \le 1$; $f_Y(y) = \int_y^1 2\,dx = 2(1 - y)$ para $0 \le y \le 1$.
- b) **No** son independientes. Como las densidades están determinadas salvo conjuntos de medida cero, la factorización debe fallar en una región de área positiva, no en un solo punto. En el triángulo $T = \{(x, y) : 0 < x < y < 1\}$, de área $1/2$, se tiene $f_{X,Y} = 0$, mientras que $f_X(x)\,f_Y(y) = 4x(1 - y) > 0$. Por tanto, $\mathbb{P}((X, Y) \in T) = 0$, pero bajo independencia valdría $\iint_T 4x(1 - y)\,dx\,dy > 0$. El soporte triangular (no rectangular) ya delata la dependencia.
- c) Para $0 < x \le 1$: $f_{Y \mid X}(y \mid x) = \frac{2}{2x} = \frac{1}{x}$ si $0 \le y \le x$; es decir, $Y \mid X = x \sim \mathcal{U}(0, x)$. Por tanto, $\mathbb{E}[Y \mid X] = X/2$.
- d) La región es $0 \le y \le 1/2$, $y \le x \le 1 - y$, de área $\int_0^{1/2} (1 - 2y)\,dy = \frac{1}{4}$. Luego $\mathbb{P}(X + Y \le 1) = 2 \cdot \frac{1}{4} = \frac{1}{2}$.

*Puntaje:* 1 por inciso.

**Reactivo 26.** Se tiene $\mathbb{E}[S \mid N] = 100N$ y $\text{Var}(S \mid N) = 400N$.

- a) $\mathbb{E}[S] = \mathbb{E}[\mathbb{E}[S \mid N]] = 100\,\mathbb{E}[N] = 400$ pesos.
- b) $\text{Var}(S) = \mathbb{E}[\text{Var}(S \mid N)] + \text{Var}(\mathbb{E}[S \mid N]) = 400(4) + 100^2(4) = 1\,600 + 40\,000 = 41\,600$. La desviación estándar es $\sqrt{41\,600} \approx 204$ pesos.

Observa que casi toda la variabilidad proviene de la incertidumbre en el número de clientes, no del gasto individual.

*Puntaje:* 1 por las esperanzas y varianzas condicionales, 1 por a), 2 por b).

**Reactivo 27.**

- a) $M_X'(t) = 2e^t M_X(t)$, así que $\mathbb{E}[X] = M_X'(0) = 2$. Además, $M_X''(t) = 2e^t M_X(t) + 4e^{2t} M_X(t)$, luego $\mathbb{E}[X^2] = M_X''(0) = 6$ y $\text{Var}(X) = 6 - 2^2 = 2$.
- b) Es la MGF de $\text{Poisson}(2)$; por el Teorema de Unicidad, $X \sim \text{Poisson}(2)$.
- c) Por independencia, $M_{X+Y}(t) = e^{2(e^t - 1)}\,e^{3(e^t - 1)} = e^{5(e^t - 1)}$, luego $X + Y \sim \text{Poisson}(5)$ y $\mathbb{P}(X + Y = 0) = e^{-5} \approx 0.0067$.

*Puntaje:* 2 por a), 1 por b), 1 por c).

**Reactivo 28.** Se sabe que $\mathbb{E}[\bar{X}_n] = \mu$ y $\text{Var}(\bar{X}_n) = \sigma^2/n = 4/n$.

- a) Por Chebyshev, $\mathbb{P}(|\bar{X}_n - \mu| \ge 0.5) \le \frac{4}{0.25\,n}$. Basta que $\frac{16}{n} \le 0.05$, es decir, $n \ge 320$.
- b) Por el TLC, $\mathbb{P}(|\bar{X}_n - \mu| < 0.5) \approx 2\Phi\left(\frac{0.5\sqrt{n}}{2}\right) - 1 \ge 0.95$ exige $\frac{0.5\sqrt{n}}{2} \ge 1.96$, es decir, $\sqrt{n} \ge 7.84$ y $n \ge 61.47$. El menor tamaño es $n = 62$.
- c) Chebyshev es válida para **cualquier** distribución con varianza finita, así que debe cubrir el peor caso y resulta conservadora. El TLC usa la forma aproximadamente normal de $\bar{X}_n$, cuyas colas son mucho más delgadas; a cambio, solo da una aproximación.

*Puntaje:* 1.5 por a), 1.5 por b), 1 por c).

</details>

<details>
<summary><strong>Mostrar / ocultar las soluciones y rúbricas de la Parte III</strong></summary>

### Rúbrica general (8 puntos por demostración)

| Criterio | Puntos | Se otorga cuando… |
| :--- | :---: | :--- |
| Estructura | 2 | Queda claro qué se supone y qué se quiere probar; los eventos y variables están definidos. |
| Desarrollo | 4 | Cada paso es correcto y está justificado por un axioma, una definición o un resultado previo citado. |
| Cierre y redacción | 2 | Se enuncia la conclusión y no se usa como hipótesis lo que se quiere probar. |

**Errores que cuestan puntos:** aplicar la aditividad a eventos que no son disjuntos, confundir independencia con exclusión mutua, «demostrar» con un ejemplo numérico una afirmación general, y olvidar el dominio de validez de una MGF.

**Demostración 29.**

a) $A$ y $A^c$ son disjuntos y $A \cup A^c = \Omega$. Por la aditividad y el axioma de normalización, $1 = \mathbb{P}(\Omega) = \mathbb{P}(A) + \mathbb{P}(A^c)$, de donde $\mathbb{P}(A^c) = 1 - \mathbb{P}(A)$.

b) Si $A \subseteq B$, entonces $B = A \cup (B \setminus A)$ con $A \cap (B \setminus A) = \emptyset$. Por aditividad, $\mathbb{P}(B) = \mathbb{P}(A) + \mathbb{P}(B \setminus A) \ge \mathbb{P}(A)$, ya que $\mathbb{P}(B \setminus A) \ge 0$ por el axioma de no negatividad.

c) Escribe $A \cup B = A \cup (B \setminus A)$ (unión disjunta) y $B = (A \cap B) \cup (B \setminus A)$ (unión disjunta). Por aditividad, $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B \setminus A)$ y $\mathbb{P}(B \setminus A) = \mathbb{P}(B) - \mathbb{P}(A \cap B)$. Sustituyendo se obtiene la fórmula.

d) Por c), $\mathbb{P}(A \cap B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cup B)$. Como $A \cup B \subseteq \Omega$, por b) $\mathbb{P}(A \cup B) \le 1$, luego $\mathbb{P}(A \cap B) \ge \mathbb{P}(A) + \mathbb{P}(B) - 1$. $\blacksquare$

*Rúbrica específica:* 2 puntos por inciso; en cada uno se descuenta 1 si no se señala que la unión empleada es disjunta.

**Demostración 30.**

a) $A = (A \cap B) \cup (A \cap B^c)$ es una unión disjunta, así que $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B)$. Por la independencia:

$$
\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A)\,\mathbb{P}(B) = \mathbb{P}(A)\,[1 - \mathbb{P}(B)] = \mathbb{P}(A)\,\mathbb{P}(B^c)
$$

b) Por a), $A$ y $B^c$ son independientes. Aplicando a) de nuevo al par $(B^c, A)$ (la independencia es simétrica), $B^c$ y $A^c$ son independientes.

c) Si $A \cap B = \emptyset$, entonces $\mathbb{P}(A \cap B) = 0$, mientras que $\mathbb{P}(A)\,\mathbb{P}(B) > 0$. Como $0 \neq \mathbb{P}(A)\,\mathbb{P}(B)$, los eventos no son independientes. Intuitivamente, saber que ocurrió $A$ da la máxima información sobre $B$: que no ocurrió. $\blacksquare$

*Rúbrica específica:* a) vale 4 puntos, b) vale 2 y c) vale 2.

**Demostración 31.**

a) Para $x \ge 0$, $\mathbb{P}(X > x) = \int_x^\infty \lambda e^{-\lambda u}\,du = e^{-\lambda x}$. Como $\{X > s + t\} \subseteq \{X > s\}$:

$$
\mathbb{P}(X > s + t \mid X > s) = \frac{\mathbb{P}(X > s + t)}{\mathbb{P}(X > s)} = \frac{e^{-\lambda(s + t)}}{e^{-\lambda s}} = e^{-\lambda t} = \mathbb{P}(X > t)
$$

b) Como $\mathbb{P}(X = 0) = 0$, con probabilidad 1 se tiene $Y \in \{1, 2, 3, \dots\}$. Para $k \ge 1$, $\{Y = k\} = \{k - 1 < X \le k\}$, luego

$$
\mathbb{P}(Y = k) = e^{-\lambda(k - 1)} - e^{-\lambda k} = \left(e^{-\lambda}\right)^{k - 1}\left(1 - e^{-\lambda}\right)
$$

que es la función de masa de una $\text{Geométrica}(p)$ con $p = 1 - e^{-\lambda}$ y $1 - p = e^{-\lambda}$. $\blacksquare$

*Rúbrica específica:* a) vale 4 puntos (1 por la función de supervivencia, 1 por la inclusión de eventos, 2 por el cálculo); b) vale 4 puntos (1 por el soporte, 1 por la igualdad de eventos, 2 por identificar la distribución y su parámetro).

**Demostración 32.**

a) Sean $\mu_X = \mathbb{E}[X]$ y $\mu_Y = \mathbb{E}[Y]$. Por la linealidad de la esperanza:

$$
\text{Var}(X + Y) = \mathbb{E}\left[\big((X - \mu_X) + (Y - \mu_Y)\big)^2\right] = \text{Var}(X) + \text{Var}(Y) + 2\,\mathbb{E}[(X - \mu_X)(Y - \mu_Y)]
$$

y el último término es $2\,\text{Cov}(X, Y)$.

b) $\text{Cov}(X, Y) = \mathbb{E}[XY] - \mathbb{E}[X]\,\mathbb{E}[Y] = 0$ si $X$ e $Y$ son independientes; sustituyendo en a), $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$.

c) $\mathbb{E}[X] = \frac{1}{3}(-1 + 0 + 1) = 0$ y $\mathbb{E}[XY] = \mathbb{E}[X^3] = \frac{1}{3}(-1 + 0 + 1) = 0$, luego $\text{Cov}(X, Y) = 0 - 0 \cdot \mathbb{E}[Y] = 0$. Sin embargo, $\mathbb{P}(X = 0, Y = 0) = \mathbb{P}(X = 0) = \frac{1}{3}$, mientras que $\mathbb{P}(X = 0)\,\mathbb{P}(Y = 0) = \frac{1}{3} \cdot \frac{1}{3} = \frac{1}{9}$. Como $\frac{1}{3} \neq \frac{1}{9}$, no son independientes: $Y$ es una función de $X$, pero la relación no es lineal. $\blacksquare$

*Rúbrica específica:* a) vale 3 puntos, b) vale 1 y c) vale 4 (2 por la covarianza nula y 2 por exhibir un par de valores donde falla la factorización).

**Demostración 33.**

a) Para $t < \lambda$:

$$
M_X(t) = \int_0^\infty e^{tx}\,\lambda e^{-\lambda x}\,dx = \lambda \int_0^\infty e^{-(\lambda - t)x}\,dx = \frac{\lambda}{\lambda - t}
$$

La integral converge porque $\lambda - t > 0$; si $t \ge \lambda$, diverge.

b) Por la independencia, la MGF de la suma es el producto de las MGF:

$$
M_{S_n}(t) = \prod_{i=1}^{n} \frac{\lambda}{\lambda - t} = \left(1 - \frac{t}{\lambda}\right)^{-n}, \quad t < \lambda
$$

que coincide con la MGF de $\text{Gamma}(n, \lambda)$ en un intervalo abierto que contiene al 0. Por el **Teorema de Unicidad** de la MGF, $S_n \sim \text{Gamma}(n, \lambda)$.

c) $M_{S_n}'(t) = \frac{n}{\lambda}\left(1 - \frac{t}{\lambda}\right)^{-n-1}$ y $M_{S_n}''(t) = \frac{n(n+1)}{\lambda^2}\left(1 - \frac{t}{\lambda}\right)^{-n-2}$. Evaluando en $t = 0$: $\mathbb{E}[S_n] = \frac{n}{\lambda}$ y $\text{Var}(S_n) = \frac{n(n+1)}{\lambda^2} - \frac{n^2}{\lambda^2} = \frac{n}{\lambda^2}$. $\blacksquare$

*Rúbrica específica:* a) vale 2 puntos (incluyendo la condición $t < \lambda$), b) vale 4 (2 por la factorización por independencia y 2 por invocar la unicidad) y c) vale 2.

**Demostración 34.**

a) Como $X \ge 0$, se cumple $X \ge a\,\mathbb{I}_{\{X \ge a\}}$ en todo $\Omega$: si $X \ge a$, el lado derecho vale $a \le X$; si no, vale $0 \le X$. Por la monotonía de la esperanza, $\mathbb{E}[X] \ge a\,\mathbb{P}(X \ge a)$, de donde se obtiene la desigualdad.

b) Aplica a) a la variable no negativa $(X - \mu)^2$ con $a = \varepsilon^2$:

$$
\mathbb{P}(|X - \mu| \ge \varepsilon) = \mathbb{P}\big((X - \mu)^2 \ge \varepsilon^2\big) \le \frac{\mathbb{E}[(X - \mu)^2]}{\varepsilon^2} = \frac{\sigma^2}{\varepsilon^2}
$$

c) Por la linealidad, $\mathbb{E}[\bar{X}_n] = \mu$; por la independencia, $\text{Var}(\bar{X}_n) = \frac{1}{n^2}\sum_{i=1}^{n}\text{Var}(X_i) = \frac{\sigma^2}{n}$. Por b), para todo $\varepsilon > 0$:

$$
\mathbb{P}(|\bar{X}_n - \mu| \ge \varepsilon) \le \frac{\sigma^2}{n\varepsilon^2} \xrightarrow[n \to \infty]{} 0
$$

que es exactamente la definición de $\bar{X}_n \xrightarrow{P} \mu$. $\blacksquare$

*Rúbrica específica:* a) vale 3 puntos, b) vale 2 y c) vale 3 (1 por la media, 1 por la varianza usando la independencia, 1 por el paso al límite y la referencia a la definición).

</details>

---

## 📊 Diagnóstico y plan de repaso

### Tabla de diagnóstico

Anota tus puntos por unidad y calcula tu porcentaje de dominio.

| Unidad | Reactivos | Puntos posibles | Mis puntos | Mi porcentaje |
| :--- | :--- | :---: | :---: | :---: |
| 1. Espacios de probabilidad y combinatoria | 1 a 4, 21, 29 | 16 | | |
| 2. Probabilidad condicional, independencia y Bayes | 5 a 8, 22, 23, 30 | 20 | | |
| 3. Variables aleatorias y familias de distribuciones | 9 a 12, 24, 25, 31 | 20 | | |
| 4. Esperanza, momentos y funciones generadoras | 13 a 16, 26, 27, 32, 33 | 28 | | |
| 5. Teoremas límite y leyes asintóticas | 17 a 19, 28, 34 | 15 | | |
| 6. Procesos estocásticos (complementaria) | 20 | 1 | | |
| **Total** | | **100** | | |

La Unidad 4 pesa más porque la esperanza y la varianza son las herramientas con las que se demuestran los teoremas límite de la Unidad 5. La Unidad 6 tiene un peso simbólico porque es complementaria y de laboratorio.

### Interpretación del resultado

| Puntaje total | Diagnóstico | Qué hacer |
| :---: | :--- | :--- |
| 85 a 100 | Preparación sólida | Repasa solo los reactivos fallados y practica la redacción de demostraciones con un límite de tiempo. |
| 70 a 84 | Preparación aceptable con huecos | Repasa las unidades con menos del 70 % y rehaz tus reactivos sin ver las soluciones. |
| 50 a 69 | Preparación insuficiente | Estudia de nuevo las secciones señaladas abajo y resuelve los ejercicios de cada unidad antes de repetir el auto-examen. |
| Menos de 50 | Se requiere un plan de estudio completo | Empieza por las Unidades 1 y 2, que son la base de todo lo demás, y busca asesoría con tu profesor. |

Más allá del total, **cualquier unidad por debajo del 60 %** merece atención prioritaria, aunque tu puntaje global sea bueno.

### Mapa de repaso

| Si fallaste el reactivo… | Repasa la sección |
| :--- | :--- |
| 1, 2 | [1.1 Pensamiento probabilístico, desarrollo histórico y combinatoria](../src/unidad1/01-fundamentos-historicos-conteo.md) |
| 3 | [1.2 Espacios muestrales, álgebra de eventos y σ-álgebras](../src/unidad1/02-espacios-muestrales-sigma-algebras.md) |
| 21, 29 | [1.3 Axiomática de Kolmogórov y propiedades fundamentales](../src/unidad1/03-axiomatica-kolmogorov-propiedades.md) |
| 4 | [1.4 Probabilidad geométrica y problemas clásicos](../src/unidad1/04-probabilidad-geometrica.md) |
| 23 | [2.1 Probabilidad condicional y regla de la multiplicación](../src/unidad2/01-probabilidad-condicional-multiplicacion.md) |
| 5, 6, 30 | [2.2 Eventos independientes y propiedades](../src/unidad2/02-independencia-estocastica.md) |
| 7 | [2.3 Particiones y Teorema de la Probabilidad Total](../src/unidad2/03-teorema-probabilidad-total.md) |
| 8, 22 | [2.4 Teorema de Bayes, pruebas diagnósticas y falacias condicionales](../src/unidad2/04-teorema-bayes-inferencia-diagnostico.md) |
| 9 (tipo de variable) | [3.1 Concepto y clasificación formal de variables aleatorias](../src/unidad3/01-concepto-clasificacion-va.md) |
| 9, 24 | [3.2 Funciones de masa, densidad y distribución acumulada](../src/unidad3/02-funciones-probabilidad-distribucion.md) |
| 10, 25 | [3.3 Vectores aleatorios, distribuciones conjuntas e independencia](../src/unidad3/03-vectores-aleatorios-distribuciones-conjuntas.md) |
| 11, 23 (b), 31 (b) | [3.4 Familias de distribuciones discretas fundamentales](../src/unidad3/04-distribuciones-discretas.md) |
| 12, 31 (a) | [3.5 Familias de distribuciones continuas fundamentales](../src/unidad3/05-distribuciones-continuas.md) |
| 13 | [4.1 Esperanza matemática, valor esperado y linealidad](../src/unidad4/01-esperanza-matematica.md) |
| 14, 15, 32 | [4.2 Momentos, varianza, covarianza y correlación](../src/unidad4/02-momentos-varianza-covarianza.md) |
| 25 (c), 26 | [4.3 Esperanza condicional y ley de varianza total](../src/unidad4/03-esperanza-condicional.md) |
| 16, 27, 33 | [4.4 Funciones generadoras de momentos y función característica](../src/unidad4/04-funciones-generadoras.md) |
| 17, 28 (a), 34 (a, b) | [5.1 Desigualdades de probabilidad y concentración](../src/unidad5/01-desigualdades-probabilidad.md) |
| 18 | [5.2 Modos de convergencia estocástica](../src/unidad5/02-modos-convergencia-estocastica.md) |
| 34 (c) | [5.3 Ley Débil y Fuerte de los Grandes Números](../src/unidad5/03-ley-grandes-numeros.md) |
| 19, 28 (b) | [5.4 El Teorema del Límite Central](../src/unidad5/04-teorema-limite-central.md) |
| 20 | [6.1 Cadenas de Markov a tiempo discreto](../src/unidad6/01-cadenas-markov-tiempo-discreto.md) |

Para practicar más reactivos de opción múltiple, consulta el [Apéndice C. Banco de reactivos institucionales resueltos](../src/apendices/c-banco-reactivos-palmat.md), y para repasar parámetros, medias y varianzas, la [Tabla sinóptica de distribuciones](../src/apendices/b-tabla-distribuciones.md).

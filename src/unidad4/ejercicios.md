# Ejercicios de la Unidad 4

## Bloque A: Esperanza matemática y linealidad

1. **El problema de las coincidencias (Desarreglos):** Se mezclan \\(n\\) cartas numeradas del 1 al \\(n\\) y se descubren una a una. Se dice que hay una coincidencia si la carta \\(i\\) aparece en la posición \\(i\\).
   - Defina las variables indicadoras \\(I\_i = \mathbb{I}(\text{coincidencia en la posición } i)\\) para \\(i = 1, \dots, n\\).
   - Sea \\(X = \sum\_{i=1}^n I\_i\\) el número total de coincidencias.
   - (a) Calcule \\(\mathbb{E}[I\_i]\\) y deduzca \\(\mathbb{E}[X]\\) para cualquier \\(n \ge 1\\).
   - (b) Calcule \\(\text{Var}(I\_i)\\) y \\(\text{Cov}(I\_i, I\_j)\\) para \\(i \neq j\\).
   - (c) Demuestre que \\(\text{Var}(X) = 1\\) para todo \\(n \ge 2\\).

2. **Cálculo de esperanza vía la fórmula de la cola:**
   - Sea \\(X \sim \text{Exp}(\lambda)\\). Utilice la fórmula de la integral de la cola (Teorema 4.6) para demostrar directamente que \\(\mathbb{E}[X] = \frac{1}{\lambda}\\).

---

## Bloque B: Varianza, covarianza y correlación

3. **No correlación vs. Independencia:**
   - Sea \\(X \sim \mathcal{U}(-1, 1)\\) y sea \\(Y = X^2\\).
   - (a) Demuestre analíticamente que \\(\text{Cov}(X, Y) = 0\\) y por ende \\(\rho(X, Y) = 0\\).
   - (b) Demuestre formalmente que \\(X\\) e \\(Y\\) **no son independientes**, evaluando \\(\mathbb{P}(X > 0.5 \text{ y } Y > 0.25)\\).

4. **Matriz de covarianza y combinaciones lineales:**
   - Sean \\(X\_1, X\_2, X\_3\\) variables aleatorias con varianzas \\(\sigma\_1^2 = 4, \ \sigma\_2^2 = 9, \ \sigma\_3^2 = 16\\) y covarianzas \\(\text{Cov}(X\_1, X\_2) = 1, \ \text{Cov}(X\_1, X\_3) = -2, \ \text{Cov}(X\_2, X\_3) = 3\\).
   - Calcule la varianza de la combinación lineal \\(W = 2X\_1 - 3X\_2 + X\_3\\).

---

## Bloque C: Esperanza condicional y varianza total

5. **El proceso de ramificación (Galton-Watson):**
   - Una población comienza con un individuo en la generación 0 (\\(Z\_0 = 1\\)). Cada individuo en la generación \\(n\\) produce un número aleatorio \\(X\\) de descendientes independientes con media \\(\mu\\) y varianza \\(\sigma^2\\).
   - Sea \\(Z\_{n+1} = \sum\_{i=1}^{Z\_n} X\_i\\) el tamaño de la generación \\(n+1\\).
   - (a) Utilice la Ley de las Esperanzas Iteradas para demostrar que \\(\mathbb{E}[Z\_n] = \mu^n\\).
   - (b) Aplique la Ley de la Varianza Total para deducir una fórmula de recurrencia para \\(\text{Var}(Z\_n)\\).

---

## Bloque D: Funciones generadoras de momentos (MGF)

6. **Identificación distribucional por MGF:**
   - La MGF de una variable aleatoria \\(X\\) es \\(M\_X(t) = (0.2 + 0.8 e^t)^5 \cdot e^{3t}\\).
   - (a) Identifique el tipo exacto de distribución y sus parámetros.
   - (b) Calcule \\(\mathbb{E}[X]\\) y \\(\text{Var}(X)\\) derivando \\(M\_X(t)\\).

7. **Suma de variables Poisson independientes:**
   - Sean \\(X\_1 \sim \text{Poisson}(\lambda\_1)\\) y \\(X\_2 \sim \text{Poisson}(\lambda\_2)\\) independientes.
   - Utilice la propiedad multiplicativa de la MGF y el Teorema de Unicidad para demostrar formalmente que \\(X\_1 + X\_2 \sim \text{Poisson}(\lambda\_1 + \lambda\_2)\\).

8. **Suma de variables Normales independientes:**
   - Sean \\(X \sim \mathcal{N}(\mu\_1, \sigma\_1^2)\\) e \\(Y \sim \mathcal{N}(\mu\_2, \sigma\_2^2)\\) independientes.
   - Demuestre mediante la MGF que \\(aX + bY \sim \mathcal{N}(a\mu\_1 + b\mu\_2, \ a^2\sigma\_1^2 + b^2\sigma\_2^2)\\).
# Probabilidad — Un curso para la Licenciatura en Matemáticas

**Autor:** Dr. Pablo Eduardo Cancino Marentes  
**Institución:** Universidad Autónoma de Nayarit, Unidad Académica de Ciencias Básicas e Ingenierías, Programa Académico de Licenciatura en Matemáticas (PALMAT).  

Este repositorio contiene el texto completo, en formato [mdBook](https://rust-lang.github.io/mdBook/), del curso-laboratorio de *Probabilidad* (clave CBIMAT-234, Plan de Estudios 2024 / Actualización 2026) de la Licenciatura en Matemáticas de la UAN. El libro cubre de manera rigurosa y formal las cinco unidades del programa oficial —espacios de probabilidad y combinatoria, probabilidad condicional e inferencia bayesiana, variables aleatorias y familias de distribuciones, teoría de momentos y operadores lineales, y leyes límite asintóticas— complementado con una unidad de procesos estocásticos y simulación de Monte Carlo con Python, y apéndices de análisis de la medida y banco de reactivos institucionales.

## Libro en formato mdBook

Disponible para lectura en línea en:  
👉 **[https://pabloecancino.github.io/libro_probabilidad/](https://pabloecancino.github.io/libro_probabilidad/)**

## Aplicación Móvil e Interactiva Complementaria

Este libro cuenta con una aplicación interactiva desarrollada bajo la norma técnica **NTE-UAN-APK-001 v1.4** de la UAN:  
📱 **[Web App Interactiva en Vivo](https://PabloeCancino.github.io/uan-apk-probabilidad/)** | 📥 **[Descargar APK Android](https://github.com/PabloeCancino/uan-apk-probabilidad/releases)** | 💻 **[Repositorio GitHub](https://github.com/PabloeCancino/uan-apk-probabilidad)**

## Estructura del libro

- **Unidad 1.** Espacios de probabilidad y combinatoria (técnicas de conteo, formalización de espacios muestrales, $\sigma$-álgebras, axiomas de Kolmogórov, principio de inclusión-exclusión y probabilidad geométrica).
- **Unidad 2.** Probabilidad condicional, independencia y Teorema de Bayes (espacio muestral reducido, independencia mutua vs. 2 a 2, Teorema de la Probabilidad Total, Teorema de Bayes, pruebas diagnósticas y falacias condicionales).
- **Unidad 3.** Variables aleatorias y familias de distribuciones (funciones de masa PMF, densidad PDF y distribución acumulada CDF, vectores aleatorios bivariados, transformaciones jacobianas, familias discretas y continuas exhaustivas).
- **Unidad 4.** Esperanza matemática, momentos y operadores lineales (linealidad de la esperanza, varianza, covarianza, correlación, esperanza condicional y leyes de varianza total, funciones generadoras MGF/PGF y función característica).
- **Unidad 5.** Teoremas límite y leyes asintóticas (desigualdades de Márkov, Chebyshev, Jensen y Chernoff, modos de convergencia estocástica, Ley Débil y Fuerte de los Grandes Números, y el Teorema del Límite Central de Lindeberg-Lévy).
- **Unidad 6 (complementaria y laboratorio).** Procesos estocásticos y simulación computacional (cadenas de Markov a tiempo discreto, métodos de Monte Carlo, transformada inversa, y laboratorio científico con Python/SciPy).
- **Apéndices.** Teoría de la medida y convergencia, tabla sinóptica de distribuciones, banco de reactivos institucionales resueltos PALMAT 2024 y bibliografía comentada.

## Cómo compilar el libro localmente

Este libro se construye con [mdBook](https://rust-lang.github.io/mdBook/). Para compilarlo localmente:

```bash
# Instalar mdBook (requiere Rust/Cargo: https://rustup.rs)
cargo install mdbook

# Clonar este repositorio
git clone https://github.com/PabloeCancino/libro_probabilidad.git
cd libro_probabilidad

# Compilar y ver el libro en el navegador con recarga automática
mdbook serve --open
```

El HTML compilado se genera en la carpeta `book/` (excluida del control de versiones).

## Publicación automática en GitHub Pages

Este repositorio incluye un flujo de trabajo de GitHub Actions (`.github/workflows/deploy.yml`) que reconstruye y publica el libro automáticamente en GitHub Pages con cada `push` a la rama `main`. Para activarlo:

1. En GitHub, ir a **Settings → Pages**.
2. En "Build and deployment", seleccionar **Source: GitHub Actions**.
3. El libro se despliega automáticamente en `https://pabloecancino.github.io/libro_probabilidad/`.

## Licencia

Este texto se publica bajo **[Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.es)**. Ver [LICENSE.md](LICENSE.md).

En resumen: puedes leer, descargar y compartir el libro completo citando la autoría, siempre que no lo modifiques ni le des uso comercial. Para permisos adicionales (traducción, adaptación, uso comercial), contacta al autor.

## Cómo citar

> Cancino Marentes, P. E. (2026). *Probabilidad: Un curso para la Licenciatura en Matemáticas*. Manuscrito publicado como texto abierto en GitHub. Disponible en: https://pabloecancino.github.io/libro_probabilidad/

## Contacto

Dr. Pablo Eduardo Cancino Marentes — pabloe.cancino@uan.edu.mx

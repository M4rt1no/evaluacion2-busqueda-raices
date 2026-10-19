# Informe de Análisis de Algoritmos de Búsqueda de Raíces

## 1. Análisis de Convergencia y Velocidad (Iteraciones por Función)
En las pruebas realizadas con las distintas funciones (polinómica, logarítmica, exponencial, trigonométrica y mixta), se observó una diferencia drástica en el número de iteraciones requeridas según la naturaleza del método:

* **Función Polinómica ($f(x) = x^3 - x - 2$):** Ambas versiones de Newton-Raphson necesitaron 5 iteraciones, mientras que la bisección tardó 20.
* **Función Logarítmica ($f(x) = \ln(x) - 1$):** Nuevamente Newton-Raphson domina en 3 iteraciones, y bisección en sentido opuesto con 19.
* **Función Exponencial ($f(x) = e^{-x}-x$):** Newton-Raphson lo logra en 3 iteraciones, y esta vez punto fijo llega hasta 25.
* **Función Trigonométrica ($f(x) = \cos(-x)-x$):** Newton-Raphson se tarda 4 iteraciones, y punto fijo 34.
* **Función Mixta ($f(x) = \sqrt{x} - \cos(x)$):** Newton-Raphson continúa liderando con 4 iteraciones, y punto fijo llega a las 295.

**¿Por qué ocurre esto?**  
Los métodos abiertos como **Newton-Raphson** aprovechan la información de la derivada para realizar saltos proporcionales a la pendiente. En contraste, los métodos cerrados reducen el intervalo de forma estricta e independiente a la forma de la curva, lo que exige una mayor cantidad de iteraciones para alcanzar la misma tolerancia de error.

---

## 2. Orden de Convergencia y Análisis del Gráfico de Error
El análisis del gráfico de error frente a iteraciones permite visualizar claramente en la mayoría de casos el orden de convergencia de cada algoritmo:

* **Bisección (Convergencia Lineal):** Se observa una línea diagonal con pendiente constante y uniforme. Cada iteración reduce el error aproximadamente a la mitad.
* **Falsa posición (Convergencia Lineal):** La pendiente es constante.
* **Punto fijo (Convergencia Lineal):** La recta tiene pendiente constante como las anteriores.
* **Secante (Convergencia Superlineal):** Se observa más rápida, pero no es muy consistente en estos casos.
* **Newton-Raphson / Newton-Raphson Modificado (Convergencia Cuadrática):** La curva presenta una forma cuadrática que cuesta representar en la gráfica debido al número de iteraciones.

---

## 3. Requisitos de Intervalo

* **Requieren cambio de signo (Métodos Cerrados):** 
  * *Bisección* y *Falsa Posición*. Exigen que $f(a) \cdot f(b) < 0$ (Teorema de Bolzano). Garantizan la convergencia, ofreciendo alta robustez.
* **No requieren cambio de signo (Métodos Abiertos):** 
  * *Punto Fijo*, *Newton-Raphson*, *Newton-Raphson Modificado* y *Secante*. Requieren una estimación inicial ($x_0$) o un par de puntos cercanos. No evalúan cambios de signo globales, lo que los hace más rápidos pero vulnerables a divergir.

---

## 4. Comportamiento en Raíces Múltiples
En este laboratorio no se trató un polinomio de raíces múltiples, sin embargo aquí se analizará:

* **Métodos cerrados:** Falla , ya que no hay cambio de signo en los extremos del intervalo ($f(a) \cdot f(b) > 0$).
* **Newton-Raphson Modificado ($u(x) = f(x)/f'(x)$):** Este método está adaptado para evitar los problemas de la multiplicidad. Tiene un comportamiento óptimo.
* **Otros métodos cerrados:** Presentan varios problemas. Se enlentecen o divergen dependiendo de la situación.

---

## 5. Influencia del Intervalo Inicial y la Estimación Inicial
El punto de partida de los algoritmos determina el éxito o fracaso:

* **En Métodos Abiertos:** Una mala estimación puede provocar divisiones por cero, divergencia o saltos hacia raíces completamente ajenas a las buscadas. Aún así el efecto en la rapidez puede variar según el método.
* **En Métodos Cerrados:** Afecta linealmente el número de iteraciones. Si el intervalo no es válido nunca llegará a una respuesta, pero si lo es, convergerá de manera segura.

---

## 6. Recomendación de Algoritmos
Lo más importante es conocer la situación del problema:

* Métodos cerrados: Para más seguridad.
* Newton-Raphson: Si se tiene una buena estimación inicial.
* Secante: Para evitar las derivadas.
* N-R Modificado: Para las funciones con multiplicidad.
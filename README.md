# evaluacion2-busqueda-raices
Laboratorio evaluado 2 - Comparación de métodos de búsqueda de raíces y su convergencia.

## Requisitos del Entorno

Se recomienda utilizar un entorno virtual de Python (`venv`).

###  Crear entorno y preparar dependencias

Desde raíz del repositorio:
```bash
bash Create_python/create_env.sh
```
### Activar el entorno
```bash
source env/bin/activate
```

Una vez activado,  puedes ejecutar tus scripts:
```bash
python src/scripts/mi_script.py
```

Para salir del entorno:
```bash
deactivate
```

## Explicación de scripts

### Métodos
* biseccion.py
* falsa_posicion.py
* punto_fijo.py
* secante.py
* newton_raphson.py
* newton_raphson_mejorado.py

Ejecutan el método descrito en el nombre. Se debe modificar el script para cambiar la función, valores iniciales y criterios de término. 
El código principal establece los parámetros, ejecuta la función que devuelve una lista con resultados de cada iteración y los muestra en terminal.

* probar_f.py

Ejecuta todos los métodos en una ejecución con los parámetros dados. Útil para comparar resultados.

### Gráficas
* graficar_funcion.py

Crea un gráfico con matplotlib de la función f(x) que se entrega. Se debe modificar el intervalo que se muestra la función y la flecha, y el valor y ubicación de la raíz. Se puede cambiar el nombre del archivo .png resultante y se guarda en la carpeta assets.

* graficar_error.py

Calcula los resultados de la función y crea un gráfico de cada método. El gráfico muestra la relación entre las iteraciones que ocurren y el error del valor obtenido y se guarda en la carpeta assets.

### Datos

* generar_csv.py

Crea un archivo .csv que se guarda en data. Entrega información de los valores de una función en cierto intervalo con determinada diferencia entre valores que entran. Lo anterior es modificable según amerite el caso.

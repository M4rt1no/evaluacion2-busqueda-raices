import os
import matplotlib

matplotlib.use("Agg")  # Backend sin ventana: guardar con savefig
import matplotlib.pyplot as plt

# Rutas relativas a este script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EVAL2_DIR = os.path.dirname(SCRIPT_DIR)
ASSETS_DIR = os.path.join(EVAL2_DIR, "assets")


import biseccion as bi
import falsa_posicion as fp
import punto_fijo as pf
import secante as se
import newton_raphson as nr
import newton_raphson_mejorado as nrm

def nueva_f(x):
    return x * (x - 1) * (x + 1) - 2

def nueva_g(x):
    return (x+2)**(1/3)

bi.f = nueva_f
fp.f = nueva_f
pf.g = nueva_g
se.f = nueva_f
nr.f = nueva_f
nrm.f = nueva_f

def generar_lista_errores(resul,x0=None):
    errores = []
    if x0:
        errores.append(abs(resul[0][0] - x0))
    for i in range(1,len(resul)):
        errores.append(abs(resul[i][0] - resul[i-1][0]))
    return errores
    
def generar_graficas_individuales(datos_metodos):
    """Recibe un diccionario donde la clave es el nombre del método
    y el valor es su lista de errores correspondiente.
    """
    os.makedirs(ASSETS_DIR, exist_ok=True)

    for nombre_metodo, errores in datos_metodos.items():
        # Validamos que la lista tenga datos (por si algún método falló y retornó -1 o -2)
        if not isinstance(errores, list) or len(errores) == 0:
            print(f"No hay datos válidos para graficar el método: {nombre_metodo}")
            continue

        iteraciones = list(range(1, len(errores) + 1))

        # 1. Creamos una nueva figura limpia para cada método
        plt.figure(figsize=(10, 6))

        plt.semilogy(
            iteraciones,
            errores,
            marker="o",
            color="#1f77b4",
            linewidth=2,
            markersize=6,
            label=f"Error ({nombre_metodo})"
        )

        plt.title(f"Convergencia de x*(x-1)*(x+1)-2 con {nombre_metodo}")
        plt.xlabel("Número de Iteración")
        plt.ylabel("Error Absoluto |x_i - x_{i-1}| (Escala Logarítmica)")
        
        plt.grid(True, which="both", alpha=0.3)
        plt.legend()
        plt.tight_layout()

        # 2. Generamos un nombre de archivo único limpiando espacios y tildes
        nombre_limpio = (
            nombre_metodo.lower()
            .replace(" ", "_")
            .replace("ó", "o")
            .replace("á", "a")
        )
        destino = os.path.join(ASSETS_DIR, f"convergencia_{nombre_limpio}_poli.png")

        # 3. Guardamos y cerramos la figura obligatoriamente
        plt.savefig(destino, dpi=120)
        plt.close()  # <-- Crucial para que las gráficas no se encimen en memoria
        
        print(f"Gráfica generada para '{nombre_metodo}' en: {destino}")


if __name__ == "__main__":
    a = 1
    b = 2
    error = 1e-6
    iter_max = 100    
    resultados_simulados = {
        "Bisección": generar_lista_errores(bi.biseccion(a, b, error, iter_max)),
        "Falsa posición": generar_lista_errores(fp.falsa_posicion(a, b, error, iter_max)),
        "Punto Fijo": generar_lista_errores(pf.punto_fijo(a, error, iter_max), a),
        "Secante": generar_lista_errores(se.secante(a, b, error, iter_max)),
        "Newton-Raphson": generar_lista_errores(nr.newton_raphson(a, error, iter_max), a),
        "Newton-Raphson mejorado": generar_lista_errores(nrm.newton_raphson_m(a, error, iter_max), a)
    }
    
    generar_graficas_individuales(resultados_simulados)
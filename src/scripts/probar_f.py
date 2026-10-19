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
pf.f = nueva_f
pf.g = nueva_g
se.f = nueva_f
nr.f = nueva_f
nrm.f = nueva_f

if __name__ == "__main__":
    a = 1
    b = 2
    error = 1e-6
    iter_max = 100
    resultados = []

    resultados.append(bi.biseccion(a, b, error, iter_max))
    resultados.append(fp.falsa_posicion(a, b, error, iter_max))
    resultados.append(pf.punto_fijo(a, error, iter_max))
    resultados.append(se.secante(a, b, error, iter_max))
    resultados.append(nr.newton_raphson(a, error, iter_max))
    resultados.append(nrm.newton_raphson_m(a, error, iter_max))

    for metodo in resultados:
        if metodo == -1 or metodo == -2:
            print("\nRaíz no encontrada, error", metodo)
        else:
            print("\nx:", metodo[-1][0])
            print("f(x):", metodo[-1][1])
            print("Iteraciones:", len(metodo))
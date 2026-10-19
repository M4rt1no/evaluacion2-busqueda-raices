import numpy as np

def f(x):
    return (x - 1) * (x - 1) * (x + 2)

def g(x):
    v = 3 * x - 2
    return np.sign(v) * np.abs(v) ** (1 / 3)

def punto_fijo(x0, error, iter_max):
    iteraciones = []
    p=x0
    for i in range(0, iter_max):
        p=g(p)
        iteraciones.append([p, f(p)])

        if abs(iteraciones[i][1])<error:
            return iteraciones
        if i>0:
            if abs(p-iteraciones[i-1][0])<error:
                return iteraciones
        if abs(p)>1e12:
            return -2
            
    return -1    

if __name__ == "__main__":

    x0=-1.5
    error=1e-6
    iter_max= 100

    iteraciones = punto_fijo(x0, error, iter_max)

    if iteraciones==-1:
        print("No se encontró raíz en", iter_max, "iteraciones")
    else:
        if iteraciones==-2:
            print("La sucesión diverge.")
        else:
            for i in range(0, len(iteraciones)):
                print("\nIteración " + str(i+1) + ":")
                print("x:", iteraciones[i][0])
                print("f(x):", iteraciones[i][1])
                if i>0:
                    print("Error(x-x_anterior):", abs(iteraciones[i][0]-iteraciones[i-1][0]))
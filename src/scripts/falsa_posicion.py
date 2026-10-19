
def f(x):
    return (x - 1) * (x - 1) * (x + 2)

def falsa_posicion(lim_min, lim_max, error, iter_max):
    if f(lim_max)*f(lim_min)>0:
        return -2
    elif f(lim_min) == 0:
        return [[lim_min, f(lim_min)]]
    elif f(lim_max) == 0:
        return [[lim_max, f(lim_max)]]
    
    iteraciones = []
    for i in range(0, iter_max):
        lim_new = (lim_min * f(lim_max) - lim_max * f(lim_min)) / (f(lim_max) - f(lim_min))
        iteraciones.append([lim_new, f(lim_new)])

        if abs(iteraciones[i][1])<error:
            return iteraciones
        if i>0:
            if abs(iteraciones[i][0]-iteraciones[i-1][0])<error:
                return iteraciones
            
        if f(lim_min)*f(lim_new)<0:
            lim_max=lim_new 
        else:
            lim_min=lim_new

    return -1    

if __name__ == "__main__":

    a=-3
    b=0
    error=1e-6
    iter_max= 100

    iteraciones = falsa_posicion(a, b, error, iter_max)

    if iteraciones==-1:
        print("No se encontró raíz en", iter_max, "iteraciones")
    else:
        if iteraciones==-2:
            print("No hay raíz en intervalo ["+str(a)+";"+str(b)+"]")
        else:
            for i in range(0, len(iteraciones)):
                print("\nIteración " + str(i+1) + ":")
                print("x:", iteraciones[i][0])
                print("f(x):", iteraciones[i][1])
                if i>0:
                    print("Error(x-x_anterior):", abs(iteraciones[i][0]-iteraciones[i-1][0]))
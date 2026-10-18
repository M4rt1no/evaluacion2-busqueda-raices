
def f(x):
    return (x - 1) * (x - 1) * (x + 2)

def secante(x0, x1, error, iter_max):
    if (f(x1)-f(x0))==0:
        return -2

    iteraciones = []
    for i in range(0, iter_max):
        if i>1:
            if (iteraciones[i-1][1] - iteraciones[i-2][1])==0:
                return -2
            x = iteraciones[i-1][0] - iteraciones[i-1][1] * (iteraciones[i-1][0] - iteraciones[i-2][0]) / (iteraciones[i-1][1] - iteraciones[i-2][1])
        elif i>0:
            x = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        else:
            x = x1
        iteraciones.append([x, f(x)])

        if abs(iteraciones[i][1])<error:
            return iteraciones
        if i>0:
            if abs(iteraciones[i][0]-iteraciones[i-1][0])<error:
                return iteraciones
            
    return -1    

if __name__ == "__main__":

    x0= -3
    x1= 0
    error=1e-6
    iter_max= 100

    iteraciones = secante(x0, x1, error, iter_max)

    if iteraciones==-1:
        print("No se encontró raíz en", iter_max, "iteraciones")
    elif iteraciones==-2:
        print("Se produjo una división por 0.")
    else:
        for i in range(0, len(iteraciones)):
            print("\nIteración " + str(i+1) + ":")
            print("x:", iteraciones[i][0])
            print("f(x):", iteraciones[i][1])
            if i>0:
                print("Error(x-x_anterior):", abs(iteraciones[i][0]-iteraciones[i-1][0]))
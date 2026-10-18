
def f(x):
    return (x**2)/2 + x - 10

def derivadaf(x):
    h = 10**(-7)
    return (f(x+h)-f(x-h))/(2*h)

def u(x):
    return f(x)/derivadaf(x)

def derivadau(x):
    h = 10**(-7)
    return (u(x+h)-u(x-h))/(2*h)

def newton_raphson(x0, error, iter_max):
    if derivadaf(x0) or derivadau(x0)==0:
        return -2

    iteraciones = []
    x=x0
    for i in range(0, iter_max):
        x = x - u(x)/derivadau(x)
        iteraciones.append([x, f(x)])

        if abs(iteraciones[i][1])<error:
            return iteraciones
        if i>0:
            if abs(iteraciones[i][0]-iteraciones[i-1][0])<error:
                return iteraciones
        if derivadaf(x)==0 or derivadau(x)==0:
            return -2

    return -1

if __name__ == "__main__":
    x0= 0
    error=1e-6
    iter_max= 100

    iteraciones = newton_raphson(x0, error, iter_max)

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

import os

import matplotlib

matplotlib.use("Agg")  # backend sin ventana: guardar con savefig
import matplotlib.pyplot as plt
import numpy as np

# Rutas relativas a este script (script/ -> Eval2/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EVAL2_DIR = os.path.dirname(SCRIPT_DIR)
ASSETS_DIR = os.path.join(EVAL2_DIR, "assets")


def f(x):
    return x * (x - 1) * (x + 1) - 2


def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)

    x = np.linspace(1, 2, 400)
    y = f(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, color="#1f77b4", linewidth=2, label="f(x) = x*(x-1)*(x+1)-2")
    plt.axhline(0, color="black", linewidth=0.8)          # eje X
    plt.axvline(0, color="black", linewidth=0.8)          # eje Y

    # Marcar la raiz x en el intervalo
    plt.plot(1.5213797067367147, 0, "o", color="#d62728", markersize=9, label="Raiz x = 1.5213797067367147")
    plt.annotate("x = 1.5213797067367147", xy=(1.5213797067367147, 0), xytext=(1.2, 1.5),
                 arrowprops=dict(arrowstyle="->", color="#d62728"))

    plt.title("Funcion f(x) = x*(x-1)*(x+1)-2 en [1, 2]")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    destino = os.path.join(ASSETS_DIR, "funcionpoli.png")
    plt.savefig(destino, dpi=120)
    plt.close()
    print(f"Imagen generada en: {destino}")


if __name__ == "__main__":
    main()
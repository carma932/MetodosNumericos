from math import *
import sympy as sp

def puntofijo():
    print("==================================================")
    print("   BIENVENIDO AL MÉTODO DE PUNTO FIJO MEJORADO    ")
    print("==================================================")
    print("Nota: Usa 'x' para la variable. Ejemplos de g(x):")
    print("  cos(x)")
    print("  (x + 2)**(1/2)")
    print("  exp(-x)\n")

    x = sp.symbols('x')
    g_texto = input("1. Introduce la función g(x): ")
    
    try:
        g = sp.lambdify(x, g_texto)
    except Exception as e:
        print("\n[Error]: La función ingresada no es válida.")
        return

    try:
        x0 = float(eval(input("2. Aproximación inicial (x0) (ej. pi/2 o 0): ")))
        n = int(input("3. Número máximo de iteraciones (n) (ej. 50): "))
        tol = float(eval(input("4. Tolerancia (ej. 10**-4 o 0.001): ")))
    except Exception as e:
        print("\n[Error]: Introdujiste un valor numérico inválido.")
        return

    print("\n" + "="*50)
    print(f"{'k':<4} | {'x_k (Aproximación)':<18} | {'Error (abs)':<15}")
    print("="*50)
    for k in range(n):
        try:
            x1 = g(x0)
        except Exception as e:
            print(f"\n[Error]: No se pudo evaluar la función en x = {x0}. {e}")
            return
        error = abs(x1 - x0)
        print(f"{k+1:<4} | {x1:<18.6f} | {error:<15.6e}")
        
        if error < tol:
            print("="*50)
            print(f"\n¡Éxito! Se encontró el punto fijo en {k+1} iteraciones.")
            print(f"El punto fijo aproximado es x = {x1:.6f}")
            return
        x0 = x1

    print("="*50)
    print(f"\n[Aviso]: Se alcanzó el número máximo de iteraciones ({n}) sin converger totalmente.")
    print(f"La última aproximación fue x = {x0:.6f}")

puntofijo()

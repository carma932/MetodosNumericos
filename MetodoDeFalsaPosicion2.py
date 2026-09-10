import sympy as sp
from math import *

def falsaposicion():
    print("==================================================")
    print("       MÉTODO DE LA FALSA POSICIÓN MEJORADO       ")
    print("==================================================")
    print("Nota: Usa 'x' para la variable. Ejemplos de f(x):")
    print("  cos(x) - x**3")
    print("  x**2 - 4")
    print("  sin(x) - exp(-x)\n")

    x = sp.symbols('x')
    f_texto = input("1. Introduce la función f(x): ")
    
    try:
        f = sp.lambdify(x, sp.sympify(f_texto), 'math')
    except Exception as e:
        print("\n[Error]: La función ingresada no es válida.")
        return

    try:
        a = float(eval(input("2. Límite inferior (x_a) (ej. 0 o 1): ")))
        b = float(eval(input("3. Límite superior (x_b) (ej. pi o 2): ")))
        n = int(input("4. Número máximo de iteraciones (n) (ej. 50): "))
        tol = float(eval(input("5. Tolerancia (ej. 10**-4 o 0.001): ")))
    except Exception as e:
        print("\n[Error]: Introdujiste un valor numérico inválido.")
        return

    try:
        fa = f(a)
        fb = f(b)
    except Exception as e:
        print(f"\n[Error]: No se pudo evaluar la función en los extremos. {e}")
        return

    if fa * fb > 0:
        print('\n[Error]: La función no cambia de signo en el intervalo dado.')
        print(f" f(a) = {fa}")
        print(f" f(b) = {fb}")
        return 

    print("\n" + "="*70)
    print(f"{'i':<4} | {'a':<11} | {'b':<11} | {'c (Raíz)':<11} | {'Error (abs)':<12}")
    print("="*70)
    
    anterior = None
    
    for i in range(1, n + 1):
        try:
            c = b - f(b) * (b - a) / (f(b) - f(a))
        except ZeroDivisionError:
            print(f"\n[Error]: División por cero detectada en la iteración {i}.")
            return

        if anterior is not None:
            error = abs(c - anterior)
        else:
            error = abs(b - a)  
            
        print(f"{i:<4} | {a:<11.5f} | {b:<11.5f} | {c:<11.5f} | {error:<12.5e}")

        if error < tol or f(c) == 0:
            print("="*70)
            print(f'\n¡Éxito! Proceso terminado en {i} iteraciones.')
            print(f'La raíz aproximada es x = {c:.6f}')
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        anterior = c
    else:
        print("="*70)
        print(f'\n[Aviso]: Se alcanzó el número máximo de iteraciones ({n}).')
        print(f'La mejor aproximación encontrada fue x = {c:.6f}')

falsaposicion()

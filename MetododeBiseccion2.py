from math import *

def biseccion():
    print("==================================================")
    print("   BIENVENIDO AL MÉTODO DE BISECCIÓN MEJORADO     ")
    print("==================================================")
    print("Nota: Usa 'x' para la variable. Ejemplos:")
    print("  cos(x) - x**3")
    print("  x**2 - 4")
    print("  sin(x) - exp(-x)\n")

    func_texto = input("1. Introduce la función f(x): ")
    
    def f(x):
        return eval(func_texto, globals(), {'x': x})

    try:
        a = float(eval(input("2. Límite inferior (a) (ej. 0 o pi/2): ")))
        b = float(eval(input("3. Límite superior (b) (ej. pi o 5): ")))
        tol = float(eval(input("4. Tolerancia (ej. 10**-6 o 0.001): ")))
        max_iter = int(input("5. Número máximo de iteraciones (ej. 50): "))
    except Exception as e:
        print("\n[Error]: Introdujiste un valor matemático inválido.")
        return

    try:
        fa = f(a)
        fb = f(b)
    except Exception as e:
        print(f"\n[Error]: No se pudo evaluar la función en los extremos. {e}")
        return

    if fa * fb > 0:
        print('\n[Error]: La función no cambia de signo en ese intervalo.')
        print(f" f(a) = {fa}")
        print(f" f(b) = {fb}")
        return 

    print("\n" + "="*75)
    print(f"{'k':<4} | {'a':<12} | {'b':<12} | {'m (Raíz)':<12} | {'Error (abs)':<12}")
    print("="*75)

    m1 = a
    m = b
    k = 0
    
    while abs(m1 - m) > tol and k < max_iter:
        m1 = m
        m = (a + b) / 2
        error = abs(m1 - m) if k > 0 else abs(b - a) 
        
        print(f"{k+1:<4} | {a:<12.6f} | {b:<12.6f} | {m:<12.6f} | {error:<12.6e}")
        
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
            
        k = k + 1
        
    print("="*75)

    if k >= max_iter and abs(m1 - m) > tol:
        print(f"\n[Aviso]: Se alcanzó el número máximo de iteraciones ({max_iter}).")
        print(f"La mejor aproximación encontrada fue x = {m}")
    else:
        print(f"\n¡Éxito! Proceso terminado en {k} iteraciones.")
        print(f"La aproximación de la raíz es x = {m:.7f}")

biseccion()


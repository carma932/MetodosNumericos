import sympy as sp
from math import *

def evaluar_entrada(texto_input):

    return float(eval(texto_input, globals()))


def ejecutar_biseccion():
    print("\n--- [MÉTODO DE BISECCIÓN] ---")
    x = sp.symbols('x')
    func_texto = input("-> Introduce la función f(x): ")
    
    try:
        f = sp.lambdify(x, sp.sympify(func_texto), 'math')
        a = evaluar_entrada(input("-> Límite inferior (a): "))
        b = evaluar_entrada(input("-> Límite superior (b): "))
        tol = evaluar_entrada(input("-> Tolerancia (ej. 10**-6): "))
        max_iter = int(input("-> Número máximo de iteraciones: "))
    except Exception as e:
        print("\n[Error]: Datos ingresados inválidos.")
        return

    if f(a) * f(b) > 0:
        print('\n[Error]: La función no cambia de signo en ese intervalo.')
        return 

    print("\n" + "="*75)
    print(f"{'k':<4} | {'a':<12} | {'b':<12} | {'m (Raíz)':<12} | {'Error (abs)':<12}")
    print("="*75)

    m1, m, k = a, b, 0
    while abs(m1 - m) > tol and k < max_iter:
        m1 = m
        m = (a + b) / 2
        error = abs(m1 - m) if k > 0 else abs(b - a)
        
        print(f"{k+1:<4} | {a:<12.6f} | {b:<12.6f} | {m:<12.6f} | {error:<12.6e}")
        
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        k += 1
        
    print("="*75)
    print(f"\n¡Proceso terminado! Raíz aproximada: x = {m:.6f} (en {k} iteraciones)")

def ejecutar_punto_fijo():
    print("\n--- [MÉTODO DE PUNTO FIJO] ---")
    x = sp.symbols('x')
    func_texto = input("-> Introduce la función g(x): ")
    
    try:
        g = sp.lambdify(x, sp.sympify(func_texto), 'math')
        x0 = evaluar_entrada(input("-> Aproximación inicial (x0): "))
        n = int(input("-> Número máximo de iteraciones (n): "))
        tol = evaluar_entrada(input("-> Tolerancia (ej. 10**-4): "))
    except Exception as e:
        print("\n[Error]: Datos ingresados inválidos.")
        return

    print("\n" + "="*50)
    print(f"{'k':<4} | {'x_k (Aproximación)':<18} | {'Error (abs)':<15}")
    print("="*50)

    for k in range(n):
        try:
            x1 = g(x0)
        except Exception as e:
            print(f"\n[Error]: No se pudo evaluar la función en x = {x0}.")
            return
            
        error = abs(x1 - x0)
        print(f"{k+1:<4} | {x1:<18.6f} | {error:<15.6e}")
        
        if error < tol:
            print("="*50)
            print(f"\n¡Éxito! Punto fijo encontrado: x = {x1:.6f} (en {k+1} iteraciones)")
            return
        x0 = x1

    print("="*50)
    print(f"\n[Aviso]: Se alcanzó el máximo de iteraciones. Último valor: x = {x0:.6f}")

def ejecutar_falsa_posicion():
    print("\n--- [MÉTODO DE LA FALSA POSICIÓN] ---")
    x = sp.symbols('x')
    func_texto = input("-> Introduce la función f(x): ")
    
    try:
        f = sp.lambdify(x, sp.sympify(func_texto), 'math')
        a = evaluar_entrada(input("-> Límite inferior (x_a): "))
        b = evaluar_entrada(input("-> Límite superior (x_b): "))
        n = int(input("-> Número máximo de iteraciones: "))
        tol = evaluar_entrada(input("-> Tolerancia (ej. 10**-4): "))
    except Exception as e:
        print("\n[Error]: Datos ingresados inválidos.")
        return

    if f(a) * f(b) > 0:
        print('\n[Error]: La función no cambia de signo en el intervalo dado.')
        return 

    print("\n" + "="*70)
    print(f"{'i':<4} | {'a':<11} | {'b':<11} | {'c (Raíz)':<11} | {'Error (abs)':<12}")
    print("="*70)
    
    anterior = None
    for i in range(1, n + 1):
        try:
            c = b - f(b) * (b - a) / (f(b) - f(a))
        except ZeroDivisionError:
            print(f"\n[Error]: División por cero en iteración {i}.")
            return

        error = abs(c - anterior) if anterior is not None else abs(b - a)
        print(f"{i:<4} | {a:<11.5f} | {b:<11.5f} | {c:<11.5f} | {error:<12.5e}")

        if error < tol or f(c) == 0:
            print("="*70)
            print(f'\n¡Éxito! Raíz aproximada: x = {c:.6f} (en {i} iteraciones)')
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        anterior = c
    else:
        print("="*70)
        print(f'\n[Aviso]: Se alcanzó el máximo de iteraciones. Último valor: x = {c:.6f}')

def menu_calculadora():
    while True:
        print("\n==================================================")
        print("     CALCULADORA DE MÉTODOS NUMÉRICOS             ")
        print("==================================================")
        print("1. Método de Bisección")
        print("2. Método de Punto Fijo")
        print("3. Método de Falsa Posición")
        print("4. Salir del programa")
        print("==================================================")
        
        opcion = input("Selecciona una opción (1-4): ")
        
        if opcion == '1':
            ejecutar_biseccion()
        elif opcion == '2':
            ejecutar_punto_fijo()
        elif opcion == '3':
            ejecutar_falsa_posicion()
        elif opcion == '4':
            print("\n¡Gracias por usar la calculadora! Saliendo...")
            break
        else:
            print("\n[Opción Incorrecta]: Por favor, elige un número del 1 al 4.")

menu_calculadora()

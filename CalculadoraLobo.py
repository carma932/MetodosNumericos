import sympy as sp
x = sp.symbols('x')

def leer_funcion(mensaje):
    while True:
        texto = input(mensaje)
        try:
            expr = sp.sympify(texto)
            return sp.lambdify(x, expr, 'math')
        except Exception:
            print("[Error]: La función ingresada no es válida. Intenta de nuevo.")

def leer_numero(mensaje):
    while True:
        try:
            entorno = {
                'pi': float(sp.pi), 'e': float(sp.E),
                'sin': __import__('math').sin, 'cos': __import__('math').cos,
                'tan': __import__('math').tan, 'exp': __import__('math').exp,
                'sqrt': __import__('math').sqrt, 'log': __import__('math').log,
            }
            return float(eval(input(mensaje), {"__builtins__": {}}, entorno))
        except Exception:
            print("[Error]: Valor numérico inválido. Intenta de nuevo.")

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except Exception:
            print("[Error]: Debes introducir un número entero. Intenta de nuevo.")

def biseccion():
    print("==================================================")
    print("   MÉTODO DE BISECCIÓN")
    print("==================================================")
    f = leer_funcion("1. Introduce la función f(x): ")
    a = leer_numero("2. Límite inferior (a): ")
    b = leer_numero("3. Límite superior (b): ")
    tol = leer_numero("4. Tolerancia: ")
    max_iter = leer_entero("5. Número máximo de iteraciones: ")
    try:
        fa = f(a)
        fb = f(b)
    except Exception as e:
        print(f"[Error]: No se pudo evaluar la función en los extremos. {e}")
        return
    if fa * fb > 0:
        print('[Error]: La función no cambia de signo en ese intervalo.')
        print(f" f(a) = {fa}")
        print(f" f(b) = {fb}")
        return
    print("=" * 75)
    print(f"{'k':<4} | {'a':<12} | {'b':<12} | {'m (Raíz)':<12} | {'Error (abs)':<12}")
    print("=" * 75)
    m1 = a
    m = b
    k = 0
    while abs(m1 - m) > tol and k < max_iter:
        m1 = m
        m = (a + b) / 2
        error = abs(m1 - m) if k > 0 else abs(b - a)
        print(f"{k + 1:<4} | {a:<12.6f} | {b:<12.6f} | {m:<12.6f} | {error:<12.6e}")
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
        k += 1
    print("=" * 75)
    if k >= max_iter and abs(m1 - m) > tol:
        print(f"[Aviso]: Se alcanzó el número máximo de iteraciones ({max_iter}).")
        print(f"La mejor aproximación encontrada fue x = {m}")
    else:
        print(f"¡Éxito! Proceso terminado en {k} iteraciones.")
        print(f"La aproximación de la raíz es x = {m:.7f}")

def falsaposicion():
    print("==================================================")
    print("   MÉTODO DE LA FALSA POSICIÓN")
    print("==================================================")
    f = leer_funcion("1. Introduce la función f(x): ")
    a = leer_numero("2. Límite inferior (x_a): ")
    b = leer_numero("3. Límite superior (x_b): ")
    n = leer_entero("4. Número máximo de iteraciones: ")
    tol = leer_numero("5. Tolerancia: ")
    try:
        fa = f(a)
        fb = f(b)
    except Exception as e:
        print(f"[Error]: No se pudo evaluar la función en los extremos. {e}")
        return
    if fa * fb > 0:
        print('[Error]: La función no cambia de signo en el intervalo dado.')
        print(f" f(a) = {fa}")
        print(f" f(b) = {fb}")
        return
    print("=" * 70)
    print(f"{'i':<4} | {'a':<11} | {'b':<11} | {'c (Raíz)':<11} | {'Error (abs)':<12}")
    print("=" * 70)
    anterior = None
    c = None
    for i in range(1, n + 1):
        try:
            c = b - f(b) * (b - a) / (f(b) - f(a))
        except ZeroDivisionError:
            print(f"[Error]: División por cero detectada en la iteración {i}.")
            return
        error = abs(c - anterior) if anterior is not None else abs(b - a)
        print(f"{i:<4} | {a:<11.5f} | {b:<11.5f} | {c:<11.5f} | {error:<12.5e}")
        if error < tol or f(c) == 0:
            print("=" * 70)
            print(f'¡Éxito! Proceso terminado en {i} iteraciones.')
            print(f'La raíz aproximada es x = {c:.6f}')
            return
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        anterior = c
    print("=" * 70)
    print(f'[Aviso]: Se alcanzó el número máximo de iteraciones ({n}).')
    print(f'La mejor aproximación encontrada fue x = {c:.6f}')

def puntofijo():
    print("==================================================")
    print("   MÉTODO DE PUNTO FIJO")
    print("==================================================")
    g = leer_funcion("1. Introduce la función g(x): ")
    x0 = leer_numero("2. Aproximación inicial (x0): ")
    n = leer_entero("3. Número máximo de iteraciones: ")
    tol = leer_numero("4. Tolerancia: ")
    print("=" * 50)
    print(f"{'k':<4} | {'x_k (Aproximación)':<18} | {'Error (abs)':<15}")
    print("=" * 50)
    for k in range(n):
        try:
            x1 = g(x0)
        except Exception as e:
            print(f"[Error]: No se pudo evaluar la función en x = {x0}. {e}")
            return
        error = abs(x1 - x0)
        print(f"{k + 1:<4} | {x1:<18.6f} | {error:<15.6e}")
        if error < tol:
            print("=" * 50)
            print(f"¡Éxito! Se encontró el punto fijo en {k + 1} iteraciones.")
            print(f"El punto fijo aproximado es x = {x1:.6f}")
            return
        x0 = x1
    print("=" * 50)
    print(f"[Aviso]: Se alcanzó el número máximo de iteraciones ({n}) sin converger totalmente.")
    print(f"La última aproximación fue x = {x0:.6f}")

def menu():
    while True:
        print("##################################################")
        print("#          CALCULADORA DE MÉTODOS NUMÉRICOS       #")
        print("##################################################")
        print(" 1) Bisección")
        print(" 2) Falsa Posición")
        print(" 3) Punto Fijo")
        print(" 4) Salir")
        opcion = input("Elige una opción (1-4): ").strip()
        if opcion == "1":
            biseccion()
        elif opcion == "2":
            falsaposicion()
        elif opcion == "3":
            puntofijo()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("[Error]: Opción no válida. Elige un número del 1 al 4.")

if __name__ == "__main__":
    menu()
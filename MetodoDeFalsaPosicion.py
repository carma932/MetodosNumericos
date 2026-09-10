import sympy as sp

x = sp.symbols('x')
f = sp.lambdify(x, sp.sympify(input('Ingrese f(x): ')), 'math')
a = float(input('Ingrese x_a: '))
b = float(input('Ingrese x_b: '))
n = int(input('Ingrese el numero de iteraciones: '))
tol = float(input('Ingrese la tolerancia: '))

if f(a) * f(b) > 0:
    print('No hay cambio de signo en el intervalo.')
else:
    anterior = None
    for i in range(1, n + 1):
        c = b - f(b) * (b - a) / (f(b) - f(a))
        error = abs(c - anterior) if anterior is not None else float('inf')
        print('x', i, '=', c, 'error =', error)

        if error < tol or f(c) == 0:
            print('La raiz aproximada es:', c)
            break

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        anterior = c
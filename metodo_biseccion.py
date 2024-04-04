import sympy as sp
from colorama import init, Fore

# Inicializar Colorama para habilitar los colores en la terminal
init(autoreset=True)

def biseccion(func, a, b, max_iter, relative_error):
    iter_count = 0
    while iter_count < max_iter:
        c = (a + b) / 2
        if abs(func(c)) < relative_error:
            return c, iter_count
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    return None, iter_count

def newton_method(func, func_deriv, initial_guess, max_iter, relative_error):
    x = initial_guess
    iter_count = 0
    while iter_count < max_iter:
        x_next = x - func(x) / func_deriv(x)
        if abs(x_next - x) / abs(x_next) < relative_error:
            return x_next, iter_count
        x = x_next
        iter_count += 1
    return None, iter_count


def secant_method(func, x0, x1, max_iter, relative_error):
    iter_count = 0
    while iter_count < max_iter:
        x_next = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(x_next - x1) / abs(x_next) < relative_error:
            return x_next, iter_count
        x0, x1 = x1, x_next
        iter_count += 1
    return None, iter_count

# Define la función para obtener la derivada de la función ingresada por el usuario
def obtener_derivada(func):
    x = sp.Symbol('x')
    expr = sp.sympify(func)  # Convertir la cadena de texto en una expresión simbólica
    derivada = sp.diff(expr, x)  # Calcular la derivada
    return sp.lambdify(x, derivada, 'numpy')  # Convertir la derivada a una función lambda

# Función para solicitar límites del intervalo
def obtener_intervalo():
    a = float(input("Ingrese el límite izquierdo del intervalo: "))
    b = float(input("Ingrese el límite derecho del intervalo: "))
    return a, b

# Función para solicitar la cantidad de iteraciones
def obtener_iteraciones_maximas():
    max_iter = int(input("Ingrese la cantidad máxima de iteraciones: "))
    return max_iter

# Función para solicitar si el usuario desea continuar
def continuar_buscando():
    response = input("¿Desea ingresar otro intervalo? (s/n): ").strip().lower()
    return response == 's'

# Mensaje de bienvenida
def mostrar_bienvenida():
    print(Fore.BLUE + "Bienvenido al programa de búsqueda de raíces")

# Mensaje de despedida
def mostrar_despedida():
    print(Fore.BLUE + "\n¡Gracias por usar nuestro programa! 🚀")

# Ejemplo de uso
mostrar_bienvenida()

while True:
    print(Fore.YELLOW + "\nSeleccione el método que desea utilizar:\n"
                        "1. Método de la bisección\n"
                        "2. Método de Newton\n"
                        "3. Método de la secante\n"
                        "4. Salir\n")

    opcion = input("Seleccione una opción (1/2/3/4): ").strip()

    if opcion == '1':
        metodo = biseccion
    elif opcion == '2':
        metodo = newton_method
    elif opcion == '3':
        metodo = secant_method
    elif opcion == '4':
        mostrar_despedida()
        break
    else:
        print(Fore.RED + "\nOpción inválida. Por favor, seleccione una opción válida.")
        continue

    print(Fore.YELLOW + "\nIngrese la función a evaluar en formato Python (por ejemplo, 'x**2 - 1').")
    user_function = input("Función: ")

    func_deriv = None
    if opcion == '2':
        print(Fore.YELLOW + "\nPara las funciones trigonométricas como seno, coseno y tangente, asegúrese de ingresarlas en formato 'sin(x)', 'cos(x)' y 'tan(x)' respectivamente.")
        func_deriv = obtener_derivada(user_function)

    func = sp.lambdify(sp.Symbol('x'), user_function, 'numpy')

    a, b = obtener_intervalo()
    initial_guess = (a + b) / 2
    max_iter = obtener_iteraciones_maximas()
    relative_error = 1e-9  # Error relativo recomendado

    if metodo == secant_method:
        x0, x1 = a, b
        root, iterations = metodo(func, x0, x1, max_iter, relative_error)
    elif metodo == biseccion:
        root, iterations = metodo(func, a, b, max_iter, relative_error)
    elif metodo == newton_method:
        root, iterations = metodo(func, func_deriv, initial_guess, max_iter, relative_error)


    if root is not None:
        print(Fore.GREEN + "\n¡Raíz encontrada! 🎉")
        print(f"{Fore.RESET}Valor de la raíz: {Fore.CYAN}{root:.8f}")
        print(f"Iteraciones realizadas: {Fore.CYAN}{iterations}")
    else:
        print(Fore.RED + "\nEl método no convergió dentro del número máximo de iteraciones. 😞")

    if not continuar_buscando():
        mostrar_despedida()
        break

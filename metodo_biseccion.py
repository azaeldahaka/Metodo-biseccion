import math
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
    print(Fore.BLUE + "Bienvenido al programa de búsqueda de raíces por el método de la bisección")

# Mensaje de despedida
def mostrar_despedida():
    print(Fore.BLUE + "\n¡Gracias por usar nuestro programa! 🚀")

# Ejemplo de uso
mostrar_bienvenida()

while True:
    print(Fore.YELLOW + "\nIngrese la función a evaluar en formato Python (por ejemplo, 'x**3 - 3*x + 1'). Asegúrate de usar 'math' para funciones matemáticas (p.ej., 'math.sin(x)').")
    user_function = input()
    func = eval("lambda x: " + user_function)  # Convertir la cadena a una función lambda

    a, b = obtener_intervalo()
    max_iter = obtener_iteraciones_maximas()
    # Recomendación de un error relativo más pequeño para lograr al menos 8 decimales de precisión.
    print("Se recomienda un error relativo de 1e-9 para lograr una precisión de 8 decimales.")
    relative_error = float(input("Ingrese el error relativo deseado: "))
    
    root, iterations = biseccion(func, a, b, max_iter, relative_error)
    if root is not None:
        print(Fore.GREEN + "\n¡Raíz encontrada! 🎉")
        # Ajuste en la impresión para mostrar 8 decimales de precisión.
        print(f"{Fore.RESET}Valor de la raíz: {Fore.CYAN}{root:.8f}")
        print(f"Iteraciones realizadas: {Fore.CYAN}{iterations}")
    else:
        print(Fore.RED + "\nEl método de la bisección no convergió dentro del número máximo de iteraciones. 😞")
    
    if not continuar_buscando():
        mostrar_despedida()
        break

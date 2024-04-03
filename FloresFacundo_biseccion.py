import math

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

# Función para solicitar el error relativo porcentual
def obtener_error_relativo():
    relative_error = float(input("Ingrese el error relativo porcentual: "))
    return relative_error

# Función para solicitar si el usuario desea continuar
def continuar_buscando():
    response = input("¿Desea ingresar otro intervalo? (s/n): ").strip().lower()
    return response == 's'

# Ejemplo de uso
print("\nBienvenido al programa de búsqueda de raíces por el método de la bisección")

while True:
    print("\nIngrese la función a evaluar en formato Python utilizando la biblioteca math (por ejemplo, 'math.sin(x)'; x**2-2+6*x): ")
    print("\tEjemplos de funciones: math.sin(x), math.cos(x), math.exp(x), math.log(x), etc.")
    user_function = input()
    
    try:
        func = eval("lambda x: " + user_function)  # Convertir la cadena a una función lambda
    except Exception as e:
        print("Error:", e)
        print("Por favor, asegúrese de que la función ingresada sea válida.")
        continue
    
    a, b = obtener_intervalo()
    max_iter = obtener_iteraciones_maximas()
    relative_error = obtener_error_relativo()
    
    while True:
        root, iterations = biseccion(func, a, b, max_iter, relative_error)
        if root is not None:
            print("\n¡Raíz encontrada!")
            print(f"Valor de la raíz: {root:.6f}")
            print(f"Iteraciones realizadas: {iterations}")
            break
        else:
            print("\nEl método de la bisección no convergió dentro del número máximo de iteraciones.")
            opcion = input("¿Qué desea hacer?\n\t1. Aumentar la cantidad de iteraciones.\n\t2. Cambiar el error relativo porcentual.\n\t0. Salir.\nSeleccione una opción (1/2): ").strip()
            if opcion == '1':
                new_max_iter = obtener_iteraciones_maximas()
                max_iter = new_max_iter
            elif opcion == '2':
                new_relative_error = obtener_error_relativo()
                relative_error = new_relative_error
            elif opcion == '0':
                break
            else:
                print("\nOpción inválida.")
                continue
    
    if not continuar_buscando():
        print("\n¡Gracias por usar nuestro programa!")
        break

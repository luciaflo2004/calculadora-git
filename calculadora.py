
# calculadora.py

# Muestra el título de la calculadora
def presentacion():
    print("====================================")
    print("  CALCULADORA MODULAR EN PYTHON     ")
    print("====================================")


# Suma dos números
def sumar(a, b):
    return a + b


# Resta dos números
def restar(a, b):
    return a - b


if __name__ == "__main__":
    presentacion()

# Multiplica dos números
def multiplicar(a, b):
    return a * b


# Divide dos números y evita la división entre cero
def dividir(a, b):
    if b == 0:
        return "Error: no es posible dividir entre cero"
    return a / b

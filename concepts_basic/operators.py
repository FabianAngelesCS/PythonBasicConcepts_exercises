"""
1. Calculadora básica
Descripción:
Pide dos números al usuario e imprime el resultado de las operaciones básicas: suma, resta, multiplicación, división y módulo.

Objetivo: Practicar operadores aritméticos (+, -, *, /, %).
"""
def getOperation():
    print("Hello wordl!")
    print("Te voy a ayudar a realizar la operacion que requieras con mi calculadora...")
    print("Primero ingresa que operaciòn deseas realizar empleando los siguientes simbolos: +, -, *, /, %")
    operation = input("Añade un simbolo de operaciòn: ")
    return operation

def tipe_operation(operation):

    if operation == "+":
        return "Suma"
    elif operation == "-":
        return  "Resta"
    elif operation == "*":
        return "Multiplicacion"
    elif operation == "/":
        return "Division"
    elif operation == "%":
        return "Porcentaje"
    else:
        print("No es una simbolo valido, intente de nuevo")
        return None

def do_operation(type_operation, num1, num2):

    try:
        primer_numero = float(num1)
        segundo_numero = float(num2)

        if type_operation == "Suma":

            return primer_numero + segundo_numero

        elif type_operation == "Resta":

            return primer_numero - segundo_numero

        elif type_operation == "Multiplicacion":

            return primer_numero * segundo_numero

        elif type_operation == "Division":
            if segundo_numero == 0:
                return "Error: División entre 0"
            return primer_numero / segundo_numero

        elif type_operation == "Porcentaje":
            if segundo_numero == 0:
                return "Error: Calcular porcentaje con 0"
            return  primer_numero * (segundo_numero/100)

        else:
            return "Operación no reconocida"
    except ValueError:
        return "Error: Ingresa número validos"

operation_to_process = None

while operation_to_process is None:
    op = getOperation()
    operation_to_process = tipe_operation(op)

print(f" Haz seleccionado la operacion:  {operation_to_process}")

primer_numero =input("Ingresa el primer nùmero: ")

segundo_numero = input("Ingresa segundo número: ")

result=do_operation(operation_to_process, primer_numero, segundo_numero)

print(f"El resultado de la operacion es: {result}")

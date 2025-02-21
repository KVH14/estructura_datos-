def multiplicar(a, b) -> int:
    resultado = 0
    cont = 0
    while cont < b:
        resultado= resultado + a
        cont=cont+ 1
    return resultado

print("Ingresa el primer número: ")
a = int(input())
print("Ingresa el segundo número: ")
b = int(input())

print("El resultado es:", multiplicar(a, b))
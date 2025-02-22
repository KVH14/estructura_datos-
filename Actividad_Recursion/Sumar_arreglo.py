arreglo=[]
print("ingresa el numero de datos que quieres ingresar")
num_veces=(int(input()))

for i in range(num_veces):
    arreglo.append(int(input("digite el numero ")))

def suma (arreglo):
    if len(arreglo) == 1:
        return arreglo[0]
    return arreglo[0] + suma(arreglo[1:])

print("la suma es ",suma(arreglo))
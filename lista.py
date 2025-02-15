numeros=list()
continuar:bool=True
def agregar (numero:int)->None:
        numeros.append(numero) 

def eliminar ()->None:
        numeros.pop() 


while continuar:
        print("1.Agregar")
        print("2.Eliminar")
        print("3.Salir")

        opcion=int(input())
        
        if opcion == 1:
                continuar=True
                x=int(input('numero'))
                agregar(x)
                print(numeros)
        elif opcion == 2:
                continuar=True
                eliminar()
                print(numeros)
        else:
                continuar=False
                
                        


                
            




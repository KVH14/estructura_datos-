persona=dict()
continuar:bool=True
def agregar_valor(clave:str,valor:str):
    persona.update({clave:valor})
def eliminar_valor():
    persona.popitem ()
    
while continuar:
        print("1.Agregar")
        print("2.Eliminar")
        print("3.Salir")

        opcion=int(input())
        
        if opcion == 1:
                continuar=True
                print("digite nombre")
                x=str(input())
                print("digite apellido")
                i=str(input())
                agregar_valor(x,i)
                print(persona)
        elif opcion == 2:
                continuar=True
                eliminar_valor()
                print(persona)
        else:
                continuar=False
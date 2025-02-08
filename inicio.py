#edad=0
#nombre="Maria"

#print("Cuantos años tiene")
#edad=int(input())
#print("Tiene cover de cuanto")
# cover=int(input())

# if cover < 50000:
#   print("no puede ingresar")

# elif edad < 18:
#    print("no puede ingresar")

# else:
#    print("puede ingresar")
temp=[]
temperatura=0
for i in range (0,5):
   print("Digite temperatura")
   temp.append(int(input()))
   temperatura=sum(temp)

print(temp)
promedio = temperatura / len(temp)
print(promedio)

if promedio <= 20 :
   print("el promedio de las temperaturas es",promedio,"la temperatura es baja")
elif promedio >= 37:
   print("el promedio de las temperaturas es",promedio,"La temperatura es alta")
else: 
   print("el promedio de las temperaturas es",promedio,"La temperatura es normal")








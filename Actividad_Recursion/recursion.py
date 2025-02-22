# numero=5
# resultado:int

# def factorial (n:int) -> int:
#     res:int =1
#     for i in range(1,n+1):
#       res*=i
#     return res
    

# print(factorial(numero))

# numero=5
# resultado:int

# def factorial (n:int) -> int:
#     res:int=1
#     cont=1
#     while cont <= n:
#       res=res*cont
#       cont=cont+1
#     return res

# print(factorial(numero))

# numero=5

# def factorial (n:int) -> int:
#     if n == 1:
#       return n
#     return factorial(n-1)*n

# print(factorial(numero))

def sumatoria (n:int)->int:
   if n <= 1:
      return n
   return sumatoria(n-1) + sumatoria(n-2)

for i in range(10):
    print(sumatoria(i), end=" ")




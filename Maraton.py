"""
Nombres y Apellidos: Octavio Juarez, Solange Altamirano, Lautaro Cejas
Fecha: 11/05/21
"""
#Codigo: Factorial, Suma de Multiplos, Diferencia de Pares y Impares

from math import factorial

I=True
mult=0
pares=0
impares=0

while I==True:
    N=int(input("Ingrese un numero: "))
    if 3<=N<=30:
        I=False
    else:
        print("Ingrese el valor correcto")

for i in range(0,N+1):
    if i%3==0 and i%5!=0:
        mult+=i
for i in range(0,N+1):
    if i%2==0:
        pares+=i
    else:
        impares+=i

resta=pares-impares
        
print("VALOR N!: ",factorial(N))
print("VALOR MULTIPLOS: ",mult)
print("VALOR RESTA: ",resta)


    


    


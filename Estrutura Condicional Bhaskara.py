import math

a=float(input("insira o valor de a: "))
b=float(input("insira o valor de b: "))
c=float(input("insira o valor de c: "))

delta=(b**2-4*a*c)


if delta<0 or a==0:
    print("Impossivel calcular a raiz")
else: 
    r1=(-b+math.sqrt(delta))/(2*a)
    r2=(-b-math.sqrt(delta))/(2*a)
    print("a primeira raiz é: ", r1)
    print("a segunda raiz é: ", r2)
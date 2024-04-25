# Faça um programa em Python que leia um número inteiro N 
# menor que 1.000 e apresente todos os números ímpares de 1 a N, inclusive N 

n=1000
while (n>=1000):
    n=int(input("Insira um valor menor que mil: "))
for i in range (1,n+1): 
    if i%2 !=0:
        print(i)
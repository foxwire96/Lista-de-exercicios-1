#Faça um programa em Python que leia um número inteiro N menor que 1.000 e 
#apresente todos os números ímpares de 1 a N, inclusive N 

N=1001
while N>=1000:
    N = int(input("Entre um valor inteiro menor que 1.000: "))

for i in range (1, N+1):
    if(i%2 != 0):
        print(i)
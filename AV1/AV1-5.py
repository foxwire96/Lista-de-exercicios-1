#Faça um programa em Python que leia um número inteiro “N”, calcule e apresente todos os seus divisores. 
#(Dica: use uma estrutura while para testar todos os possíveis divisores)


n=int(input("Insira um numero: "))
i=1
while (i<=n):
    if n%i==0:
        print(i)
    i=i+1   

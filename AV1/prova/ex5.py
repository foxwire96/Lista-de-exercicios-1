#Faça um programa em Python que leia um número inteiro “N”, calcule e apresente 
#todos os seus divisores. (Dica: use uma estrutura while para testar todos os possíveis divisores)

N = int(input("Digite um número inteiro: "))
i = 1
while i <= N:
    if N%i == 0:
        print(i)
    
    i=i+1
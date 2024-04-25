#Faça um programa que calcule o fatorial de um número positivo informado pelo usuário.

a=int(input("Insira um numero: "))

if a>=1:
    fatorial=a
    while a>1:
        a=a-1
        fatorial=fatorial*a
    print(fatorial)
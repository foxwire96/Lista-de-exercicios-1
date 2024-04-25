#Faça um programa em Python que leia um número inteiro “N” maior que zero, e escreva a sequência de Fibonacci com “n” termos

n=0
numeroAnterior=0
numeroAtual=1
while (n<=0):
    n=int(input("Insira um numero maior que zero: "))

soma=numeroAnterior+numeroAtual
print(soma)

fibonacci=str(soma)

if n>1:
    for i in range (1, n):
        soma=numeroAnterior+numeroAtual
        fibonacci=fibonacci+", "+str(soma)
        numeroAnterior=numeroAtual
        numeroAtual=soma
print(f"n={n}; R: {fibonacci}")
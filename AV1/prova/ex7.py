# Faça um programa em Python que leia um número inteiro “N” maior que zero, e escreva a sequência de Fibonacci com “n” termos:
# Ex: n=1 R: 1
	# n=3; R: 1,1,2
	# n=5; R: 1,1,2,3,5

N = 0
numeroAnterior = 0
numeroAtual = 1
while N<=0:
    N = int(input("Digite um número inteiro maior que 0: "))

soma = numeroAnterior + numeroAtual
print (soma)
fibonacci = str(soma)

if(N>1):
    for i in range (1, N):
        soma = numeroAnterior + numeroAtual
        fibonacci = fibonacci + ", "  + str(soma)
        numeroAnterior = numeroAtual
        numeroAtual = soma

print (f"n = {N}; R: {fibonacci}")


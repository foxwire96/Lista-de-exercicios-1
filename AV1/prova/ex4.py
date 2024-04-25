# Faça um programa em Python que leia um conjunto indeterminado de dados, contendo cada um a 
# idade de um indivíduo, e calcule e imprima a média aritmética (com 1 casa decimal) de idades 
# do grupo. O último dado, que não entrará no cálculo da média deve ser um valor negativo.

N = 0
soma = 0
contator = 0

while (N >=0):
    N = int (input ("Digite uma idade: "))
    if N >=0:
        soma = soma + N
        contator = contator + 1

media = soma / contator

print (f'A média aritmética das idades é: {media:.1f}')



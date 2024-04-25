#Faça um programa em Python que leia um conjunto indeterminado de dados, 
# contendo cada um a idade de um indivíduo, e calcule e imprima a média aritmética (com 1 casa decimal) de idades do grupo. 
#O último dado, que não entrará no cálculo da média deve ser um valor negativo.

a=0
b=0
i=0
while (b>=0):
    b=int(input("Insira um numero: "))
    if b>0:
        a=a+b
        i+=1
if i>0:
    media=a/i
    print (f'{media:.1f}')
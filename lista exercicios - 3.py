#Escreva um programa que imprima todos os números pares compreendidos entre 85 e 907. O programa deve também calcular a soma destes valores

soma=0

for i in range (85, 907):
    if i%2==0:
        print(i)
        soma=soma+i
print(soma)
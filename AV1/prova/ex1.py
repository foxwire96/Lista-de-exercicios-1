#Faça um programa que calcule e apresente o valor da hipotenusa “c” de um triângulo retângulo, dado o valor de seus catetos “a” e “b”, segundo a fórmula:
#c=√(a^2+b^2 )

a = int(input("Entre o valor do primeiro cateto: "))
b = int(input("Entre o valor do segundo cateto: "))

c = ((a**2) + (b**2)) ** (1/2)

print("O valor da hipotenusa é: ", c)


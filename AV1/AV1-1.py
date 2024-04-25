# Faça um programa que calcule e apresente o valor da hipotenusa “c” de um
# triângulo retângulo, dado o valor de seus catetos “a” e “b”, segundo a fórmula:

a = int(input("Valor de A "))
b = int(input("Valor de B "))

c=((a**2)+(b**2))**(1/2)
print(c)
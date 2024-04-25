#Faça um programa que leia os 3 lados quaisquer de um triangulo e determine se ele é um triangulo retângulo. 
#Para isto utilize a fórmula do item anterior nesta checagem. (Garanta que os lados sejam números positivos.)

a=0
texto = "Digite um valor inteiro positivo"
while a<=0:
    a = int(input("Entre o valor do primeiro lado: "))
    if a<=0:
        print (texto)
    
b=0
while b<=0:
    b = int(input("Entre o valor do segundo lado: "))
    if b<=0:
        print (texto)

c=0
while c<=0:
    c = int(input("Entre o valor do terceiro lado: "))
    if c<=0:
        print (texto)

if ((a == ((b**2) + (c**2)) ** (1/2)) or (b == ((a**2) + (c**2)) ** (1/2)) or (c == ((a**2) + (b**2)) ** (1/2))):
    print ("É um triângulo retângulo")
else:
    print ("Não é um triângulo retângulo")

        
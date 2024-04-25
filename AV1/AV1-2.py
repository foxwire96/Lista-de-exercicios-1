# Faça um programa que leia os 3 lados quaisquer de um triangulo e 
# determine se ele é um triangulo retângulo. Para isto utilize a fórmula do item anterior nesta checagem. 
# (Garanta que os lados sejam números positivos.)

a=0
while a<=0:
    a=int(input("Insira o primeiro numero positivo "))

b=0
while b<=0:
    b=int(input("Insira o segundo numero positivo "))
    

c=0
while c<=0:
    c=int(input("Insira o terceiro numero positivo "))
    

if (c==((a**2)+(b**2))**(1/2)) or (a==((b**2)+(c**2))**(1/2)) or (b==((a**2)+(c**2))**(1/2)):
    print("é um triangulo retangulo ") 
else:
    print("Não é um triangulo retangulo ")
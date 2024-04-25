#Escreva um programa que imprima os 100 primeiros números ímpares.

contador=0
num=0

while contador<100:
    if num%2!=0:
        print(num)
        contador=contador+1
    num=num+1
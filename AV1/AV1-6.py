#Um posto de combustível deseja gerenciar a preferência de produto por seus clientes. 
#Para isto é solicitado um programa em Python que apresente o menu segundo a tabela abaixo e leia o código do combustível escolhido:
#Caso o usuário digite um valor inválido, deve ser solicitado um novo valor até que seja válido. 
#O programa é encerrado quando se digita o código 4, quando então o cálculo é feito e a mensagem “Muito Obrigado” 
#juntamente com a resposta é apresentada.

contadorGasolina=0
contadorAlcool=0
contadorDiesel=0

i=0

while i==0:
    print("Combustivel------------Código")
    print("Gasolina---------------1")
    print("Alcool-----------------2")
    print("Diesel-----------------3")
    print("Fim--------------------4")
    codigo=int(input("Digite um dos valores acima: "))
    if codigo>=1 and codigo<=4:
        if codigo==4:
            i=1
            print("Muito obrigado")
            print("Alcool: ", contadorAlcool)
            print("gasolina: ", contadorGasolina)
            print("Diesel: ", contadorDiesel)
        elif codigo==3:
            contadorDiesel=contadorDiesel+1
        elif codigo==2:
            contadorAlcool=contadorAlcool+1
        elif codigo==1:
            contadorGasolina=contadorGasolina+1
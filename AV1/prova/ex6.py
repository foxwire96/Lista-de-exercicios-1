# Um posto de combustível deseja gerenciar a preferência de produto por seus clientes. Para isto 
# é solicitado um programa em Python que apresente o menu segundo a tabela abaixo e leia o código do combustível escolhido:

# Combustível	Código
# Gasolina	      1
# Álcool	      2
# Diesel	      3
# Fim	          4

#Caso o usuário digite um valor inválido, deve ser solicitado um novo valor até que seja válido. 
#O programa é encerrado quando se digita o código 4, quando então o cálculo é feito e a mensagem “Muito Obrigado” juntamente com a resposta é apresentada.

i = 0
contatorGasolina = 0
contatorAlcool = 0
contatorDiesel = 0

while (i==0):

    print ("Combustível ------ Código")
    print ("Gasolina --------- 1")
    print ("Álcool ----------- 2")
    print ("Diesel ----------- 3")
    print ("Fim -------------- 4")

    N = int(input("Digite um dos valores acima: "))

    if(N>=1 and N<=4):

        if (N == 4):

            i=1
             
            print ("Muito obrigado")
            print ("Álcool: ", contatorAlcool)
            print ("Gasolina: ", contatorGasolina)
            print ("Diesel: ", contatorDiesel)
        else:

            if N == 1:
                contatorGasolina = contatorGasolina + 1
            elif  N == 2:
                contatorAlcool = contatorAlcool + 1
            else:
                contatorDiesel = contatorDiesel + 1





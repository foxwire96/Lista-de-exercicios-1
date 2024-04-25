x=float(input("Insira uma coordenada x: "))
y=float(input("Insira uma coordenada y: "))

if x>0 and y>0:
    print("O ponto está no primeiro quadrante")

if x<0 and y>0:
    print("O ponto está no segundo quadrante")

if x<0 and y<0:
    print("O ponto está no terceiro quadrante")

if x>0 and y<0:
    print("O ponto está no quarto quadrante")

else: 
    print("O ponto está na origem (0, 0)")

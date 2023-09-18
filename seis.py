"""
    Programa 6
    Aluno - Vinícius Santos Nímia
    Matrícula - 12211FIS237
"""

print("Teste 6 - Area e perimetro do retangulo - Desenvolvido por Vinícius Santos Nímia")
#Solicitando as medidas de string

comprimento = input("Insere o comprimento do retangulo: ")
largura  = input("Insere a largura do retangulo: ")

#Convertendo as medidas em float
comprimento1 = float(comprimento)
largura1 = float(largura)

#Calculando a area e o perimetro
area = comprimento1 * largura1
perimetro = 2 * (largura1 + comprimento1)

print(f"A area do retangulo é de {area}")
print(f"O perimetro do retangulo é de {perimetro}")
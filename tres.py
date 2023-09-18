"""
    Programa 3
    Aluno - Vinícius Santos Nímia
    Matrícula - 12211FIS237
"""

#Calcular a média de tantos números

def calcular_media(lista_de_numeros):
    total = sum(lista_de_numeros)
    media = total/len(lista_de_numeros)
    return media

#valores pré-determinados

numeros =[]

while True:
    entrada = input("Digite um número qualquer e P para parar: ")

    #verificando se o usuário deseja parar
    if entrada =="p" or entrada == "P":
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor insere um número válido")
if len(numeros) > 0:
    media = sum(numeros)/len(numeros)
    print(f"A media dos números inseridos é: {media}")
else:
    print("Nenhum número foi inserido")
"""
    Programa 4
    Aluno - Vinícius Santos Nímia
    Matrícula - 12211FIS237
"""

print("Teste 4 - Divisiveis de 1 a 1000 - Desenvolvido por Vinícius Santos Nímia")

#Inicializando uma lista para armenizar
numeros_divisiveis = []

#Usando um loop for
for numero in range(1, 1000):
    #Verificando se os numeros sao divisiveis por 2 e por 3
    if numero % 2 == 0 and numero % 3 == 0:
        numeros_divisiveis.append(numero)

#Imprimindo os numeros
print(f"Números divísiveis por 2 e por 3: {numeros_divisiveis}")

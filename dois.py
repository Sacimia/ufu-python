"""
    Programa 2
    Aluno - Vinícius Santos Nímia
    Matrícula - 12211FIS237
"""
print("Teste 2 - Maior, menor ou igual - Desenvolvido por Vinícius Santos Nímia")
#Deve-se inserir os valores de entrada
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

# Certifique-se de converter os valores de entrada em números inteiros para comparação adequada.
valor1 = int(valor1)
valor2 = int(valor2)

#Os valores de entrada serão identificadas de tal modo que seja maior valor
if valor1 > valor2:
    maiorvalor = valor1
elif valor2 > valor1:
    maiorvalor = valor2
#De tal modo que o valor do int (integer) será transformado em um valor de uma string
else:
    maiorvalor = "Os valores são iguais " + str(valor1) + " = " + str(valor2)

print("O maior valor é:", maiorvalor)



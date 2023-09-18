"""
    Programa 11
    Aluno - Vinícius Santos Nímia
    Matrícula - 12211FIS237
"""

print("Teste 11 - Numeros primos - Desenvolvido por Vinícius Santos Nímia")

def e_primo(numero):
    if numero <=1:
        return False
    for i in range (2, int(numero**0.5) +1):
        if numero % i == 0:
            return False
    return True

inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

print("Números primos no intervalo entre ", inicio, " e", fim, ": ")
for numero in range(inicio, fim + 1):
    if e_primo(numero):
        print(numero)
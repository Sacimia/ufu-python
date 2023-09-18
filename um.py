"""
    Programa 1
    Aluno - Vinícius Santos Nímia
    Matrícula - 12211FIS237
"""
print("Teste - Definindo um horário para ocorrer a cada saudação")
import datetime

#Definindo um horário para ocorrer a cada saudação

def saudacao():
    hora_atual = datetime.datetime.now().hour
    if 6 <= hora_atual <12:
        return "Bom dia"
    elif 12 <= hora_atual<18:
        return "Boa tarde"
    else:
        return "Boa noite"
nome  = input("Qual é o seu nome: ")
if nome.strip() != "":
    mensagem_saudacao = saudacao()
    mensagem_personalizada = f"{mensagem_saudacao}, {nome}"
    print(mensagem_personalizada)
else:
    print("Corrige ou senão você está fornecendo dados errados")

##import sys
##print(f"Você está usando Python {sys.version}")
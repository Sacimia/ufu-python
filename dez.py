"""
    Programa 10
    Aluno - Vinícius Santos Nímia
    Matrícula - 12211FIS237
"""

print("Teste 10 - Convertendo quantidades de segundos em hórario")

#Solicitando uma quantidade de segundos
segundos = int(input("Insere uma quantidade de segundos: "))

#Calculando horas, segundo e minutos
horas = segundos // 3600  # Uma hora tem 3600 segundos
segundos_restantes = segundos % 3600
minutos = segundos_restantes // 60  # Um minuto tem 60 segundos
segundos_final = segundos_restantes % 60

# Formata a saída com dois dígitos para horas, minutos e segundos
horas_formatadas = f"{horas:02d}"
minutos_formatados = f"{minutos:02d}"
segundos_formatados = f"{segundos_final:02d}"

# Exibe o resultado no formato "horas:minutos:segundos"
print(f"{horas_formatadas}:{minutos_formatados}:{segundos_formatados}")

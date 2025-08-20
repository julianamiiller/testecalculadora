nota = float(input("Digite a nota final (0 a 10): "))
presenca = float(input("Digite o percentual de presença (0 a 100): "))

if nota > 7 and presenca > 75:
    print("Aprovado")
else:
    print("Reprovado")
soma = 0

for i in range(1, 5):
    nota = float(input(f"Digite a nota {i}: "))
    soma += nota

media = soma / 4

print(f"Média final: {media:.2f}")

if media >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")
# Lista para armazenar os nomes
nomes = []

# Loop para pedir 5 nomes
for i in range(1, 6):
    nome = input(f"Digite o {i}º nome: ")
    nomes.append(nome)

# Exibindo os nomes em maiúsculo
print("\nNomes em maiúsculo:")
for nome in nomes:
    print(nome.upper())
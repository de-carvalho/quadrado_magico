lado = int(input("Digite o lado do quadrado mágico (maior que 2): "))

soma_esperada = (lado + lado ** 3) // 2
print("A soma esperada para cada linha, coluna e diagonal é:", soma_esperada)

matriz = []
numeros_usados = []

print("Agora insira os números do quadrado mágico (sem repetir):")
for i in range(lado):
    linha = []
    for j in range(lado):
        numero_valido = 0
        while numero_valido == 0:
            num = int(input(f"Digite o número para a posição [{i+1}][{j+1}]: "))
            if num not in numeros_usados and num > 0:
                numero_valido = 1
                numeros_usados.append(num)
                linha.append(num)
            else:
                print("Número repetido ou inválido. Tente novamente.")
    matriz.append(linha)

linhas_certas = 1
for i in range(lado):
    soma = 0
    for j in range(lado):
        soma = soma + matriz[i][j]
    if soma != soma_esperada:
        linhas_certas = 0

colunas_certas = 1
for j in range(lado):
    soma = 0
    for i in range(lado):
        soma = soma + matriz[i][j]
    if soma != soma_esperada:
        colunas_certas = 0

soma_diagonal1 = 0
for i in range(lado):
    soma_diagonal1 = soma_diagonal1 + matriz[i][i]

soma_diagonal2 = 0
for i in range(lado):
    soma_diagonal2 = soma_diagonal2 + matriz[i][lado - 1 - i]

print("\nMatriz:")
for i in range(lado):
    print(matriz[i])

if linhas_certas == 1 and colunas_certas == 1 and soma_diagonal1 == soma_esperada and soma_diagonal2 == soma_esperada:
    print("É um Quadrado Mágico!")
else:
    print("Não é um Quadrado Mágico.")
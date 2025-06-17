lado = int(input("Digite o lado do quadrado mágico: "))

somaEsperada = (lado + lado ** 3) // 2

matriz = []
numerosUsados = []

for i in range(lado):
    linha = []
    for j in range(lado):
        numeroValido = 0
        while numeroValido == 0:
            num = int(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
            if num not in numerosUsados:
                numerosUsados.append(num)
                numeroValido = 1
            else:
                print("Número já utilizado. Tente novamente.")

            
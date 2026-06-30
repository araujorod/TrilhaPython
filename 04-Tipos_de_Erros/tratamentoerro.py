# TRATAMETNO DE ERROS

# 01-EXECUTE O CÓDIGO E TESTE OS ERROS.
# 02-IDENTIFIQUE O ERRO E COLOQUE NO EXCEPTION

total_gols = 0

for jogo in range(1, 4):
    numero_valido: bool = False

    while numero_valido == False:
        try:
            gols: int = int(input(f"Quandos gols o Brasil fez no jogo {jogo}?"))
            numero_valido = True
        except ValueError:
            print("Valor inválido. Digite um numero inteiro.")

    total_gols += gols

    if gols == 0:
        print("O Brasil não marcou gols nesse joeo. \n")
    elif gols == 1:
        print("O Brasil marcou 1 gols nesse joeo. \n")
    else:
        print(f"O Brasil marcou {gols} nesse joeo. \n")

print(f"O Brasil fez {total_gols} gols.")

media: float = total_gols / 3

print(f"Média de gols por jogo: {media:.2f}")

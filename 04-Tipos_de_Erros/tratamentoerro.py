# TRATAMETNO DE ERROS

# 01-EXECUTE O CÓDIGO E TESTE OS ERROS.
# 02-IDENTIFIQUE O ERRO E COLOQUE NO EXCEPTION

total_gols = 0

for jogo in range(1, 4):
    numero_valido: bool = False

    while numero_valido == False:
        try:
            gols: int = int(input("Quandos gols o Brasil fez?"))
            numero_valido = True
        except ValueError:
            print("Valor inválido. Digite um numero inteiro.")

    total_gols += gols

print(f"O Brasil fez {gols} gols.")

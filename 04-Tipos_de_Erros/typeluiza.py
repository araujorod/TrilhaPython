# CONVERTENDO TIPOS NO PYTHON

total_gols: int = 0

for jogo in range(1, 4):
    gols: int = int(input(f"Quantos gols o Brasil fez nesse {jogo}?:"))

    total_gols += gols

    if gols == 0:
        print("O Brasil não marcou nesse jogo\n")
    elif gols >= 1:
        print("O Brasil marcou 1 gol nesse jogo\n")
    else:
        print("O Brasil marcou {gols} nesse jogo\n")

    # print(total_gols)

print(f"Total de gols do Brasil: {total_gols}\n")

media: float = total_gols / 3

print(f"Media de gols por jogo {media:.2f}\n")

print(f"Media de gols por jogo {round(media, 2)}\n")

###### DESAFIOS #####

texto = "hoje e nossa segunda aula do bootcamp, bootcamp de pyhton"

novo_texto = texto.replace(",", "")

palavras = novo_texto.split()

contagem_de_palavras = {}

print(palavras)

for palavra in palavras:
    if palavra in contagem_de_palavras:
        contagem_de_palavras[palavra] = +1
    else:
        contagem_de_palavras[palavra] = 1

print(contagem_de_palavras)

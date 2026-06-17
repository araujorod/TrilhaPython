nome = "Rodrigo"  # str (String) - Texto
idade = 52  # int (Inteiro) - Número sem casas decimais
estado = "Minas Gerais"  # str (String)
tem_cachorro = True  # bool (Booleano) - Verdadeiro ou Falso
altura = 1.58  # float (Ponto Flutuante) - Número com casas decimais

print(type(nome))
print(type(idade))
print(type(estado))
print(type(tem_cachorro))
print(type(altura))

# Escrever as regras de utilização das variáveis
# 1. Não podem começar com números
# 2. Não podem ter espaços
# 3. Não podem ter caracteres especiais
# 4. Devem ser escritas em snake_case

print(f"Olá {nome}, você tem {idade} anos e mora em {estado}.")

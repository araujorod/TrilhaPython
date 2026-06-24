# # Erro de typo geralmente acontece quando tentamos fazer operações com tipos de dados diferntes:
# # Exemplo: Inteiro + String

# from typing import clear_overloads

# p1 = "3"
# p2 = 1
# p3 = 2.5
# p4 = True


# # print(p1 + p2) # Resultado será TypeError: can only concatenate str (not "int") to str

# print(type(p1))  # 'str'
# print(type(p2))  # 'int'
# print(type(p3))  # 'float'
# print(type(p4))  # 'bool'


# # isinstance()

# print(
#     isinstance(p1, str)
# )  # Com o "isinstance" passamos a variável e o tipo, e o print retorna se é 'True' ou "False'

# # Type Hint - Dica de tipo: Colocar o tipo de valor que é esperado pela variável. Apenas uma dica, não existe nenhum tipo de trava.True

# time: str = "Brasil"
# adversario: str = "Argentina"
# gols: int = 3.5
# classificado: bool = False

# print(f"{time} fez {gols} gols contra {adversario}.")

# if isinstance(gols, int):
#     print("A variavel gols pode ser usada em cálculos.")
# else:
#     print("A variavel gols não pode ser usada em cálculos.")

# if classificado:
#     print("O time está classificado")
# else:
#     print("O time não está classificado")

# try:
#     print(gols / gols)
# except:
#     print("Alguma coisa deu errado")
# else:
#     print("Calculo realizado")
# finally:
#     print("Programação Python")


# numero = int(input("Insira um núemro:"))

# print(type(numero))

# if isinstance(numero, int):
#     print("A variável é uma inteiro!")
# else:
#     print("A variável não é um inteiro!")

usuario = input("Digite seu nome:")

if usuario.isdigit():
    print("Você digitou seu nome errado.")
    exit()
elif len(usuario) == 0:
    print("Você não digitou nada.")
    exit()
elif usuario.isspace():
    print("Voce digitou so espaçoes.")
    exit()
else:
    print("Seu nome foi registrado.")

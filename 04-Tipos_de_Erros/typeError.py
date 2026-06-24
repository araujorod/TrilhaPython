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

time: str = "Brasil"
adversario: str = "Argentina"
gols: int = 3.5
classificado: bool = False

print(f"{time} fez {gols} gols contra {adversario}.")

if isinstance(gols, int):
    print("A variavel gols pode ser usada em cálculos.")
else:
    print("A variavel gols não pode ser usada em cálculos.")

if classificado:
    print("O time está classificado")
else:
    print("O time não está classificado")

"""


LEN - QUANTIDADE DE CARACTERES

- Não funciona com tipos numérios (int, float e bool)

em Python tudo é um objeto, e objetos geralmente tem métodos atrelados à ele



CTRL + / PARA ATIVAR E DESATIVAR O COMENTÁRIO DA SELEÇÃO


"""


# CHECANDO QUANTIDADE MÍNIMA DE CARACTERES
# usuario = input('Digite seu usuário: ')
# qtd_caracteres = len(usuario)
#
# print(usuario, qtd_caracteres, type(qtd_caracteres))
#
# if qtd_caracteres < 6:
#     print('Mínimo de 6 caracteres.')
# else:
#     print('Você foi cadastrado.')


# SOMANDO QUANTIDADE DE CARACTERES DE DUAS STRINGS
string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')

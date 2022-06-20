"""
OPERADORES RELACIONAIS (realizar comparações entre coisas)

== - igual a...
> - maior que...
>= - maior ou igual a...
< - menor que...
<= - menor ou igual a...
!= - diferente de...

será sempre uma expressão BOOL

"""

num_1 = 3
num_2 = 2

print(2 == '2')
print(num_1, num_2)
print(num_1 == num_2)


expressao = num_1 != num_2
print(expressao)


print('\n')                                                              # Aperte CTRL + / para comentar seleção

# print('Você só pode pegar empréstimo se tiver idade mínima de 18 anos.')
# nome = input('Qual o seu nome?: ')
# idade = input('Qual sua idade?: ')
# idade = int(idade) # TypeCasting: Alterando o input de string para int
#
# # Mínimo para pegar empréstimo
# idade_minima = 18
#
# if idade >= idade_minima: # Para que aqui sejam comparados dois ints
#     print(f'{nome} pode pegar o empréstimo.')
# else:
#     print(f'{nome} NÃO pode pegar o empréstimo.')

print('\n')

print('Você só pode pegar empréstimo se tiver idade entre 20 e 30 anos de idade.')
nome = input('Qual o seu nome?: ')
idade = input('Qual sua idade?: ')
idade = int(idade) # TypeCasting: Alterando o input de string para int

# Mínimo para pegar empréstimo
idade_menor = 20 # muito jovem
idade_maior = 30 # muito velho

if idade >= idade_menor and idade <= idade_maior: # Para que aqui sejam comparados dois ints
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
"""

CONDIÇÕES IF, ELIF E ELSE -

ELIF:
O bloco elif é usado quando se faz necessário checar outras condições ou variações da mesma condição.
O bloco elif depende do bloco if, ou seja, é necessário primeiro usar o bloco if e somente se a expressão do bloco if for falsa, o bloco elif será verificado.

ELSE:
O bloco else só é executado quando nenhuma condição de if ou elif for verdadeira.
Por isso, quando precisamos de um valor padrão ou de uma resposta contrária à condição, é necessário adicionar o bloco else.

"""
if True:
    print("verdadeiro.")

    num_1 = 2
    num_2 = 4

print(num_2 + num_1)
print('\n')

if False:
    print('Verdadeira.')
    print('test teste 2')
elif True:
    print('Agora é verdadeiro.')
    nome = input('Qual o seu nome?')
    print (f'Seu nome é {nome}')
elif False:
    print('Mais uma verdadeira.')
    print(22+22)
else:
    print('Não é verdadeiro')
    print('Olá')

#print('A minha expressã não é verdadeira.')

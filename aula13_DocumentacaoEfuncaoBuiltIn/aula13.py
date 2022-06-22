"""

DOCUMENTAÇÃO E FUNÇÕES BUILT-IN ÚTEIS:
https://docs.python.org/3/library/stdtypes.html

- Acompanhar sempre a documentação da tecnologia que estiver usando, principalmente para tiver dúvidas de comandos
  especificos.

- PARA ATIVAR/DESATIVAR COMENTÁRIO DE SELEÇÃO: CTRL + /

string methods: são funções de string, de texto

isdecimal, isdigit, isnumeric, checar se pode ser convertido para inteiro mas ai tem aquele problema que só vai checar número positivos que não tem ponto flutuante
você pode usar o try/except para tentar contornar esse erro quando vc não sabe exatamente oq o usuário pode digitar e isso pode quebrar seu programa no meio do caminho.

"""


# num1 = input('Digite um número: ') # vou receber o número como string
# num2 = input('Digite outro número: ') # vou receber o número como string
#
# num1 = int(num1) # vou converter de string pra int
# num2 = int(num2) # vou converter de string pra int pra poder fazer o cálculo e printar
#
# print(num1 + num2)

##############################################################################################################################################################

# num1 = input('Digite um número: ') # vou receber o número como string
# num2 = input('Digite outro número: ') # vou receber o número como string
#
# # isnumeric, isdigit, isdecimal (todas essas funções/métodos vão me retornar o mesmo resultado (bool), pode me ajudar a não ter um erro no meu programa
# print(num1.isnumeric()) # me retorna um booleano falando se eu posso ou não converter para numerico/int
# print(num2.isnumeric()) # pode ser convertido para um inteiro? True: os dois podem ser convertidos para números e não vão me gerar nenhum erro

##############################################################################################################################################################

# num1 = input('Digite um número: ') # vou receber o número como string
# num2 = input('Digite outro número: ') # vou receber o número como string
#
# # nesse momento eu não estou preocupado com o número negativo ou número de ponto flutuante então eu posso utilizar essa função mas se eu colocar um -1 por exemplo retornará o else pq o "-" não é um dígito.
# if num1.isdigit() and num2.isdigit(): # isso vai retornar true or false então, se os dois forem um dígito
#     num1 = int(num1) # Quer dizer que eu posso fazer essa conversão)
#     num2 = int(num2) # Quer dizer que eu posso fazer essa conversão)
#
#     print(num1 + num2) # e aqui eu posso fazer minha conta
# else:
#     print('Não pude converter os números para realizar contas') # se der errado
#
#     # o programa flui bem melhor pq agora a gente não está deixando o erro ocorrer
#     # a gente ta checando antes oq o usuário digitou pra depois fazer conversões, contas, etc...

##############################################################################################################################################################

# FUNÇÕES CRIADAS/HAND-MADE/DIY:
# https://github.com/luizomf/check-numbers-python/blob/master/chk_numbers.py

# import re
#
#
# def is_float(val): # CHECANDO SE UMA STRING PODE SER CONVERTIDA PARA FLOAT
#     if isinstance(val, float): return True
#     if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
#
#     return False
#
#
# def is_int(val): # CHECANDO SE UMA STRING PODER SER CONVERTIDA PARA INTEIRO
#     if isinstance(val, int): return True
#     if re.search(r'^\-{,1}[0-9]+$', val): return True
#
#     return False
#
#
# def is_number(val): # CHECANDO SE UMA STRING PODER SER CONVERTIDA PARA QUALQUER NÚMERO
#     return is_int(val) or is_float(val)
#
#
# ###########
# #  USAGE  #
# ###########
#
# # ESTOU EXTENDENDO AS FUNÇÕES DO PYTHON / CRIANDO MINHAS PRÓPRIAS FUNÇÕES:
#
#
# # Float
# print(is_float('-101.0112'))  # True
# # Int
# print(is_int('-1010112'))  # True
# # Numbers in general (float ou int)
# print(is_number('-1010.112'))  # True
#
# # False
# print(is_number('123a'))  # False
#
#
# num1 = input('Digite um número: ') # será recebido como string
# num2 = input('Digite outro número: ') # será recebido como string
#
# if is_number(num1) and is_number(num2): # SE numero1 for número e numero2 for número
#     num1 = float(num1) # então converta para float
#     num2 = float(num2) # então converta para float
#
#     print(num1 + num2) # faça a soma e printe o resultado.
# else:
#     print('ERROR') # Se não, dê erro.

num1 = input('Digite um número: ') # será recebido como string
num2 = input('Digite outro número: ') # será recebido como string1

try: # tente (como se fosse if)
    num1 = float(num1) # converter numero1 para float
    num2 = float(num2) # converter numero1 para float

    print(num1 + num2) # faça a soma do numero1 e numero2 e printe o resultado
except: # (fomo se fosse else)
    print('ERROR') # Se não, dê erro:

    # Olha Python, tenta executar o meu código, se ocorrer qualquer erro no meu código vc executa outro bloco de código,
    # mas não apresenta aquele seu erro na tela.

    #




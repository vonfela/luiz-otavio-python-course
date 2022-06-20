"""
OPERADORES LOGICOS ()

and
or
not (inversor/inversão)
in
not in

será sempre uma expressão BOOL

"""
                                    # OPERADOR AND
# (Verdadeiro e Verdadeiro?) = Verdadeiro
# comparacao1 and comparacao2

# (Verdadeiro e Falso?) = Falso,  pq as duas comparações PRECISAM SER verdadeiras
# comparacao1 and comparacao2

                                    # OPERADOR OR
# verdadeiro OU verdadeiro? = Verdadeiro, QUALQUER UMA das duas expressões que passar um valor verdadeiro, a expressão inteira será verdadeira
# comp1 or comp2

                                    # OPERADOR NOT
# a = 2
# b = 3
#
# if b > a: # está sendo passado TRUE
#     print('B é maior do que A.')
# else:
#     print('A é maior do que B.')


# a = 2
# b = 3
#
# if not b > a:  # está sendo INVERTIDO PARA FALSE
#     print('B é maior do que A.')
# else:
#     print('A é maior do que B.') # Este será o resultado mesmo não sendo verdade


# checar variáveis vazias
# a = ''
# b = 0
#
# if not a:
#     print('Por favor preencha o valor de A.')
# if not b:
#     print('Por favor preencha o valor de B')

                                                     # OPERADOR IN e NOT IN
# nome = 'Felipe'
#
# if 'eli' in nome:
#     print('existe')
# else:
#     print('NÃO existe')

nome = 'Felipe'

if 'e' not in nome:
    print('NÃO existe')
else:
    print('EXISTE')

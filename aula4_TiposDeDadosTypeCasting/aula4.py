"""
Tipos de dados:
str - string - textos 'Assim' e "assim"
int - Inteiro - 123456 0 -10 -50
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93
boll - booleano/lógico - True/False   10==10

"""

print('Luiz', type('Luiz'))
print(10, type(10))
print('25.23', type('25.23'))
print('l' == 'l', type('l' == 'l'))
print(bool('')) #lista vazia avalia em false

#type casting que é converter o tipo do argumento para outro tipo:

print('Felipe', type('Felipe'))
print('Felipe', type('Felipe'), bool('Felipe'))
print('10', type('10'), type(int('10'))) #type casting, conversão de tipo
#print('luiz', int('luiz')) #não tem como, não da pra converter string para inteiro


print('\n')
print('#Exercício:')
#string: nome
print('Nome: Felipe', type('Felipe'))

#int: idade
print('Idade:', 27, type(27))

#float: altura
print('Altura:', 1.69, type(1.69))

#É maior de idade 27 > 18?
print('É maior de idade?', 27 > 18, type(27 > 18))
"""
aula 7 - introdução à formatação de strings


"""

nome = 'Felipe Cavalcanti'
idade = 27 # int
altura = 1.69 # float
peso = 90
e_maior = idade > 18 #bool
imc = peso / altura**2


print(nome, 'tem', idade, 'anos de idade e seu IMC é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}') # formatar, exibir valores formatados, não preciso me preocupar com o tipo da variavel
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}') # :.exibir2casasDecimais F(é um número de ponto flutuante)
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))

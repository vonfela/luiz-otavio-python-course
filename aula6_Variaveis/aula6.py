"""
variáveis

Iniciar com letra, pode conter números, separar com _, letras minúsculas

= Operador de atribuição, aquela variável recebe(=) aquele valor

"""

nome = 'Felipe'
print(nome, type(nome))
print('\n')

nome = 'Felipe Cavalcanti'
idade = 27 # int
altura = 1.69 # float
peso = 90
e_maior = idade > 18 #bool
imc = peso / altura**2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Peso:', peso)
print('É maior de idade:', e_maior)
print('\n')

print(idade * altura)
print('\n')

# Exercício: calcular IMC, indice de massa corporal:

print(nome, 'tem', idade, 'de idade e seu IMC é', imc)

"""

INPUT, ENTRADA DE DADOS -


"""

nome = input("Qual seu nome? ") #input guardará a informação como uma string, mesmo se eu digitaer um número int/float
idade = input("Qual sua idade? ")
nascimento = 2022 - int(idade) #casting, alterando o valor armazenado na idade de string para inteiro

print()

print(f'{nome} tem {idade} anos e nasceu em {nascimento}.')
print(f'O usuáruio digitou {nome} e o tipo da variável é '
      f'{type(nome)}')

print()

numero_1 = input('Digite um número: ')
numero_2 = input('Digite um outro número: ')
print(numero_1 + numero_2) # O resultado será concatenado pois o valor armazenado no input é uma string


numero_1 = int(input('Digite um número: ')) # Solução 1: converter direto o input/valor
numero_2 = input('Digite um outro número: ')
numero_2 = int(numero_2)  # Solução 2: modificar o tipo/formato da variável
print(numero_1 + numero_2) # O resultado será concatenado pois o valor armazenado no input é uma string


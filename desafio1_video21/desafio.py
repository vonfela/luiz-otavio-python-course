"""

- Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
- Criar variável com o ano atual (int)
- Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
- Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
- Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

"""

nome = 'Felipe'
idade = 28
altura = 1.69
peso = 90.100
aa = 2022
nascimento = aa - idade
imc = peso / altura**2

print(f'{nome} tem {idade} anos, {altura:.1f} de altura e pesa {peso:.0f}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {nascimento}.')

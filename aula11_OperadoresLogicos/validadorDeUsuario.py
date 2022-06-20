# CHECAGEM DE USUARIO E SENHA (muito simples, não usar em produção)

user = input('User: ')
pas = input('Password: ')

user_db = 'felinha'
pas_db = '123123'

if user_db == user and pas_db == pas:
    print('LOGGED IN')
else:
    print('User or password incorrect.')

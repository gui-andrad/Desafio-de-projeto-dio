nome = str(input('Digite seu nome completo: ')).strip()
nm = nome.split()
print('O primeiro nome é {} '.format(nm[0]))
print('O último nome é {}'.format(nm[len(nm)-1]))
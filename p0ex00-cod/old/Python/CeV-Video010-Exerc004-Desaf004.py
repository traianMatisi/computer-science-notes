dados = input('Digite o que você quiser: ')
print('O tipo primitivo (class) desse dado é:', type(dados))
print('Esse dado só possui espaços?', dados.isspace())
print('Esse dado só possui números?', dados.isnumeric())
print('É alfabético?', dados.isalpha())
print('É alfanumérico?', dados.isalnum())
print('São maiúsculas?', dados.isupper())
print('São minúsculas?', dados.islower())
print('Está capitalizada?', dados.istitle())
print('Procure outras definições em IDLEs e livros e seja feliz!')
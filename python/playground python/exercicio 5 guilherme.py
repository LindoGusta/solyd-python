print('O Convite.')
print('=============================================')

convidados = input('Coloque o numero de convidados: ')
lista_convidados = []

i = 1
while i <= int(convidados):     # for i in range(int(convidados))
    nome_convidado = input('Nome do convidado #'+ str(i) +': ')
    lista_convidados.append(nome_convidado)
    i += 1

print(f'\nSerao convidados {convidados} para a festa\n')

print(':LISTA DE CONVIDADOS:')
for convidado in lista_convidados:
    print(convidado)
print('=============================================')
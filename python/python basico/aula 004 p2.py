frase = "Cala a boca, levi"
lista_de_nomes = ['Marcos Antônio Nascimento', 'Mariana','Guilherme', 'Guilherme', 'Cala a boca levi']
frasen = frase + ". Chato pra caramba"

frase_separada = frase.split(',') #transformo a frase em uma lista e escolho onde quero cortar
print(frase_separada)

print(frasen)

contador = 0
for nome in lista_de_nomes:
    contador += 1

print(contador)

#ou

print(len(lista_de_nomes))

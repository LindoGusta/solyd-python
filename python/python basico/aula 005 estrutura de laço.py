nomes = ["Gustavo", "Guilherme", "Levi", "Whisky"]
palavra = ("Gustavin do Grau heheheha")

for i in range(len(nomes)):
    print(nomes[i])
    nomes.append('Eae')

print(nomes)

for i in palavra:
    print(i)

a = 0

while a < 10:
    print("a é menor que 10: ", a)
    a = a + 1

numero = 0

while True:
    print(numero)
    if numero == 20:
        break
    numero += 1

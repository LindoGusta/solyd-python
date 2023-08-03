print("Olá, vai fazer uma festa? Quantos serão os convidados? ")
convidados = int(input())
numero = 1
lista_de_convidados = []

print(f"Ok, {convidados} convidados, quais os nomes de cada um?")
for i in range(convidados):
    lista_de_convidados.append(input(f"Digite o nome do convidado número {numero}: "))
    numero = numero + 1

for convidado in lista_de_convidados:
    print(convidado)

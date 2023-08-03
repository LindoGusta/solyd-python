frase = "Cala a boca levi"
lista_de_nomes = ['Marcos Antônio Nascimento', 'Mariana','Guilherme', 'Guilherme', 'Cala a boca levi']
lista_de_nomes.append('Cauan') #insere item a lista, sempre em ultimo
lista_de_nomes.remove('Mariana') #remove um item da lista
    #lista_de_nomes.clear() #exclui tudo da lista, pra testar, deve-se excluir todas as funções de print abaixo
lista_de_nomes.insert(1, 'Creosvaldo') #escolho onde quero inserir um item
lista_de_nomes[0] = 'Claudineia' #vai substituir o item 0 por claudineia

contar_Guilherme = lista_de_nomes.count("Guilherme") #vai contar quantos guilherme tem na lista

print(frase[0]) #vai printar a primeira letra da 'frase', no caso a letra número 0

print(lista_de_nomes[0]) #vai printar o nome 0, no caso, Marcos Antonio Nascimento, ja agr, claudineia kkkkkkkkk

print(frase[0:6]) #vai pegar todas as letras de 1 a 6   
print(frase[0:6:2]) #pula de tantas em tantas letras

print(lista_de_nomes[-1]) #vai printar o ultimo item

print(lista_de_nomes)

print(contar_Guilherme)

print(lista_de_nomes.pop())
print(lista_de_nomes)

idade = int(input("Qual sua idade? "))
peso = int(input("Quanto você pesa em kg? "))
altura = int(input("Quanto você mede em cm? "))

a1 = idade >= 18
a2 = peso >= 60
a3 = altura >= 170
a4 = a1 + a2 + a3

if a4 >= 3:
    print("Você pode entrar no Exército Brasileiro!")

else:
    print("Você não pode entrar no Exército Brasileiro")

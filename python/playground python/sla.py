# Definir número de anos
anos = 30

# Calcular segundos em potência de 10
segundos = anos * 365 * 24 * 60 * 60
potencia_de_10 = len(str(segundos)) - 1

# Imprimir resultado
print("Você viveu aproximadamente", segundos, "segundos.")
print("Isso é equivalente a 10 elevado a", potencia_de_10, "segundos.")
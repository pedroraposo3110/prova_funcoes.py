# Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721
def reverso_numero(numero):
    numero_str = str(numero)
    reverso = numero_str[::-1]
    return int(reverso)


numero = 127
reverso = reverso_numero(numero)
print(f"O reverso de {numero} é {reverso}")

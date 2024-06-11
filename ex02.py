#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado. 
def contar_digitos(numero):
    return len(str(numero))

# Exemplo de uso
numero = 127
quantidade_digitos = contar_digitos(numero)
print(f"O número {numero} possui {quantidade_digitos} dígitos.")

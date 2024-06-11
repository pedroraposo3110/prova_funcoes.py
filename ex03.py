# Faça uma função que computa a potência ab para valores a e b(assuma números inteiros) passados por parâmetro (não use o operador **).
def potencia(a, b):
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado

# Exemplo de uso
base = 2
expoente = 5
resultado = potencia(base, expoente)
print(f"A potência de {base} elevado a {expoente} é {resultado}")

# Solicitando a string e o número inteiro ao usuário
texto = input("Digite uma string: ")
numero = int(input("Digite um número inteiro: "))

# Repetindo o texto o número de vezes informado com espaçamento entre as repetições
resultado = (texto + ' ') * numero

# Removendo o espaço extra no final e apresentando o resultado na tela
print("Texto repetido:", resultado.rstrip())

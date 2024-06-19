# Solicitando os números ao usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Solicitando a operação desejada
operacao = input("Digite a operação desejada (+ para soma, - para subtração, * para multiplicação, / para divisão): ")

# Realizando a operação selecionada
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    # Verificando se o segundo número é zero para evitar divisão por zero
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Divisão por zero não é possível"
else:
    resultado = "Operação inválida"

# Apresentando o resultado na tela
print(f"Resultado da operação {operacao}: {resultado}")

# Solicitando as três notas ao usuário
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Solicitando o tipo de média ao usuário
tipo_media = input("Deseja calcular a média simples (S) ou média ponderada (P)? ").upper()

# Verificando o tipo de média escolhida e calculando
if tipo_media == 'S':
    # Calculando média simples
    media = (nota1 + nota2 + nota3) / 3
    print(f"A média simples das notas {nota1}, {nota2} e {nota3} é: {media}")
elif tipo_media == 'P':
    # Solicitando qual nota terá peso 2 na média ponderada
    peso2 = input("Qual nota terá peso 2 na média ponderada? (1 para a primeira, 2 para a segunda, 3 para a terceira): ")
    
    # Calculando média ponderada
    if peso2 == '1':
        media = (nota1 * 2 + nota2 + nota3) / 4
    elif peso2 == '2':
        media = (nota1 + nota2 * 2 + nota3) / 4
    elif peso2 == '3':
        media = (nota1 + nota2 + nota3 * 2) / 4
    else:
        print("Opção inválida para escolha de peso.")
        media = None
    
    if media is not None:
        print(f"A média ponderada das notas {nota1}, {nota2} e {nota3} é: {media}")
else:
    print("Opção de média inválida. Escolha entre média simples (S) ou média ponderada (P).")

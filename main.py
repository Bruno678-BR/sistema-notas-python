def adicionar_nota(lista):

    nota = float(input("Digite a nota: "))

    lista.append(nota)

def mostrar_notas (lista):

    for numero in lista:
        print(numero)

def media_notas(lista):

    soma = 0

    for numero in lista:
        soma += numero
    media = soma/len(lista)
    return media

def maior_notas(lista):

    maior = lista[0]

    for numero in lista:
        if numero > maior:
            maior = numero
    return maior

def aprovados_notas(lista):

    contador = 0

    for numero in lista:
        if numero >= 7:
            contador += 1
    return contador

lista = []

while True:

    print()
    print("[1] - Adicionar uma nota")
    print("[2] - Mostrar a/as notas")
    print("[3] - Media das notas")
    print("[4] - Mostrar a maior nota")
    print("[5] - Quantidade de aprovados")
    print("[6] - Sair")

    opcao = int(input("Qual opção você escolhe? "))

    if opcao == 1:
        adicionar_nota(lista)
    elif opcao == 2:
        if len(lista) == 0:
            print("Nenhuma nota cadastrada!")
        else:
            print("Notas cadastradas:")
            mostrar_notas(lista)
    elif opcao == 3:
        if len(lista) == 0:
            print("Nenhuma nota cadastrada para calcular a media!")
        else:
            media = media_notas(lista)
            print(f"A media de notas é {media}")
    elif opcao == 4:
        if len(lista) == 0:
            print("Nenhuma nota cadastrada!")
        else:
            maior = maior_notas(lista)
            print(f"A maior nota é {maior}")
    elif opcao == 5:
        if len(lista) == 0:
            print("Nenhuma nota cadastrada")
        else:
            aprovados = aprovados_notas(lista)
            print(f"Foram aprovados {aprovados}")
    elif opcao == 6:
        print("Saindo do sistema!")
        break
    else:
        print("Opção inválida!")  
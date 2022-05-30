lista = []

def cadastro():

    np = int(input("Insira o numero de pessoas deseja cadastrar:"))

    for i in range(np):
        lista.append(input("\nNome: "))

def vizualizar():
    for i in range(len(lista)):
        print(i,":",lista[i],sep = "")

def atualizar():
    while True:
        qual = int(input("\nQual elemento desejas atualizar: "))
        if qual < 0 or qual > len(lista):
            print("Esse elemento nao existe!\n")
            continue
        lista[qual] = input("Novo nome:")
        break

def remove():
    while True:
        qual = int(input("\nQual elemento desejas apagar: "))
        if qual < 0 or qual > len(lista):
            print("Esse elemento nao existe!\n")
            continue
        del lista[qual]
        break

while True:
    action = int(input('\nO que desejas fazer?:\n1)Cadastrar pessoas\n2)Vizualizar lista\n3)Atualizar lista\n4)Ver a lista em ordem alfabetica\n5)Remover elemento\n6)Sair\n:'))

    if action == 1:
        cadastro()

    elif action == 2:
        if len(lista) == 0:
            print("Nao ha lista para ser vista")
            continue
        vizualizar()

    elif action == 3:
        if len(lista) == 0:
            print("Nao ha lista para ser atualizada")
            continue
        atualizar()

    elif action == 4:
        if len(lista) == 0:
            print("Nao ha lista para ser ordenada")
            continue
        print(sorted(lista))

    elif action == 5:
        if len(lista) == 0:
            print("Nao ha lista para ser atualizada")
            continue
        remove()

    elif action == 6:
        break

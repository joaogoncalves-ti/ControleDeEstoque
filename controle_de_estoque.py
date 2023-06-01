produtos = []

while True:
    print('MENU')
    print('1 - Cadastrar um novo produto')
    print('2 - Listar cadastros')
    print('3 - Sair')

    opcao = int(input('Escolha a opção desejada. '))

    if opcao == 1:
        print("Opção de cadastrar novo produto selecionada...")
        produto = input("Que produto você quer cadastrar?: ")
        marca = input("Qual a marca desse produto?: ")

        cadastro = {
            'produto': produto,
            'marca': marca          
        }
        
        produtos.append(cadastro)
        print('Cadastro realizado com sucesso!')
    elif opcao == 2:
        print("Opção de listar selecionada...")
        for x in produtos:
            print("-----------------------------")
            print("produto: " + x['produto'])
            print("marca: " + x['marca'])
            print("-----------------------------")

    elif opcao == 3:
        print("Encerrando programa...")
        break

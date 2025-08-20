while True:

    print("\n1 - soma \n2 - subtração \n3 - multiplicação \n4 - divisão \n5 - sair ")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 5:
        print("Você saiu!!! ")
        break

    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    soma = num1 + num2 
    subtraçao = num1 - num2
    multiplicacao = num1 * num2
    divisao = num1 / num2

    if opcao ==1:
        print(f"A soma é {soma}.")
        

    elif opcao ==2:
        print(f"O resultado é {subtraçao}. ")


    elif opcao ==3:
        print(f'O resultado é {multiplicacao}')

    elif opcao ==4:
        print(f"O resultado é {divisao}")

    else:
         print("Opção inválida. ")

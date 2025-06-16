menu = """
---------
[d] Depositar
[s] Saque
[e] Extrato
[f] sair

----------- 
"""

saldinho = 0
limite_usuario = 500
extrato = ""
numero_saques = 0

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de depósito"))
        if valor > 0:
            saldinho += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado pelo usuároi é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldinho = valor > saldinho
        excedeu_limite = valor > limite_usuario
        excedeu_saques = numero_saques >= 3

        if excedeu_saldinho:
            print("Seu saldinho não é suficiente para realizar essa ação!")
        elif excedeu_limite:
            print("Erro! Seu limitinho não é suficiente para realizar essa ação!")
        elif excedeu_saques:
            print("Número de saques diários foi excedidos!")

        elif valor >0:
            saldinho += valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! o valor informado é inválido")

    elif opcao == "e":

        print(f"\n Seu extrato bancário: -------------------")
        if not extrato.strip():
            print("Extrato vazio!")
        else:
            print(extrato)
        print (f"\n saldinho: R$ {saldinho:.2f}")
        print("=="*6)

    elif opcao == "f":
        break

    else:
        print("Operação INVÁLIDA,! digitou uma solicitação incorreta")
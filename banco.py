menu= """
######################################
#   Bem-vindo ao Sistema Bancário!   #
######################################
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

######################################

=>  """


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input('Informe o valor do depósito: '))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
        else:
            print("Valor de depósito inválido. Tente novamente.")
       
    elif opcao =="s":
        valor = float(input('Informe o valor do saque: '))
        if valor > saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor > limite:
            print(f"Valor do saque excede o limite de R$ {limite:.2f}.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"Limite de saques diários atingido ({LIMITE_SAQUES} saques).")
        elif valor <= 0:
            print("Valor de saque inválido. Tente novamente.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    elif opcao == "e":
        print("=== Extrato ===")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("================")
    elif opcao == "q":
        print('Obrigado por usar nosso sistema!')        
        break
    else:                   
        print("Opção inválida. Tente novamente.")   
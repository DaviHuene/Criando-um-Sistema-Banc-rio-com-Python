import textwrap

def menu (): 
    menu = """\n
    ======================================
    #   Bem-vindo ao Sistema Bancário!   #
    ======================================
    #        Escolha uma opção:          #
    #------------------------------------#
    #   [d]Depositar                     #
    #   [s] Sacar                        #
    #   [e]Extrato                       #
    #   [nc]Nova Conta                   #
    #   [lc]listar Contas                #
    #   [nu]Novo Usuário                 #
    #   [q]Sair                          #   
    #                                    #
    ======================================
    =>  """
    return input(textwrap.dedent(menu))
def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito realizado com sucesso! Saldo atual: R$ {saldo:.2f}")
    else:
        print("Valor de depósito inválido. Tente novamente.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
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
    return saldo, extrato, numero_saques

def exibir_extrato(extrato, saldo):
    print("=== Extrato ===")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("================")


def criar_usuarios(usuarios):
    nome = input("Informe o nome do usuário: ")
    cpf = input("Informe o CPF do usuário (apenas números): ")
    endereco = input("Informe o endereço do usuário: ")
    telefone = input("Informe o telefone do usuário: ")

    if any(u['cpf'] == cpf for u in usuarios):
        print("Usuário já cadastrado com este CPF.")
        return
    
    usuario = {
        "nome": nome,
        "cpf": cpf
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} cadastrado com sucesso!")


def criar_conta (agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário para criar a conta: ")
    usuario = next((u for u in usuarios if u['cpf'] == cpf), None)
    
    if not usuario:
        print("Usuário não encontrado. Cadastre o usuário primeiro.")
        return None
    
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    print(f"Conta criada com sucesso! Agência: {agencia}, Número da Conta: {numero_conta}")
    return conta

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    
    print("=== Lista de Contas ===")
    for conta in contas:
        print(f"Agência: {conta['agencia']}, Número da Conta: {conta['numero_conta']}, Usuário: {conta['usuario']['nome']}")
    print("========================")


    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
 

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor a depositar: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor a sacar: R$ "))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)

        elif opcao == "e":
            exibir_extrato(extrato, saldo)

        elif opcao == "nc":
            conta = criar_conta(AGENCIA, len(contas) + 1, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "nu":
            criar_usuarios(usuarios)

        elif opcao == "q":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")
  
main()     

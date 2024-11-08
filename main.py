

import textwrap



# Menu de opções
def menu():
    menu = """\n
====================MENU======================
    [1]\tDepositar
    [2]\tSacar 
    [3]\tExtrato 
    [4]\tNova conta
    [5]\tListar contas
    [6]\tNovo usuário
    [0]\tSair 
    -> """
    return input(textwrap.dedent(menu))

# Função depositar
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n ---Depósito realizado com sucesso ---")
    else:
        print("\n @@@ Operação falhou! O valor informado é inválido. @@@")

    return saldo, extrato

# Função sacar

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n @@@ Operação falhou! vocé não tem saldo sufuciente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n @@@ Operação falhou! Numero máximo de saque excedido. @@@")
    elif valor > 0:
        saldo-=valor
        extrato+= f"Saque:\t\t\r4 {valor:.2f}\n"
        numero_saques+=1
        print("\n --- Saque realizado com sucesso!---")
    else:
        print("\n @@@ Operação falhou! o valor informado é invalido @@@")
    
    return saldo, extrato

# Função para exibir extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n --------------EXTRATO------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("\n Saldo:\t\tR$ {saldo:.2f}")
    print("------------------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o cpf (somente numeros):")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n @@@ CPF já cadastrado")
        return

    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o endereco")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("---Usuário criado com sucesso!")

# Função para filtrar usuário
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Conta criada com sucesso! ---")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C: \t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

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
# Opção de depósito
        if opcao == "1":
            valor = float(input("informe o valor do deposito:"))
        
            saldo, extrato = depositar(saldo, valor, extrato)
        
# Opção de saque
        elif opcao == "2":
            valor = float(input(" Informe o valor do saque: "))
        
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
        )

# Opção de extrato
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

# Criar contas
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta :
                contas.append(conta)

# Listar contas
        elif opcao == "5":
            listar_contas(contas)

# Criar usuario
        elif opcao == "6":
            criar_usuario(usuarios)

        
# Sair da aplicação
        elif opcao == "0":
            break

        else:
            print("Operação inválida, digite a opção desejada: 1,2,3,4,5,6 ou 0")
            break
main()
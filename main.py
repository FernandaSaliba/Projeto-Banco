# Menu de opções
menu = """

[1] Depositar
[2] Sacar 
[3] Extrato 
[0] Sair 

-> """
# declaração das variáveis
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# laço de repetição
while True:
    opcao = input(menu)
# Opção de depósito
    if opcao == "1":
        valor = float(input("informe o valor do deposito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("deposito realizado com sucesso!")
        
        else:
            print("Operação falhou! o valor informado é inválido")
# Opção de saque
    elif opcao == "2":
        valor = float(input(" Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        print("Saque realizado com sucesso!")

        if excedeu_saldo:
            print("Operação falhou! saldo insuficiente")
        
        elif excedeu_limite:
            print("Limite excedido")

        elif excedeu_saques:
            print("Saque excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            

        else:
            print("Valor inválido")
# Opção de extrato
    elif opcao == "3":
        print("EXTRATO")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        
# Sair da aplicação
    elif opcao == "0":
        break

    else:
        print("Operação inválida, digite a opção desejada: 1,2,3 ou 0")
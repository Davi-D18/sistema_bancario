import os

saldo = 0
limite = 500
extrato = {}
numero_saques = 0
numero_depositos = 0
LIMITE_SAQUES = 3

def sacar(valor):
    limpar_terminal()
    global saldo, numero_saques
    if numero_saques >= LIMITE_SAQUES:
        print("Limite de saques atingido!")
        return
    elif valor > limite:
        print("Valor acima do limite permitido!")
        return
    elif valor <= 0:
        print("Valor inválido!")
        return
    
    if valor <= saldo:
        saldo -= valor
        print("Saque realizado com sucesso!")
        numero_saques += 1

        extrato.update({f"saque -> {numero_saques}": valor})
    else:
        print("Saldo insuficiente!")

def depositar(valor):
    limpar_terminal()

    if valor <= 0:
        print("Valor inválido!")
        return

    global saldo, numero_depositos
    saldo += valor

    print(f"""
    Depósito realizado com sucesso!
    Valor: R${valor:.2f}
    """)

    numero_depositos += 1
    extrato.update({f"deposito -> {numero_depositos}": valor})

def exibir_extrato():
    limpar_terminal()

    if not extrato:
        print("não foram realizadas movimentações")
        return

    print("Depósitos:")
    for key, value in extrato.items():
        if "deposito" in key:
            print(f"{key}: +{value}")
    
    print("\n----------\nSaques:")
    for key, value in extrato.items():
        if "saque" in key:
            print(f"{key}: -{value}")
    
    print(f"\nSaldo atual: R${saldo:.2f}")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
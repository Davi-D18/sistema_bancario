from utils import (
    cadastrar_usuario,
    criar_conta_corrente,
    depositar,
    exibir_extrato,
    sacar,
)
from utils.data import conta_corrente, usuarios

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[nc] Nova Conta Corrente
[nu] Novo Usuário 

=> """

while True:

    opcao = input(menu)

    if opcao == "d":
      valor = float(input("Digite o valor que deseja depositar: "))
      depositar(valor)
    elif opcao == "s":
      valor = float(input("Digite o valor que deseja sacar: "))
      sacar(valor)
    elif opcao == "e":
      exibir_extrato()
    elif opcao == "nc":
      criar_conta_corrente()
    elif opcao == "nu":
      cadastrar_usuario()
    elif opcao == "q":
        break
    elif opcao == "v_user":
        print(usuarios)
    elif opcao == "v_conta":
        print(conta_corrente)
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
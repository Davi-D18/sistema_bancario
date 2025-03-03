from utils import depositar, exibir_extrato, sacar

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

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
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
from .data import conta_corrente, usuarios


def criar_conta_corrente():
    agencia = "001"
    numero_conta = len(conta_corrente) + 1

    try:
        cpf_usuario = int(input("Informe o CPF: "))
    except ValueError:
        print("CPF inválido! Deve ser numérico.")
        return

    if cpf_usuario in usuarios:
        conta_corrente.append({
            numero_conta: {
                "agencia": agencia,
                "usuario": cpf_usuario,
                "numero_conta": numero_conta,
            }
        })
        print("Conta corrente criada com sucesso!")
    else:
        print("Usuário não cadastrado. Realize o cadastro primeiro.")

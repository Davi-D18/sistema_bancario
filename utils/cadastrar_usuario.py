from .data import usuarios
from .functions import limpar_terminal


def cadastrar_usuario():
    limpar_terminal()

    try:
        cpf = int(input("Informe seu CPF: "))
    except ValueError:
        print("CPF inválido! Deve ser numérico.")
        return

    if cpf in usuarios:
        print("Usuário já cadastrado!")
        return

    nome = input("Informe seu nome: ")
    data_nascimento = input(
        "Informe sua data de nascimento (dia/mês/ano - ex: 01/01/2000): "
    )
    logradouro = input("Informe seu logradouro: ")
    numero = input("Informe o número: ")
    bairro = input("Informe o bairro: ")
    cidade = input("Informe a cidade: ")
    estado = input("Informe o estado: ")

    endereco = f"{logradouro}, {numero} - {bairro}, {cidade} - {estado}"

    usuarios[cpf] = {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
    }
    print("Usuário cadastrado com sucesso!")

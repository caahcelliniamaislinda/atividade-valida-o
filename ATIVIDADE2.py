class Cliente:
    def __init__(self, nome, idade, saldo, statusCadastro):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.statusCadastro = statusCadastro

    def validar_nome(self, nome):
        if nome is None or nome == "":
            return False
        return True

    def validar_idade(self, idade):
        if idade < 18:
            return False
        return True

    def validar_saldo(self, saldo):
        if saldo < 0:
            return False
        return True

    def validar_status_cadastro(self, statusCadastro):
        return statusCadastro

    def validar_cliente(self):
        if (
            self.validar_nome(self.nome)
            and self.validar_idade(self.idade)
            and self.validar_saldo(self.saldo)
            and self.validar_status_cadastro(self.statusCadastro)
        ):
            return True
        else:
            return False

# Exemplo de uso:
cliente1 = Cliente("João", 25, 100, True)

# Validar o cliente
if cliente1.validar_cliente():
    print("Cliente válido!")
else:
    print("Cliente inválido!")


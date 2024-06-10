class Cadastro:
    def __init__(self, nome, idade, saldo, statusCadastro):
        self.nome = nome
        self.idade = idade
        self.saldo = saldo
        self.statusCadastro = statusCadastro

    def validar_nome(self):
        if self.nome is None or self.nome == "":
            return False
        return True

    def validar_idade(self):
        if self.idade < 18:
            return False
        return True

    def validar_saldo(self):
        if self.saldo < 0:
            return False
        return True

    def validar_status_cadastro(self):
        return self.statusCadastro

    def validar_cadastro(self):
        if (
            self.validar_nome()
            and self.validar_idade()
            and self.validar_saldo()
            and self.validar_status_cadastro()
        ):
            return True
        else:
            return False

# Exemplo de uso:
cadastro1 = Cadastro("Ana", 20, 500, True)

# Validar o cadastro
if cadastro1.validar_cadastro():
    print("Cadastro válido!")
else:
    print("Cadastro inválido!")


class Cadastro:
    def __init__(self):
        print("Construtor")

    def validarNome(self, nome):
        if len(nome) == 0:
            print("Erro: O valor nome não pode ser vazio")
        else:
            self.nome = nome
            print("Valor cadastrado com sucesso:", self.nome)


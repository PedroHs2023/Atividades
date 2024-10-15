class Restaurante :
    nome        = ''
    categoria   = ''
    ativo       = False
    def verificar_status(self):
        if self.ativo:
            print(f'O restaurante {self.nome} esta desativado')
        else:
            print(f'O restaurante {self.nome} esta ativado')

    def verificar_categoria(self):
        if self.categoria:
            print(f'Sim a categoria do {self.nome} esta correta')
        else:
            print(f'A categoria do {self.nome} esta incorreta')

    def mudar_nome(self):
        self.nome = novo_nome = input('Digite um novo nome: ')
        print(f'Nome atualizado {self.nome}')

    def desativar_restaurante(self):
        self.ativo = False
    
    def ativar_restaurante(self):
        self.ativo = True
            



restaurante_praca               = Restaurante()
restaurante_praca.nome          = 'Praca'
restaurante_praca.categoria     = 'Italiana'
restaurante_praca.ativo         = False

restaurante_pizza               = Restaurante()
restaurante_pizza.nome          = 'Pizza Planet'
restaurante_pizza.categoria     = 'Fast Food'
restaurante_pizza.ativo         = True

print(vars(restaurante_praca))
restaurante_praca.verificar_status()
restaurante_pizza.verificar_status()
restaurante_pizza.verificar_categoria()
restaurante_praca.mudar_nome()
restaurante_praca.ativar_restaurante()
print(vars(restaurante_praca))

class Carro:
    carros = []

    def __init__(self, ano, cor, modelo):
        self.ano = ano
        self.modelo = modelo
        self.cor = cor

carro1 = Carro('2000', 'Amarelo', 'Sedan')

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, n_estrelas, cidade, ativo):
        self.nome = nome
        self.categoria = categoria
        self.n_estrelas = n_estrelas
        self.cidade = cidade
        self.ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

restaurante_Peninha = Restaurante('Peninha', 'Restaurante do povo', '3', 'Criciuma', '')
print(restaurante_Peninha)
        
class Cliente:
    clientes = []

    def __init__(self, nome, idade, peso, altura):
        self.nome   = nome
        self.idade  = idade
        self.peso   = peso
        self.altura = altura
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade}'
    
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'{cliente.nome} | {cliente.idade} anos')

cliente1 = Cliente('Osvaldo', '40','95', '1.85')

Cliente.listar_clientes()
class Contabancaria:
    contas = []

    def __init__(self,nome , id, saldo, ativo):
        self.nome = nome.title()
        self.id = id
        self.saldo = saldo
        self._ativo =  False
        Contabancaria.contas.append(self)
    
    def __str___(self):
        return f'{self.id} | {self.nome} | {self.saldo}'
    
    @classmethod
    def listar_contas(cls):
        print(f'{'Nome da conta'.ljust(33)} | {'Id'.ljust(33)} | {'Saldo'.ljust(33)} | {'Status'}')
        for conta in cls.contas:
            print(f'{conta.nome.ljust(33)} | {conta.id.ljust(33)} | {conta.saldo.ljust(33)} | {conta.ativo}')
    
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


conta1 = Contabancaria('leonardo kindermann mito campos', '01', '1.000.000.000','')
conta1.alternar_estado()
conta2 = Contabancaria('pedro lixo henrique', '02', '0', '')


Contabancaria.listar_contas()
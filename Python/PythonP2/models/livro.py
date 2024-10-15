
class Livro:

    livros = []

    def __init__(self,ano, titulo, autor, ativo):
        self._ano = ano
        self._titulo = titulo
        self._autor = autor
        self._ativo = False
        Livro.livros.append(self)

    def __str__(self):
        return f'O livro {self._titulo} de {self._autor} dos anos {self._ano}'

    @classmethod
    def listar_livros(cls):
        print(f'{'Nome do Livro'.ljust(33)} | {'Autor'.ljust(33)} |{'Status'}')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(33)} | {livro._autor.ljust(33)} | {livro._ativo}')

    @classmethod
    def verificar_disponibilidade(cls):
        ano_procurado = input('Digite o ano do livro que você procura: ')
        livros_encontrados = []
        for livro in cls.livros:
            if str(livro._ano) == ano_procurado:  # Comparando com o ano da instância
                livros_encontrados.append(livro)

        if livros_encontrados:
            print('Livros encontrados:')
            for livro in livros_encontrados:
                print(f'Título: {livro._titulo}, Autor: {livro._autor}, Ano: {livro._ano}')
        else:
            print('Livro não encontrado')

    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def emprestar_livro(self):
        self._ativo = not self._ativo          




    @property

    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'
    
    def emprestar_livro(self):
        self._ativo = not self._ativo



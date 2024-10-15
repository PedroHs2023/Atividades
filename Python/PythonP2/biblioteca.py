from models.livro import Livro

livro1 = Livro(2000, 'Alice no pais das maravilhas', 'Leonardo di caprio', '')
livro2 = Livro(2002, 'Branca de neve', 'Justim biber', '')
livro3 = Livro(2000, 'Rapunzel', 'Leonardo di caprio', '')
livro4 = Livro(2000, 'Chapeuzinho Vermelho', 'Leonardo di caprio', '')


    

def main():

    #livro1.emprestar_livro()
    Livro.verificar_disponibilidade()   
    #Livro.listar_livros()



if __name__ == '__main__':
    main()
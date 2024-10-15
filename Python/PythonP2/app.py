from models.restaurante import Restaurante

restaurante_praca       = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Leonardo',4)
restaurante_praca.receber_avaliacao('Lais',3)
restaurante_praca.receber_avaliacao('Francisco',5)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
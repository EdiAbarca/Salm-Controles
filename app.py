from modelos.restaurante import Restaurante

restaurante_praça = Restaurante('praça', 'Gourmet')
restaurante_praça.receber_avaliacao('Gui', 4)
restaurante_praça.receber_avaliacao('Lais', 8)
restaurante_praça.receber_avaliacao('Emy', 2)


def main():
    Restaurante.listar_restaurantes()





if __name__ == '__main__':
    main()
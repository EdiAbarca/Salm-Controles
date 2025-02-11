from modelos.avaliacao import Avaliacao

class Restaurante: 
    """Representa um restaurante e suas características."""
    restaurantes = []
    
    def __init__(self, nome, categoria): # metodo especial. a função init é um construtor da classe, que obriga que os atributos dentro dos parenteses sejam fornecidos para que sejam gravados.
        """
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        """ 
        self._nome = nome.title() # o .title define o valor retornado sempre com a primeira letra em maiuscula
        self._categoria = categoria.upper() # o .upper define o valor retornado sempre com todas as letras em maiuscula
        self._ativo = False #o ._ na variavel mantém o atributo privado, ou seja, não é esperado que o usuario acesse ele.
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    
    def __str__(self): # A função __str__ em uma classe Python é um método especial que permite definir uma representação em formato de string para os objetos dessa classe o self é a referencia da estancia atual que chama o atributo a que se refere
        """Retorna uma representação em string do restaurante."""
        return f' {self._nome}  |  {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        """Exibe uma lista formatada de todos os restaurantes."""
        print(f'{'Nome do Restaurante'.ljust(25)}  |  {'Categoria'.ljust(25)}  |  {'Avaliação'.ljust(25)}  |  {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)}  |  {restaurante._categoria.ljust(25)}  |  {str(restaurante.media_avaliacoes).ljust(25)}  |  {restaurante.ativo}')
    
    @property # O decorador @property em Python permite definir métodos que podem ser acessados como atributos, facilitando a encapsulação e melhorando a interface do código. Ele transforma uma função em um atributo de leitura.
    def ativo(self):
        """Retorna um símbolo indicando o estado de atividade do restaurante.""" 
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        """Alterna o estado de atividade do restaurante."""
        self._ativo = not self._ativo  

    def receber_avaliacao(self, cliente, nota):
        """
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        """
        if 0 < nota <= 5 : 
            avaliacao = Avaliacao(cliente, nota) 
            self._avaliacao.append(avaliacao)  

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações do restaurante."""    
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    




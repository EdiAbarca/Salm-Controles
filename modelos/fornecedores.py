class Fornecedores: 
    """Representa um fornecedor e suas características."""
    fornecedores_cadastrados = []
    
    def __init__(self, cnpj, razao_social, endereco_logradouro, endereco_numero, cidade, estado, telefone, email): # metodo especial. a função init é um construtor da classe, que obriga que os atributos dentro dos parenteses sejam fornecidos para que sejam gravados.
        """
        Inicializa uma instância de fornecedor.

        Parâmetros:
        - cnpj (str): O CNPJ do fornecedor.
        - razao_social (str): O nome do fornecedor.
        """ 
        self.cnpj = cnpj() 
        self.razao_social = razao_social.upper() # o .upper define o valor retornado sempre com todas as letras em maiuscula  
        self.endereco_logradouro = endereco_logradouro.title() # o .title define o valor retornado sempre com a primeira letra em maiuscula
        self.endereco_numero = endereco_numero()
        self.cidade = cidade.upper()
        self.estado = estado.upper()
        self.telefone = telefone()
        self.email = email()
        
        self._ativo = False #o ._ na variavel mantém o atributo privado, ou seja, não é esperado que o usuario acesse ele.
        self._avaliacao = []
        Fornecedores.fornecedores_cadastrados.append(self)

    def __str__(self): # A função __str__ em uma classe Python é um método especial que permite definir uma representação em formato de string para os objetos dessa classe o self é a referencia da estancia atual que chama o atributo a que se refere
        """Retorna uma representação em string do fornecedor."""
        return f' {self.cnpj}  |  {self.razao_social}  |  {self.endereco_logradouro}  |  {self.endereco_numero}  |  {self.cidade}  |  {self.estado}  |  {self.telefone}  |  {self.email}'    
    
    @classmethod
    def listar_fornecedores(cls):
        """Exibe uma lista formatada de todos os fornecedores."""
        print(f'{'CNPJ'.ljust(25)}  |  {'EMPRESA'.ljust(25)}  |  {'Endereço'.ljust(25)}  |  {'NUMERO'.ljust(25)}  |  {'CIDADE'.ljust(25)}  |  {'ESTADO'.ljust(25)}  |  {'TELEFONE'.ljust(25)}  |  {'EMAIL'}')
        for fornecedor in cls.fornecedores:
            print(f'{str(fornecedor.cnpj).ljust(25)}  |  {fornecedor.razao_social.ljust(25)}  |  {fornecedor.endereco_logradouro.ljust(25)}  |  {str(fornecedor.endereco_numero).ljust(25)}  |  {fornecedor.cidade.ljust(25)}  |  {fornecedor.estado.ljust(25)}  |  {str(fornecedor.telefone).ljust(25)}  |  {fornecedor.email}')
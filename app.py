from modelos.fornecedores import Fornecedores
from modelos.empenhos import Empenhos

def criar_fornecedor():
    """
    Função para criar um objeto da classe Fornecedores com base nas entradas do usuário.
    """
    print("\n--- Cadastro de Fornecedor ---")
    cnpj = input("CNPJ: ")
    nome = input("Nome: ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    complemento = input("Complemento: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla): ")
    cep = input("CEP: ")
    telefone = input("Telefone: ")
    email = input("Email: ")

    # Cria o objeto Fornecedores
    fornecedor = Fornecedores(
        cnpj=cnpj,
        nome=nome,
        logradouro=logradouro,
        numero=numero,
        complemento=complemento,
        bairro=bairro,
        cidade=cidade,
        estado=estado,
        cep=cep,
        telefone=telefone,
        email=email
    )

    print("\nFornecedor cadastrado com sucesso!")
    return fornecedor


def criar_empenho(fornecedor):
    """
    Função para criar um objeto da classe Empenhos com base nas entradas do usuário.
    """
    print("\n--- Cadastro de Empenho ---")
    numero_empenho = input("Número do Empenho (formato ANO+NE+sequência de seis números, ex: 2025NE000001): ")
    data_emissao = input("Data de Emissão (dd/mm/aaaa): ")
    itens_empenho = input("Itens do Empenho (separados por vírgula): ").split(",")
    quantidade_itens = list(map(int, input("Quantidade de cada item (separados por vírgula): ").split(",")))
    valor_unitario_itens = list(map(float, input("Valor Unitário de cada item (separados por vírgula): ").split(",")))
    natureza_despesa = input("Natureza de Despesa (formato 00.00.00): ")
    natureza_despesa_detalhada = input("Natureza de Despesa Detalhada (formato 00): ")
    solicitante = input("Solicitante: ")

    # Cria o objeto Empenhos
    empenho = Empenhos(
        numero_empenho=numero_empenho,
        data_emissao=data_emissao,
        cnpj_favorecido=fornecedor.cnpj,
        itens_empenho=itens_empenho,
        quantidade_itens=quantidade_itens,
        valor_unitario_itens=valor_unitario_itens,
        natureza_despesa=natureza_despesa,
        natureza_despesa_detalhada=natureza_despesa_detalhada,
        solicitante=solicitante
    )

    # Adiciona observações
    while True:
        observacao = input("Adicionar observação (ou deixe em branco para sair): ")
        if observacao.strip() == "":
            break
        empenho.adicionar_observacao(observacao)

    print("\nEmpenho cadastrado com sucesso!")
    return empenho


def main():
    """
    Função principal do programa.
    """
    print("Bem-vindo ao Sistema de Cadastro de Fornecedores e Empenhos!")

    # Cadastra um fornecedor
    fornecedor = criar_fornecedor()

    # Cadastra um empenho para o fornecedor
    empenho = criar_empenho(fornecedor)

    # Exibe os dados cadastrados
    print("\n--- Dados do Fornecedor ---")
    print(fornecedor)

    print("\n--- Dados do Empenho ---")
    print(empenho)


if __name__ == "__main__":
    main()
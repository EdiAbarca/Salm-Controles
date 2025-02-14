from datetime import datetime
from modelos.fornecedores import Fornecedores

class Empenhos:
    """
    Classe que representa um empenho, contendo informações como número do empenho, data de emissão,
    favorecido, itens do empenho, valores, status, observações, etc.
    """
    def __init__(self, numero_empenho, data_emissao, cnpj_favorecido, itens_empenho, quantidade_itens,
                 valor_unitario_itens, natureza_despesa, natureza_despesa_detalhada, solicitante):
        self.numero_empenho = numero_empenho
        self.data_emissao = data_emissao
        self.favorecido = self.buscar_favorecido(cnpj_favorecido)
        self.itens_empenho = itens_empenho
        self.quantidade_itens = quantidade_itens
        self.valor_unitario_itens = valor_unitario_itens
        self.valor_total_itens = self.calcular_valor_total_itens()
        self.valor_total_empenho = sum(self.valor_total_itens)
        self.valor_executado = 0.0
        self.valor_pendente = self.valor_total_empenho
        self.natureza_despesa = natureza_despesa
        self.natureza_despesa_detalhada = natureza_despesa_detalhada
        self.solicitante = solicitante
        self.status = "Pendente"
        self.observacoes = []

    def buscar_favorecido(self, cnpj):
        """
        Simula a busca de um fornecedor pelo CNPJ.
        """
        # Aqui, estamos criando um objeto Fornecedores fictício para simular a busca.
        return Fornecedores(
            cnpj=cnpj,
            nome="Fornecedor Exemplo Ltda",
            logradouro="Rua Exemplo",
            numero="123",
            complemento="Sala 456",
            bairro="Centro",
            cidade="São Paulo",
            estado="SP",
            cep="01234-567",
            telefone="(11) 9876-5432",
            email="contato@fornecedor.com"
        )

    def calcular_valor_total_itens(self):
        """
        Calcula o valor total de cada item multiplicando a quantidade pelo valor unitário.
        """
        return [quantidade * valor_unitario for quantidade, valor_unitario in zip(self.quantidade_itens, self.valor_unitario_itens)]

    def atualizar_status(self, valor_executado):
        """
        Atualiza o status do empenho com base no valor executado.
        """
        self.valor_executado += valor_executado
        self.valor_pendente = self.valor_total_empenho - self.valor_executado

        if self.valor_pendente == 0:
            self.status = "Recebido"
        elif self.valor_executado > 0:
            self.status = "Recebido Parcialmente"
        else:
            self.status = "Pendente"

    def adicionar_observacao(self, observacao):
        """
        Adiciona uma observação ao histórico de observações com a data de inserção.
        """
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.observacoes.append(f"{data_atual} - {observacao}")

    def __str__(self):
        """
        Retorna uma representação legível do objeto Empenhos.
        """
        return (
            f"Número do Empenho: {self.numero_empenho}\n"
            f"Data de Emissão: {self.data_emissao}\n"
            f"Favorecido: {self.favorecido.nome} (CNPJ: {self.favorecido.cnpj})\n"
            f"Itens do Empenho: {', '.join(self.itens_empenho)}\n"
            f"Valor Total do Empenho: R$ {self.valor_total_empenho:.2f}\n"
            f"Valor Executado: R$ {self.valor_executado:.2f}\n"
            f"Valor Pendente: R$ {self.valor_pendente:.2f}\n"
            f"Status: {self.status}\n"
            f"Observações: {', '.join(self.observacoes)}"
        )
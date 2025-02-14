class Fornecedores:
    """
    Classe que representa um fornecedor com informações de CNPJ, nome, endereço e contato.
    """
    def __init__(self, cnpj, nome, logradouro, numero, complemento, bairro, cidade, estado, cep, telefone, email):
        self.cnpj = cnpj
        self.nome = nome
        self.endereco = {
            'logradouro': logradouro,
            'numero': numero,
            'complemento': complemento,
            'bairro': bairro,
            'cidade': cidade,
            'estado': estado,
            'cep': cep
        }
        self.contato = {
            'telefone': telefone,
            'email': email
        }

    def __str__(self):
        endereco_formatado = (
            f"{self.endereco['logradouro']}, {self.endereco['numero']} {self.endereco['complemento']} - "
            f"{self.endereco['bairro']}, {self.endereco['cidade']}/{self.endereco['estado']}, {self.endereco['cep']}"
        )
        contato_formatado = f"Telefone: {self.contato['telefone']}, Email: {self.contato['email']}"
        return (
            f"Fornecedor: {self.nome}\n"
            f"CNPJ: {self.cnpj}\n"
            f"Endereço: {endereco_formatado}\n"
            f"Contato: {contato_formatado}"
        )
from pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome, sobrenome,endereco, telefone, email, genero):
        super().__init__(nome, sobrenome)
        self._endereco = endereco
        self._telefone = telefone
        self._email = email
        self._genero = genero

    def __str__(self):
        return f"Nome :{self._nome} {self._sobrenome}\nEndereco:{self._endereco}\nTelefone: {self._telefone}\nEmail: {self._email}\nGenero: {self._genero}"
    
    def contato(self):
        return f"Telefone: {self._telefone}\nEmail: {self._email}"
    
    def atualizar_endereco(self, endereco):
        self._endereco = endereco
        return f"Endereço atualizado para {self._endereco}"
    
    def to_dict(self):
        return {
            "nome": self._nome,
            "sobrenome": self._sobrenome,
            "endereco": self._endereco,
            "telefone": self._telefone,
            "email": self._email,
            "genero": self._genero
        }
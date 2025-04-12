class Pessoa:
    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome

    def __str__(self):
        return f"{self._nome} {self._sobrenome}"
    
    def get_nome(self):
        return self._nome
    
    def get_sobrenome(self):
        return self._sobrenome
    
    def nome_completo(self):
        return f"{self._nome} {self._sobrenome}"
    
    def saldar(self):
        return f"Olá, {self._nome} {self._sobrenome}!"
    
    
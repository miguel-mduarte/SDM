class Categoria:
    def __init__(self, nome, descricao):
        self._nome = nome
        self._descricao = descricao

    def __str__(self):
        return f"{self._nome}: {self._descricao}"
    
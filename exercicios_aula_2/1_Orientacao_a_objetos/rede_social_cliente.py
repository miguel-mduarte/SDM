from cliente import Cliente
from rede_social import RedeSocial

class RedeSocialCliente:
    def __init__(self, cliente: Cliente, redeSocial: RedeSocial):
        self._cliente = cliente
        self._redeSocial = redeSocial

    def __str__(self):
        return f"{self._cliente}\n{self._redeSocial}"
from cliente import Cliente


class Pedido:
    def __init__(self, preco_total, status, cliente: Cliente):
        self._preco_total = preco_total
        self.status = status
        self._cliente = cliente
        
    def __str__(self):
        return f"Preço total: {self._preco_total}\nStatus: {self.status}\nCliente: {self._cliente}"
    
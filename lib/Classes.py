class nodo():
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

    def __str__(self):
        return f'Valor: {self.valor}'

    def get_arbol(self):
        strOut = ""
        strOut += f'NP {self.valor}'
        if self.izq is not None:
            strOut += f'Iz[{self.valor}]->[{self.izq.valor}]'
        if self.der is not None:
            strOut += f'Dr[{self.valor}]->[{self.der.valor}]'
        return strOut


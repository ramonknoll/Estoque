class Almoxarifado:
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []

    def adicionar(self, produto):
        self.produtos.append(produto)

    def contar_em_falta(self):
        total = 0 

        for p in self.produtos:
            if p.situacao() == "Em falta":
                total += 1
                
        return total
from produtos.almoxarifado import Almoxarifado

almox = Almoxarifado()

p = almox.buscar("P002")
print(p.nome, p.quantidade)
print(almox.buscar("P999"))

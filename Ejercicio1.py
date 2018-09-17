__author__ = 'Leonel Gonzalez'


from Ejercicio import *

otralista = []
supermercado = ['fruta','agua', 'refresco', 'pan', 'pastel']
estructuradedatos = ['agustin pimentel', 'francisco pineda', 'enrique bello']
precios = [12, 34, 45, 47]
porcentajes = [.34, .56, .12, 1.2]

listas = memDinamica(supermercado)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.agregarelementoarray('cerveza')
listas.imprimirLista()

lista2 = memDinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(89)
lista2.imprimirLista()
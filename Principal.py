__author__='Kevin Alonso'

from MemoriaDinamica import *
lista = []
papeleria = ['cuaderno','lapiz', 'goma', 'regla', 'tijera']
precios = [10, 5, 6, 6, 8]

listas = MemoriaDinamica(papeleria)
listas.imprimirLista()
listas.ordenarLista()
listas.imprimirLista()
listas.recorrerArreglo()
listas.imprimirLista()
listas.agregarelementoarray('colores')
listas.imprimirLista()
listas.eliminarElemento('cuaderno')
listas.imprimirLista()
papeleria.pop(2)
listas.imprimirLista()
listas.insertarNPosicion(3, 'Corrector')
listas.imprimirLista()
lista2 = MemoriaDinamica(precios)
lista2.imprimirLista()
lista2.agregarelementoarray(15)
lista2.imprimirLista()



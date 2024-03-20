from lib import *
print(Archivo,numero,Rojo)
print('--------------------------------------------------------------------------')
print("Árbol Extensión:")
print_arbol(arbol)
print()
print('--------------------------------------------------------------')
print("Recorrido InOrder:")
print(LVR(arbol))
print()

print("Recorrido PreOrder:")
print(VLR(arbol))
print()

print("Recorrido PostOrder:")
print(LRV(arbol))
print()

print('--------------------------------------------------------------------------------------')
print("Arbol Ordenado")
print(Ordenado(arbol))



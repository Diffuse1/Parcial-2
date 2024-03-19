from lib import *
imprimir ()
print('--------------------------------------------------------------------------')
print("Árbol ordenado:")
print_arbol(arbol)
print()

print("Recorrido InOrder:")
print(LVR(arbol))
print()

print("Recorrido PreOrder:")
print(VLR(arbol))
print()

print("Recorrido PostOrder:")
print(LRV(arbol))
print()


print("Arbol Ordenado")
print(arbol)
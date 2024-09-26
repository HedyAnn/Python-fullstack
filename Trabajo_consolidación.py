# Ejercicio de consolidación

lista_nombres={
    "magos": ['Harry Houdini', 'David Blaine', 'Teller'],
    "cientificos":['Newton','Hawking','Einstein'],
    "otros": ['Messi','Pele','Juanes']
}

def imprimir_nombres(lista):
    for categoria, nombres in lista.items():
        for nombre in nombres:
            print(nombre)
print("NOMBRES SIN MODIFICAR:")
imprimir_nombres(lista_nombres)

def hacer_grandioso(lista):
    lista["magos"] = [f"El gran {mago}" for mago in lista["magos"]]

hacer_grandioso(lista_nombres)

print("\nNOMBRES MODIFICADOS:")
imprimir_nombres(lista_nombres)
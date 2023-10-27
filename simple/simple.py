import random

# Creo la lista de diccionarios con la funcion random
def simple_list():
    lista_de_diccionarios = []
    for i in range(10):
        diccionario = {
            "id": i + 1,
            "age": random.randint(1, 100) 
        }
        lista_de_diccionarios.append(diccionario)
    return lista_de_diccionarios

# Ordeno por edad en orden ascendente
def sort_list(dicts):
    return sorted(dicts, key=lambda x: x["age"])
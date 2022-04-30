
def fill():
    list = []
    size = int(input("Ingrese la longitud de la lista: "))
    for i in range(1, size + 1):
        data = input("Ingrese el dato número {0} de la lista: ".format(i))
        list.append(data)
    return list

def invert(list):
    new_list = []
    for i in list:
        new_list.insert(0, i)
    return new_list

list = fill()

print("La lista original es:\n", list)
print("La lista invertida es:\n", invert(list))

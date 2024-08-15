# Creación e inicialización de la lista
my_list = []  # Inicializamos una lista vacía

print("Lista inicial:", my_list)  # Imprimimos la lista inicial (vacía)

# Agregación de elementos
my_list.append(1)  # Agregamos un nuevo elemento al final de la lista
my_list.append(2)  # Agregamos otro elemento
my_list.append(3)  # Agregamos otro elemento

print("Después de agregar elementos:", my_list)  # Imprimimos la lista después de agregar elementos

# Inserción de un elemento en una posición específica
my_list.insert(1, 1.5)  # Insertamos el valor 1.5 en la posición 1

print("Después de la inserción:", my_list)  # Imprimimos la lista después de la inserción

# Eliminación de un elemento
my_list.remove(2)  # Eliminamos la primera aparición del valor 2

print("Después de la eliminación del 2:", my_list)  # Imprimimos la lista después de eliminar el elemento

# Eliminación del último elemento
removed_element = my_list.pop()  # Eliminamos y obtenemos el último elemento

print("Elemento eliminado con pop:", removed_element)  # Imprimimos el elemento eliminado
print("Lista después de pop:", my_list)  # Imprimimos la lista después de la operación pop

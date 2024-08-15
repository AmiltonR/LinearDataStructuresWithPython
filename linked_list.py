class Node:
    def __init__(self, data):
        self.data = data  # Dato almacenado en el nodo
        self.next = None  # Puntero al siguiente nodo en la lista


class LinkedList:
    def __init__(self):
        self.head = None  # Inicialmente, la lista está vacía (no tiene nodos)

    def append(self, data):
        new_node = Node(data)  # Crear un nuevo nodo con el dato proporcionado

        if self.head is None:  # Si la lista está vacía
            self.head = new_node  # El nuevo nodo es ahora la cabeza de la lista
        else:
            current = self.head
            while current.next:  # Iterar hasta el último nodo de la lista
                current = current.next
            current.next = new_node  # Enlazar el último nodo al nuevo nodo

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_after(self, prev_data, new_data):
        current = self.head

        # Buscar el nodo que contiene prev_data
        while current and current.data != prev_data:
            current = current.next

        if current is None:
            print("El nodo con el dato proporcionado no existe.")
            return

        new_node = Node(new_data)
        new_node.next = current.next
        current.next = new_node

    def delete(self, key):
        current = self.head
        previous = None

        while current and current.data != key:
            previous = current
            current = current.next

        if current is None:  # El dato no se encontró en la lista
            print("El nodo con el dato proporcionado no existe.")
            return

        if previous is None:  # El nodo a eliminar es la cabeza
            self.head = current.next
        else:
            previous.next = current.next


# Uso de la lista enlazada
ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Output: 1 -> 2 -> 3 -> None

# Insertar después de un nodo específico
ll.insert_after(2, 4)
ll.display()  # Output: 1 -> 2 -> 4 -> 3 -> None

# Eliminar un nodo
ll.delete(3)
ll.display()  # Output: 1 -> 2 -> 4 -> None

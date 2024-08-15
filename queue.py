# Implementación de una cola usando una lista
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)  # Agrega el elemento al final de la cola

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Elimina y retorna el primer elemento de la cola
        else:
            return None  # Retorna None si la cola está vacía

    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # Retorna el primer elemento sin eliminarlo
        else:
            return None  # Retorna None si la cola está vacía

    def size(self):
        return len(self.queue)  # Retorna el tamaño de la cola

    def display(self):
        print(self.queue)  # Imprime la cola


# Ejemplo de uso
if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Cola después de encolar elementos:")
    q.display()

    print("Primer elemento en la cola (peek):", q.peek())

    print("Elemento desencolado:", q.dequeue())
    print("Cola después de desencolar un elemento:")
    q.display()

    print("Tamaño de la cola:", q.size())

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# Ejemplo de uso
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Pila después de los push:", stack.stack)
    print("Elemento en la cima:", stack.peek())
    print("Tamaño de la pila:", stack.size())
    print("Elemento extraído con pop:", stack.pop())
    print("Pila después del pop:", stack.stack)
    print("¿La pila está vacía?", stack.is_empty())

class NodoCola:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Cola:
    def __init__(self):
        self.frente = None
        self.final = None
        self.tamanio = 0

    def agregar(self, dato):
        nodo = NodoCola(dato)
        if self.frente is None:
            self.frente = nodo
        else:
            self.final.siguiente = nodo
        self.final = nodo
        self.tamanio += 1

    def apartar_actualizar(self):
        if not self.cola_vacia():
            dato = self.frente.dato
            if self.frente == self.final:
                self.frente = None
                self.final = None
            else:
                self.frente = self.frente.siguiente
            self.tamanio -= 1
            return dato
        else:
            return None

    def cola_vacia(self):
        return self.frente is None

    def en_frente(self):
        if not self.cola_vacia():
            return self.frente.dato
        else:
            return None

    def tamanio(self):
        return self._tamanio

    def mostrar_cont_2(self):
        if self.cola_vacia():
            print("La cola está vacía")
            return
        actual = self.frente
        while True:
            print(actual.dato, end=' ')
            actual = actual.siguiente
            if actual == self.frente:
                break
        print()

    def mostrar_cont(self):
        if not self.cola_vacia():
            aux = self.frente
            while True:
                print(aux.dato)
                aux = aux.siguiente
                if aux == self.frente:
                    break
        else:
            print("La cola está vacía")

# Ejemplo de uso
#cola = Cola()
#cola.agregar(1)
#cola.agregar(2)
#cola.agregar(3)

#print("Elemento en frente:", cola.en_frente())
#print("Tamaño de la cola:", cola.tamanio())
#print("Desapartar elemento:", cola.apartar_actualizar())
#print("Tamaño de la cola después de desapartar:", cola.tamanio())
#cola.mostrar_cont()
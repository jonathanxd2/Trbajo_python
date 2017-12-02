class listausuarios:
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def add(self, objeto):
        nuevoNodo = _usuarioNodo(objeto)
        nuevoNodo.next = self._head
        self._head = nuevoNodo
        self._size += 1

    def _busca( self, target):
        curNode = self._head
        while curNode is not None and curNode.id != target :
            curNode =curNode.next
        return curNode


    def __iter__(self):
        return _listaiterator(self._head)

class _usuarioNodo(object):
    def __init__(self,objeto):
        self.id = objeto.id
        self.name= objeto.name
        self.fecha = objeto.fecha
        self.amistades = None
        self.fotos = None
        self.next = None

class _listaiterator:
    def __init__(self, listahead):
        self._curNode = listahead

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNode is None:
            raise StopIteration
        else:
            nodo = self._curNode
            self._curNode =self._curNode.next
            return nodo


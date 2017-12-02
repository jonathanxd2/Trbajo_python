class listaamistad:
    def __init__(self):
        self._head = None
        self._size = 0
    def __len__(self):
        return self._size

    def add(self, objeto,fecha):
        nuevoNodo = _amistadNodo(objeto,fecha)
        nuevoNodo.next = self._head
        self._head = nuevoNodo
        self._size += 1

    def __iter__(self):
        return _listaiterator(self._head)

    def _busca( head, target):
        curNode = head
        while curNode is not None and curNode._usuario.id != target :
            curNode =curNode.next
        return curNode


class _amistadNodo(object):
    def __init__(self,usuario,fecha):
        self._usuario = usuario
        self._fecha = fecha
        self._next = None


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

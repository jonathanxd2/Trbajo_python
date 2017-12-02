class FotosFileReader:

    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputfile = None

    def open(self):
        self._inputfile = open(self._inputSrc, "r")

    def close(self):
        self._inputfile.close()
        self._inputfile = None

    def buscaTodos(self):
        listaFotos=list()
        foto = self.buscaFoto()
        while foto != None:
            listaFotos.append(foto)
            foto = self.buscaFoto()
        return listaFotos

    def buscaFoto(self):
        linea = self._inputfile.readline()
        if linea == "" :
            return None
        foto = FotoRecord()
        foto.fecha = linea.strip()
        foto.url = self._inputfile.readline().strip()
        foto.idSubio=int(self._inputfile.readline())
        foto.cant = int(self._inputfile.readline())
        listaE = list()
        for i in range(foto.cant):
            codigo = int(self._inputfile.readline() )
            listaE.append(codigo)
        foto.listaEtiquet=listaE
        return foto

class FotoRecord:
    def __init__(self):
        self.fecha = None
        self.url = None
        self.idSubio = 0
        self.cant = 0
        self.listaEtiquet = None
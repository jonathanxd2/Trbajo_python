class AmistadesFileReader:

    def __init__(self, inputSrc):
        self._inputSrc = inputSrc
        self._inputfile = None

    def open(self):
        self._inputfile = open(self._inputSrc, "r")

    def close(self):
        self._inputfile.close()
        self._inputfile = None

    def buscaTod(self):
        listaAmig=list()
        amistad = self.buscaReg()
        while amistad != None:
            listaAmig.append(amistad)
            amistad  = self.buscaReg()
        return listaAmig

    def buscaReg(self):
        linea = self._inputfile.readline()
        if linea == "" :
            return None
        amigo = AmigoRecord()
        amigo.idAmio = int(linea)
        amigo.idAmio2 = int(self._inputfile.readline())
        amigo.fecha=self._inputfile.readline().strip()
        return amigo

class AmigoRecord:
    def __init__(self):
        self.idAmio = 0
        self.idAmio2 = 0
        self.fecha = None
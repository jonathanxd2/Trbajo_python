class UsuarioFileReader:
    #Crea una nueva instancia del estudiante
    def __init__(self, inpsrc):
        self._inpsrc=inpsrc
        self._inputfile =None

    def open(self):
        self._inputfile = open(self._inpsrc, "r")

    def close(self):
        self._inputfile.close()
        self._inputfile = None

    def buscaTod(self):
        listaUsu=list()
        usuario = self.buscaReg()
        while usuario != None:
            listaUsu.append(usuario)
            usuario  = self.buscaReg()
        return listaUsu

    def buscaReg(self):
        linea = self._inputfile.readline()
        if linea == "" :
            return None
        usuario = Usuario()
        usuario.id = int(linea)
        usuario.name = self._inputfile.readline().strip()
        usuario.fecha=self._inputfile.readline().strip()
        return usuario

class Usuario:
    def __init__(self):
        self.id =0
        self.name = None
        self.fecha = None




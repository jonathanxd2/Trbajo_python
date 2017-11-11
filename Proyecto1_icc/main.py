class ListaAmigos:
    def __init__(self):
        self.prim=None
        self.ulti=None
        self.len=None

class ListaUsuarios:
    def __init__(self):
        self.prim =None
        self.ulti =None
        self.len = None
class Amistad:
    def __init__(self,usuario,fechaIni):
        self.fechaIni =fechaIni
        self.usario = usuario


class NodoAmigo:
    def __init__(self, amigo):
        self.amigo = amigo
        self.next = None
class Fecha:
    def __init__(self,dia,mes,anio):
        self.dia=dia
        self.mes=mes
        self.anio=anio

class  Usuario:
    def __init__(self,codigo,nombre,fecha):
        self.codigo = codigo
        self.nombre = nombre
        self.dia = fecha.dia
        self.mes = fecha.mes
        self.anio = fecha.anio
        #lista de amistades
        #lista de fotos


    def __str__(self):
        return (self.codigo)

class Foto:
    def __init__(self,fecha, url, etiquetas):
        self.fecha = self.fecha
        self.url = url
        self.etiquetas =etiquetas



with open('usuarios.txt', 'r') as myfile:
    codigo = myfile.readline()
    nombre = myfile.readline().replace('\n', '')
    dia,mes,anio = myfile.readline().split()
    fecha = Fecha(dia,mes,anio)
    usr1 = Usuario(codigo,nombre,fecha)


with open('fotos.txt', 'r') as myfile:

    dia,mes,anio = myfile.readline().split()
    fecha = Fecha(dia,mes,anio)
    url = myfile.readline()

    usr1 = Usuario(codigo,nombre,fecha)



print(codigo)
print(nombre)
print()
print(dia,mes,anio)
print()
print(usr1)


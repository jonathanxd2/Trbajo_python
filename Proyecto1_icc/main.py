class ListaAmigos:
    def __init__(self):
        self.prim=None
        self.ulti=None
        self.len=None

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





def main():

    with open('usuarios.txt', 'r') as myfile:
        codigo = myfile.readline()
        nombre = myfile.readline().replace('\n', '')
        dia,mes,anio = myfile.readline().split()
        fecha = Fecha(dia,mes,anio)
        usr1 = Usuario(codigo,nombre,fecha)

    print(codigo)
    print(nombre)
    print(dia,mes,anio)
    print(usr1)



    

if __name__ == '__main__':
    main()
from usuariofile import UsuarioFileReader
from amistadesFile import AmistadesFileReader
from fotosFile import FotosFileReader
def main():

    FILEN = "usuarios.txt"
    readerUsu = UsuarioFileReader(FILEN)
    readerUsu.open()
    usuarioListUsu = readerUsu.buscaTod()
    readerUsu.close()
    #printReport(usuarioListUsu)

    print("-----------------------------------------------")
    FILEAMISTAD = "amistades.txt"
    readerAmistad = AmistadesFileReader(FILEAMISTAD)
    readerAmistad.open()
    amistadlistaDeAmi = readerAmistad.buscaTod()
    readerAmistad.close()
    # printAmistad(amistadlistaDeAmi)


    FILEFOTO = "fotos.txt"
    readerFoto = FotosFileReader(FILEFOTO)
    readerFoto.open()
    fotoslistaDeFotos = readerFoto.buscaTodos()
    readerFoto.close()
    #printFotos(fotoslistaDeFotos)


    while 1:

        id = int(input("Elige el Usuario: "))

        for usu in usuarioListUsu:
            if usu.id == id :
                usuario = usu


        print("*ID:", usuario.id)
        print("*Nombre:",usuario.name)
        print("*Fecha Nacimiento:",usuario.fecha)
        print("*Fotos:")
        for foto in fotoslistaDeFotos:
            if (foto.idSubio == usuario.id):
                foto = foto
                print(foto.fecha+", ", end='')
                print(foto.url+",", end='')
                print(" Etiquetados:", end='')
                lista = foto.listaEtiquet
                for i in range(foto.cant):
                    print(foto.listaEtiquet[i],",",end='')
                print()
        print("*Amistaades:")
        for amigo in amistadlistaDeAmi:
            if (amigo.idAmio == usuario.id):
                amigo = amigo
                print(amigo.fecha,",","ID:" ,amigo.idAmio2)
            if (amigo.idAmio2 == usuario.id):
                amigo = amigo
                print(amigo.fecha,",","ID:" ,amigo.idAmio)
        print()
        input("Presione Enter para continuar...")

        print("-----------------------------------------------------")

def printAmistad(theList):
    for record in theList:
        print(record.idAmione)
        print(record.idAmitwo)
        print(record.fecha)


def printReport(theList):
    for record in theList:
        print(record.id)
        print(record.name)
        print(record.fecha)
    print("-"*10)

def printFotos(lista):
    for foto in lista:
        print(foto.fecha)
        print(foto.url)
        print(foto.idSubio)
        print(foto.cant)
        for i in foto.listaEtiquet:
            print(i)
        print()
main()
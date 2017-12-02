from usuariofile import UsuarioFileReader
from amistadesFile import AmistadesFileReader
from fotosFile import FotosFileReader
from listaUsuarios import listausuarios
from listaAmistad import listaamistad

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


#----------------------------------------------------------
    listaUsu = listausuarios()
    for elem in usuarioListUsu:
        listaUsu.add(elem)

    for elemento in listaUsu:
        print(elemento.name)
#------------------------------------------------------------
    for amistad in amistadlistaDeAmi:
        #busca amistad 1 , agrega amistad 2 asu lista de amistad vacia

        listaAmis1 =listaamistad()
        usuario1 = listaUsu._busca(amistad.idAmio)
        usuario2 = listaUsu._busca(amistad.idAmio2)

        if usuario1.amistades == None :
            usuario1.amistades = listaAmis1
            usuario1.amistades.add(usuario2,amistad.fecha)
        else:
            usuario1.amistades.add(usuario2, amistad.fecha)


        #ahora agregamos al usuario 1, en la lista del amigo 2
        listaAmis2 =listaamistad()
        if usuario2.amistades == None :
            usuario2.amistades = listaAmis2
            usuario2.amistades.add(usuario1,amistad.fecha)
        else:
            usuario2.amistades.add(usuario1, amistad.fecha)



    for elemento in listaUsu:
        print(elemento.name)
        print(elemento.amistades._h)






                #nodo=listaUsu._busca(125)
    #print(nodo.name)

if __name__ == '__main__':
    main()

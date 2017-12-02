from tkinter import *


from usuariofile import UsuarioFileReader
from amistadesFile import AmistadesFileReader
from fotosFile import FotosFileReader
from listaUsuarios import listausuarios
from listaAmistad import listaamistad

#
#
#ESTE ES EL MAIN PRINCIPAL, AQUI SE TIENE QUE DAR COMPILAR Y APARECERA EL ENTORNO GRAFICO
#
#
#
#

app = Tk()
app.geometry("700x500+300+100")
app.title("Red Social")

app.columnconfigure(0, weight=40)
app.rowconfigure(0, weight=40)

valor = ""
entrada_texto = Entry(app, width=10, textvariable=valor)
entrada_texto.place(x=100, y=90)


def abrirfoto():
    imgBoton = PhotoImage(file="demilovato.png")
    lblImagen.Imagen = Label(app, image=imgBoton).place(x=385, y=150)


def hacer_click():


    listaUsu = listausuarios()
    for elem in usuarioListUsu:
        listaUsu.add(elem)

   # for elemento in listaUsu:
    #    print(elemento.name)
        # ------------------------------------------------------------
    for amistad in amistadlistaDeAmi:
        # busca amistad 1 , agrega amistad 2 asu lista de amistad vacia

        listaAmis1 = listaamistad()
        usuario1 = listaUsu._busca(amistad.idAmio)
        usuario2 = listaUsu._busca(amistad.idAmio2)

        if usuario1.amistades == None:
            usuario1.amistades = listaAmis1
            usuario1.amistades.add(usuario2, amistad.fecha)
        else:
            usuario1.amistades.add(usuario2, amistad.fecha)

        # ahora agregamos al usuario 1, en la lista del amigo 2
        listaAmis2 = listaamistad()
        if usuario2.amistades == None:
            usuario2.amistades = listaAmis2
            usuario2.amistades.add(usuario1, amistad.fecha)
        else:
            usuario2.amistades.add(usuario1, amistad.fecha)







    try:


        _valor = int(entrada_texto.get())

        if not (listaUsu.__contains__(_valor)):
            etiquetanom.config(text="Usuario no existente")
        else:
            usuario = listaUsu._busca(_valor)




        # print("*ID:", usuario.id)
        # print("*Nombre:", usuario.name)
        # print("*Fecha Nacimiento:", usuario.fecha)
        # print("*Fotos:")
        etiquetanom.config(text=usuario.name)
        etiquetafecha.config(text=usuario.fecha)

        for foto in fotoslistaDeFotos:
            z = 0
            if (foto.idSubio == usuario.id):
                foto = foto
                # print(foto.fecha + ", ", end='')
                lstFotos.insert(z, foto.fecha)

                # print(foto.url + ",", end='')
                # print(" Etiquetados:", end='')
                lstFotos.insert(z, foto.url)
                #m = 0
                # if foto.url != "":
                #   botonabrirfotos = Button(app, text="Abrir foto", command=abrirfoto, bg="pink")
                #  botonabrirfotos.place(x= 280, y=m+200)
                # m=m+20
                lstFotos.insert(z, "Etiquetados:")
                lista = foto.listaEtiquet
                z = z + 1
                for i in range(foto.cant):
                    # print(foto.listaEtiquet[i], ",", end='')
                    lstFotos.insert(z, foto.listaEtiquet[i])
                    z = z + 1
                print()

        # print("*Amistaades:")



        for elem in listaUsu:

                if elem.id == _valor:

                    for amistad in elem.amistades:
                        lstAmigos.insert(0, "Fecha de inicio de amistad: ")
                        lstAmigos.insert(1, amistad._usuario.fecha)
                        lstAmigos.insert(2,"ID:")
                        lstAmigos.insert(3, amistad._usuario.id, "")




    except ValueError:
        etiquetanom.config(text="Error")


def refresh():
    etiquetanom.config(text=" ")
    etiquetafotos.config(text=" ")
    etiquetafecha.config(text=" ")
    lstAmigos.delete(0, END)
    lstFotos.delete(0, END)
    imgBoton = PhotoImage(file="blanco.png")
    lblImagen.Imagen = Label(app, image=imgBoton).place(x=385, y=150)


def ventanados():
    app.withdraw()
    win = Toplevel()
    win.geometry("750x500")
    imgBoton = PhotoImage(file="foto_red_social.png")
    lblImagen.Imagen = Label(win, image=imgBoton).place(x=80, y=0)
    botonjon = Button(app, text="Regresar", bg="pink")
    botonjon.place(x=740, y=50)


FILEN = "usuarios.txt"
readerUsu = UsuarioFileReader(FILEN)
readerUsu.open()
usuarioListUsu = readerUsu.buscaTod()
readerUsu.close()

FILEAMISTAD = "amistades.txt"
readerAmistad = AmistadesFileReader(FILEAMISTAD)
readerAmistad.open()
amistadlistaDeAmi = readerAmistad.buscaTod()
readerAmistad.close()

FILEFOTO = "fotos.txt"
readerFoto = FotosFileReader(FILEFOTO)
readerFoto.open()
fotoslistaDeFotos = readerFoto.buscaTodos()
readerFoto.close()

imgBoton = PhotoImage(file="blanco.png")
lblImagen = Label(app, image=imgBoton).place(x=385, y=150)

nombre = PhotoImage(file="prueba.png")
lblNombre = Label(app, image=nombre).place(x=180, y=0)

etiquetanom = Label(app, text="")
etiquetanom.place(x=100, y=120)

etiquetafotos = Label(app, text="")
etiquetafotos.place(x=100, y=180)

lstAmigos = Listbox(app, width=40, height=7)
lstAmigos.place(x=110, y=320)
lstAmigos.insert(0, "")

lstFotos = Listbox(app, width=25, height=7)
lstFotos.place(x=110, y=185)
lstFotos.insert(0, "")

etiquetafecha = Label(app, text="")
etiquetafecha.place(x=150, y=150)

etiqueta2 = Label(app, text="Usuario: ")
etiqueta2.place(x=30, y=90)

etiqueta3 = Label(app, text="Nombre: ")
etiqueta3.place(x=30, y=120)

etiqueta4 = Label(app, text="Fotos: ")
etiqueta4.place(x=30, y=180)

etiqueta5 = Label(app, text="Amigos: ")
etiqueta5.place(x=30, y=310)

etiqueta6 = Label(app, text="Diseño del trabajo ")
etiqueta6.place(x=30, y=450)

etiqueta7 = Label(app, text="Fecha de Nacimiento:")
etiqueta7.place(x=30, y=150)

boton = Button(app, text="Buscar", command=hacer_click, bg="pink")
boton.place(x=180, y=85)

botonfotos = Button(app, text="Abrir foto", command = abrirfoto, bg="pink")
botonfotos.place(x=280, y=185)

botonrefresh = Button(app, text="Refresh", command=refresh, bg="pink")
botonrefresh.grid(column=1, row=7)

botondiseno = Button(app, text="Abrir diseño", bg="pink", command=ventanados)
botondiseno.place(x=150, y=450)

app.mainloop()
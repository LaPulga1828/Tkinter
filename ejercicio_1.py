# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import PhotoImage



# ------------------
# ventana principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#establecer tamaño de la ventana
ventana_principal.geometry('805x405')

#titulo de la ventana
ventana_principal.title("JkAnime")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#<clolor de fondode la ventana principal
ventana_principal.config(bg="darkorchid4")

#Agrgamos un widget a la ventana principal
letrero=Label(text="\nLa mejor pagina para Ver Anime Online Gratis\n",bg="darkorchid4")
letrero.pack()

#Agrgamos un widget a la ventana principal
letrero2=Label(text="\nLaPulga1828\n",bg="darkorchid4")
letrero2.pack()

#Agrgamos un widget a la ventana principal
letrero2=Label(text="\nmira los ultimos capitulos de los animes del momento sin ninguna restriccion\n",bg="darkorchid4")
letrero2.pack()

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).Cada accion del usuario se conoce como un evento.El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()



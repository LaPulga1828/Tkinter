# se importa la librería tkinter con todas sus funciones
from tkinter import *
from tkinter import PhotoImage



# ------------------
# ventana principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#establecer tamaño de la ventana
ventana_principal.geometry('800x500')

#titulo de la ventana
ventana_principal.title("JkAnime")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#clolor de fondode la ventana principal
ventana_principal.config(bg="darkorchid4")

#-----------------
# Frame entrada
#-----------------

Frame_entrada=Frame(ventana_principal)
Frame_entrada.config(bg='yellow',width=780 ,height=240 )
Frame_entrada.place(x=10,y=10)

Frame_operaciones=Frame(ventana_principal)
Frame_operaciones.config(bg='blue',width=780 ,height=120 )
Frame_operaciones.place(x=10,y=250)

Frame_soluciones=Frame(ventana_principal)
Frame_soluciones.config(bg='red',width=780 ,height=120)
Frame_soluciones.place(x=10,y=370)

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).Cada accion del usuario se conoce como un evento.El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()



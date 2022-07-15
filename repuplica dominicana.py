# se importa la librería tkinter con todas sus funciones
from tkinter import *

# ------------------
# ventana principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#establecer tamaño de la ventana
ventana_principal.geometry('800x500')

#titulo de la ventana
ventana_principal.title("Republica dominicana")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#clolor de fondode la ventana principal
ventana_principal.config(bg="darkorchid4")

#-----------------
# Frame entrada
#-----------------

Frame_entrada=Frame(ventana_principal)
Frame_entrada.config(bg='blue',width=390,height=240 )
Frame_entrada.place(x=10,y=10)

Frame_entrada=Frame(ventana_principal)
Frame_entrada.config(bg='red',width=390,height=240 )
Frame_entrada.place(x=10,y=240)

Frame_entrada=Frame(ventana_principal)
Frame_entrada.config(bg='red',width=390,height=240 )
Frame_entrada.place(x=390,y=10)

Frame_entrada=Frame(ventana_principal)
Frame_entrada.config(bg='blue',width=390,height=240 )
Frame_entrada.place(x=390,y=240)


Frame_entrada=Frame(ventana_principal)
Frame_entrada.config(bg='white',width=100,height=470 )
Frame_entrada.place(x=340,y=10)

Frame_entrada=Frame(ventana_principal)
Frame_entrada.config(bg='white',width=780,height=100 )
Frame_entrada.place(x=10,y=190)


# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).Cada accion del usuario se conoce como un evento.El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()



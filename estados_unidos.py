# se importa la librería tkinter con todas sus funciones
from tkinter import *

# ------------------
# ventana principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#establecer tamaño de la ventana
ventana_principal.geometry('840x540')

#titulo de la ventana
ventana_principal.title("Estados unidos")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#clolor de fondode la ventana principal
ventana_principal.config(bg="darkorchid4")

#-----------------
# Frame entrada
#-----------------

Frame_franjas1=Frame(ventana_principal)
Frame_franjas1.config(bg='red',width=820,height=40)
Frame_franjas1.place(x=10,y=10)

Frame_franjas2=Frame(ventana_principal)
Frame_franjas2.config(bg='white',width=820,height=40)
Frame_franjas2.place(x=10,y=50)

Frame_franjas3=Frame(ventana_principal)
Frame_franjas3.config(bg='red',width=820,height=40)
Frame_franjas3.place(x=10,y=90)

Frame_franjas4=Frame(ventana_principal)
Frame_franjas4.config(bg='white',width=820,height=40)
Frame_franjas4.place(x=10,y=130)

Frame_franjas5=Frame(ventana_principal)
Frame_franjas5.config(bg='red',width=820,height=40)
Frame_franjas5.place(x=10,y=170)

Frame_franjas6=Frame(ventana_principal)
Frame_franjas6.config(bg='white',width=820,height=40)
Frame_franjas6.place(x=10,y=210)

Frame_franjas7=Frame(ventana_principal)
Frame_franjas7.config(bg='red',width=820,height=40)
Frame_franjas7.place(x=10,y=250)

Frame_franjas8=Frame(ventana_principal)
Frame_franjas8.config(bg='white',width=820,height=40)
Frame_franjas8.place(x=10,y=290)


Frame_franjas9=Frame(ventana_principal)
Frame_franjas9.config(bg='red',width=820,height=40)
Frame_franjas9.place(x=10,y=330)

Frame_franjas10=Frame(ventana_principal)
Frame_franjas10.config(bg='white',width=820,height=40)
Frame_franjas10.place(x=10,y=370)

Frame_franjas11=Frame(ventana_principal)
Frame_franjas11.config(bg='red',width=820,height=40)
Frame_franjas11.place(x=10,y=410)

Frame_franjas12=Frame(ventana_principal)
Frame_franjas12.config(bg='white',width=820,height=40)
Frame_franjas12.place(x=10,y=450)

Frame_franjas13=Frame(ventana_principal)
Frame_franjas13.config(bg='red',width=820,height=40)
Frame_franjas13.place(x=10,y=490)

Frame_franjas13=Frame(ventana_principal)
Frame_franjas13.config(bg='blue',width=410.5,height=280)
Frame_franjas13.place(x=10,y=10)




# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).Cada accion del usuario se conoce como un evento.El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()

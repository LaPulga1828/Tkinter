# se importa la librería tkinter con todas sus funciones
from curses.textpad import Textbox
from os import pread
from tkinter import *
from tkinter import messagebox
from turtle import width

#---------------
#Funciones de la app
#-------------------

def sumar():
    #messagebox.showinfo("suma 1.0","Hizo click en el boton de sumar")
    c=int(a.get())+ int(b.get())
    T_resultados.insert(INSERT," la suma de " + a.get() + " + " + b.get() + " es igual " + str(c) + "\n")

def borrar():
    messagebox.showinfo("SUMA  1.0","Los datos seran borrados...")
    a.set("")
    b.set("")
    T_resultados.delete("1.0","end")



def salir():
    messagebox.showinfo("Suma1.0","La app se cerrara...")
    ventana_principal.destroy()

# ------------------
# ventana principal
# ------------------

# se declara una variable llamada ventana_principal y que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

#establecer tamaño de la ventana
ventana_principal.geometry('800x500')

#titulo de la ventana
ventana_principal.title("Calculadora 1.0")

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#clolor de fondode la ventana principal
ventana_principal.config(bg="darkorchid4")

#------------------
#variables blobales
#-----------------
a=StringVar()
b=StringVar()
c=IntVar()

#-----------------
# Frame entrada
#-----------------

Frame_entrada=Frame(ventana_principal)
Frame_entrada.config(bg='black',width=780 ,height=240 )
Frame_entrada.place(x=10,y=10)

#etiqueta para el titulo de la app
titulo=Label(Frame_entrada, text= "Colegio san jose de guanenta " )
titulo.config(bg='green',fg='white', font=('Arial', 18) )
titulo.place(x=390, y=10)

#etiqueta para el subtitulo de la app
subtitulo=Label(Frame_entrada, text= "Especialidad de sistemas " )
subtitulo.config(bg='green',fg='white', font=('Arial', 15) )
subtitulo.place(x=390, y=40)

#etiqueta para el titulo de la app
subtitulo2=Label(Frame_entrada, text= "SUMA DE ENTEROS " )
subtitulo2.config(bg='black',fg='white', font=('Arial', 21) )
subtitulo2.place(x=390, y=70)

#Imagen_logo de la app
logo=PhotoImage(file="descarga.png")
etiq_logo=Label(Frame_entrada, image=logo)
etiq_logo.place(x=10, y=10)

#etiqueta para valor A
etiq_a=Label(Frame_entrada,text="a=")
etiq_a.config(bg='black',fg='white', font=('Arial', 21),anchor=CENTER )
etiq_a.place(x=398, y=120)

# entry para el valor de a
entry_a=Entry(Frame_entrada,width=4, textvariable=a)
entry_a.config(font=("Arial",20),justify=CENTER)
entry_a.focus_set()
entry_a.place(x=487, y=120)

#etiqueta para valor B
etiq_b=Label(Frame_entrada,text="b=")
etiq_b.config(bg='black',fg='white', font=('Arial', 21),anchor=CENTER )
etiq_b.place(x=585, y=120)

# entry para el valor de b
entry_b=Entry(Frame_entrada,width=4, textvariable=b)
entry_b.config(font=("Arial",20),justify=CENTER)
entry_b.place(x=682, y=120)

#-----------------
# Frame operaciones
#-----------------

Frame_operaciones=Frame(ventana_principal)
Frame_operaciones.config(bg='black',width=780 ,height=120 )
Frame_operaciones.place(x=10,y=260)

#boton de sumar
#button_sumar=Button(Frame_operaciones, text="SUMAR",width=9)
#button_sumar.config(font=("Arial",18),justify=CENTER)
button_sumar1=PhotoImage(file="suma.png")
button_sumar=Button(Frame_operaciones, image=button_sumar1, width=105, height=105 ,command=sumar)
button_sumar.place(x=116, y=7)

#boton de borrar entradas y resultados
button_borrar1=PhotoImage(file="borrar.png")
button_borrar=Button(Frame_operaciones, image=button_borrar1, width=105, height=105 ,command=borrar)
#button_borrar=Button(Frame_operaciones, text="BORRAR",width=9)
#button_borrar.config(font=("Arial",18),justify=CENTER)
button_borrar.place(x=337, y=7)

#boton de salir
#button_salir=Button(Frame_operaciones, text="SALIR",width=9)
#utton_salir.config(font=("Arial",18),justify=CENTER)
button_salir1=PhotoImage(file="salir.png")
button_salir=Button(Frame_operaciones, image=button_salir1, width=105, height=105 ,command=salir) 
button_salir.place(x=558, y=7)

#-----------------
# Frame resultados
#-----------------

Frame_resultados=Frame(ventana_principal)
Frame_resultados.config(bg='black',width=780 ,height=90)
Frame_resultados.place(x=10,y=390)

#area de texto de para resultados
T_resultados=Text(Frame_resultados, width=55 , height=3)
T_resultados.config(bg='purple', fg="white" ,font=('Arial', 19))
T_resultados.pack()

# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en boton, escribir, etc).Cada accion del usuario se conoce como un evento.El metodo mainloop() es un bucle infinito.
ventana_principal.mainloop()
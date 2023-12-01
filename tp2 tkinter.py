import tkinter
from tkinter import ttk
from tkinter import Tk
import tkinter as tk
from funciones import *
from tkinter import messagebox

# Esta funcion sirve para crear una tarea en la cual ahi un boton diseñado en la ventana que yo al poner un nombre en un ventana de texto y toque el boton se crre una tarea 
def agregar():
    descripcion = cajadetexto.get()
    tarea = agregar_tarea(descripcion)
    treeview.insert("" ,
    tkinter.END,
    text=[tarea["descripcion"]],
    values=[tarea["fecha"],tarea["completada"]])
 
 # Esta funcion sirve para que una vez yo haga click a alguna tarea y toque el boton llamado eliminar desaparezca la tarea 
def eliminar():
  eliminar_tarea  = messagebox.askyesno("confirmar","¿Estas seguro que quieren eliminar la tarea?")
  if eliminar_tarea:
    confirmar_eliminar = treeview.selection()
  if confirmar_eliminar:
    treeview.delete(confirmar_eliminar)

# esta funcion lo que haces que completar la tarea que vos eleciones la pasa de false a true
def completar():
  completar_tarea  = messagebox.askyesno("confirmar","¿Estas seguro que quieren completar la tarea?")
  if completar_tarea:
    completarTarea = treeview.selection()#Creo una variable completarTarea = llamo al tree y le paso el metodo selection que selecciona la tarea dentro del tre para despues completarla o eliminarla
  if completarTarea:
       treeview.item(completarTarea, values = (treeview.item(completarTarea)['values'][0], True))# En el if llamo a la variable completar tarea y le agrego tree y le paso el metodo item que adentro tiene un values que por default es falso entonces le decis que al tocar el boton completar pase de False a True 

def salir():
   salir_de_la_ventana = messagebox.askyesno("Confirmacion","¿Estas seguro que deseas salir de esta ventana?")
   if salir_de_la_ventana:
      ventana.quit()

ventana = tkinter.Tk()
ventana.resizable(height=0,width=0)
ventana.geometry("700x300")

 # Es este bloque es como crear una ventana y modificarle sus tamanos
boton_eliminar= tkinter.Button(ventana,text="Eliminar",bg= "red",activebackground="red",command=eliminar,width=20)
boton_crear= tkinter.Button(ventana,text="Agregar",bg= "green",activebackground="green", command=agregar,width=20)
boton_completar= tkinter.Button(ventana,text="Completar",bg="yellow",activebackground="yellow",command=completar,width=20)
boton_salir= tkinter.Button(ventana,text="Salir",bg="skyblue",activebackground="skyblue",command=salir,width=20)
 
 # Este bloque es para  crear un boton y modificarle sus manaños,color y agregarle una funcion 
cajadetexto= tkinter.Entry(ventana,font= "helvetica 12")


# En este bloque es para crear una caja de texto y agragarla a la ventana y modificar su letra 
treeview = ttk.Treeview(columns=("descri", "compl"))
treeview.heading("#0", text="nombre")
treeview.heading("descri", text="fecha de creacion")
treeview.heading("compl", text="realizado")

# Con este bloque le agregas la caracterizacion a la columna 
treeview.pack()
etiqueta = tkinter.Label(text="Agregar Tarea:")
etiqueta.pack()

cajadetexto.pack()
boton_crear.pack(side=tk.LEFT)
boton_completar.pack(side=tk.LEFT)
boton_eliminar.pack(side=tk.LEFT)
boton_salir.pack(side=tk.LEFT)

# Con este bloque haces que se visualizen los botones en la ventana la ventana 
ventana.mainloop()
# Con este bloque haces que se ejecute y corra el programa,
	

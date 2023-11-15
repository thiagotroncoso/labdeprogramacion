import tkinter as tk
import tkinter
from tkinter import ttk
from funciones import *


def cambiar_estado():
    global estado
    estado = not estado  # Invierte el valor de la variable
# Inicializa la variable de estado en False
estado = False
def agregar():
    descripcion = cajadetexto.get()
    tarea = agregar_tarea(descripcion)
    treeview.insert("" ,
    tkinter.END,
    text=[tarea["descripcion"]],
    values=[tarea["fecha"],tarea["completada"]])
 # Esta funcion sirve para crear una tarea en la cual ahi un boton diseñado en la ventana que yo al poner un nombre en un ventana de texto y toque el boton se crre una tarea 

def eliminar():
  selecionador_de_item = treeview.selection()
  if selecionador_de_item:
    treeview.delete(selecionador_de_item)
    
# Crea un botón que llama a la función cambiar_estado
boton = tk.Button(ventana,text="Cambiar a True",command=cambiar_estado)
boton_eliminar= tkinter.Button(ventana,text="eliminar",bg= "red",activebackground="red",command=eliminar)
boton_crear= tkinter.Button(ventana,text="crear",bg= "green",activebackground="green", command=agregar)

ventana = tkinter.Tk()
ventana.resizable(height=0,width=0)
ventana.geometry("700x500")

cajadetexto= tkinter.Entry(ventana,font= "helvetica 12")
treeview = ttk.Treeview(columns=("descri", "compl"))
treeview.heading("#0", text="nombre")
treeview.heading("descri", text="fecha de creacion")
treeview.heading("compl", text="realizado")
treeview.pack()
cajadetexto.pack()
boton.pack()
boton_eliminar.pack()
boton_crear.pack()
# Ejecuta la aplicación
ventana.mainloop()
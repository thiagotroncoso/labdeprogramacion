import tkinter
from tkinter import ttk
from funciones import *

def agregar():
    descripcion = cajadetexto.get()
    tarea = agregar_tarea(descripcion)
    treeview.insert("" ,
    tkinter.END,
    text=[tarea["descripcion"]],
    values=[tarea["fecha"],tarea["completada"]])

def eliminar():
  selecionador_de_item = treeview.selection()
  if selecionador_de_item:
    treeview.delete(selecionador_de_item)

def completar():
    pass
ventana = tkinter.Tk()
ventana.resizable(height=0,width=0)
ventana.geometry("700x500")
boton_eliminar= tkinter.Button(ventana,text="eliminar",bg= "red",activebackground="red",command=eliminar)
boton_crear= tkinter.Button(ventana,text="crear",bg= "green",activebackground="green", command=agregar)
boton_completar= tkinter.Button(ventana,text="completar",bg="yellow",activebackground="yellow",command=completar)
cajadetexto= tkinter.Entry(ventana,font= "helvetica 12")
treeview = ttk.Treeview(columns=("descri", "compl"))
treeview.heading("#0", text="nombre")
treeview.heading("descri", text="fecha de creacion")
treeview.heading("compl", text="realizado")

treeview.pack()
cajadetexto.pack()
boton_crear.pack()
boton_completar.pack()
boton_eliminar.pack()
ventana.mainloop()

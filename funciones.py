from datetime import date #para poder colocar el comando que te diga el dia,mes,año de la creacion de dicionario
import os  #para poder utilizar el clear
import time  #para poder poner para que te de un tiempo de poder leer y se borre

mostrar_tareas = []

def agregar_tarea():
    ladescripcion = input("tarea a agregar:")

    tarea = {"descripcion": ladescripcion,
	   "fecha": date.today().strftime("%d-%m-%y") ,
        "completada": False}
    
    mostrar_tareas.append(tarea)
    print("su tarea", ladescripcion, "se agrego a la lista ")
  
def listar_la_tarea():
    print("Lista de tus tareas:")
    lista = 0
    for iterar in mostrar_tareas:
        print(lista, iterar)
        lista += 1

def eliminar_la_tarea():
    listar_la_tarea()
    eliminar = int(input("Eliminar la tarea: "))
    mostrar_tareas.pop(eliminar)
    print("Su tarea fue eliminada de la lista")

def completar_tu_tarea():
    listar_la_tarea()
    completar = int(input("Completar la tarea: "))
    mostrar_tareas [completar] ["completada"] = True
    print("Su tarea ha sido completada")


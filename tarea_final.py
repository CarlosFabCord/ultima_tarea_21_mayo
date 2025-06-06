import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import math
import csv
import os
import pandas as pd
from tkinter.scrolledtext import ScrolledText
import io

proyecto = "proyectos_contruc.csv"



def reg_proyect():
################################################################################3
    
    id_proyecto = str(nombre_proyect.get())
    longitud_Oper = longitud.get()
    angulo = math.radians(random.uniform(30,90))
    operacion = math.tan(angulo)*float(longitud_Oper)

    resultado.set(operacion)

    fila = {
        'Id_proyecto': id_proyecto,
        'Longitud': longitud_Oper,
        'Angulo' : angulo,
        'Resultado': operacion      
    }

    
    # Verificar si ya existe el archivo
    archivo_existe = os.path.isfile(proyecto)

    with open(proyecto, 'a', newline='') as f:
        escritor = csv.DictWriter(f, fieldnames=fila.keys())
        if not archivo_existe: #Cambia a False si "os.path.isfile()"" es True, y cambia a True si da False
            escritor.writeheader() #Si True, entonces crea un archivo nuevo
        escritor.writerow(fila) #Si False, salta aquí





def ver_proyect():
    try:
        buscar=nombre_proyect.get()
        archivo_existe = os.path.isfile(proyecto)
        if archivo_existe==True:
            data = pd.read_csv(proyecto)
            data["Id_proyecto"] = data["Id_proyecto"].astype(str)
            uni_fila=data[data['Id_proyecto']==buscar]
            lista=uni_fila.values.tolist()[0]
            longitud.set(lista[1])
            resultado.set(lista[3])
        else:
            arc_inexistente="El archivo no se ha creado aún. Registre al menos un proyecto"
            resultado.set(arc_inexistente)

    except IndexError:
        messagebox.showerror("Error", "El proyecto no existe")   



def act_proyect():
    global proyecto
    try:
        buscar=nombre_proyect.get()
        archivo_existe = os.path.isfile(proyecto)
        if archivo_existe==True:
            data = pd.read_csv(proyecto)
            data["Id_proyecto"] = data["Id_proyecto"].astype(str)
            indice = data['Id_proyecto']==buscar
            data.loc[indice, 'Longitud'] = longitud.get()
            data.to_csv(proyecto, index=False)      
    
        else:
            arc_inexistente="El archivo no se ha creado aún. Registre al menos un proyecto"
            resultado.set(arc_inexistente)
        
    except IndexError:
        messagebox.showerror("Error", "El proyecto no existe")




def elim_proyect():
    global proyecto

    buscar = nombre_proyect.get()
    if not buscar:
        messagebox.showwarning("Aviso", "Ingrese un NOMBRE de proyecto para eliminar")
        return

    if not os.path.isfile(proyecto):
        messagebox.showwarning("Aviso", "El archivo no se ha creado aún. Registre al menos un proyecto.")
        return

    data = pd.read_csv(proyecto)
    data["Id_proyecto"] = data["Id_proyecto"].astype(str)
    coincidencias = data[data['Id_proyecto'] == buscar]

    if coincidencias.empty:
        messagebox.showerror("Error", "El proyecto no existe")
    else:
        data = data[data['Id_proyecto'] != buscar]
        data.to_csv(proyecto, index=False)
        messagebox.showinfo("Éxito", f"Proyecto '{buscar}' eliminado correctamente.")

def imprimir_tabla():
    global proyecto
    try:
        text_area.delete("1.0", tk.END)
        buffer = io.StringIO()
        DataFrame = pd.read_csv(proyecto)
        texto_imprimir = DataFrame.to_string()
        buffer.write(texto_imprimir)
        imprimir = buffer.getvalue()
        text_area.insert(tk.END, imprimir)
    except:
        messagebox.showerror("No hay nada qué imprimir")  

###########################################################################

################### Id del proyecto

ventana = tk.Tk()
ventana.title("Proyectos de construcción")
ventana.configure(bg="#e6f0fa")

nombre_proyect = tk.StringVar()###
nombre_proyect_label = tk.Label(ventana, text="Nombre del proyecto", bg="#e6f0fa", fg="#003366", font=("Arial", 11, "bold"))
nombre_proyect_label.grid(row=0, column=0, padx=10, pady=5)
nombre_proyect_entry = tk.Entry(ventana, textvariable=nombre_proyect, font=("Arial", 11))
nombre_proyect_entry.grid(row=0, column=1, padx=10, pady=5)
################### Entrada de longitud
longitud = tk.DoubleVar()
longitud_label = tk.Label(ventana, text="Longitud", bg="#e6f0fa", fg="#003366", font=("Arial", 11, "bold"))
longitud_label.grid(row=1, column=0, padx=10, pady=5)
longitud_entry = tk.Entry(ventana, textvariable=longitud, font=("Arial", 11))
longitud_entry.grid(row=1, column=1, padx=10, pady=5)
################# Label resultado
resultado = tk.StringVar()
etiqueta_resultado = tk.Label(ventana, text="Resultado:", bg="#e6f0fa", fg="#003366", font=("Arial", 11, "bold"))
etiqueta_resultado.grid(row=2, column=0, padx=10, pady=5)
resultado_salida = tk.Label(ventana, text="", textvariable=resultado, bg="#ffffff", fg="#000000", font=("Arial", 11))
resultado_salida.grid(row=2, column=1, padx=10, pady=5)
################## Botón de registro
boton_reg_proyect = tk.Button(ventana, text="Registra el proyecto", command=reg_proyect, bg="#1f4e79", fg="white", font=("Arial", 10, "bold"), activebackground="#4a90e2")
boton_reg_proyect.grid(row=3, column=0, padx=10, pady=5)
################# Botón de ver registro
boton_ver_proyect = tk.Button(ventana, text="Ver proyecto", command=ver_proyect, bg="#1f4e79", fg="white", font=("Arial", 10, "bold"), activebackground="#4a90e2")
boton_ver_proyect.grid(row=3, column=1, padx=10, pady=5)
################# Botón de actualizar proyecto
boton_act_proyect = tk.Button(ventana, text="Actualizar", command=act_proyect, bg="#4a90e2", fg="white", font=("Arial", 10, "bold"), activebackground="#6fb3f2")
boton_act_proyect.grid(row=4, column=0, padx=10, pady=5)
################ Botón de eliminar un proyecto
boton_elim_proyect = tk.Button(ventana, text="Eliminar", command=elim_proyect, bg="#cc0000", fg="white", font=("Arial", 10, "bold"), activebackground="#ff3333")
boton_elim_proyect.grid(row=4, column=1, padx=10, pady=5)
############### Botón imprimir tabla
boton_impr_tabla = tk.Button(ventana, text="Mostrar tabla", command=imprimir_tabla, bg="#1f4e79", fg="white", font=("Arial", 10, "bold"), activebackground="#4a90e2")
boton_impr_tabla.grid(row=5, column=0, padx=10, pady=5)

text_area = ScrolledText(ventana, width=70, height=30, font=("Courier New", 10), bg="white", fg="black")
text_area.grid(row=6, column=1, padx=10, pady=5)




ventana.mainloop()

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

ventana = tk.Tk()
ventana.title("Proyectos de construcción")

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

  try:
    buscar=nombre_proyect.get()
    archivo_existe = os.path.isfile(proyecto)
    if archivo_existe==True:      
      data = pd.read_csv(proyecto)
      data["Id_proyecto"] = data["Id_proyecto"].astype(str)
      indice = data[data['Id_proyecto']==buscar].index
      data.drop(index=indice, inplace=True)
      data.to_csv(proyecto, index=False)
    
    else:
      arc_inexistente="El archivo no se ha creado aún. Registre al menos un proyecto"
      resultado.set(arc_inexistente)
  
  except IndexError:
        messagebox.showerror("Error", "El proyecto no existe")

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

nombre_proyect = tk.StringVar()###
nombre_proyect_entry = tk.Entry(ventana, textvariable=nombre_proyect)
nombre_proyect_entry.grid(row=0, column=1)
nombre_proyect_label = tk.Label(ventana, text="Nombre del proyecto")
nombre_proyect_label.grid(row=0, column=0)


################### Entrada de longitud
longitud = tk.DoubleVar()###
longitud_entry = tk.Entry(ventana,textvariable= longitud)
longitud_entry.grid(row=1, column=1)
longitud_label = tk.Label(ventana, text="Longitud")
longitud_label.grid(row=1, column=0)


################# Label resultado

resultado = tk.StringVar()###
resultado_salida = tk.Label(ventana, text="", textvariable=resultado)
resultado_salida.grid(row=2, column=1)

etiqueta_resultado = tk.Label(ventana, text="Resultado: ")
etiqueta_resultado.grid(row=2, column=0)

################## Botón de registro

boton_reg_proyect = tk.Button(ventana, text="Registra el proyecto", command=reg_proyect)
boton_reg_proyect.grid(row=3, column=0)

################# Botón de ver registro

boton_ver_proyect = tk.Button(ventana, text="Ver proyecto", command=ver_proyect)
boton_ver_proyect.grid(row=3, column=1)

################# Botón de actualizar proyecto

boton_act_proyect = tk.Button(ventana, text="Actualizar", command= act_proyect)
boton_act_proyect.grid(row=4, column=0)

################ Botón de eliminar un proyecto

boton_elim_proyect = tk.Button(ventana, text= "Eliminar", command= elim_proyect)
boton_elim_proyect.grid(row=4, column=1)

############### Botón imprimir tabla

boton_impr_tabla = tk.Button(ventana, text="Mostrar tabla", command= imprimir_tabla)
boton_impr_tabla.grid(row=5, column=0)

text_area = ScrolledText(ventana, width= 70, height=30)
text_area.grid(row=6, column=1)

ventana.mainloop()










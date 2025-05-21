import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import math
import csv
import os

proyecto = "proyectos_contruc.csv"

def reg_proyect():
    if os.path.exists(proyecto):
        return pd.read_csv(proyecto)
    else:
        return pd.dataframe(Columns=["nombre","longitud","resultado"])
        
def agregar_datos():
    dataframe.to_csv(DOCUMENTO, index=false)
ventana.title("Proyectos de construcción")

nombre_proyect = tk.StringVar()
nombre_proyect_entry = tk.Entry(ventana, textvariable=nombre_proyect)
nombre_proyect_entry.grid(row=0, column=1)
nombre_proyect_label = tk.Label(ventana, text="Nombre del proyecto")
nombre_proyect_label.grid(row=0, column=0)


longitud = tk.StringVar()
longitud_entry = tk.Entry(ventana,textvariable= longitud)
longitud_entry.grid(row=1, column=1)
longitud_label = tk.Label(ventana, text="Longitud")
longitud_label.grid(row=1, column=0)


boton_reg_proyect = tk.Button(ventana, text="Registra el proyecto", command=reg_proyect)
boton_reg_proyect.grid(row=2, column=0)


ventana.mainloop()










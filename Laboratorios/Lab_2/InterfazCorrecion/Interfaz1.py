#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 09:28:01 2022

@author: EstefanyRueda y PedroGómez
"""


from ast import Return
import tkinter as tk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
from scipy import stats
from tkinter import messagebox
from statistics import mode,mean,median
import seaborn as sns
#from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
#from matplotlib.figure import Figure


#varEleccion=[]
master=tk.Tk()
master.title("")
# se debe dar tamano al frame no a al master, la master se adpata al tamano del frame
#master.geometry('500x500')

frame=Frame(master,width=600,height=650)
mensaje=Label(frame)
mensaje.pack()
mensaje.grid(row=9,column=4)
#---------------------- Lectura Archivo ---------------------------------------

archivo = 'abalone.csv'
datos=pd.read_csv(archivo)
datos.columns=["Sex","Length","Diameter","Height","Whole Weight","Shucked weight","Viscera weight","Shell weight","Rings"]


#---------------------- Funciones ---------------------------------------------

#Grafica con atipicos

def graficarAtipicos(dats=None):
    if(dats==None):
        dats=datos
    varEleccion = selecionado()
    
    
    if(radioValue.get()==1):
        if(len(varEleccion)>1):
            mensaje.config(text="Selecciona una variable")
        else:
            plot.hist(x=datos[varEleccion[0]])
            plot.title("Histograma")
            plot.show()

    elif(radioValue.get()==2):
        if(len(varEleccion)>1):
            mensaje.config(text="Selecciona una variable")
        else:
            graph = plot.figure()
            ax = graph.add_subplot(111)
            res = stats.probplot(datos[varEleccion[0]], dist=stats.norm, sparams=(6,), plot=ax)
            plot.title("Normalización")
            plot.show()

    elif(radioValue.get()==3):
        if(len(varEleccion)>1):
            mensaje.config(text="Selecciona una variable")
        else:
            plot.boxplot(x=datos[varEleccion[0]])
            plot.title("Boxplot")
            plot.show()

    elif(radioValue.get()==4):

        if(len(varEleccion)>2):
            mensaje.config(text="Selecciona una variable")
        else:
            plot.scatter(datos[varEleccion[0]], datos[varEleccion[1]])
            plot.title("Grafica de Dispersion")
            plot.show()



def selecionado():
    varEleccion = []
    if(longitudVar1.get()== 1):
        varEleccion.append("Length")
    if(pesoEnteroVar2.get()==1):
        varEleccion.append("Whole Weight") 
    if(pesoCaparazonVar3.get()==1):
        varEleccion.append("Shell weight")
    if(diametroVar4.get()==1):
        varEleccion.append("Diameter")
    if(pesoCascaraVar5.get()==1):
        varEleccion.append("Shucked weight")
    if(numAnillosVar6.get()==1):
        varEleccion.append("Rings")
    if(alturaVar7.get()==1):
        varEleccion.append("Height")
    if(pesoViscerasVar8.get()==1):
        varEleccion.append("Viscera weight")

    return varEleccion

def sinAtipicos():
    al = txtAtipico.get()

    limitMax = []
    limitMin = []
    for i in range (1, len(datos.columns)):
        q75 = np.quantile(datos[datos.columns[i]],.75)
        q25 = np.quantile(datos[datos.columns[i]],.25)
        intr_qr = q75 - q25
        limitMax.append(q75 + (float(al) * intr_qr))
        limitMin.append(q25 - (float(al) * intr_qr))
    atipicos = None
    datosSin = []

    cont = 0

    for i in datos.columns:
        if(i == "Sex"):
            continue    
        atipicos = (datos[i] >= limitMin[cont]) & (datos[i] <= limitMax[cont])
        datosSin.append(datos[i][atipicos])
        cont += 1

    graficarAtipicos(datosSin)

def estadisticas(dats = None):
    if(dats == None):
        dats = datos
    seleccion = selecionado()
    #contadores
    col = 0
    cont = 0
    txt = None
    #listas
    moda = []
    media = []
    mediana = []
    s = []
    c = [] #curtosis
    encabezado = Toplevel()
    encabezado.title('Analisis estadistico')
    
    for i in range(0, len(seleccion),2):
        print(seleccion[i])
        moda.append(mode(datos[seleccion[i]]))
        media.append(mean(datos[seleccion[i]]))
        mediana.append(median(datos[seleccion[i]]))
        s.append(stats.skew(datos[seleccion[i]]))
        c.append(stats.kurtosis(datos[seleccion[i]]))
        #fig, ax = plot.subplots() 
        #ax.set_ylabel('Media, meidana, moda simetria, curtosis')
        #tipos=[media[cont],mediana[cont],moda[cont],s[cont],c[cont]]
        #ax.set_title('Cantidad de Ventas por Pais')
        #plot.bar(seleccion[i],media[cont])
        #plot.savefig('barras_simple.png')
        #plot.show()
        txt = Label(encabezado,text=f"Estadisticas de {seleccion[i]}---\nMedia: {media[cont]}\nMediana: {mediana[cont]}\nModa: {moda[cont]}\nSimetria: {s[cont]}\nCurtosis: {c[cont]}", width=25)
        txt.config(borderwidth=2, relief="ridge")
        txt.grid(row=cont,column=col, padx= 10, pady=10)
        
        if(col == 2):
            cont+=1 
            col = 0
        else:
            col += 1
       
    


#---------------------- Interfaz ----------------------------------------------
frame.pack(fill="both",expand="True") #poner el frame en el master y que se expanda en todas direcciones con la ventana 

#txt=Label(frame,text="Grafica con atipicos")
#txt.place(x=0,y=0)
#Abreviacion
Label(frame,text="GRAFICA CON ATIPICOS").grid(row=0,column=0)

radioValue = tk.IntVar() 


rdioOne = tk.Radiobutton(frame, text='Histograma',
                             variable=radioValue, value=1) 


rdioTwo = tk.Radiobutton(frame, text='Normalizacion',
                             variable=radioValue, value=2) 


rdioThree = tk.Radiobutton(frame, text='Boxplot',
                             variable=radioValue, value=3)


rdioFour = tk.Radiobutton(frame, text='Dispersion',
                             variable=radioValue, value=4)

rdioOne.grid(row=1,column=3)
rdioTwo.grid(row=2,column=3)
rdioThree.grid(row=1,column=4)
rdioFour.grid(row=2,column=4) 

Label(frame,text="Tipo de Grafica").grid(row=0,column=3)


Label(frame,text="Variables de entrada").grid(row=3,column=3)

longitudVar1 = IntVar()
pesoEnteroVar2 = IntVar()
pesoCaparazonVar3 = IntVar()
diametroVar4 = IntVar()
pesoCascaraVar5 = IntVar()
numAnillosVar6 = IntVar()
alturaVar7 = IntVar()
pesoViscerasVar8 = IntVar()


C1 = Checkbutton(frame, text = "Longitud", variable = longitudVar1, \

                 onvalue = 1, offvalue = 0, command=selecionado)
C2 = Checkbutton(frame, text = "Peso Entero", variable = pesoEnteroVar2, \
                 onvalue = 1, offvalue = 0, command=selecionado)
C3 = Checkbutton(frame, text = "Peso Caparazon", variable = pesoCaparazonVar3, \
                 onvalue = 1, offvalue = 0, command=selecionado)
C4 = Checkbutton(frame, text = "Diametro", variable = diametroVar4, \
                 onvalue = 1, offvalue = 0, command=selecionado)
C5 = Checkbutton(frame, text = "Peso Cascara", variable = pesoCascaraVar5, \
                 onvalue = 1, offvalue = 0, command=selecionado)
C6 = Checkbutton(frame, text = "# de Anillos", variable = numAnillosVar6 , \
                 onvalue = 1, offvalue = 0, command=selecionado)
C7 = Checkbutton(frame, text = "Altura", variable = alturaVar7, \
                 onvalue = 1, offvalue = 0, command=selecionado)
C8 = Checkbutton(frame, text = "Peso Viseras", variable = pesoViscerasVar8, \
                 onvalue = 1, offvalue = 0, command=selecionado)
    

C1.grid(row=4,column=3)
C2.grid(row=5,column=3)
C3.grid(row=6,column=3)
C4.grid(row=4,column=4)
C5.grid(row=5,column=4)
C6.grid(row=6,column=4)
C7.grid(row=4,column=5)
C8.grid(row=5,column=5)

#-------------------------------------------------------------------------------


btn1=tk.Button(frame,text="Graficar los datos originales", command=lambda:graficarAtipicos())
btn1.grid(row=6,column=5)

Label(frame,text="GRAFICA SIN ATIPICOS").grid(row=7,column=0)

Label(frame,text="Valor del factor del alfa para los atipicos").grid(row=7,column=3)

varAtipico=StringVar()
txtAtipico=tk.Entry(frame,textvariable=varAtipico)
txtAtipico.grid(row=7,column=4)


btn2=tk.Button(frame,text="Eliminar Atipicos",command=lambda:sinAtipicos())
btn2.grid(row=7,column=5)


Label(frame,text="GRAFICA").grid(row=8,column=4)

btn1=tk.Button(frame,text="Mostrar Estadisticas", command=lambda:estadisticas())
btn1.grid(row=9,column=5)




master.mainloop()



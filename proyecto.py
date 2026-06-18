import csv
import codecs
import streamlit as st
import matplotlib.pyplot as plt

#st.write("empecemos a trabajar equipo")

def diccionario():
    with open('ny_testing - Hoja 1.csv', encoding="utf-8") as csvfile:
        dataset = csv.reader(csvfile)
        lista = []
        for row in dataset:
            lista.append(row)
        return lista

def dic(lista):
    titulos=lista[0]
    demas_data=lista[1:]
    dicc={}
    var=0
    for titulo in titulos:
        dicc[titulo]=[]
        for linea in demas_data:
            dicc[titulo].append(linea[var])
        var+=1
    return dicc

#print(dic(diccionario()))
#print(dic(diccionario()).keys())

def separador_barras(lis,dato):
    palabra=""
    for char in dato:
        if char!="":
            if char!="/":
                palabra+=char
            else:
                lis.append(palabra)
                palabra=""
    lis.append(palabra)
    return lis
    

def lista_de_autos(diccionario):
    lista1=diccionario["VEHICLE TYPE CODE 1"]
    lista2=diccionario["VEHICLE TYPE CODE 2"]
    lista3=diccionario["VEHICLE TYPE CODE 3"]
    lista4=diccionario["VEHICLE TYPE CODE 4"]
    lista5=diccionario["VEHICLE TYPE CODE 5"]
    lis=[]
    for dato in lista1:
        lis=separador_barras(lis,dato)
    for dato in lista2:
        lis=separador_barras(lis,dato)
    for dato in lista3:
        lis=separador_barras(lis,dato)
    for dato in lista4:
        lis=separador_barras(lis,dato)
    for dato in lista5:
        lis=separador_barras(lis,dato)
    return lis

def conteo_autos(lista):
    dic_cont={}
    for auto in lista:
        if auto in dic_cont:
            dic_cont[auto]+=1
        elif auto!="":
            dic_cont[auto]=1
    return dic_cont

def mayores_cinco(diccionario):
    los_5={}
    max_variable1=["",0]
    max_variable2=["",0]
    max_variable3=["",0]
    max_variable4=["",0]
    max_variable5=["",0]
    for clave in diccionario:
        if max_variable1[1]<diccionario[clave]:
            max_variable1=[clave,diccionario[clave]]
            max_variable2=[max_variable1[0],max_variable1[1]]
            max_variable3=[max_variable2[0],max_variable2[1]]
            max_variable4=[max_variable3[0],max_variable3[1]]
            max_variable5=[max_variable4[0],max_variable5[1]]
    los_5[max_variable1[0]]=max_variable1[1]
    los_5[max_variable2[0]]=max_variable2[1]
    los_5[max_variable3[0]]=max_variable3[1]
    los_5[max_variable4[0]]=max_variable4[1]
    los_5[max_variable5[0]]=max_variable5[1]
    return los_5

def total_de_5(diccionario):
    var=0
    for item in diccionario.items():
        var+=item
    return item
        



def grafico_torta(diccionario):
    le_5=mayores_cinco(diccionario)
    total=total_de_5(le_5)
    nom=le_5.keys()
    labels = nom[0], nom[1], nom[2], nom[3],nom[4]
    sizes = [le_5[nom[0]]/total, le_5[nom[1]]/total, le_5[nom[2]]/total, le_5[nom[3]]/total,le_5[nom[4]]/total]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels)

#def lista_de_accidentes():
def main():
    estructura_datos=dic(diccionario())
    print(conteo_autos(lista_de_autos(estructura_datos)))

main()
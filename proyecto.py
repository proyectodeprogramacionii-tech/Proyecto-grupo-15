import streamlit as st
import dataset
st.write("empecemos a trabajar equipo")
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
    

def lista_de_autos():
    lista1=dataset["VEHICLE TYPE CODE 1"]
    lista2=dataset["VEHICLE TYPE CODE 2"]
    lista3=dataset["VEHICLE TYPE CODE 3"]
    lista4=dataset["VEHICLE TYPE CODE 4"]
    lista5=dataset["VEHICLE TYPE CODE 5"]
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
        else:
            dic_cont[auto]=1
    return dic_cont

print(conteo_autos(lista_de_autos()))

import streamlit as st
import dataset
linea_titulos="CRASH DATE,CRASH TIME,BOROUGH,ZIP CODE,LATITUDE,LONGITUDE,LOCATION,ON STREET NAME,CROSS STREET NAME,OFF STREET NAME,NUMBER OF PERSONS INJURED,NUMBER OF PERSONS KILLED,NUMBER OF PEDESTRIANS INJURED,NUMBER OF PEDESTRIANS KILLED,NUMBER OF CYCLIST INJURED,NUMBER OF CYCLIST KILLED,NUMBER OF MOTORIST INJURED,NUMBER OF MOTORIST KILLED,CONTRIBUTING FACTOR VEHICLE 1,CONTRIBUTING FACTOR VEHICLE 2,CONTRIBUTING FACTOR VEHICLE 3,CONTRIBUTING FACTOR VEHICLE 4,CONTRIBUTING FACTOR VEHICLE 5,COLLISION_ID,VEHICLE TYPE CODE 1,VEHICLE TYPE CODE 2,VEHICLE TYPE CODE 3,VEHICLE TYPE CODE 4,VEHICLE TYPE CODE 5"
st.title("Proyecto grupal de programacion")
st.write("empecemos a trabajar equipo")

def cuantas_comas_dataset(linea,dato):
    """
    segun el dato que necesitamos;devuelve la cantidad de comas necesarias para llegar a el
    """
    buscador=""
    comas=0
    for char in linea:
            if buscador!=dato:
                if char!=",":
                    buscador+=char
                else:
                    buscador=""
                    comas+=1
    return comas

def appendear_autos(lis,linea,comas_vei):
    vei=""
    coma_var=0
    for char in linea:
            if char==",":
                coma_var+=1
            
            if coma_var==comas_vei:
                if char!="/":
                    vei+=char
                else:
                    lis.append(vei)
                    vei=""
            elif coma_var>comas_vei:
                if vei!="":
                    lis.append(vei)
    return lis
    
def tipo_de_auto():
    lista_de_autos=[]
    comas_vei1=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 1")
    comas_vei2=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 2")
    comas_vei3=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 3")
    comas_vei4=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 4")
    comas_vei5=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 5")
    for linea in dataset:
        lista_de_autos=appendear_autos(lista_de_autos,linea,comas_vei1)
        lista_de_autos=appendear_autos(lista_de_autos,linea,comas_vei2)
        lista_de_autos=appendear_autos(lista_de_autos,linea,comas_vei3)
        lista_de_autos=appendear_autos(lista_de_autos,linea,comas_vei4)
        lista_de_autos=appendear_autos(lista_de_autos,linea,comas_vei5)
    return lista_de_autos
def contar_autos

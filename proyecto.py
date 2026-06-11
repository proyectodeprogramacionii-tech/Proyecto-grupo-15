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
def appendear_autos(lis,linea,coma_var,comas_vei):
    vei=""
    
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
                    vei=""
            return lis
    
def tipo_de_auto():
    lista_de_autos=[]
    comas_vei1=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 1")
    comas_vei2=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 2")
    comas_vei3=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 3")
    comas_vei4=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 4")
    comas_vei5=cuantas_comas_dataset(linea_titulos,"VEHICLE TYPE CODE 5")
    coma_var=0
    vei=""
    for linea in dataset:
        for char in linea:
            if char==",":
                coma_var+=1
            
            if coma_var==comas_vei1:
                if char!="/":
                    vei+=char
                else:
                    lista_de_autos.append(vei)
                    vei=""
            elif coma_var>comas_vei1:
                if vei!="":
                    lista_de_autos.append(vei)
                    vei=""
            coma_var=0
        for char in linea:
            if char==",":
                coma_var+=1
            if coma_var==comas_vei2:
                if char!="/":
                    vei+=char
                else:
                    lista_de_autos.append(vei)
                    vei=""
            else:
                if vei!="":
                    lista_de_autos.append(vei)
                    vei=""
        for char in linea:
            if coma_var<comas_vei3:
                coma_var+=1
            elif coma_var==comas_vei3:
                if char!="/":
                    vei+=char
                else:
                    lista_de_autos.append(vei)
                    vei=""
            else:
                if vei!="":
                    lista_de_autos.append(vei)
                    vei=""
        for char in linea:
            if coma_var<comas_vei4:
                coma_var+=1
            elif coma_var==comas_vei4:
                if char!="/":
                    vei+=char
                else:
                    lista_de_autos.append(vei)
                    vei=""
            else:
                if vei!="":
                    lista_de_autos.append(vei)
                    vei=""
            coma_var=0
        for char in linea:
            if coma_var<comas_vei5:
                coma_var+=1
            elif coma_var==comas_vei5:
                if char!="/":
                    vei+=char
                else:
                    lista_de_autos.append(vei)
                    vei=""
            else:
                if vei!="":
                    lista_de_autos.append(vei)
                    vei=""
            coma_var=0
    return lista_de_autos
def contar_autos

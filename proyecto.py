import csv
import codecs
import streamlit as st
import matplotlib.pyplot as plt

#iniciar con python -m streamlit run proyecto.py

def dataset():
    """
    lista de lista donde cada lista es una fila del excel de donde recibo la informacion
    """
    with open('ny_testing - Hoja 1.csv', encoding="utf-8") as csvfile:
        dataset = csv.reader(csvfile)
        lista = []
        for row in dataset:
            lista.append(row)
        return lista

def dic(lista):
    """
    lista:list(list)
    list(list)->dic(list)
    recibe una lista de listas
    """
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
def coma_a_punto(string):
    return string.replace(",", ".")

def separador_barras(lis,dato):
    """
    dato:string
    string-> list(string)
    recibe un string y analiza si tiene una barra que separa el texto, si no la tiene 
    forma una lista con un solo elemento que es la string, si tiene una barra, devuelve una lista
    con 2 elementos, con la parte anterior a la barra y la parte que le sigue, exceptuando a la barra

    """
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
    
def suma_5listas(l1,l2,l3,l4,l5):
    """
    l1:list(str)
    l2:list(str)
    l3:list(str)
    l4:list(str)
    l5:list(str)
    l1,l2,l3,l4,l5->list(str)
    recibe 5 listas de  string y devuelve una sola
    """
    var=separador_barras([],l1)+separador_barras([],l2)+separador_barras([],l3)+separador_barras([],l4)+separador_barras([],l5)
    return var

def lista_de_autos(diccionario):
    lista1=diccionario["VEHICLE TYPE CODE 1"]
    lista2=diccionario["VEHICLE TYPE CODE 2"]
    lista3=diccionario["VEHICLE TYPE CODE 3"]
    lista4=diccionario["VEHICLE TYPE CODE 4"]
    lista5=diccionario["VEHICLE TYPE CODE 5"]
    listafinal=lista1+lista2
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

def conteo_lista(lista):
    """
    lista:list(string)
    list(string)->dic(string)(int)
    recibe una lista de string, devuelve un diccionario donde las claves son todas las string distintas y
    su valor un int que refleja la cantidad de veces que aparece
    """
    dic_cont={}
    for auto in lista:
        if auto in dic_cont:
            dic_cont[auto]+=1
        elif auto!="":
            dic_cont[auto]=1
    return dic_cont

def mayores_cinco(diccionario):
    """
    diccionario:dicc(str)[int]
    dicc->dicc
    recibe un diccionario y devuelve los 5 valores mas grandes
    """
    los_5={}
    max_variable1=["",0]
    max_variable2=["",0]
    max_variable3=["",0]
    max_variable4=["",0]
    max_variable5=["",0]
    for clave in diccionario:
        valor=diccionario[clave]
        if max_variable1[1]<valor:
            max_variable5=[max_variable4[0],max_variable4[1]]
            max_variable4=[max_variable3[0],max_variable3[1]]
            max_variable3=[max_variable2[0],max_variable2[1]]
            max_variable2=[max_variable1[0],max_variable1[1]]
            max_variable1=[clave,valor]
        
        elif max_variable2[1]<valor:
            max_variable5=[max_variable4[0],max_variable4[1]]
            max_variable4=[max_variable3[0],max_variable3[1]]
            max_variable3=[max_variable2[0],max_variable2[1]]
            max_variable2=[clave,valor]
        
        elif max_variable3[1]<valor:
            max_variable5=[max_variable4[0],max_variable4[1]]
            max_variable4=[max_variable3[0],max_variable3[1]]
            max_variable3=[clave,valor]
       
        elif max_variable4[1]<valor:
            max_variable5=[max_variable4[0],max_variable4[1]]
            max_variable4=[clave,valor]
        
        elif max_variable5[1]<valor:
            max_variable5=[clave,valor]
    los_5[max_variable1[0]]=max_variable1[1]
    los_5[max_variable2[0]]=max_variable2[1]
    los_5[max_variable3[0]]=max_variable3[1]
    los_5[max_variable4[0]]=max_variable4[1]
    los_5[max_variable5[0]]=max_variable5[1]
    return los_5

#print(mayores_cinco({"a":1000,"b":5,"c":800,"d":20,"e":700,"f":10,"g":600}))

def suma_de_valores(diccionario):
    """
    diccionario:dicc(string)[int]
    dicc->int    
    suma todos los valores de un diccionario
    """
    var=0
    for item in diccionario.values():
        var+=item
    return var

def diccionario_factores(diccionario):
    lista1=diccionario["CONTRIBUTING FACTOR VEHICLE 1"]
    lista2=diccionario["CONTRIBUTING FACTOR VEHICLE 2"]
    lista3=diccionario["CONTRIBUTING FACTOR VEHICLE 3"]
    lista4=diccionario["CONTRIBUTING FACTOR VEHICLE 4"]
    lista5=diccionario["CONTRIBUTING FACTOR VEHICLE 5"]
    listalat=diccionario["LATITUDE"]
    listalon=diccionario["LONGITUDE"]
    dic={}
    for index in range(0,len(lista1)):
        var=suma_5listas(lista1[index],lista2[index],lista3[index],lista4[index],lista5[index])
        for factor in var:
            if factor!="":
                if listalat[index] != "" and listalon[index] != "":
                    lat=float(coma_a_punto(listalat[index]))
                    long=float(coma_a_punto(listalon[index]))
                    if factor not in dic:
                        dic[factor]=[[lat],[long]]
                    else:
                        dic[factor][0].append(lat)
                        dic[factor][1].append(long)
    return dic

def lista_calles(diccionario):
    """
    diccionario:dic(str)[list]
    dicc->list[string]
    recibe un diccionario y devuelve una lista de 3 elementos con los nombres de las calles en donde sucedio un accidente
    lista({"ON STREET NAME":[1,2,34,45],"CROSS STREET NAME":[3,4,6,12],"OFF STREET NAME":["","","",""]}))==[[1,3,""],[2,4,""],[34,6,""],[45,12,""]]
    lista({"ON STREET NAME":[1,2,34,45],"CROSS STREET NAME":["","","",""],"OFF STREET NAME":["","","",""]}))==[[1,"",""],[2,"",""],[34,"",""],[45,"",""]]
    lista({"ON STREET NAME":["","","",""],"CROSS STREET NAME":["","","",""],"OFF STREET NAME":["a","b","c","d"]}))==[["","","a"],["","","b"],["","","c"],["","","d"]]

    """
    lista1=diccionario["ON STREET NAME"]
    lista2=diccionario["CROSS STREET NAME"]
    lista3=diccionario["OFF STREET NAME"]
    long=len(lista1)
    lista_final=[]
    for index in range(0,long):
        lista_final.append([lista1[index],lista2[index],lista3[index]])
    return lista_final

def conteo_lista_calles(lista):
    """
    lista:list(string)
    list(list(string))->dic(string)(int)
    recibe una lista de listas de 3 elementos que son todos string, devuelve un diccionario donde las claves son todas los elementos distintos y
    su valor un int que refleja la cantidad de veces que aparece
    ej:
    conteo([["hola","",""],["","","adios"],["malos","adios",""]])=={"hola":1,"adios":1,"Entre malos y adios":1}
    conteo([["hola","",""],["hola","",""],["malos","adios",""]])=={"hola":2,"Entre malos y adios":1}
    conteo([["malos","adios",""],["malos","adios",""],["malos","adios",""]])=={"Entre malos y adios":3}
    """
    dic_cont={}
    for calle in lista:
        if  calle[0]=="":
            clave = calle[2]   
        else:
            if calle[1] == "":
                clave = calle[0]
            else:
                clave = "Entre " + calle[0] + " y " + calle[1]
        if clave in dic_cont:
            dic_cont[clave] += 1
        else:
            dic_cont[clave] = 1
    return dic_cont




def cual_factor(diccionario):
    nom=[]
    for x in diccionario:
        nom.append(x)
    factor=st.selectbox("Seleccione el factor contribuyente al accidente", nom, index=0, 
                 key=None, help=None,on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, 
                 label_visibility="visible", accept_new_options=False, filter_mode="fuzzy", width="stretch", bind=None)
    return factor


def mapa_factores(diccionario,factor="Driver Inattention"):
    dic=diccionario_factores(diccionario)
    st.map(data={"lat":dic[factor][0],"lon":dic[factor][1]}, latitude=None, longitude=None, color=None, size=None, zoom=None, width="stretch", height=500, use_container_width=None)


def grafico_torta(diccionario):
    le_5=mayores_cinco(diccionario)
    nom=[]
    for x in le_5:
        nom.append(x)
    total=suma_de_valores(le_5)
    labels = nom[0], nom[1], nom[2], nom[3],nom[4]
    sizes = [le_5[nom[0]]/total, le_5[nom[1]]/total, le_5[nom[2]]/total, le_5[nom[3]]/total,le_5[nom[4]]/total]
    fig , ax = plt.subplots()
    ax.pie(sizes, labels=labels,colors=["red","green","black","pink","orange"])
    ax.set_title("¿Cuáles son las cinco clases de vehiculos que mas accidentes sufren?")
    return fig

def tabla_calles(diccionario):
    st.table(data=diccionario, border=True, width="stretch", height="content", hide_index=None, hide_header=None)

def distribucion_pantalla(estructura_datos):
    dic_autos=(conteo_lista(lista_de_autos(estructura_datos)))
    dic_factores=diccionario_factores(estructura_datos)
    calles_5=mayores_cinco(conteo_lista_calles((lista_calles(estructura_datos))))
    st.set_page_config(layout="wide")
    st.title("Accidentes en Nueva York", anchor=None, help=None, width="stretch", text_alignment="left")
    col1, col2 = st.columns(2,gap="medium", vertical_alignment="top", border=False, width="stretch")
    with col1:
        st.header("Localización de accidentes según el factor de riesgo que lo induce: ", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
        factor=cual_factor(dic_factores)
        mapa_factores(estructura_datos,factor)
        st.header("Calles mas accidentadas", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
        tabla_calles(calles_5)
    with col2:
        st.header("clases de autos con mas tendencia a estar involucrados en un accidente ", anchor=None, help=None, divider=False, width="stretch", text_alignment="center")
        fig_torta_autos= grafico_torta(dic_autos)
        st.pyplot(fig_torta_autos)


#def lista_de_accidentes():
def main():
    estructura_datos=dic(dataset())
    distribucion_pantalla(estructura_datos)
   
    
    
main()

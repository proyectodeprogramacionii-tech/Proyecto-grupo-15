import codecs;
def string_a_lista(linea):
    """
    segun el dato que necesitamos;devuelve la cantidad de comas necesarias para llegar a el
    """
    buscador=""
    lista=[]
    for char in linea:
            if char!=",":
                buscador+=char
            elif buscador==",":
                 lista.append(buscador)
                 buscador=""
    lista.append(buscador)
    return lista

def dic(lista):
    titulos=lista[0]
    demas_data=lista[1:]
    long=len(demas_data[0])
    dicc={}
    var=0
    for titulo in titulos:
        dicc[titulo]=[]
        for linea in demas_data:
            dicc[titulo].append(linea(var))
        var+=1
    return dicc
    
def main():
    archivo = open("Motor_Vehicle_Collisions_sample_12K.csv")
    linea = archivo.readline()
    lista=[]
    while linea != '':
        linea = archivo.readline()
        lista+=string_a_lista(lista)
    return dic(lista)
        
archivo.close()

import codecs;
def string_a_lista(linea):
    """
    segun el dato que necesitamos;devuelve la cantidad de comas necesarias para llegar a el
    """
    buscador=""
    comas=[]
    for char in linea:
            if char!=",":
                buscador+=char
            elif buscador!="":
                 comas.append(buscador)
                 buscador=""
    comas.append(buscador)
    return comas
# Lectura del dataset
archivo = open("Motor_Vehicle_Collisions_sample_12K.csv")
linea = archivo.readline()
while linea != '':
    print(linea)
    linea = archivo.readline()

archivo.close()

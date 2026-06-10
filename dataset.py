import codecs;

# Lectura del dataset
archivo = open("Motor_Vehicle_Collisions_sample_12K.csv")
linea = archivo.readline()
while linea != '':
    print(linea)
    linea = archivo.readline()

archivo.close()
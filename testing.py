from proyecto import *

def dataset():
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

def test_coma_a_punto():
    assert(coma_a_punto("hola mundo"))=="hola mundo"
    assert(coma_a_punto("hola, mundo"))=="hola. mundo"
    assert(coma_a_punto("123,45"))=="123.45"

def test_separador_barras():
    assert(separador_barras([],"hola mundo"))==["hola mundo"]
    assert(separador_barras([],"hola/mundo"))==["hola","mundo"]
    assert(separador_barras(["adios"],"hola/mundo"))==["adios","hola","mundo"]

def test_suma_5listas():
    assert(suma_5strings([" "],[" "],[" "],[" "],[" "]))==[" "," "," "," "," "]
    assert(suma_5strings(["1"],["2"],["3"],["4"],["5"]))==["1","2","3","4","5"]

def test_lista_de_autos():
    assert(lista_de_autos(dic(dataset())))==['Refrigerated Van', 'Station Wagon', 'Sport Utility Vehicle', 'Box Truck', 
                                             'Sedan', 'TRAC', 'Pick-up Truck', 'Sedan', 'Sedan', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Station Wagon', 'Sport Utility Vehicle', 
                                             'Station Wagon', 'Sport Utility Vehicle', 'Station Wagon', 'Sport Utility Vehicle', 
                                             'Station Wagon', 'Sport Utility Vehicle', 'Sedan', 'Sedan', 'Bike', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Station Wagon', 'Sport Utility Vehicle', 'Taxi', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Pick-up Truck', 'Sedan', 'Flat Bed', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Sedan', 'Sedan', 'Sedan', 'Station Wagon', 'Sport Utility Vehicle', 
                                             'Sedan', 'Sedan', 'Sedan', 'Box Truck', '4 dr sedan', 'Sedan', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Taxi', 'Station Wagon', 'Sport Utility Vehicle', 'Sedan', 
                                             'Sedan', 'Bike', 'Station Wagon', 'Sport Utility Vehicle', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Station Wagon', 'Sport Utility Vehicle', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Station Wagon', 'Sport Utility Vehicle', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Bike', 'Sedan', 'Garbage or Refuse', 'Sedan', 'Station Wagon', 
                                             'Sport Utility Vehicle', 'Box Truck', 'Sedan', 'Station Wagon', 'Sport Utility Vehicle', 
                                             'Box Truck']

def test_mayores_cinco():
    assert(mayores_cinco({"A":4,"B":66,"C":32,"D":23,"E":45}))=={"B":66,"E":45,"C":32,"D":23,"A":4}
    assert(mayores_cinco({"A":1,"B":2,"C":3,"D":4,"E":5}))=={"A":1,"B":2,"C":3,"D":4,"E":5}
    assert(mayores_cinco({"A":90,"B":80,"C":70,"D":60,"E":50,"F":40}))=={"A":90,"B":80,"C":70,"D":60,"E":50}

def test_suma_de_valores():
    assert(suma_de_valores({"A":4,"B":66,"C":32,"D":23,"E":45}))==170
    assert(suma_de_valores({"A":1,"B":2,"C":3,"D":4,"E":5}))==15
    assert(suma_de_valores({"A":0,"B":0,"C":0,"D":0,"E":0}))==0

def test_diccionario_factores():
   assert(diccionario_factores(dic(dataset())))=={ 'Driver Inattention': [[40.69953, 40.744892, 40.744892, 40.71755, 40.810177, 40.610268,
                                                                        40.67325], 
                                                                        [-73.91103, -73.77022, -73.77022, -73.76458, -73.93741, -73.9547, 
                                                                         -73.94932]], 
                                                    'Distraction': [[40.69953, 40.744892, 40.744892, 40.71755, 40.810177, 40.610268, 
                                                                     40.67325], 
                                                                    [-73.91103, -73.77022, -73.77022, -73.76458, -73.93741, -73.9547, 
                                                                     -73.94932]], 
                                                    'Backing Unsafely': [[40.6026, 40.610268], [-74.17225, -73.9547]], 
                                                    'Driver Inexperience': [[40.744892, 40.744892, 40.762955, 40.739265], 
                                                                            [-73.77022, -73.77022, -73.831955, -73.99545]], 
                                                    'Following Too Closely': [[40.77304, 40.758327], [-73.83052, -73.957825]], 
                                                    'Unspecified': [[40.77304, 40.875122, 40.875122, 40.73566, 40.8429, 40.75546, 
                                                                     40.702557, 40.702557, 40.758327, 40.758327, 40.786495, 
                                                                     40.799675, 40.799675, 40.719776, 40.71755, 40.826397, 
                                                                     40.637375, 40.851803, 40.851803, 40.714104, 40.64647, 
                                                                     40.64647, 40.68917, 40.67325, 40.829098, 40.739265], 
                                                                    [-73.83052, -73.905174, -73.905174, -73.91521, -73.93843, 
                                                                     -73.88631, -73.96074, -73.96074, -73.957825, -73.957825, 
                                                                     -73.79463, -73.93979, -73.93979, -74.00681, -73.76458, 
                                                                     -73.92116, -73.95947, -73.90922, -73.90922, -73.95322, 
                                                                     -74.01257, -74.01257, -73.74941, -73.94932, -73.81575, -73.99545]], 
                                                    'Unsafe Speed': [[40.65061, 40.799675, 40.822006], [-73.94397, -73.93979, -73.93062]], 
                                                    'Aggressive Driving': [[40.8429, 40.835968, 40.637375], 
                                                                           [-73.93843, -73.869995, -73.95947]], 
                                                    'Road Rage': [[40.8429, 40.835968, 40.637375], 
                                                                  [-73.93843, -73.869995, -73.95947]], 
                                                    'Obstruction': [[40.75546], [-73.88631]], 
                                                    'Debris': [[40.75546], [-73.88631]], 
                                                    'Fatigued': [[40.702557], [-73.96074]], 
                                                    'Drowsy': [[40.702557], [-73.96074]], 
                                                    'Other Vehicular': [[40.835968, 40.810177], [-73.869995, -73.93741]], 
                                                    'Unsafe Lane Changing': [[40.786495], [-73.79463]], 
                                                    'Pedestrian': [[40.719776], [-74.00681]], 
                                                    'Bicyclist': [[40.719776], [-74.00681]], 
                                                    'Other Pedestrian Error': [[40.719776], [-74.00681]], 
                                                    'Confusion': [[40.719776], [-74.00681]], 
                                                    'Failure to Yield Right-of-Way': [[40.762955], [-73.831955]], 
                                                    'View Obstructed': [[40.714104], [-73.95322]], 
                                                    'Limited': [[40.714104], [-73.95322]], 
                                                    'Turning Improperly': [[40.829098], [-73.81575]]}
def test_lista_calles():
    assert(lista_calles({"ON STREET NAME":[1,2,34,45],"CROSS STREET NAME":[3,4,6,12],"OFF STREET NAME":["","","",""]}))==[
        [1,3,""],[2,4,""],[34,6,""],[45,12,""]]
    assert(lista_calles({"ON STREET NAME":[1,2,34,45],"CROSS STREET NAME":["","","",""],"OFF STREET NAME":["","","",""]}))==[
        [1,"",""],[2,"",""],[34,"",""],[45,"",""]]
    assert(lista_calles({"ON STREET NAME":["","","",""],"CROSS STREET NAME":["","","",""],"OFF STREET NAME":["a","b","c","d"]}))==[
        ["","","a"],["","","b"],["","","c"],["","","d"]]

def test_conteo_lista_calles():
    assert(conteo_lista_calles([["hola","",""],["","","adios"],["malos","adios",""]]))=={"hola":1,"adios":1,"Entre malos y adios":1}
    assert(conteo_lista_calles([["hola","",""],["hola","",""],["malos","adios",""]]))=={"hola":2,"Entre malos y adios":1}
    assert(conteo_lista_calles([["malos","adios",""],["malos","adios",""],["malos","adios",""]]))=={"Entre malos y adios":3}

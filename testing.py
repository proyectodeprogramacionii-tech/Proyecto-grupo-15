from proyecto.py import conteo_lista_calles as conteo
from proyecto.py import lista_calles as lista

def test_conteo():
    assert(conteo[["hola","",""],["","","adios"],["malos","adios",""]])=={"hola":1,"adios":1,"entre malos y adios":1}
    assert(conteo[["hola","",""],["hola","",""],["malos","adios",""]])=={"hola":2,"entre malos y adios":1}
    assert(conteo[["malos","adios",""],["malos","adios",""],["malos","adios",""]])=={"entre malos y adios":3}

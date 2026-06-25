from proyecto.py import conteo_lista_calles as conteo
from proyecto.py import lista_calles as lista

def test_conteo():
    assert(conteo([["hola","",""],["","","adios"],["malos","adios",""]]))=={"hola":1,"adios":1,"entre malos y adios":1}
    assert(conteo[["hola","",""],["hola","",""],["malos","adios",""]])=={"hola":2,"entre malos y adios":1}
    assert(conteo[["malos","adios",""],["malos","adios",""],["malos","adios",""]])=={"entre malos y adios":3}
def test_lista():
    assert (lista({"ON STREET NAME":[1,2,34,45],"CROSS STREET NAME":[3,4,6,12],"OFF STREET NAME":["","","",""]})==[[1,3,""],[2,4,""],[34,6,""],[45,12,""]]
    assert (lista({"ON STREET NAME":[1,2,34,45],"CROSS STREET NAME":["","","",""],"OFF STREET NAME":["","","",""]})==[[1,"",""],[2,"",""],[34,"",""],[45,"",""]]
    assert (lista({"ON STREET NAME":["","","",""],"CROSS STREET NAME":["","","",""],"OFF STREET NAME":["a","b","c","d"]})==[["","","a"],["","","b"],["","","c"],["","","d"]]

from libro import Libro
from autor import Autor

def get_list(nombre_fichero):
    f = open(str(nombre_fichero)+".txt", mode="rt", encoding="utf-8")

    texto = f.read()
    #print("Leemos  caracteres: "+texto)
    f.close()   

    dic = {"clave1": "" , "clave2": "" , "clave3": ""}
    
    if str(texto) == " ":
      raise ValueError("El fichero está vacío")
    else:
        for i in range(0, len(texto)):

            if len(texto.split(" ") == 3:
                dic.update({clave3: str(texto.split(" "))})

            if len(texto.split(" ") == 2:
                dic.update({clave2: str(texto.split(" "))})

            if len(texto.split(" ") == 1:
                dic.update({clave1: str(texto.split(" "))})
    return dic





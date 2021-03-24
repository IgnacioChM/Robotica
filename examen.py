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

            if len(texto.split(" ")) == 3:
                dic.update({clave3: str(texto.split(" "))})

            if len(texto.split(" ")) == 2:
                dic.update({clave2: str(texto.split(" "))})

            if len(texto.split(" ")) == 1:
                dic.update({clave1: str(texto.split(" "))})
    return dic



def mas_antiguos(lista, anyo):
    lista_final = []
    for i in lista:

        if i.get_anyo() == anyo or i.get_anyo() < anyo:
            lista_final += i.get_titulo()

        if i.get_anyo() > 2021:
            raise ValueError("Todavía no existe")
        if i.get_anyo() < 1900:
            raise ValueError("Es anterior al 1900")


    return lista_final






# --- main() ---
Libro1 = Libro(au ="Pepe", ti = "PE", an = 2005)
Libro2 = Libro(au ="Jose", ti = "JO", an = 2001)
Libro3 = Libro(au ="Ana", ti = "AN", an = 2004)
Libro4 = Libro(au ="Nadia", ti = "NA", an = 2000)


lista_libros = [Libro1, Libro2, Libro3, Libro4]
mas_antiguo = mas_antiguos(lista_libros, 2001)
print(mas_antiguo)


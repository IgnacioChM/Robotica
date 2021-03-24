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



def get_minimum(lista):
    menor=lista[0]
    for i in range(1,len(lista)):
        if lista[i]<menor:
            menor=lista[i]
    return menor
#---main---
listas = [6,3,8,2,5]
res = get_minimum(listas)
print(res)


def mas_antiguos(lista, anyo):
    for i in lista:
        lista_claves = i.get_anyo()
        if lista_claves == "an":
            print (i.get_anyo())








# --- main() ---
Libro1 = Libro(au ="Pepe", ti = "PE", an = 2000)
Libro2 = Libro(au ="Jose", ti = "JO", an = 2001)
Libro3 = Libro(au ="Ana", ti = "AN", an = 2002)


lista_libros = [Libro1, Libro2, Libro3]
#mas_antiguo = mas_antiguos(lista_libros, 1900)



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
            if len(texto.split(" ") == 1
                dic[] = 1




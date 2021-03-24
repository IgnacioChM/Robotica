class Libro:
  
  """ 
  Características de los libros
  """

  def __init__(self, au, ti, an):
    self.__autor = au
    self.__titulo = ti
    self.__anyo = an

  def get_anyo(self):
        return self.__anyo

    
  def get_titulo(self):
        return self.__titulo
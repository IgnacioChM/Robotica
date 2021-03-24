import unittest
from libro import Libro
from autor import Autor
class Pruebas(unittest.TestCase):
    """ 
    Clase donde se realizan los test
    """

    def test_creacion_objetos_libro(self):
        l1 = Libro1 = Libro(au ="Pepe", ti = "PE", an = 2005)
        self.assertEqual(l1.get_anyo(), 2005)
        self.assertEqual(l1.get_titulo(), "PE")


    #def test_mas_antiguos(self):
 


if __name__ == "__main__":
    unittest.main()
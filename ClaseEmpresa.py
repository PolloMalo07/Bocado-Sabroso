## Aqui ira todo lo resalcionado con todas las sedes que tenga la empresa. 
from ClaseRestaurante import Restaurante

class Empresa:
    def __init__(self, nombre : str):

        if len(nombre.strip()) == 0:
            raise ValueError("la cadena con el nombre de la empresa no puede estar vacía")
        
        self.nombre = nombre.lower()
        self.restaurantes = []

    def agregar_restaurante(self, ciudad: str, dirreccion , horario , cantidad_de_mesas: int):
        if len(ciudad.strip()) == 0 or len(dirreccion.strip()) == 0 or len(horario.strip()) == 0:
            raise ValueError("La ciudad, dirección y horario no pueden estar vacíos")
        
        nuevo_restaurante = Restaurante(ciudad, dirreccion, horario, cantidad_de_mesas)
        self.restaurantes.append(nuevo_restaurante)

    def calcular_cantidad_Restaurantes(self):
        return len(self.restaurantes)
    a

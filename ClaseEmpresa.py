## Aqui ira todo lo resalcionado con todas las sedes que tenga la empresa. 
from ClaseRestaurante import Restaurante

class Empresa:
    def __init__(self, nombre : str):

        if len(nombre.strip()) == 0:
            raise ValueError("la cadena con el nombre de la empresa no puede estar vacía")
        
        self.nombre = nombre.lower()
        self.restaurantes = []
        self.consumo_general = {
            "rapida": 0,
            "tradicional": 0,
            "saludable": 0,
            "gourmet": 0
        }

    def agregar_restaurante(self, ciudad: str, direccion , horario_apertura, horario_cierre , cantidad_de_mesas: int):
        if len(ciudad.strip()) == 0 or len(direccion.strip()) == 0 or len(horario_apertura.strip() or len(horario_cierre.strip())) == 0:
            raise ValueError("La ciudad, dirección y horario no pueden estar vacíos")
        
        nuevo_restaurante = Restaurante(ciudad, direccion, horario_apertura, horario_cierre, cantidad_de_mesas)
        self.restaurantes.append(nuevo_restaurante)

    def calcular_cantidad_Restaurantes(self):
        return len(self.restaurantes)
    

    def registrar_consumo_general(self):
        # Reinicia el consumo general antes de sumar
        self.consumo_general = {
            "rapida": 0,
            "tradicional": 0,
            "saludable": 0,
            "gourmet": 0
        }
        for restaurante in self.restaurantes:
            for categoria, cantidad in restaurante.consumo.items():
                if categoria in self.consumo_general:
                    self.consumo_general[categoria] += cantidad

    def porcentaje_productos_consumidos_por_categoria_general(self):
        
        total = sum(self.consumo_general.values()) # 
        if total == 0:
            print("No hay consumo registrado en ninguna sede.")
            return
        for categoria, cantidad in self.consumo_general.items():
            porcentaje = (cantidad / total) * 100
            print(f"{categoria}: {porcentaje:.2f}%")    

    def calcular_zona_mesas_mas_utilizadas_y_tasa_ocupacion_sedes_general(self):
        todas_las_sedes = self.restaurantes
        if not todas_las_sedes:
            raise ValueError("No hay restaurantes registrados en la empresa.")
        
        uso_mesas_general = {2: {"total": 0, "ocupadas": 0, "libres": 0},
                    4: {"total": 0, "ocupadas": 0, "libres": 0},  
                    8: {"total": 0, "ocupadas": 0, "libres": 0}}
        
        for sede in todas_las_sedes:
            uso_sede = sede.zona_mesas_mas_utilizadas()
            for capacidad in [2, 4, 8]: 
                uso_mesas_general[capacidad]["total"] += uso_sede[capacidad]["total"]
                uso_mesas_general[capacidad]["ocupadas"] += uso_sede[capacidad]["ocupadas"]
                uso_mesas_general[capacidad]["libres"] += uso_sede[capacidad]["libres"]
        zona_mas_utilizada = None
        max_ocupadas = -1
        tasa_ocupacion = 0

        for capacidad, valores in uso_mesas_general.items():
            if valores["ocupadas"] > max_ocupadas:
                max_ocupadas = valores["ocupadas"]
                zona_mas_utilizada = capacidad  
                total = valores["total"]
                tasa_ocupacion = (max_ocupadas / total) * 100 if total > 0 else 0
        
        return zona_mas_utilizada, tasa_ocupacion

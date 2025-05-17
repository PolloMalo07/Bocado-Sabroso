from datetime import datetime
from ClaseMesas import *
from random import randint

class Restaurante:
    def __init__(self, ciudad: str, dirreccion, horario):

        self.ciudad = ciudad
        self.dirreccion = dirreccion
        self.horario = horario
        self.mesas = self.generar_matriz_mesas()
        self.fecha_creacion = datetime.now().date()


    def determinar_mesa_disponible(self, personas: int):
        """
        Busca mesas disponibles que puedan alojar al menos 'personas'.
        Retorna una mesa aleatoria disponible adecuada.
        """
        opciones = []
        for i in range(self.mesas.filas): ##recorre filas
            for j in range(self.mesas.columnas): ##recorre columnas
                mesa = self.mesas.matriz[i][j] ## accede a la mesa
                ##verifica si la mesa no está ocupada y si la capacidad es mayor o igual a la cantidad de personas
                if not mesa["ocupado"] and mesa["capacidad"] >= personas: 
                    opciones.append((i, j)) ## agrega la posición de la mesa a las opciones
        ##si no hay opciones, lanza una excepción
        if not opciones:
            raise ValueError(f"No hay mesas disponibles para {personas} personas")
        ##si hay opciones, selecciona una aleatoria
        ##y retorna la fila y columna de la mesa    
        return opciones[randint(0, len(opciones) - 1)]
    

    def AsignarMesa(self, cantidad_personas: int):
        if cantidad_personas <= 0 or cantidad_personas > 8:
            raise ValueError("La cantidad de personas debe ser entre 1 y 8")
        
        fila, columna = self.determinar_mesa_disponible(cantidad_personas) 
        mesa = self.mesas.matriz[fila][columna]
        if mesa["ocupado"]:
            raise ValueError("La mesa ya está ocupada")
        
        mesa["ocupado"] = True  # Marcar como ocupada
        return mesa["id"]   # Retornar el id de la mesa
    

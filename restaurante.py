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
        self.consumo = {}


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
    

    def liberar_mesa(self, id_mesa: str): #Se le ingresa el id de la mesa que se quiere liberar
        for i in range(self.mesas.filas):
            for j in range(self.mesas.columnas):
                if self.mesas.matriz[i][j]["id"] == id_mesa: #Busca la mesa en la matriz
                    self.mesas.matriz[i][j]["ocupado"] = False #Marca la mesa como no ocupada
                    return
        raise ValueError("La mesa no existe o no está ocupada") #Si no se encuentra la mesa o si está vacía, lanza una excepción
    
    
    def zona_mesas_mas_utilizadas(self):
        uso_mesas = {2: {"total": 0, "ocupadas": 0, "libres": 0},
                    4: {"total": 0, "ocupadas": 0, "libres": 0},  #crea un diccionario para almacenar el uso de las mesas
                    8: {"total": 0, "ocupadas": 0, "libres": 0}}

        for fila in self.mesas.matriz:
            for mesa in fila: #recorre la matriz de mesas
                capacidad = mesa["capacidad"] #obtiene la capacidad de la mesa
                uso_mesas[capacidad]["total"] += 1 #le suma 1 al numero total de mesas de esa capacidad
                if mesa["ocupado"]:
                    uso_mesas[capacidad]["ocupadas"] += 1 #le suma 1 al numero de mesas ocupadas de esa capacidad
                else:
                    uso_mesas[capacidad]["libres"] += 1 #le suma 1 al numero de mesas libres de esa capacidad
        return uso_mesas
    

    ##comentarios antes de la función:
    ##1. las capacidades de las mesas son 2, 4 y 8 y se ejecuta una vez el for para cada una de ellas
    ##2. el diccionario de uso de mesas es un diccionario que almacena la cantidad total de mesas de cada capacidad, la cantidad de mesas ocupadas y la cantidad de mesas libres

    
    def calcular_tasa_ocupacion(self, uso_mesas): #llama al diccionario de uso de mesas
        for capacidad, valores in uso_mesas.items(): #recorre el diccionario de uso de mesas
            total = valores["total"] #obtiene el total de mesas de la capacidad que estamos trabajando
            ocupadas = valores["ocupadas"] #obtiene el total de mesas ocupadas de esa capacidad
            if total > 0: #si el numero total de mesas de la capacidad que estamos trabajando es mayor a 0
                tasa_ocupacion = (ocupadas / total) * 100 #calcula la tasa de ocupación
            else:
                tasa_ocupacion = 0 #si no hay mesas de esa capacidad, la tasa de ocupación es 0
            print(f"Capacidad {capacidad}: Tasa de ocupación: {tasa_ocupacion:.2f}%")

    def agregar_consumo(self, producto: str, precio: float):
        self.consumo[producto] = precio #Agregar el producto y el precio al diccionario

    def calcular_consumo_subtotal(self):
        subtotal = 0
        for producto, precio in self.consumo.items(): #Recorre el diccionario que guarda el consumo
            subtotal += precio #Suma el precio de cada producto al subtotal y lo va acumulando
        return subtotal #Retorna el subtotal
    
    def calcular_propina(self):
        porcentaje_propina = 0.10 #10% de propina
        return self.calcular_consumo_subtotal() * porcentaje_propina #Calcula la propina multiplicando el subtotal por el porcentaje de propina
    
    def calcular_total(self, incluir_propina:str): #Incluir propina o no
        subtotal = self.calcular_consumo_subtotal()
        propina = self.calcular_propina()
        
        if incluir_propina.lower() == "si": #Si se incluye la propina
            return subtotal + propina #Retorna el subtotal más la propina
        else:
            return subtotal #Retorna solo el subtotal si no se incluye la propina
        
    def mostrar_consumo(self, incluir_propina: str):
        print("Consumo:")
        for producto, precio in self.consumo.items(): #Recorre el diccionario que guarda el consumo y muestra el producto y el precio
            print(f"{producto}: ${precio:.2f}")
        print(f"Subtotal: ${self.calcular_consumo_subtotal():.2f}") 
        if incluir_propina.lower() == "si" : #Si se incluye la propina
            print(f"Propina: ${self.calcular_propina():.2f}") #Muestra la propina
        print(f"Total: ${self.calcular_total(incluir_propina):.2f}") #Muestra el total si se incluye la propina o si no se incluye

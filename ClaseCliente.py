from datetime import date

class Cliente:

    def __init__(self, nombre:str, fecha_nacimiento:date, sexo_biológico:str):

        if len(nombre.strip()) == 0:
            raise ValueError("la cadena con el nombre del cliente no puede estar vacía")
        
        if fecha_nacimiento >= date.today():
            raise ValueError("La fecha de nacimiento debe ser anterior a la fecha actual.")
        
        if sexo_biológico not in ("M", "F"):
            raise ValueError("El sexo biológico debe ser 'M' o 'F'.")

        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo_biológico = sexo_biológico

    def calcular_edad_actual_años(self):
        fecha_hoy = date.today()
        edad = None
        restar = 0
        diferencia_años = fecha_hoy.year - self.fecha_nacimiento.year
        diferencia_meses = fecha_hoy.month - self.fecha_nacimiento.month
        diferencia_días = fecha_hoy.day - self.fecha_nacimiento.day
        if diferencia_meses < 0 or (diferencia_meses == 0 and diferencia_días < 0):
            restar = 1
        edad = diferencia_años - restar
        return edad

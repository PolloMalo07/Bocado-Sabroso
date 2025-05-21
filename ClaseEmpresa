## Aqui ira todo lo resalcionado con todas las sedes que tenga la empresa. 
class Empresa:
    def __init__(self):
        self.consumo = {} #Crear un diccionario vacío para almacenar el consumo

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
        
    def mostrar_consumo(self, incluir_propina: bool):
        print("Consumo:")
        for producto, precio in self.consumo.items(): #Recorre el diccionario que guarda el consumo y muestra el producto y el precio
            print(f"{producto}: ${precio:.2f}")
        print(f"Subtotal: ${self.calcular_consumo_subtotal():.2f}") 
        if incluir_propina: #Si se incluye la propina
            print(f"Propina: ${self.calcular_propina():.2f}") #Muestra la propina
        print(f"Total: ${self.calcular_total(incluir_propina):.2f}") #Muestra el total si se incluye la propina o si no se incluye

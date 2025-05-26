
from datetime import datetime, date
from ClaseEmpresa import Empresa
from ClaseRestaurante import Restaurante
from ClaseCliente import Cliente
from funciones import esEntero, esPositivo, pedirNombreyApellido, validar_horario_apertura_cierre

def pedir_fecha_nacimiento():
    while True:
        fecha_str = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            if fecha >= date.today():
                print("La fecha debe ser anterior a hoy.")
            else:
                return fecha
        except ValueError:
            print("Formato incorrecto. Use YYYY-MM-DD.")

def pedir_sexo_biologico():
    while True:
        sexo = input("Ingrese el sexo biológico (M/F): ").strip().upper()
        if sexo in ("M", "F"):
            return sexo
        else:
            print("Solo se permite 'M' o 'F'.")

def menu_empresa():
    nombre_empresa = input("Ingrese el nombre de la empresa: ").strip()
    empresa = Empresa(nombre_empresa)
    while True:
        print("\n--- MENÚ EMPRESA ---")
        print("1. Agregar restaurante")
        print("2. Lista de restaurantes")
        print("3. Registrar consumo general")
        print("4. Ver porcentaje de consumo general")
        print("5. Ver zona de mesas más utilizada y tasa de ocupación general")
        print("6. Administrar restaurante específico")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ciudad = input("Ciudad: ").strip()
            direccion = input("Dirección: ").strip()
            horario_apertura, horario_cierre = validar_horario_apertura_cierre("Ingrese horario apertura y cierre (HH:MM HH:MM): ")
            while True:
                mesas = input("Cantidad de mesas (16, 25, 36, 64): ")
                if mesas in ("16", "25", "36", "64"):
                    mesas = int(mesas)
                    break
                else:
                    print("Solo se permiten 16, 25, 36 o 64 mesas.")
            empresa.agregar_restaurante(ciudad, direccion, f"{horario_apertura}-{horario_cierre}", mesas)
            print("Restaurante agregado.")
        elif opcion == "2":
            print("\nRestaurantes registrados:")
            for idx, r in enumerate(empresa.restaurantes, 1):
                print(f"{idx}. {r.ciudad} - {r.dirreccion} - {r.horario}")
        elif opcion == "3":
            empresa.registrar_consumo_general()
            print("Consumo general registrado.")
        elif opcion == "4":
            empresa.porcentaje_productos_consumidos_por_categoria_general()
        elif opcion == "5":
            try:
                zona, tasa = empresa.calcular_zona_mesas_mas_utilizadas_y_tasa_ocupacion_sedes_general()
                print(f"Zona de mesas más utilizada: {zona} personas, Tasa de ocupación: {tasa:.2f}%")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "6":
            if not empresa.restaurantes:
                print("No hay restaurantes registrados.")
                continue
            print("\nSeleccione el restaurante a administrar:")
            for idx, r in enumerate(empresa.restaurantes, 1):
                print(f"{idx}. {r.ciudad} - {r.dirreccion} - {r.horario}")
            while True:
                seleccion = input("Ingrese el número del restaurante: ")
                if esEntero(seleccion) and 1 <= int(seleccion) <= len(empresa.restaurantes):
                    restaurante = empresa.restaurantes[int(seleccion)-1]
                    menu_restaurante(restaurante)
                    break
                else:
                    print("Selección inválida.")
        elif opcion == "7":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")

def menu_restaurante(restaurante):
    while True:
        print(f"\n--- MENÚ RESTAURANTE {restaurante.ciudad} ---")
        print("1. Asignar mesa")
        print("2. Liberar mesa")
        print("3. Agregar consumo")
        print("4. Ver porcentaje de consumo por categoría")
        print("5. Ver tiempo promedio de permanencia")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            nombre = pedirNombreyApellido("nombre")
            fecha_nac = pedir_fecha_nacimiento()
            sexo = pedir_sexo_biologico()
            cliente = Cliente(nombre, fecha_nac, sexo)
            if cliente.calcular_edad_actual_años() < 18:
                print("Solo se permite el ingreso a mayores de edad.")
                continue
            while True:
                personas = input("Cantidad de personas (2-8): ")
                if esEntero(personas) and 2 <= int(personas) <= 8:
                    personas = int(personas)
                    break
                else:
                    print("Ingrese un número entre 2 y 8.")
            try:
                id_mesa = restaurante.AsignarMesa(personas)
                print(f"Mesa asignada: {id_mesa}")
            except Exception as e: 
                print(f"Error: {e}")
        elif opcion == "2":
            id_mesa = input("Ingrese el ID de la mesa a liberar: ").strip()
            try:
                restaurante.liberar_mesa(id_mesa)
                print("Mesa liberada correctamente.")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "3":
            print("Categorías: rapida, tradicional, saludable, gourmet")
            categoria = input("Ingrese la categoría: ").strip().lower()
            precio = input("Ingrese el precio: ")
            if categoria not in ("rapida", "tradicional", "saludable", "gourmet"):
                print("Categoría no válida.")
                continue
            if not esPositivo(precio):
                print("El precio debe ser positivo.")
                continue
            restaurante.agregar_consumo(categoria, float(precio))
            print("Consumo agregado.")
        elif opcion == "4":
            restaurante.porcentaje_productos_consumidos_por_categoría_sede_específica()
        elif opcion == "5":
            fecha = input("Ingrese la fecha (YYYY-MM-DD): ")
            try:
                promedio = restaurante.tiempo_promedio_permanencia(fecha)
                print(f"Tiempo promedio de permanencia: {promedio:.2f} minutos")
            except Exception as e:
                print(f"Error: {e}")
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    # Iniciar el programa   

    menu_empresa()

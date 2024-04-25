
class Te: # Clase Te
    # Atributo de clase para almacenar los precios
    PRECIOS = {   # Formato: precio
        '300gr': 3000,
        '500gr': 5000
    }

    def __init__(self, sabor, formato): # Constructor de la clase
        self.sabor = sabor # Atributos de instancia
        self.formato = formato # Atributos de instancia

    @staticmethod   # staticmethod para poder usarlo sin necesidad de crear una instancia de la clase
    def obtener_tiempo_recomendacion(sabor): 
        if sabor == 1:                        
            return 3, "Consumir al desayuno" 
        elif sabor == 2:
            return 5, "Consumir al medio día"
        elif sabor == 3:
            return 6, "Consumir al atardecer"
        else:
            return None, "Sabor no válido"

    @staticmethod               # staticmethod para poder usarlo sin necesidad de crear una instancia de la clase
    def obtener_precio(formato): 
        return Te.PRECIOS.get(formato, None)


if __name__ == "__main__": # Punto de entrada al programa
    sabor = int(input("Ingresa el número de sabor (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
    formato = input("Ingresa el formato (300gr o 500gr): ")

    tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor) 
    precio = Te.obtener_precio(formato)

    if tiempo and precio: 
        print(f"Tiempo de preparación: {tiempo} minutos")
        print(f"Recomendación: {recomendacion}")
        print(f"Precio: ${precio}")
    else:
        print("Sabor o formato no válidos. Verifica los valores ingresados.")

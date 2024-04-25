
from te import Te # Importamos la clase Te

def main():  
    sabor = int(input("Ingresa el número de sabor (1: Té negro, 2: Té verde, 3: Agua de hierbas): "))
    formato = input("Ingresa el formato (300gr o 500gr): ")

    tiempo, recomendacion = Te.obtener_tiempo_recomendacion(sabor) 
    precio = Te.obtener_precio(formato)

    if tiempo and precio:   
        print(f"Sabor del té le recomendamos: {recomendacion}")
        print(f"Formato: {formato}")
        print(f"Precio: ${precio}")
        print(f"Tiempo de preparación: {tiempo} minutos")
        print(f"Recomendación: {recomendacion}")
    else:
        print("Sabor o formato no válidos. Verifica los valores ingresados.")

if __name__ == "__main__":  
    main()

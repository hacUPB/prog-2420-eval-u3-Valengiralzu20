#Sistema de reservas de Cinema
def main():
    def mostrar_asientos(sala):
        """Muestra el estado de los asientos en la sala."""
        for fila in range(len(sala)):
            for columna in range(len(sala[0])):
                print("❌" if sala[fila][columna] else "✅", end=" ")
            print()  # Salto de línea al final de cada fila


    def mostrar_cartelera(peliculas):
        """Muestra la cartelera de películas disponibles."""
        print("Cartelera:")
        for index, (pelicula, info) in enumerate(peliculas.items(), start=1):
            # Imprime el índice, el nombre de la película y su información
            print(f"{index}. {pelicula} - Sala: {info['sala']} - Hora: {info['hora']}")
        print()  # Salto de línea después de mostrar la cartelera


    def seleccionar_pelicula(peliculas):
        """Permite al usuario seleccionar una película de la cartelera."""
        mostrar_cartelera(peliculas)
        while True:
            try:
                # Solicita al usuario que ingrese el número de la película
                opcion = int(input("Seleccione el número de la película que desea ver: "))
                # Verifica si la opción ingresada es válida
                if 1 <= opcion <= len(peliculas):
                    # Obtiene el nombre de la película seleccionada
                    pelicula_seleccionada = list(peliculas.keys())[opcion - 1]
                    return pelicula_seleccionada
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                # Maneja el error si la entrada no es un número
                print("Entrada inválida. Ingrese un número.")


    def calcular_precio(hora):
        """Calcula el precio de la entrada según la hora."""
        hora = int(hora.split(":")[0])  # Obtiene la hora de la cadena
        return 6000 if hora < 15 else 12000  # Precio diferente según la hora


    def reservar_asientos(sala):
        """Muestra los asientos y permite reservar uno."""
        mostrar_asientos(sala)

        while True:
            # Solicita al usuario que ingrese la fila y columna del asiento
            fila = int(input("Ingrese el número de fila: "))
            columna = int(input("Ingrese el número de columna: "))

            # Verifica si las coordenadas son válidas
            if 0 <= fila < len(sala) and 0 <= columna < len(sala[0]):
                if sala[fila][columna]:
                    # Si el asiento está reservado, solicita otro
                    print("Asiento no disponible. Seleccione otro.")
                else:
                    # Reserva el asiento y actualiza el estado
                    sala[fila][columna] = True
                    print("Su asiento ha sido reservado.")
                    mostrar_asientos(sala)  # Muestra la matriz actualizada
                    break
            else:
                # Si la ubicación es inválida, solicita una nueva entrada
                print("Asiento inválido. Ingrese otra opción.")


    # Diccionario con las películas disponibles y su información
    peliculas = {
        "La sustancia": {"sala": 1, "hora": "11:00"},
        "Beetlejuice": {"sala": 2, "hora": "16:00"},
        "Venom": {"sala": 3, "hora": "19:00"},
    }

    # Matrices que representan el estado de los asientos en cada sala
    salas = {
        1: [[False, False, False],
            [False, False, False],
            [False, False, False]],
        2: [[False, False, False],
            [False, False, False],
            [False, False, False]],
        3: [[False, False, False],
            [False, False, False],
            [False, False, False]],
    }

    # Programa principal
    while True:
        print("Bienvenido a Cinema UPB")
        print("1. Ver cartelera")
        print("2. Reservar asiento")
        print("3. Salir")

        # Bucle para asegurar que se procese una opción válida
        while True:
            opcion = input("Ingrese una opción: ")
            if opcion in ["1", "2", "3"]:
                break  # Sal del bucle si la opción es válida
            else:
                print("Opción inválida. Por favor, ingrese 1, 2 o 3.")  # Mensaje para opciones no válidas

        if opcion == "1":
            mostrar_cartelera(peliculas)  # Muestra la cartelera
        elif opcion == "2":
            pelicula = seleccionar_pelicula(peliculas)  # Permite seleccionar una película
            sala_seleccionada = peliculas[pelicula]["sala"]  # Obtiene la sala de la película
            reservar_asientos(salas[sala_seleccionada])  # Permite reservar un asiento

            # Calcula y muestra el precio de la entrada
            precio = calcular_precio(peliculas[pelicula]["hora"])
            print(f"El precio de la entrada es: ${precio}")
        elif opcion == "3":
            break  # Sale del bucle y termina el programa

if __name__ == "__main__":
    main()

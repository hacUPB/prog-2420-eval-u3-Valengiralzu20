#HAY QUE ORGANIZAR ESTÁ MUY DESORDENADO, DEMASIADO 
def main():
    def mostrar_asientos(sala):
     for fila in range(len(sala)):
        for columna in range(len(sala[0])):
            print("❌" if sala[fila][columna] else "✅", end=" ")
             print()
      
def mostrar_cartelera(peliculas):
    for pelicula, info in peliculas.items():
        print(f"Película: {pelicula}")
        print(f"  Sala: {info['sala']}")
        print(f"  Hora: {info['hora']}")
        print()

def seleccionar_pelicula(peliculas):
    mostrar_cartelera(peliculas)
    pelicula_seleccionada = input("Ingrese la película que desea ver: ")
    while pelicula_seleccionada not in peliculas:
        print("Película no disponible. Intente nuevamente.")
        pelicula_seleccionada = input("Ingrese el nombre de la película que desea ver: ")
    return pelicula_seleccionada

def calcular_precio(hora):
  
  hora = int(hora.split(":")[0]) 
  if hora < 15: 
    precio = 6000
  else:
    precio = 12000
  return precio

def reservar_asientos(sala):
    mostrar_asientos(sala)

    while True:
       fila = int(input("Ingrese el número de fila: "))
       columna = int(input("Ingrese el número de columna: "))
       
       if 0<= fila <len(sala) and 0<=columna<len(sala[0]):
        if sala [fila][columna]:
            print("Asiento no disponible. Seleccione otro.")
        else:
            sala[fila][columna] = True
            print("Su asiento ha sido reservado.")
            break
       else: 
          sala [fila][columna]=True
          print ("Asiento inválido. Ingrese otra opción.")

peliculas = {
    "La sustancia": {"sala": 1, "hora": "11:00"},
    "Beetlejuice": {"sala": 2, "hora": "16:00"},
    "Venom": {"sala": 3, "hora": "19:00"},
}

salas = {
    1: [[False, True, False],
         [True, True, True],
         [False, False, False]],
    2: [[False, False, False],
         [True, True, False],
         [False, False, False]],
    3: [[True, False, True],
         [True, True, False],
         [False, True, True]]
}

# Programa principal
while True:
    print("Bienvenido al cine")
    print("1. Ver cartelera")
    print("2. Reservar asiento")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        mostrar_cartelera(peliculas)
    elif opcion == "2":
        pelicula = seleccionar_pelicula(peliculas)
        sala_seleccionada = peliculas[pelicula]["sala"]
        reservar_asientos(salas[sala_seleccionada]) #se modifico comas por corchetes 
        mostrar_asientos(salas[sala_seleccionada])
        
        precio= calcular_precio(peliculas[pelicula]["hora"])
        print(f"El precio de la entrada es: ${precio}")
    elif opcion == "3":
        break
    else:
        print("Opción inválida")



if __name__ == "__main__":
    main()

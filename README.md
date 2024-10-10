[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre: Valentina Giraldo Zuluaga
ID: 000464879 

## Cinema UPB 
### Descripción detallada
Explica el problema que elegiste resolver: el problema escogido para resolver fue el sistema de reservas para un cine. Con este programa se busca que el cine pueda tener un control de los asientos que se van vendiendo por películas, se registre el valor de los asientos, el dinero que se va recaudando, y que si un asiento ya esta elegido no permita elegirlo nuevamente, además debe tener en cuenta la tarifa según el horario de la película si es entre 10:00 am a 3:00 es tarifa especial y si es después de las 3:00 pm es tarifa full.  Para simplificar el programa la compra solo se puede realizar en taquilla. 

Justifica la importancia o utilidad de tu programa: el desarrollo de este programa busca gestionar de manera eficiente la venta de entradas. Este programa permitirá al cine llevar un control de los asientos disponibles, registrar las ventas y calcular los ingresos generado. También ayudará a identificar las tarifas según el horario seleccionado. Con todo esto se busca evitar que se venda 2 veces un mismo asiento y se simplifica el proceso de compra en taquilla. 

### Alcance 
Define claramente las funcionalidades que tendrá tu programa: 

-Películas y horarios: hacer un diccionario de películas y crear funciones según la película en la que se definan sala, fecha, hora.

-Distribución de asientos: representar visualmente la distribución de los asientos en cada sala, en la que se indiquen asientos disponibles y ocupados. 

-Cálculo de precio: calcular el precio total de la compra según la hora.

-Registro de ventas: almacenar el registro de ventas de manera que el cine pueda evidenciar cuánto vendió. 
-Emitir un ticket en el cual se muestren detalles de la reserva. 

### Específica que casos o situaciones cubrirá: 
Las situaciones que cubrirá será la de comprar entradas en la cual podrá: seleccionar película, seleccionar horario, seleccionar asiento, calcular el precio según la hora, emitirá los detalles de la reserva.  

### Estructura de datos utilizados 
#### Para la estructura de datos se utilizará: 
-Diccionario para las películas: en la cual se tenga una clave del título de la película, y un diccionario para los valores en el cual se incluya horario, tarifa y sala.

-Una matriz para representar las salas: las filas y columnas representan los asientos y poner un while en el que esté el valor y sea true cuando el asiento está disponible y false cuando está ocupado.

-Conjunto para los asientos ocupados de una película, los elementos serán el numero de asientos ocupados para una película en particular, se debe agregar operaciones con las cuales se permita verificar rápidamente si un asiento está disponible o si ya ha sido reservado. 

### Pseudocódigo 
#### Definición de estructuras de datos
peliculas = {}  # Diccionario de películas

salas = []  # Lista de matrices para las salas

asientos_ocupados = {}  # Diccionario para almacenar los asientos ocupados por película

##### Función para iniciar sistema
def iniciar_sistema():
  #### Para aregar películas al diccionario
  peliculas["Deadpool"] = {"horario": datetime.datetime(2023, 4, 24, 15, 0), "tarifa": "full", "sala": 1}

  #### Crear matrices para las salas
  sala1 = [[True for _ in range(5)] for _ in range(5)]
  salas.append(sala1)

##### Función para mostrar la cartelera
def mostrar_cartelera():
  for pelicula, datos in peliculas.items():
    print(f"{pelicula}: {datos['horario']}, {datos['tarifa']}, Sala {datos['sala']}")

##### Para reservar un asiento 
def reservar_asiento(pelicula, fila, columna):
  if pelicula not in peliculas:
    print("Película no encontrada")
    return


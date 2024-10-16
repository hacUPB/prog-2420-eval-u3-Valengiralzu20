[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre: Valentina Giraldo Zuluaga
ID: 000464879 

## Cinema UPB 
### Descripción 
El problema escogido para resolver fue el sistema de reservas para un cine. Con este programa se busca que el cine pueda tener un control de los asientos que se van vendiendo. En este programa se tendrán varias opciones de películas, varias salas y diferentes horarios. En las condiciones que tendrá el programa es que si el usuario asiste antes de las 3:00 pm tendrá un precio especial. Este programa solo podrá ser controlado por Cinema UPB.

### Utilidad
El desarrollo de este programa busca gestionar de manera eficiente la venta de entradas. Este programa permitirá al cine llevar un control de los asientos disponibles, y calcular el precio según el horario escogido. Permitirá además del control de asientos, tener un control del total acumulado. Con todo esto se busca evitar que no se venda varias veces un mismo asiento y se simplifica el proceso de compra en taquilla. 

### Funcionalidades del programa
-Películas y horarios: hacer un diccionario de películas y crear funciones según la película en la que se definan sala, fecha, hora

-Distribución de asientos: representar visualmente la distribución de los asientos en cada sala, en la que se indiquen asientos disponibles y ocupados.

-Cálculo de precio: calcular el precio total de la compra según la hora

-Registro de ventas: almacenar el registro de ventas de manera que el cine pueda evidenciar cuánto vendió. 
 

### Casos o situaciones que cubrirá 
Las situaciones que cubrirá será la de comprar entradas en la cual podrá: seleccionar película, seleccionar horario, seleccionar asiento, calcular el precio según la hora, y se tendrá un control del total acumulado de las ventas del cine. 
  

### Estructura de datos a utilizar 
-Diccionario para las películas: en la cual se tenga una clave del título de la película, y un diccionario para los valores en el cual se incluya horario, tarifa y sala.

-Una matriz para representar las salas: las filas y columnas representan los asientos y poner un while en el que esté el valor y sea true cuando el asiento está disponible y false cuando está ocupado.

-Conjunto para los asientos ocupados de una película, los elementos serán el numero de asientos ocupados para una película en particular, se debe agregar operaciones con las cuales se permita verificar rápidamente si un asiento está disponible o si ya ha sido reservado. 

### Pseudocódigo 

FUNCION mostrar_asientos(sala)

    PARA cada fila en sala HACER

        PARA cada columna en sala[fila] HACER

            SI sala[fila][columna] ES VERDADERO ENTONCES

                IMPRIMIR "❌"

            SINO

                IMPRIMIR "✅"

            FIN SI

        FIN PARA

        IMPRIMIR SALTO_DE_LINEA

    FIN PARA

FIN FUNCION

FUNCION mostrar_cartelera(peliculas)

    IMPRIMIR "Cartelera:"

    PARA cada pelicula, info EN peliculas HACER

        IMPRIMIR indice, pelicula, info["sala"], info["hora"]

    FIN PARA

    IMPRIMIR SALTO_DE_LINEA

FIN FUNCION

FUNCION seleccionar_pelicula(peliculas)

    mostrar_cartelera(peliculas)

    MIENTRAS VERDADERO HACER

        INTENTAR

            opcion = CONVERTIR_A_ENTERO(entrada_del_usuario)

            SI opcion es válida ENTONCES

                pelicula_seleccionada = pelicula correspondiente a opcion

                RETORNAR pelicula_seleccionada

            SINO

                IMPRIMIR "Opción no válida."

            FIN SI

        EXCEPTO ValorError

            IMPRIMIR "Entrada inválida."

    FIN MIENTRAS

FIN FUNCION

FUNCION calcular_precio(hora)

    hora = OBTENER_HORA_DE_CADENA(hora)

    RETORNAR 6000 SI hora < 15 SINO 12000

FIN FUNCION

FUNCION reservar_asientos(sala)

    mostrar_asientos(sala)

    MIENTRAS VERDADERO HACER

        fila = CONVERTIR_A_ENTERO(entrada_del_usuario)

        columna = CONVERTIR_A_ENTERO(entrada_del_usuario)
        
        SI coordenadas son válidas ENTONCES

            SI sala[fila][columna] ES VERDADERO ENTONCES

                IMPRIMIR "Asiento no disponible."

            SINO

                sala[fila][columna] = VERDADERO

                IMPRIMIR "Su asiento ha sido reservado."

                mostrar_asientos(sala)

                SALIR

            FIN SI

        SINO

            IMPRIMIR "Asiento inválido."

        FIN SI

    FIN MIENTRAS

FIN FUNCION

INICIO DEL PROGRAMA

DEFINIR peliculas COMO diccionario

DEFINIR salas COMO diccionario

MIENTRAS VERDADERO HACER

    IMPRIMIR "Bienvenido a Cinema UPB"

    IMPRIMIR "1. Ver cartelera"

    IMPRIMIR "2. Reservar asiento"

    IMPRIMIR "3. Salir"

    MIENTRAS VERDADERO HACER

        opcion = entrada_del_usuario

        SI opcion en ["1", "2", "3"] ENTONCES

            SALIR

        SINO

            IMPRIMIR "Opción inválida."

        FIN SI

    FIN MIENTRAS

    SI opcion == "1" ENTONCES

        mostrar_cartelera(peliculas)

    SINO SI opcion == "2" ENTONCES

        pelicula = seleccionar_pelicula(peliculas)

        sala_seleccionada = obtener_sala_de(pelicula)

        reservar_asientos(salas[sala_seleccionada])

        precio = calcular_precio(peliculas[pelicula]["hora"])

        IMPRIMIR "El precio de la entrada es:", precio

    SINO

        SALIR

    FIN SI

FIN MIENTRAS

FIN DEL PROGRAMA

# Documentación del proyecto

Acá se pretende documentar el proceso de análisis y el paso a paso para la realización del código, también los inconvenientes presentados durante la elaboración de este. En el archivo README.md se documentó las generalidades y objetivos del programa. 

Para iniciar el proceso de la elaboración del código, inicialmente se empezará realizando por secciones para analizar cómo se utilizarían los elementos. 

1. Se hizo una función la cual mostrará los asientos disponibles y los asientos ocupados. Para esto se creo una función la cual muestre los asientos de la sala y se utilizó condicionales para indicarle al programa que símbolo mostrar si está ocupado o si está disponible. 
Esta función toma como entrada una lista de listas que representa los asientos, luego itera sobre cada fila y columna de la matriz, e imprime x si el asiento esta ocupado (valor True) o ✓ si está disponible (valor False). 
Para ver que la función si funciona se crea una matriz que representa la sala 1 y se ponen los valores True o False para que muestre la sala y la disponibilidad de los asientos. 
Sin embargo, aun el programa no funciona para que a medida que el usuario vaya ingresando las sillas vendidas se muestre la disponibilidad. Por el momento solo sirve para ver como se debería ver la sala a medida que se vayan vendiendo los asientos. 
![Imagen 1](image-12.png)
 
2. Se creó una función para mostrar las opciones de la cartelera, dentro de esta función se creo un diccionario de películas en el cual está el nombre de la película, la hora y la sala. Luego se creó una función para poder seleccionar la película, en esta se utiliza la función anterior y se pide al usuario que ingrese el nombre de la película y devuelve el nombre de la película. 
![Imagen 2](image-13.png)
 
3. Se creó una función que calcule el precio de la entrada según el horario de la película, esta función toma como entrada una cadena de texto que representa la hora de la película, extrae la hora y la convierte en numero entero para facilitar la comparación, hace las respectivas comparaciones y devuelve el valor calculado.
![alt text](image-2.png)
  
4. Se creó una función para reservar asientos, en este se muestra los asientos de la sala seleccionada y pide al usuario que ingrese el número de la fila y columna, valida si el asiento está disponible y actualiza la matriz si está libre. 
![alt text](image-3.png)
 
5. Una vez se crearon las funciones que se deben utilizar en el sistema de reservas de Cinema UPB, se debe crear un programa que integre todas estas. Inicialmente fue un poco complicado porque si bien ya estaban las funciones se debía encontrar la manera de que el programa pudiera hacer todo a la vez. 
6. Se probó cada función por separado para evidenciar que si realizara lo que se requería. Después de esto se creo un bucle en el cual si era True se ejecutara y mostrara un menú de opciones en el que de la bienvenida al cine, permita ver las opciones de película, pueda reservar asiento, o salir del programa. 
7. Cuando se empezó a escribir todo el código completo se presentaron algunos errores y es por esto que se tuvieron que hacer modificaciones en las funciones. Acá se realizó cambios en la función mostrar_asientos. 
![alt text](image-4.png) 

8. En la función reservar_asientos se hicieron varias modificaciones en el bucle de modo que le dijera al usuario si el asiento estaba disponible para poder hacer la reserva o si ya no estaba disponible, también indicaba cuando era un asiento invalido o sea que no está dentro de la matriz. 
![alt text](image-5.png)
 
9. Ahora se escribió el código completo después de hacer modificaciones en las funciones, sin embargo sigue presentando errores, los cuales se identificaron haciendo pruebas de escritorio. El código inicialmente quedó así: 
![alt text](image-6.png)
![alt text](image-7.png)
![alt text](image-8.png)
![alt text](image-9.png)

10. Algunos de los errores que se presentan es que cuando se realiza la prueba de escritorio, se selecciona que se desea hacer una reserva, se selecciona la película, y apenas se hace la selección muestra los asientos disponibles en la sala, a veces así se seleccione un asiento que está disponible el programa muestra que no está disponible. Por lo tanto se debe revisar el código cuidadosamente para poder identificar donde se está presentando el problema. 

11. Realizando más pruebas de escritorio en ocasiones sale un error que dice que se presenta “IndexError: asignación a lista fuera del rango”. Esto pasa cuando se indica que la columna es 3, y este error se presenta con todas las películas. Todos estos errores presentados se están documentando con el fin de poder identificar en qué situaciones se están presentando errores. 


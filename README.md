# Pancake-Profundidad
Este código implementa un algoritmo para resolver el problema de la pila,
que consiste en encontrar la secuencia de movimientos necesarios para ordenar una pila de elementos.
El algoritmo utiliza la búsqueda en profundidad para explorar todas las posibles combinaciones de movimientos y encontrar la solución óptima.
Funciones
generar_movimientos(pila): Esta función genera una lista de todas las posibles combinaciones de movimientos que se pueden realizar en una pila dada. 
Los movimientos se generan invirtiendo una sección de la pila y concatenando el resultado con el resto de la pila.

buscar_solucion_profundidad(pila): Esta función resuelve el problema de la pila utilizando la búsqueda en profundidad. 
Comienza con la pila inicial y realiza movimientos sucesivos hasta encontrar la solución. La función devuelve una lista de movimientos necesarios para ordenar la pila.

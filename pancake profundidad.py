def generar_movimientos(pila):
    n = len(pila)
    movimientos = []
    for i in range(2, n+1):
        # Crea una nueva lista con los primeros i elementos de la pila,
        # los invierte y luego los concatena con el resto de la pila
        movimientos.append(pila[:i][::-1] + pila[i:])
    return movimientos


def buscar_solucion_profundidad(pila):
    # Crea un conjunto para almacenar las pilas que ya han sido visitadas
    visitados = set()
    # Crea una pila que contiene la pila inicial y una lista vacía para almacenar los movimientos
    stack = [(pila, [])]

    # Itera hasta que no hayan más elementos en la pila
    while stack:
        # Obtiene la última pila de la pila de pilas y la lista de movimientos que llevaron a esa pila
        pila_actual, movimientos = stack.pop()

        # Verifica si la pila actual es la pila ordenada, si es así, devuelve la lista de movimientos
        if pila_actual == sorted(pila_actual):
            return [list(mov) for mov in movimientos]

        # Genera todos los posibles movimientos y los agrega a la pila si no han sido visitados
        for movimiento in generar_movimientos(pila_actual):
            if tuple(movimiento) not in visitados:
                visitados.add(tuple(movimiento))
                stack.append((movimiento, movimientos + [movimiento]))

# Ejemplo de uso
pila = ['d', 'b', 'c', 'a']
pila_objetivo = ['a', 'b', 'c', 'd']
solucion = buscar_solucion_profundidad(pila)
print(f"La solución para la pila {pila} es:")
for mov in solucion:
    print(mov)

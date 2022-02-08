def validate (opciones, eleccion):
    while eleccion not in opciones:
        eleccion = input('Ha ingresado una opción no válida. Por favor escoja alguna de las opciones disponibles:')

        return eleccion

    if __name__ == '__main__ ':
        opciones = ['1','2','3']
        eleccion = input('Escoja una Opción:')
        validate (opciones, eleccion)

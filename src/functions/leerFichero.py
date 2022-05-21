# Importes
import os
import codecs

# Funcion para limpiar pantalla
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def datosFichero():
    # Carpeta con los archivos de prueba
    files_dir = f'{os.getcwd()}\\src\\data\\'
    # Contenedor del nombre de los ficheros actuales
    fich = []
    fichero = ''

    # Recorrer la carpeta e imprimir qué archivos tiene
    for base, dirs, files in os.walk(files_dir):
        
        # Recorrer el array que contiene los archivos de forma interna
        for index, file in enumerate(files):
            fich.append({(index+1): file});
    # Limpiando consola
    clearConsole()

    # Ciclo para elegir archivo
    while True:
        print('\n\n\tElegir un fichero:')
        for fichero in fich:
            
            # Ciclo para acceder a cada elemento
            for key in fichero:
                print(f'{key}. {fichero[key]}')

        eleccion = input('\nNumero de Archivo: ')
        
        try:
            eleccion = int(eleccion)
            if eleccion > len(fich):
                clearConsole()
                print('Fichero fuera de rango, intenta de nuevo')
            elif eleccion > 0 and eleccion <= len(fich):
                #  For para acceder al index e info
                for eleccion in fich[(eleccion-1)]:
                    fichero = fich[eleccion-1][eleccion]
                    print(f'Elegiste el fichero: "{fich[eleccion-1][eleccion]}"\n\n')
                break
        except:
            clearConsole()
            print('No valido, prueba nuevamente.\n')

    # Creamos la ruta concatenando lo que tenemos
    ruta = files_dir + fichero

    # Leyendo contenido del archivo
    lector = codecs.open(ruta, 'r', 'utf-8')

    contenido = lector.read()
    lector.close()
    
    return contenido
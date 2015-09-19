__author__ = 'ING26'
from collections import defaultdict

# abrir archivo de texto
text_file = open("Entrado.txt", "r")

# leer el texto y almacenar el contenido en un arreglo
# e ir dividiendo la cadena en bloques despues de las comas
datos = text_file.read().splitlines()

# alacenamos los bloques de datos en sus variables correspondientes
q            = datos[0].split(" ")     # conjunto de estados
sigma        = datos[1].split(" ")      # el alfabeto del lenguaje
inicio       = datos[2].split(" ")[0]   # el estado inicial del automata
                                        # como retorna una lista y es un solo elemento se saca directamente
finales      = datos[3].split(" ")      # conjunto de estados finales del automata
cambios      = datos[4].split(" ")    # arreglo de tabla de transiciones
arregloTemporal = []                    # almacenara la cadena dividida de la tabla de transicion

# recorrer la cadena del archivo para dividir la cadena despues de cada guion medio
for cambio in cambios:
    arregloTemporal.append(cambio.split("-"))

# crear un diccionario para representar la tabla de transiciones
transiciones = defaultdict(dict)
for i in range(0,len(arregloTemporal)):
    # el diccionario tendra la siguiente estructura
    # ej:  transiciones["q0"]["A"] esto retornara el estado que sigue
    # aqui estamos creando las llaves del diccionario para accesar al valor
    # ej: { 'q0' : { 'A' : 'q1' } } en este ejemplo tenemos transicion de q0  a q1 recibiendo el simbolo  A
    transiciones[arregloTemporal[i][0]][arregloTemporal[i][1]] = arregloTemporal[i][2]

# lista de palbras
palabras=["AB","AC","AAA","AAAA","ABBA"]

# Inicializamos la maquina de estados
# asignando el estado de inicio
estadoActual= inicio

###########################################################
# le pasamos la lista de palabras para procesarlos
for palabra in palabras:
    for char in palabra: # obtener un caracter de la palabra
            if char in sigma:
                estadoActual = transiciones[estadoActual][char] #saca los datos de la tabla de transiciones
            else:
                # si el caracter no esta en el alfabeto termina de recorrer la cadena
                # reseteamos el estado
                estadoActual = ""
                break

    # al terminar el escaneo de la cadena verifica el ultimo estado donde se detuvo
    # y hace una comparacion con el conjunto de estados finales
    # si el estado actual esta en el conjunto de estados finales es una cadena reconocida
    # si no es asi, es una cadena no reconocida por el lenguaje.
    if estadoActual in finales:
        print "Palabra "+palabra+" Reconocido"
    else:
        print "Palabra " + palabra+" No Reconocido"

    # resetear la maquina de estados
    # igualando el estado actual con el estado inicial
    estadoActual = inicio
#########################################################

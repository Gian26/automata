__author__ = 'ING26'
from collections import defaultdict
class leerArchivo:
    def __init__(self,archivo):
        # abrir archivo de texto
        self.__text_file      = open(archivo, "r")
        self.__quintupla      = []

    def setTuplas(self):
        datos = self.__text_file.read().split(',')
        self.__quintupla.append(datos[0].split(" ") )     # conjunto de estados
        self.__quintupla.append(datos[1].split(" ") )    # el alfabeto del lenguaje
        self.__quintupla.append(datos[2].split(" ")[0] )  # el estado inicial del automata
                                                            # como retorna una lista y es un solo elemento se saca directamente
        self.__quintupla.append(datos[3].split(" "))      # conjunto de estados finales del automata
        self.__quintupla.append(self.__crearDiccionario(datos[4].split(" ") ))    # arreglo de tabla de transiciones

    def getTuplas(self):
        return self.__quintupla

    def __crearDiccionario(self,cambios):
        arregloTemporal     = []                    # almacenara la cadena dividida de la tabla de transicion
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
        return transiciones

class StateMachine:
    def __init__(self,quintupla):
        #atributos de la clase
        # alacenamos los bloques de datos en sus variables correspondientes
        self.q            = quintupla[0]                # conjunto de estados
        self.sigma        = quintupla[1]                # el alfabeto del lenguaje
        self.inicio       = quintupla[2]                # el estado inicial del automata
                                                        # como retorna una lista y es un solo elemento se saca directamente
        self.finales      = quintupla[3]                # conjunto de estados finales del automata
        self.transiciones = quintupla[4]                # arreglo de tabla de transiciones

        #self.palabras=["AB","AC","AAA","AAAA","ABBA"]   # lista de palbras

    def __transitions(self,estadoActual,char):
        return self.transiciones[estadoActual][char] #saca los datos de la tabla de transiciones

    def validarCadena(self,palabra):
        # Inicializamos la maquina de estados
        # asignando el estado de inicio
        estadoActual = self.inicio

        ###########################################################
        # le pasamos la lista de palabras para procesarlos
        for char in palabra: # obtener un caracter de la palabra
            if char in self.sigma and estadoActual in self.q:
                estadoActual = self.__transitions(estadoActual,char) #saca los datos de la tabla de transiciones
            else:
                # si el caracter no esta en el alfabeto termina de recorrer la cadena
                # reseteamos el estado
                estadoActual = ""
                break

        # al terminar el escaneo de la cadena verifica el ultimo estado donde se detuvo
        # y hace una comparacion con el conjunto de estados finales
        # si el estado actual esta en el conjunto de estados finales es una cadena reconocida
        # si no es asi, es una cadena no reconocida por el lenguaje.
        if estadoActual in self.finales:
            return True
        else:
            return False

archivo = leerArchivo("Entrado.txt")
archivo.setTuplas()

M1 = StateMachine(archivo.getTuplas())
print M1.validarCadena("ABBA")
print M1.validarCadena("AA")
print M1.validarCadena("ABA")
print M1.validarCadena("ABAC")


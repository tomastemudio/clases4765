#=====================================================================
#                  CLASE 8 - MANEJO DE ARCHIVOS Y DATOS
#=====================================================================

# DOS FORMAS DE ABRIR UN ARCHIVO

## funciones del open, close (w, r, a)

## FORMA 1 - open
# archivo_abierto = open('texto.txt', 'w')
# print(type(archivo_abierto))

# archivo_abierto.close() # Para cerrar el archivo.


## FORMA 2 - with open
# with open('texto.txt', 'w') as archivo_abierto:  ## Esto no permite no tener que cerrar el archivo.
    # Trabajamos con el archivo.
# Una vez fuera del with el archivo se cierra solo.

#=========================================================================================================================================
#                                                             WRITE
#=========================================================================================================================================

# USANDO 'W'
## Pisa lo que tiene el archivo

# archivo_abierto = open('clase_8/texto.txt', 'w')    ## Va a buscar la carpeta 'clase_8' con el archivo txt dentro.
# archivo_abierto = open('entregables/texto.txt', 'w')  ## Aca si anda xq mi carpeta 'entregables' existe.

# archivo_abierto = open('clases/clase_8/texto.txt', 'w')              ## Aca si funciona xq el open crea archivos, no crea carpetas.

# archivo_abierto.write("Esto es una prueba\n")
# archivo_abierto.write("Soy otra cosa")              ## Se sobreescribe. La 'w' sobreescribe.
# archivo_abierto.write("Pise el texto")

# archivo_abierto.close()

#------------------------------------------------------------------------------------------------------------------------------------------

# USANDO 'A'
## la 'a' le agrega.

# archivo_abierto = open('clases/clase_8/texto123.txt', 'a')

# archivo_abierto.write("Esto es una prueba\n")
# archivo_abierto.write("Soy otra cosa")              
# archivo_abierto.write("Pise el texto")

# archivo_abierto.close()

#=========================================================================================================================================
#                                                             READ
#=========================================================================================================================================

# read, readlline, readlines

# archivo_abierto = open(r'datos.txt', 'r')
# archivo_abierto = open(r'clases/clase_8/datos.txt', 'r', encoding = "utf-8")   ## Con el encoding me lee caracteres especiales.
# archivo_abierto = open(r'/Users/tomastemudio/Desktop/Python_Coder/texto123.txt', 'r')
# print(type(archivo_abierto))

# print(archivo_abierto.read())      ## El read lee todo el texto pero trabaja con un puntero. Una vez que se ejecuta lo lee y queda el puntero al final. Lo lee solo una vez.
# print(archivo_abierto.read(2)) ## Me devuelve hasta el indice que le indico.
# print('---------------')
# print(archivo_abierto.read())      ## No se imprime el texto entre lineas xq el 'read' solo lee una vez.
# print('---------------')
# print(archivo_abierto.readline())
# print(archivo_abierto.readline())  
# print('---------------')
# print(archivo_abierto.readlines())    ## Genera una lista de cada tipo de oracion.
# print(archivo_abierto.readlines())    ## Si hago dos 'readlines' juntos, el segundo me devuelve una lista vacia xq en el primero el cursor quedo al final.
# print(len(archivo_abierto.readlines())) ## Me aparece cero xq el cursor queda al final.

# archivo_abierto.close()

#------------------------------------------------------------------------------------------------------------------------------------------

# FORMA DE REUTILIZAR UN TEXTO
## El texto esta en una variable, no se esta leyendo desde un archivo abierto

# archivo_abierto = open(r'datos.txt', 'r', encoding = "utf-8")

# texto = archivo_abierto.read()

# print(archivo_abierto.read())
# archivo_abierto.close()

# print('---------------')
# print('---------------')
# print(texto)
# print('---------------')
# print('---------------')
# print(texto)
# print('---------------')
# print('---------------')

#------------------------------------------------------------------------------------------------------------------------------------------

#=========================================================================================================================================
#                                                             SEEK
#=========================================================================================================================================

# FUNCIONALIDAD QUE NOS PERMITE UBICAR EL CURSOR

# archivo_abierto = open('clases/clase_8/datos.txt', 'r', encoding="utf-8")

# print(archivo_abierto.read())
# archivo_abierto.seek(1)            ## Luego de la linea, el texto arranca desde el indice 1.
# print('-------------------')
# print(archivo_abierto.read())

# lineas = archivo_abierto.readlines()
# print(archivo_abierto.readlines())

# archivo_abierto.seek(4)                         ## Siempre hay que tener en cuenta la ubicacion del puntero. El 'seek' ubica el puntero.
# print(archivo_abierto.readlines())

# archivo_abierto.close()

## OTRA FORMA DE ABRIR EL ARCHIVO.
# with open ('clases/clase_8/datos.txt', 'r', encoding="utf-8") as archivo_abierto:
#     print(archivo_abierto.read())
#     archivo_abierto.seek(1)            ## Luego de la linea, el texto arranca desde el indice 1.
#     print('-------------------')
#     print(archivo_abierto.read())


## OTRO EJEMPLO

# archivo_abierto = open('clases/clase_8/datos.txt', 'r', encoding="utf-8")

# lineas = archivo_abierto.readlines()

# archivo_abierto.close()

# nuevas_lineas = []
# for linea in lineas:
#     nuevas_lineas.append(linea.upper())
#     # nuevas_lineas.append(linea.capitalize())
# print(nuevas_lineas)

# archivo_abierto = open('clases/clase_8/datos.txt', 'w', encoding="utf-8")
# # archivo_abierto.write(''.join(nuevas_lineas))
# archivo_abierto.write(nuevas_lineas[0])                 ## Me escribe en el txt solo el primer elemento de la lista 'listas_nuevas'.
# archivo_abierto.close()

#------------------------------------------------------------------------------------------------------------------------------------------

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }

# with open('clases/clase_8/datos_auto.txt', 'w') as archivo:
#     archivo.write(f'{auto["motor"]}\n')
#     archivo.write(f'{auto["color"]}\n')
#     archivo.write(f'{auto["vidrios"]}\n')
#     archivo.write(f'{auto["pasajeros"]}\n')
#     archivo.write(f'{auto.get("Ricardo", "otro valor")}\n')

## DE ESTA FORMA MANTENGO EL FORMATO DEL DICCIONARIO EN EL TXT.
# with open('clases/clase_8/datos_auto.txt', 'w') as archivo:
#     archivo.write('''
# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# ''')

#=========================================================================================================================================
#                                                             JSON
#=========================================================================================================================================


# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }

# lista = [1,2,3,4,5,6,7,8,9]

# import json

# DUMP
## Escribe

# with open('clases/clase_8/mi_archivo.json', 'w') as archivo_para_guardar:
#     json.dump(auto, archivo_para_guardar, indent=4)   ## El primer valor es lo que escribe. El segundo es donde queremos que se guarde. El tercero son los espacios que queremos que tenga.

# with open('clases/clase_8/mi_archivo.json', 'w') as archivo_para_guardar:
    # json.dump(lista, archivo_para_guardar, indent=4) 

#------------------------------------------------------------------------------------------------------------------------------------------
    
# LOAD
## Para leer.

# with open('clases/clase_8/mi_archivo.json', 'r') as archivo_para_leer:
#     datos = json.load(archivo_para_leer)
#     print(datos)
#     print(type(datos))

#------------------------------------------------------------------------------------------------------------------------------------------

# PANDAS

# import pandas as pd

# datos = pd.read_csv('clases/clase_8/dataset_viajes_sube.csv')
# # print(datos)

# # NOT A NUMBER (NaN) ==> null, None

# # print(datos.head())     ## POR DEFECTO NOS MUESTRA LOS PRIMEROS 5 ELEMENTOS.
# # print(datos.head(10))   ## LE PEDIMOS LOS PRIMEROS 10 ELEMENTOS.

# # print(datos.tail())     ## ES COMO EL HEAD PERO DE ABAJO PARA ARRIBA.
# # print(datos.tail(3))

# # print(datos.sample(3))  ## DE TODOS LOS VALORES NOS MUESTRA 3 VALORES RANDOM.

# # print(datos)
# print(datos['TIPO_TRANSPORTE'])                     ## LE PEDIMOS QUE NOS PASE UNA COLUMNA.
# print(datos['TIPO_TRANSPORTE'].value_counts())      ## DENTRO DE CADA VALOR UNICO, ME DICE LA CANTIDAD DE ESTOS QUE HAY.


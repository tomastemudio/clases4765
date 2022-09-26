#=====================================================================
#                  CLASE 7 - METODOS DE COLECCIONES
#=====================================================================

#=========================================================================================================================================
#                                                             STRINGS
#=========================================================================================================================================

# METODO UPPER 

# cadena1 = 'soY la pRimer cadena'
# print(cadena1)
# cadena1_en_mayusculas = cadena1.upper()
# # cadena1 = cadena1.upper()
# print(cadena1)
# print(cadena1_en_mayusculas)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO LOWER

# cadena1 = 'soY la pRimer cadena'
# cadena1_en_minuscula = cadena1.lower()
# print(cadena1)
# print(cadena1_en_minuscula)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO CAPITALIZE

# cadena1 = 'soY la pRimer cadena'
# cadena1_capitalizada = cadena1.capitalize()
# print(cadena1)
# print(cadena1_capitalizada)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO TITLE

# cadena1 = 'soY la pRimer cadena'
# cadean_titulada = cadena1.title()
# print(cadena1)
# print(cadean_titulada)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO COUNT

# cadena1 = 'soY la pRimer cadena'
# cadena1 = 'soY la pRimer cadenaoY  oY'
# print(cadena1.count('oy'))
# print(cadena1.count('oY'))
# print(cadena1.count('a'))
# print(cadena1.count('a', 2))
# print(cadena1.count('a', 2, 16)) ## El tercer valor es hasta donde queremos que busque.

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO FIND
### Busca de izquierda a derecha

# cadena1 = 'soY la pRimer oY cadena'
# print(cadena1.find('oy'))
# print(cadena1.find('oY'))
# print(cadena1.find('oY', 2, 17))  ## Aca me busca del indice 2 al 17
# print(cadena1.find('oY', 2, 14))
# print(cadena1.find('oY', 2, 15))

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO RFIND
### Busca de derecha a izquierda

# cadena1 = 'soY la pRimer oY cadena'
# print(cadena1.rfind('oy'))
# print(cadena1.rfind('oY'))
# print(cadena1.rfind('oY', 1, 4))

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO SPLIT Y JOIN
### El join agrega entre los espacios

# cadena2 = 'segunda cadena al rescate'
# # cadena2_spliteada = cadena2.split()        ## Si no le pasa nada al split me separa por espacios.
# # cadena2_spliteada = cadena2.split('a')  ## Aca el split me separa cada vez que encuentra un 'a'.
# cadena2_spliteada = cadena2.split('ca') ## Aca el split me separa cada vez que encuentra un 'ca'.
# cadena2_spliteada = cadena2.split('q')    ## Como la 'q' no esta, devuelve una lista de solo un entero.
# cadena2_spliteada = list(cadena2)         ## No usamos esto xq no separa por letra.
# print(cadena2)
# print(cadena2_spliteada)

# print('co'.join(cadena2_spliteada))

# lista = ['11','12','13','14','15','16']
# conjunto = {'11','12','13','14','15','16'}
# print(' <-> '.join(lista))
# print(' <-> '.join(conjunto))

# palabra = 'pepe'
# print('123'.join(palabra))
# print(1.join(palabra))            ## Genera error.
# print('123'.join([palabra]))        ## Aca no va a pasar nada.

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO STRIP

# password = input('Ingrese un password: ')
# print(password.strip())                         ## Si lo pasamos asi, saca los espacios.
# print(password)

# print(password.strip('tor'))                    
# print(password.strip())
# print(password)
# print('..dsapepea.sd'.strip('asd'))               ## Saco los ultimos dos. 
# print('..dsapepea.sd'.strip('asd.'))              ## Arranca de izq a derecha. Elimina todo hasta llegar a la p. Luego va al final y va de derecha a izq hasta la e.

# EL STRIP SE DETIENE CUANDO LLEGA A LOS VALORES QUE NO INDICASTE.
# VA SACANDO DE AMBOS LADOS. 

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO REPLACE

# palabra_repetida = 'cadena cadena cadena cadena cadena'
# palabra_repetida_modificada = palabra_repetida.replace('cadena', 'otra')  ## Me reemplaza la palabra 'cadena' por la palabra 'otra'
# print(palabra_repetida)
# print(palabra_repetida_modificada)
# print(palabra_repetida.replace('cadena', 'otra', 3))        ## Aca me lo reemplaza solo 3 veces.

#=========================================================================================================================================
#                                                              LISTAS
#=========================================================================================================================================



## METODO CLEAR

# lista1 = ['primera', 'lista', 2]
# lista2 = ['segunda', 'lista', 2]
# lista1 = []
# lista2.clear()
# print(lista1)
# print(lista2)

#------------------------------------------------------------------------------------------------------------------------------------------

# ## METODO EXTEND

# lista1 = ['primera', 'lista', 2]
# lista2 = ['segunda', 'lista', 2]
# lista1 += lista2
# print(lista1)
# lista1.extend(lista2)
# # lista1.extend('otro')
# print(lista1)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO INSERT

# lista2 = ['segunda', 'lista', 2]
# dicc = {
#     'llave': 'valor'
# }
# print(lista2)
# lista2.insert(1, dicc)   ## Lo inserta en el indice 1.
# print(lista2)
# lista2.insert(3, 'hola')
# print(lista2)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO REVERSE

# lista2 = ['segunda', 'lista', 2]
# print(lista2)
# # lista2 = lista2[::-1]    ## El slicing te crea una lista nueva.
# # print(lista2)
# lista2.reverse()   ## El 'reverse' modifica la lista existente.
# print(lista2)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO SORT

# lista_numeros = [5,1,2,3,4,10]
# lista_numeros.sort()                ## Me modifica la lista ordenando los numeros.
# # lista_numeros.sort(reverse=True)      ## Me ordena de mayor a menor.
# print(lista_numeros)

# lista_numeros = ['5','1','2','3','4','10']
# lista_numeros = ['hola', 'eres', 'pepe']
# lista_numeros.sort()
# print(lista_numeros)
#------------------------------------------------------------------------------------------------------------------------------------------

#=========================================================================================================================================
#                                                               CONJUNTOS
#=========================================================================================================================================


## COPY
### Nos permite copiar un set y generar uno nuevo

# conjunto1 = {1, 'conjunto1', (1, True)}
# # conjunto3 = conjunto1          ## El 'add' termino modificando el conjunto3 y no el conjunto1. Xq les otorgue el mismo valor
# conjunto3 = conjunto1.copy()   ## Me permite generar una copia del conjunto 1.
# print(conjunto3)
# conjunto1.add(456)
# print(conjunto3)
# print(conjunto1)

### listas o tuplas -->> lista2 = lista[:] / tupla2 = [:]
# lista1 = [1,2,3,4,5]
# lista2 = lista1    
# # lista2 = lista1[:]   ## Si utilizo esto me genera un copia de la 'lista1' y me lo guarda en la variable 'lista2'
# print(lista2)
# lista1.append(45)      ## Aca si antes utilize 'lista2 = lista1' cuando modifico la lista1 me va a terminar modificando la lista2 y no quiero eso.
# print(lista2)
# print(lista1)

# # ver foto


#------------------------------------------------------------------------------------------------------------------------------------------

## METODO ISDISJOINT (DISTINTOS)
### Se fija que todos los elemento sean distintos. Si hay uno igual ya me devuelve un 'false'.
### El primero siempre debe ser un set. El segundo puede ser una lista, tupla, otro set.

# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable1 = (1, 'conjunto1', (1, True))

# iterable2 = (1, 'valor2', (2, True))
# print(conjunto1.isdisjoint(iterable2))

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO ISSUBSET
### Pregunta si todos los elementos del conjunto estan en el iterable.
### Compara los valores de un set con los valores de un iterable
### Los iterables son una coleccion de datos.

# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable1 = (1, 'conjunto1', (1, True), 45)

# print(conjunto1.issubset(iterable1))

# iterable2 = (1, 'conjunto1', (1, True))
# print(conjunto1.issubset(iterable2))

# iterable3 = (2, 'conjunto1', (1, True))
# print(conjunto1.issubset(iterable3))

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO ISSUPERSET
### Es la inversa del issubset. Pregunta si el iterable esta dentro del conjunto

# conjunto1 = {1, 'conjunto1', (1, True),32}
# iterable1 = (1, 'conjunto1', (1, True), 45)

# print(conjunto1.issuperset(iterable1))

# iterable2 = (1, 'conjunto1', (1, True))
# print(conjunto1.issuperset(iterable2))

# iterable3 = (2, 'conjunto1', (1, True))
# print(conjunto1.issuperset(iterable3))

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO UNION
### Devuelve un valor nuevo.
### Genera un set nuevo.

# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable1 = (2, 'conjunto1', (1, True), 45)

# conjunto3 = conjunto1.union(iterable1)
# print(conjunto1)
# print(conjunto3)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO DIFFERENCE
### Nos devuelve los datos que son distintos.

# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable1 = (2, 'valor2', (1, True), 45)

# print(conjunto1.difference(iterable1))  ## El 'difference' no modifica el dato base. Nos devuelve un valor nuevo.
# print(conjunto1)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO DIFFERENCE_UPDATE
### Este si modifica el base, con los elementos que esten en el base pero no esten en el otro.

# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)

# conjunto1.difference_update(iterable1)
# print(conjunto1)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO INTERSECCION
### Nos devuelve los elementos que se repiten en los dos. NOS DA ALGO NUEVO.

# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# print(conjunto1.intersection(iterable1))
# print(conjunto1)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO INTERSECTION_UPDATE
### Nos modifica el base con los elementos que se repiten. MODIFICA EL BASE.

# conjunto1 = {1, 'conjunto1', (1, True)}
# iterable1 = (1, 'valor2', (1, True), 45)
# conjunto1.intersection_update(iterable1)
# print(conjunto1)
#------------------------------------------------------------------------------------------------------------------------------------------

#=========================================================================================================================================
#                                                           DICCIONARIOS
#=========================================================================================================================================

## METODO GET
### Nos permite obtener la info de una llave en especial.


# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# # valor1 = auto('motor')
# # print(valor1)
# valor2 = auto.get('color')
# print(valor2)
# valor3 = auto.get('ricardo')   ## Me va devolver un 'none' xq no existe la llave 'ricardo'.
# print(valor3)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO KEYS
### Para pedirle las llaves. Nos devuelve un listado con las llaves del diccionario.

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# print(auto.keys())
# print(list(auto.keys()))
# for llave in auto.keys():    ## Bucle que me muestra valor a valor las llaves que tiene el diccionario.
#     print(llave)

#------------------------------------------------------------------------------------------------------------------------------------------

## METODO VALUES
### Es como el 'keys', solo que me muestra los valores que hay en cada llave.

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# print(auto.values())
# print(list(auto.values()))
# for valor in auto.values():
#     print(valor)
#------------------------------------------------------------------------------------------------------------------------------------------

## METODO ITEMS
### Me permite generar un 'dict_items'. Devuelve una lista de tuplas que dentro tienen la llave y valor.

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# print(auto.items())
# print(list(auto.items()))
# for llave, valor in auto.items():
#     print(f'Para la llave {llave} el valor es {valor}')

#------------------------------------------------------------------------------------------------------------------------------------------

#=========================================================================================================================================
#                                                       EJERCICIO - COLECCIONES 1
#=========================================================================================================================================


# texto = 'gordon lanzó su curva&strawberry ha fallado por un pie! -gritó Joe Castiglione&dos pies -le corrigió Troop&strawberry menea la cabeza como disgustado...-agrega el comentarista'

# lista = texto.split('&')
# print(lista)
# lista[0] = lista[0] + '..'   ## Le agregas dos puntitos en la posicion 0.
# lista2 = []
# for oracion in lista:
#     lista2.append(oracion[0].upper() + oracion[1:])  ## Podemos usar upper o capitalize. Le indica el indice 0 para la primer letra. Dsps le indico que cada oracion continue normalmente.

# texto2 = '.\n- '.join(lista2)   ## \n me hace un salto de linea.
# texto2 += '.'  ## Le agregamos el punto al final.

# print(texto2)
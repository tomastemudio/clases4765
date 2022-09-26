#=====================================================================
#                  CLASE 6 - CONJUNTOS Y DICCIONARIOS
#=====================================================================

# lista = ['soy', 'una', 'lista', 2, True]
# tupla = ('soy', 'una', 'tupla', 2, True)
# conjuntos = {'soy', 'una', 'conjunto', 1, True}

# otros_datos = []
# otros_datos1 = ()
# otros_datos2 = {}
# otros_datos3 = set() ## Me crea un set.
# print(type(otros_datos))
# print(type(otros_datos1))
# print(type(otros_datos2))
# print(type(otros_datos3))


# lista = ['soy', 'una', 'lista', 2, True]
# tupla = ('soy', 'una', 'tupla', 2, True)
# conjunto = {'soy', 'uno', 'conjunto',1, True} ## Por poner el 1, el True no aparece cuando imprimo.
# conjunto1 = {'soy', 'uno', 'conjunto', 1, False} ## Si pongo el 0 no va a aparecer el False.

# lista[1] = 'uno' ## Modificar la posicion 1 de la lista
# print(lista)
# tupla[1] = 'uno' ## Esto genera un error xq la tuplas son inmutables.
# print(tupla)
# conjunto[1] = 'uno' ## No se puede xq los conjuntos no tienen indices.
# print(conjunto)

# print(lista[1])
# print(tupla[1])
# print(conjunto[1])
# print(conjunto) ## Los conjuntos no se guardan como los cargos xq no tienen indices.
# print(conjunto1)

#==============================================================================================================================

# prueba = {1, 2, 3, 'hola', 'como', 'estas'}
# otra_prueba1 = [(1,2,3), [6,7,8]]
# otra_prueba2 = ((1,2,3), [6,7,8])
# otra_prueba3 = {(1,2,3), [6,7,8]} ## Los sets necesitan que los valores que tienen adentro sean inmutables. No puede tener lista adentro.
# print(otra_prueba1)
# print(otra_prueba2)
# print(otra_prueba3)

#==============================================================================================================================

# SET GENRADO CON ITERABLES

# lista_prueba = [1,2,3,'hola','como','estas',['otra','lista']] ## Me va a dar error xq tiene lista adentro.
# lista_prueba = [1,2,3,'hola','como','estas',('otra','lista')]
# conjunto_prueba = set(lista_prueba) 
# tupla_prueba = (1,2,3,'hola','como','estas')
# conjunto_prueba = set(tupla_prueba)
# print(conjunto_prueba)
# conjunto_prueba2 = set(range(10))
# print(conjunto_prueba2)

#==============================================================================================================================

# NO SE REPITEN VALORES

# lista = [1,2,3,4,5,6,6,6,6,6,1,2,3]
# conjunto = [1,2,3,4,5,6,6,6,6,6,1,2,3]
# print(lista)
# # print(conjunto)
# print(set(lista))

#==============================================================================================================================

# FUNCIONES INTEGRADAS

# auto = {'v8', 'Negro', (6,'blindados')}
# # print(auto)

# ## METODO ADD

# lista = [1,2,3,'probando']
# tupla = (1,2,3,'probando')
# # auto.add('descapotable') ## Le agrega valores al set.
# # auto.add(lista) # No se pueden agregar listas
# auto.add(tupla)
# print(auto)

#==============================================================================================================================

# METODO UPDATE

# auto = {'v8', 'Negro', (6,'blindados')}
# lista = ['soy', 'una', 'lista']
# tupla = ('soy', 'una', 'tupla')
# cadena = 'soy una cadena'
# rango = range(15)
# auto.update(lista)
## Esto es lo mismo que:
# auto.add('soy')
# auto.add('una')
# auto.add('lista')

# auto.update(tupla)
# auto.update(cadena)
# auto.update(range)
# print(auto)

#==============================================================================================================================

# FUNCION LEN

# auto = {'v8', 'Negro', (6,'blindados')}
# print(len(auto))

#==============================================================================================================================

# METODO DISCARD
## Nos permite eliminar elementos

# auto = {'v8', 'Negro', (6,'blindados')}
# auto.discard('lista') ## Aca el valor 'lista' no esta pero no se genera un error.
# print(auto)
# auto.add('lista')
# print(auto)
# auto.discard('lista')
# print(auto)

#==============================================================================================================================

# REMOVE
## La dif con discard es que si pongo remove a un elemento que no esta se genera un error.

# auto = {'v8', 'Negro', (6,'blindados')}
# auto.remove('lista') ## Aca se genera un error xq el valor 'lista' no esta en el set.
# print(auto)
# auto.add('lista')
# print(auto)
# auto.remove('lista')
# print(auto)

#==============================================================================================================================

# OPERADOR IN

# auto = {'v8', 'Negro', (6,'blindados')}

# # for dato in auto:
# #     print(dato)

# # print('descapotable' in auto) # Genera booleano
# # print('caño de escape' not in auto) # Genera booleano

# lista = [1,2,3,4]
# print(1 in lista)

#==============================================================================================================================

# METODO CLEAR

# auto = {'v8', 'Negro', (6,'blindados')}
# print(auto)
# auto.clear() # Limpia el set
# print(auto)

# METODO POP

# auto = {'v8', 'Negro', (6,'blindados')}
# print(auto)
# valor = auto.pop() # El pop saca elemento tras elemento. Sada el primer elemento de como para Python quedo ordenado y no de como esta escrito.
# print(auto)
# print(valor)

# while len(auto):
#     print(auto)
#     valor = auto.pop()
#     print(valor)

#==============================================================================================================================

# Ejercicio

# grupo = {'Miguel', 'Blanca', 'Mario', 'Andrés'}
# agregar = ('Ana', 'Ramon', 'Marta', 'David', 'Eric')

# # grupo.update(agregar)
# print(grupo)

# grupo.discard('Mario')
# grupo.discard('Miguel')
# grupo.discard('Esteban') # Si uso remove aca es un error.
# print(grupo)

#==============================================================================================================================
#==============================================================================================================================

# DICCIONARIOS
## Diccionarios tienen un clave y un valor

# dicc = {clave: valor1, clave2: valor2, clave3: valor3}

# auto = {'v8', 'Negro', (6,'blindados')}
# print(auto)
# motor = 'v8'
# color = 'negro'

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# print(auto)

# ACCESO, MUTABILIDAD, ASIGNACION, AGREGADO DE VALORES
# lista = ['soy', 'una', 'lista']
# print(lista[1])
# lista[1] = 24
# print(lista)

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# print(auto['motor'])
# print(auto['caño de escape']) # Error. No esta en el diccionario
# print(auto.get('motor'))
# print(auto.get('caño de escape')) # No me genera erro. Me devuelve un 'none'. 'none' representa la nada misma.
# print(auto.get('caño de escape', input('Que valor por defecto queres: '))) # Si caño de escape no esta me va a mostrar el input.
# print(auto.get('caño de escape', 45)) # Si caño de escape no esta me va a mostrar el 45.

# print(auto)
# auto['motor'] = 'v12' # Me cambia el valor del diccionario que quiero cambiar.
# print(auto['motor']) 
# auto['modelo'] = 2016 # Agrega este elemento al diccionario.
# print(auto)
# auto['pasajeros'] += 1
# print(auto)

#==============================================================================================================================

# FUNCIONES DE DICCIONARIOS

## FUNCION LEN

# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# print(len(auto))

## METODO UPDATE
# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# pepe = (1,2)
# auto.update({pepe: 'valor1', 'llave2': 'valor2', 'motor': 'v12'}) ## Los valores que no estan se agregan y los que ya estan se actualizan si son distintos.
# print(auto)
# print(auto[(1,2)]) ## Me da el valor de la llave que es una tupla.

## FUNCION DEL (para borrar llaves)
# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# del auto['color']
# print('auto')
# del auto('v8')

## OPERADOR IN( busca solo las llaves)
# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# print('motor' in auto)
# print('v8' in auto) # Aca me va a dar mal xq v8 no es una llave.

## METODO CLEAR (nos permite borrar el valor del diccionario)
# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# auto.clear()
# auto = {} ## otra forma de hacerlo
# print(auto)

## METODO POP
# auto = {
#     'motor': 'v8',
#     'color': 'Negro',
#     'vidrios': (6, 'blindados'),
#     'pasajeros': 4,
# }
# print(auto)
# valor = auto.pop() ## Borra el valor que le indiquemos. Si o si nos pide indicarle un valor.
# print(auto)
# print(valor)

# print(auto)
# valor = auto.pop('pasajeros') ## Borra la llave 'pasajeros'
# print(auto)
# print(valor) # Nos devuelve el valor que estaba usando la llave que borramos.

# print(auto)
# valor = auto.pop('ricardo') 
# print(auto)
# print(valor)

# print(auto)
# valor = auto.pop('ricardo', 'este valor sale por defecto si no se encuetra la llave buscada') # Si no esta la primer llave muestra lo que esta dsps de la coma. 
# print(auto)
# print(valor)


#==============================================================================================================================

# Ejercicio Dicts

# animales = {
#     'elefante': ''
# }
# print(animales)
# animales_a_agregar = {
#     'perro': 'Bobby',
#     'tigre': 'Pepe',
#     'mono': 'Homero'
# }

# animales.update(animales_a_agregar)
# print(animales)

# # Modificar una llave
# animales['elefante'] = 'Trompis'
# print(animales)
# animales['delfin'] = 'Manolo' # Me agrega el valor al diccionario.
# print(animales)

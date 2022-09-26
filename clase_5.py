#=====================================================================
#                  CLASE 5 - CONTROLADORES DE FLUJO 2
#=====================================================================

# WHILE
# while True:
#     print('Se ejecuto el print') ## Para cortar el bucle infinito, apreto 'command+C'

#==============================================================================================================================

# Ejemplo 1

# repetir_menu = True # Bandera/flag
# while repetir_menu:
#     print('''
# ==================
#         MENU
# ==================
# 1. Retirar efectivo.
# 2. Cambiar contraseña.
# 3. Salir
# ''')
#     opcion_elegida = input('Ingrese la operacion a realizar: ')
#     if opcion_elegida == '1':
#         print('Retiro efectivo')
#     elif opcion_elegida == '2':
#         print('Cambio la contraseña')
#     elif opcion_elegida == '3':
#         print('Hasta luego!')
#         repetir_menu = False # Si pongo la opcion 3, cuando uso este False me frena la accion. Este comando me frena el bucle.
#     else:
#         print('Vuelva a intentar con una opcion valida')

#==============================================================================================================================\

# Ejemplo 2 

# numeros = [14, 45, 5, 1234, 1, 4, 9, 15, 25]
# valor_extraido = 0
# while valor_extraido != 5:
#     valor_extraido = numeros.pop() # El pop va sacando numeros hasta que se llega hasta el 5 y corta el bucle.
#     print(valor_extraido)

# # Otra forma distinta
# valor_extraido = 0
# while valor_extraido != 5: 
#     print(valor_extraido)
#     valor_extraido = numeros.pop()


# hasta = int(input('Ingrese un numero hasta donde quiera sumar 5: '))
# suma = 0
# while hasta:
#     suma += hasta
#     hasta -= 1
# print(f'La suma es {suma}')

#==============================================================================================================================\

# 'break'   Siempre esta ligado a un 'if'

# edad_perro = 0
# while True:
#     print('Guaua')
#     if edad_perro <= 15:
#         edad_perro += 1 # Se le suma un año al perro cuando su edad es menor o igual a 15
#     else:
#         break # El 'break' corta la ejecucion de nuestro while.


# edad_perro = 1
# while True:
#     print('Guaua')
#     if edad_perro < 5:
#         edad_perro += 1 
#     else:
#         break
#     print('Mas valores')

# edad_perro = 0
# while edad_perro != 5:
#     print('Guaua')
#     edad_perro += 1
#     print('Mas valores')

#==============================================================================================================================

# Continue    Nos permite saltar a la siguente iteracion.
## Este codigo sirve para encontrar los numeros impares desde el 0 al 10

# numero = 0
# while numero < 10:
#     numero += 1
#     if numero%2 == 0: # Para saber si es par.
#         continue # Va a saltear el print(numero) si es par.
#     print(numero)

# print('Sali del while')

#==============================================================================================================================

# pass 

# edad_perro = 0
# edad_gato = 0
# if edad_perro == edad_gato:
#     pass #...
# pass
# print('Estoy fuera del if')
# pass

#==============================================================================================================================
#==============================================================================================================================

# While - else

# condicion = 10
# while condicion:
#     valor1 = 8
#     suma = valor1 + condicion
#     if suma == 20:
#         break
#     print(f'La suma dio un resultado {suma}')
#     condicion -= 1
# else: # nunca pasa por este bloque de codigo porque se corta el while si la suma da 20.
#     print('Pase por el else')
# ## El 'else' se ejecuta cuando el 'while' se termine por sus propios medios.
# variable = 'Aca ya estamos fuera del bucle'
# print(variable)

#==============================================================================================================================

# for (se conoce cantidad de iteraciones)

# for <varuiable> in <coleccion>:
#   <bloque de codigo>

# indice = 0
# lista = [10,9,8,7,6,5,4,3,2,1]
# for dato_de_la_lista in lista: # Toma el primer valor de la lista y la va recorriendo hasta llegar al ultimo valor.
#     valor1 = 10
#     suma = valor1 + dato_de_la_lista
#     print(f'La suma dio un resultado {suma}')

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)
# print(lista)

# Otro ejemplo donde se puede modificar la lista al finalizar el for.
# indice = 0
# lista = [10,9,8,7,6,5,4,3,2,1]
# for dato_de_la_lista in lista: # Toma el primer valor de la lista y la va recorriendo hasta llegar al ultimo valor.
#     valor1 = 10
#     suma = valor1 + dato_de_la_lista
#     print(f'La suma dio un resultado {suma}')
#     list[indice] = dato_de_la_lista * 2
#     indice += 1

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)
# print(lista)

#==============================================================================================================================
#==============================================================================================================================

# Enumerate

# lista = [10,9,8,7,6,5,4,3,2,1]
# for indice, valor_de_la_lista in enumerate(lista):  # Al 'enumerate' le podemos pedir dos variables.
#     valor1 = 10
#     suma = valor1 + valor_de_la_lista
#     print(indice, valor_de_la_lista)    # El 'indice' son las posiciones de los elementos dentro de la lista.
#     print(f'La suma dio un resultado {suma}')
#     lista[indice] = valor_de_la_lista * 2  # Agarra la lista y en el indice agarra el mismo numero que estaba y lo multiplica por dos.

# variable = 'Aca ya estamos fuera del bucle'
# print(variable)
# print(lista)

#==============================================================================================================================
#==============================================================================================================================

# Range    Es esclusivo de numeros.

# lista = [10,9,8,7,6,5,4,3,2,1]

# range(<valor final sin incluirlo>)
# range(<valor final incluido> , <valor final sin incluir>)
# range(<valor final incluido> , <valor final sin incluir>, <saltos>)

# for numero in range(5, 9, 2):   # range(<valor final incluido> , <valor final sin incluir>, <saltos>)
# for numero in range(5, 9):    # range(<valor final incluido> , <valor final sin incluir>)
# for numero in range(5):       # range(<valor final sin incluirlo>)
# for numero in range(9, 5, -2):   # El -2 me genera que retroceda.
#     valor1 = 10
#     suma = valor1 + numero
#     print(f'La suma dio un resultado {suma}')

#==============================================================================================================================
#==============================================================================================================================

# for numero in range(5, 9):
#     # if numero == 7:        ## Llega al 7 y se frena.
#     #     break
#     # if numero == 7:
#     #     continue           ## Salte el 7 y continua.
#     # if numero == 7:        
#     #     pass               ## Llega la 7 y no pasa nada.
#     print(numero)
# else:
#     print('Pase por el else')

# print(list(range(5,9)))

#==============================================================================================================================
#==============================================================================================================================

# sum

# print(sum(range(1,5,2)))   # sum realiza la suma de los valores que ponga dentro de el

#==============================================================================================================================

#========================
#      FIN DE CLASE
#========================
# if True:
#     print('Hola, empece con los if')
#     a = 15
#     b = 14
#     print(a + b)
# print('mas codigo')
# ---------------------------------------------------------------------------------------------------------------------------------

# if False:
#     print('No deberia aparecer')
# ---------------------------------------------------------------------------------------------------------------------------------

# primer_numero = int(input('Ingrese un numero: '))
# segundo_numero = int(input('Ingrese un numero: '))

# if primer_numero < segundo_numero:
#     print('El primer valor es menor al segundo')
# elif primer_numero == segundo_numero:
#     print('Los valores son iguales')
# else:
#     print('El segundo valor es menor al primero')

# if primer_numero < segundo_numero and primer_numero != segundo_numero - 5:
#     print('Se cumplio la condicion compleja')
# ---------------------------------------------------------------------------------------------------------------------------------

## ANIDADO DE UN IF

# primer_numero = int(input('Ingrese un numero: '))
# segundo_numero = int(input('Ingrese un numero: '))

# if primer_numero < segundo_numero:
#     print('Primer numero es menor')
#     if primer_numero == segundo_numero - 3:
#         print('Primer numero es igual a segundo numero menos 3')
# ---------------------------------------------------------------------------------------------------------------------------------

## ELSE

# if True:
#     pass # Significa que tengo codigo pero no hace nada este codigo
# else:
#     ...

# primer_numero = int(input('Ingrese el primer numero: '))
# segundo_numero = int(input('Ingrese el primer numero: '))
# var = 15

# if primer_numero == segundo_numero:
#     print('Son iguales')
#     if primer_numero < var:
#         print('Son mayores a var')
#     else:
#         print('Son menores a var')
# else:
#     print('No son iguales')

# if False:
#     print('Hola')
#     if True: 
#         print('True')
# else:
#     print('Pase por el else')
# ---------------------------------------------------------------------------------------------------------------------------------

## ELIF

# primer_numero = int(input('Ingrese el primer numero: '))
# segundo_numero = int(input('Ingrese el primer numero: '))

# if primer_numero < segundo_numero:
#     print('Primero numero es menor que segundo numero')
# elif primer_numero == segundo_numero:
#     print('Son iguales')
# else:
#     print('Segundo numero es menor que primer numero')

# if primer_numero < 20:
#     print('Es menor a 20')
#     if primer_numero < 30:
#         print('Es menor a 30')
#         if primer_numero < 40:
#             print('Es menor a 40')
#             if primer_numero < 50:
#                 print('Es menor a 50')  ## El problema de esto es que me sale todo junto. Para que salga solo uno mirar lo de abajo(usando elif)

# if primer_numero < 20:
#     print('Es menor a 20')
# elif primer_numero < 30:
#     print('Es menor a 30')
# elif primer_numero < 40:
#     print('Es menor a 40')
# elif primer_numero < 50:
#     print('Es menor a 50')
# else:
#     print('No se cumplio ninguna condicion anterior')
# ---------------------------------------------------------------------------------------------------------------------------------

# nota = 5
# if nota < 4:
#     print('Malo')
# if nota < 7:
#     print('Bueno')
# if nota < 9:
#     print('Muy bueno')
# if nota < 11:
#     print('Excelente')
# else:
#     print('Pone una nota de 0 a 10') ## No seria la manera correcta de hacerlo, xq me salen varias opciones. Forma correcta es la de abajo.

# if nota < 4:
#     print('Malo')
# elif nota < 7:
#     print('Bueno')
# elif nota < 9:
#     print('Muy bueno')
# elif nota < 11:
#     print('Excelente')
# else:
#     print('Pone una nota de 0 a 10')
# ---------------------------------------------------------------------------------------------------------------------------------

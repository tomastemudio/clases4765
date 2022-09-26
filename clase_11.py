#==========================================================================================================================================
#                                                           CLASE 11 - EXCEPCIONES
#==========================================================================================================================================

#=====================================================================
#                           ERRORES DE SINTAXIS
#=====================================================================

# print('pepe)
# prnt('pepe')

#=====================================================================
#                           ERRORES SEMANTICOS
#=====================================================================

# lista = []
# lista.pop()  ## Error de indice xq quiere extraer de algo que no tiene nada.

# print(int(input('Ingrese un numero: '))) ## Me genera un error de valor

#=====================================================================

# EJ 1

# def dividir(a, b):
#     return a/b

# print(dividir(5, 7))
# print(dividir(5, 0)) ## Error de division xq no se puede dividir por 0.

# Escapar del error
# def dividir(a, b):
#     if b == 0:
#         return "none"
#     return a/b

# def dividir(a,b):
#     if b != 0:
#         return a/b

# print(dividir(5, 7))
# print(dividir(5, 0))

#=====================================================================
#                           EXEPCIONES
#=====================================================================

# TRY - EXCEPT

# try:
#     ...     ## Los '...' permiten continuar el bucle sin hacer nada.
# except:
#     ...


# EJEMPLO 1



# def dividir(a, b):
#     try:
#         return a/b
#     except:
#         return 'No se puede dividir por 0.'

# print(dividir(5,1))
# print(dividir(5,0))
# print(dividir('5',1))

# EJEMPLO 2

# valor = 15
# try:
#     valor *= 15
#     print(valor)
#     valor+=15
#     print(valor)
#     valor/=0                ## Aca se genera el error.
#     print(valor)
#     valor-=5
#     print(valor)
#     valor*=15
#     print(valor)
# except:
#     # print('Se genero un error.')
#     ...     ## Si no quiero mostrar un mensaje pongo un pass.

# print('Este mensaje lo quiero mostrar siempre.')  ## Si no tuviera el try-except y hubiese un error, este mensaje no se mostraria.

#=====================================================================

# ELSE

# EJEMPLO 1

# a = 5
# b = 0
# try:
#     valor = a/b
# except:
#     print('No se puede dividir por 0.')
# else:
    # print(f'La division dio como resultado {valor}.')  ## Se ejecuto el 'else' cuando no se genera un error interno en el try.

# EJEMPLO 2

# a = 5
# b = 1
# c = 0
# try:
#     valor = a/b
#     valor /= c      ## El resultado de valor lo divide por c.
# except:
#     print('No se puede dividir por 0.')
# else:
#     print(f'La division dio como resultado {valor}.')

# a = 5
# b = 1
# c = 0
# try:
#     valor = a/b 
# except:
#     # valor = a/c     ## Esto se ejecuta solo cuando haya un error.
#     print('No se puede dividir por 0.')
# else:
#     valor /= c
#     print(f'La division dio como resultado {valor}.')

# a = 5
# b = 1
# c = 0
# try:
#     try:
#         valor = a/b 
#     except:
#         # valor = a/c     
#         print('No se puede dividir por 0.')
#     else:
#         valor /= c
#         print(f'La division dio como resultado {valor}.')
# except:
#     print('Exploto despues del try.')

# EJEMPLO 3

# def dividir(a, b):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por cero')
#     else:
#         print(f'La division dio como resultado{valor}.')

# EJEMPLO 4

# def dividir(a, b, c):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por cero')
#     else:
#         print(f'La division dio como resultado {valor}.')
#         valor /= c

# # Se busca el try mas cercano.
# try:
#     dividir(5, 1, 'c')
# except:
#     print('No se puede acomodar el valor.')

# EJEMPLO 5

# def dividir(a, b, c):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por cero')
#         return 'No se puede dividir por cero'
#     else:
#         print(f'La division dio como resultado {valor}.')
#         return f'La division dio como resultado {valor}.')


# EJEMPLO 6

# while(True):
#     try:
#         n = input('Introduce un numero: ')
#         m = 4
#         if n == "n":
#             break
#         else:
#             n = float(n)
#         print(f'{n}/{m} = {n/m}')
#     except:
#         print('Ha ocurrido un error, introduce bien el numero.')  ## Si entra al except no pasa por el else.
#     else:
#         print('Todo ha funcionado correctamente')
#         break

# EJEMPLO 7

# def par_o_impar(numero):
#     try:
#         if int(numero) % 2 == 0:
#             return("Par")
#         else:
#             return('Impar')
#     except:
#         return 'Debe ingresar un numero'

# print(par_o_impar(input('Ingresame un numero y te digo que es: ')))

#=====================================================================

# FINALLY

# EJEMPLO 1

# def dividir(a, b):
#     try:
#         valor = a/b
#     except:
#         print('No se puede dividir por cero')
#         # return 'No se puede dividir por cero'
#     else:
#         print(f'La division dio como resultado {valor}.')
#         # return f'La division dio como resultado {valor}.')
#     finally:        ## El finally se ejecuta siempre sin importar si pasa por el try o el except.
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal.') 

# dividir(5,0)
# # dividir(5,1)
# # print(dividir(5,0))
# # print(dividir(5,1))

# EJEMPLO 2

# f = open('clase_11/test.txt', 'w')
# try:
#     f.write('Probando')
#     5/0
#     print('Try')
# except:
#     print('Except')
# else:
#     print('else')
# finally:
#     f.close()  ## Aca el finally nos permite siempre cerrar el open.    

#=====================================================================
#                           EXCEPCIONES MULTIPLES
#=====================================================================

# TYPE().__NAME__

# print(5)
# print(type(5))
# print(type(5) == int)
# print(type(5).__name__)
# print(type(5).__name__ == 'int')
# print(type(5.5).__name__ == 'float')
# print(type('5.5').__name__ == 'str')

# EJEMPLO 1

# def dividir(a, b):
#     try:
#         valor = a/b
#     except Exception as error:
#         return 'No se puede dividir por cero'
#     else:
#         return f'La division dio como resultado {valor}.'
#     finally:       
#         print('Yo te paso por aca si te fue bien en la cuenta o si te fue mal.') 

# print(dividir(5, input('Ingrese un numero: ')))


# def dividir(a, b):
#     try:
#         valor = a/b
#         # valor = a/int(b)
#     except Exception as error:    ## En vez de 'error' puedo poner cualquiercosa.
#         # print(type(error).__name__)
#         print(f'{type(error).__name__}: {error}')
#     else:
#         print(f'La division dio como resultado {valor}.')
#     finally:       
#         print('Mensaje del finally.') 

# # dividir(5, input('Ingrese un numero: '))
# dividir(5, int(input('Ingrese un numero: ')))

# EJEMPLO 3
## Cuando entra en un exceot no toma los otros.

# EL PRIMERO DEBE SER EL MAS ESPECIFICO Y ABAJO LOS QUE ABARCAN MAS.
# def dividir(a,b):
#     try:
#         valor = a/b
#         print(valor)
#     except ArithmeticError:
#         print('Paso por el arithmetic')
#     except ZeroDivisionError:
#         print('No se puede dividir por 0')   ## arithmetic es padre del zerodivision. Por eso se muestra el arithmetic.
#     except TypeError:
#         print('No funciona si me pasas strings')
#     except Exception as error:                      ## Si no es ninguno de los de arriba, lo agarra el exception.
#         print(error)
#         print('Soy el exception de adentro de la funcion')
#     else:
#         print(f'La division dio como resultado {valor}.')

# dividir(5,1)
# dividir(5,0)
# dividir(5,'c')

# def dividir(a,b):
#     try:
#         valor = a/b
#         print(valor)
#     except ZeroDivisionError as zero_error:
#         print('No se puede dividir por 0.', zero_error)
#     except TypeError as type_error:
#         print('No funciona si me pasas strings', type_error)
#     except ArithmeticError as arit_error:
#         print('Paso por el arithmetic')
#     #except Exception as base_error:
#      #   print('Error sin manejo desarrollado', base_error)
#     else:
#         print(f'La division dio como resultado {valor}.')

# dividir(5,1)
# dividir(5,0)
# dividir(5,'c')
# dividir(5,'5')


# PODEMOS TRABAJAR POR FUERA ALGO MAS GENERICO. SI ARRIBA NO LO TOMA, VA A SALIR AFUERA.

# def dividir(a,b):
#     try:
#         valor = a/b
#         print(valor)
#     except ZeroDivisionError as zero_error:
#         print('No se puede dividir por 0.', zero_error)
#     except TypeError as type_error:
#         print('No funciona si me pasas strings', type_error)
#     except ArithmeticError as arit_error:
#         print('Paso por el arithmetic')
#     else:
#         print(f'La division dio como resultado {valor}.')

# # dividir(5,1)
# # dividir(5,0)
# # dividir(5,'c')
# # dividir(5,'5')

# try:
#     dividir(5,1)
#     dividir(5, 0)
#     dividir(5, 'c')
#     dividir(5, 2, 0)
# except Exception as error:
#     print('Error sin manejo desarrollado.', error)




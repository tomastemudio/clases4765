#==========================================================================================================================================
#                                                           CLASE 9 - FUNCIONES
#==========================================================================================================================================

# print('Hola')
# len('Hola')
# print(len('Hola'))


# cant_letras = 0
# for letra in 'Hola':
#     cant_letras += 1
# print(cant_letras)


#=========================================================================================================================================

# SINTAXIS DE LAS FUNCIONES

# def NOMBRE(PARAMETROS):
    # SENTENCIAS
    #RETURN [EXPRESION]

# El nombre de una funcion no puede iniciar con un numero.
# El nombre si puede contener numeros.

#=========================================================================================================================================

# def mostrar_palabra():
#     print('Perro')

# # mostrar_palabra()
# # valor_retornado = mostrar_palabra()
# # print(valor_retornado)     ## Me muestra un 'none' xq la funcion no tiene un return.

# nuevo_texto = f'{mostrar_palabra()} es un animal'
# print(nuevo_texto) # Aca me va a dar vacio xq la funcion no tiene un return.

# def retornar_palabra():
#     return('Tomás')

# retornar_palabra()
# valor_retornado = retornar_palabra()
# print(valor_retornado)
# print(type(retornar_palabra()))
# print(retornar_palabra() * 5)

# nuevo_texto = f'{retornar_palabra()} es un nombre'
# print(nuevo_texto)

## EJEMPLO CON LISTA
# def devolver_una_lista():
#     return list(range(6))

# valores = devolver_una_lista()
# print(valores)
# print(valores[1:4])
# print(devolver_una_lista())
# print(devolver_una_lista()[1:4])

#------------------------------------------------------------------------------------------------------------------------------------------

# SCOPE (ALCANCE)


# def sumar_numeros():
#     valor1 = 15
#     valor2 = 56
#     valor3 = 15
#     return valor1 + valor2 + valor3

# # LAS VARIABLES DEFINIDAS DENTRO DE LA FUNCION NO EXISTEN FUERA DE LA FUNCION.
# # EL 'RETURN' LO USAMOS PARA QUE HAYA UNA RELACION CON EL EXTERIOR.

# suma_de_valores = sumar_numeros()
# print(suma_de_valores)

# # LAS FUNCIONES PUEDEN USAR VALORES EXTERNOS.

# valor1 = 4
# def sumar_numeros1():
#     valor2 = 56
#     valor3 = 15
#     return valor1 + valor2 + valor3  # De todas formas la funcion usa el valor1.
# # valor1 = 4  # Es lo mismo ponerlo aca o arriba.

# suma_de_valores1 = sumar_numeros1()
# print(suma_de_valores1)
# print(valor1)

# OTRO EJEMPLO

# valor2 = 5
# def sumar_numeros2():
#     valor1 = 15
#     valor2 = 56
#     valor3 = 15
#     return valor1 + valor2 + valor3 

# suma_de_valores2 = sumar_numeros2()
# print(suma_de_valores2)   ## Va a usar el 15 como valor1. Xq para una funcion tiene mas valor una variable interna que una externa.
# print(valor2)

#------------------------------------------------------------------------------------------------------------------------------------------

# def contar_letras(letras_a_contar):
#     cant_letras = 0
#     for letra in letras_a_contar:
#         cant_letras += 1
#     return cant_letras

# print(contar_letras("Tomas"))

#------------------------------------------------------------------------------------------------------------------------------------------

# MOMENTOS DE UNA FUNCION

# - Definimos la funcion.
# - Llamo a la funcion ejecuta su codigo.
# - Revisa si tiene un return.
# - Si no tiene un return devuelve el 'none' por defecto.
# - Si tiene un return devuelvo lo que tiene a continuacion del return.

#------------------------------------------------------------------------------------------------------------------------------------------

# def desordeno_tus_argumentos(param1, param2, param3, param4, param5):
#     return param3, param5, param4, param2, param1

# print(desordeno_tus_argumentos(1,2,3,4,5))  ## Nos devuelve una tupla.
# print(list(desordeno_tus_argumentos(1,2,3,4,5))) ## Asi nos devuelva una lista.
# valor1 = 23
# print(desordeno_tus_argumentos(1,2,3,4,valor1))

#------------------------------------------------------------------------------------------------------------------------------------------

## DESESTRUCTURAR

# primero, segundo, tercero, cuarto, quinto = (1,2,3,4,5)
# print(primero)
# print(segundo)
# print(tercero)
# print(cuarto)
# print(quinto)


# def desordeno_tus_argumentos(param1, param2, param3, param4, param5):
#     return param3, param5, param4, param2, param1

# print(desordeno_tus_argumentos(1,2,3,4,5))
# primero, segundo, tercero, cuarto, quinto = desordeno_tus_argumentos(1,2,3,4,5)
# # Terminar

#------------------------------------------------------------------------------------------------------------------------------------------

# Ej - Par o Impar

# def par_o_impar(numero):
#     if numero % 2 == 0:
#         return("Par")
#     else:
#         return('Impar')

# print(par_o_impar(int(input('Ingresame un numero y te digo que es: '))))

# # print(par_o_impar(2))
# # print(par_o_impar(3))


#------------------------------------------------------------------------------------------------------------------------------------------

# DESAFIO - AÑO BISIESTO


#==========================================================================================================================================
#                                                           CLASE 10 - FUNCIONES II
#==========================================================================================================================================

#=====================================================================
#                  ARGUMENTOS Y PARAMETROS
#=====================================================================

# Argumento: Es cuando llamamos la funcion
# Parametros: Es cuando definimos la funcion.

# def nombre_funcion(param1, param2):
#     var1 = 5
    #===============================
    # return      # Un return que no tiene nada nos sirve para cortar la ejecucion. Es como un 'break'

    # EJ:

    # suma = param1 + param2 + var1
    # return # Aca como es un return vacio corta la ejecucion.
    # if suma > 30:
    #     return 'Es mayor a 30'
    # return 'Es menor a 30'
    #===============================
    # return param1 + param2 + var1
    #===============================
    # suma = param1 + param2 + var1
    # return suma
    #===============================
    # suma = param1 + param2 + var1
    # if suma > 30:
    #     return 'Es mayor a 30'
    # else:
    #     return 'Es menor a 30'
    
    # ESTO DE ABAJO ES LO MISMO QUE LO DE ARRIBA.

    # suma = param1 + param2 + var1
        # if suma > 30:
    #     return 'Es mayor a 30'
    # return 'Es menor a 30'
    #===============================

# # print(nombre_funcion)
# print(nombre_funcion(5, 25))
# print(nombre_funcion(1, 21))

#------------------------------------------------------------------------------------------------------------------------------------------

#ARGUMENTOS POR POSICION

# def restar(num1, num2):
#     return num1 - num2

# primera_ejecucion = restar(1,5)
# print(f'Primera ejecucion: {primera_ejecucion}')
# segunda_ejecucion = restar(5,1)
# print(f'Segunda ejecucion: {segunda_ejecucion}')
# restar(4) ## Me genera un error xq le pase solo un parametro

#------------------------------------------------------------------------------------------------------------------------------------------

# ARGUMENTOS POR NOMBRE

# def restar(num1, num2):
#     return num1 - num2

# primera_ejecucion = restar(1,5)
# print(f'Primera ejecucion: {primera_ejecucion}')
# segunda_ejecucion = restar(num2=5,num1=1)
# print(f'Segunda ejecucion: {segunda_ejecucion}')

# OTRO EJEMPLO

# def devuelva_iterable(var1, var2, var3, var4, var5):
    # return var1, var2, var3, var4, var5

# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(4,3,1,5,2))
# print(devuelva_iterable(var4=4,var3=3,var1=1,var5=5,var2=2))
# ## Combinados
# print(devuelva_iterable(1,2,3,var5=5,var4=4))
# print(devuelva_iterable(var5=5,var4=4,1,2,3)) ## Esto me da error xq si o si cunado combinamos hay que pasar primero por posicion.
# print(devuelva_iterable(var2=2,3,4,var1=1,5))
# print(devuelva_iterable(1,2,4,var3=3))          ## Le estoy dando al 'var3' dos valores, el '4' y el 'var3=3'.

#------------------------------------------------------------------------------------------------------------------------------------------

# LLAMADAS SIN ARGUMENTOS

# PARAMETROS POR DEFECTO

## De estas forma se genera un error.
# def devuelva_iterable(var1, var2, var3, var4, var5):
#     return var1, var2, var3, var4, var5

# print(devuelva_iterable(1,2,3,4,5))
# print(devuelva_iterable(1,2,3,4))
# print(devuelva_iterable(1,2,3))
# print(devuelva_iterable(1,2))
# print(devuelva_iterable(1))
# print(devuelva_iterable())

## De esta forma no se genera error
# def devuelva_iterable2(var1=1, var2=2, var3=3, var4=4, var5=5):
#     return var1, var2, var3, var4, var5

# print(devuelva_iterable2(1,2,3,4,5))
# print(devuelva_iterable2(1,2,3,4))
# print(devuelva_iterable2(1,2,3))
# print(devuelva_iterable2(1,2))
# print(devuelva_iterable2(1))
# print(devuelva_iterable2())
# print(devuelva_iterable2(5))       ## Sale el '5' en el primero lugar y el resto de los numeros en los siguientes.
# print(devuelva_iterable2(5,15))
# print(devuelva_iterable2(var3=5,var5=15))
# print(devuelva_iterable2(5,var5=15))
# print(devuelva_iterable2(var5=15))

# def restar(num1, num2):
#     return num1 - num2
# primer_ejecucion = restar(15,1)
# print(primer_ejecucion)

# def restar(num1=5, num2=1):
#     return num1 - num2
# primer_ejecucion = restar()
# print(primer_ejecucion)

# def restar(num1, num2=1):
#     return num1 - num2
# primer_ejecucion = restar(15,5)
# print(primer_ejecucion)

# def restar(num1=5, num2=1):
#     return num1 - num2
# primer_ejecucion = restar(num2=10,num1=4)
# print(primer_ejecucion)

# Ejemplo

# print('pepe fort se fue de viaje')
# print('pepe', 'fort','se', 'fue', 'de', 'viaje')
# print('pepe', 'fort','se', 'fue', 'de', 'viaje', sep=',')               ## 'sep' es para separar los valores. Por defecto tiene un espacio.
# print('pepe', 'fort','se', 'fue', 'de', 'viaje', sep=',', end='\n')     ## 'end' por defecto tiene '\n'
# print('pepe', 'fort','se', 'fue', 'de', 'viaje', sep=',', end=' ')
# print('pepe', 'fort','se', 'fue', 'de', 'viaje', sep=',', end=' ')
# print('pepe', 'fort','se', 'fue', 'de', 'viaje', sep=',', end='(estoy al final)')
# print('pepe', 'fort','se', 'fue', 'de', 'viaje', sep=',', end=' ')
# print('pepe', 'fort','se', 'fue', 'de', 'viaje', end='))))(((( ')

#==========================================================================================================================================

# ARGUMENTOS X VALOR Y REFERENCIA

# conjunto1 = {1, 'conjunto1', (1, True)}

# Recordatorio
#Posiciones de disco    |L15||L25|L14|L10|    |

#guarda{1, 'conjunto1', (1,True)} En la posicion L15 de disco
# conjunt1 <--- posicion del disco L15
                           

#==========================================================================================================================================

# PASO POR VALOR

# Ver en debug como funciona
# def cambio(valor):
#     print(valor)
#     valor = 'Otro valor'
#     print(valor)

# valor = 'pepe'
# cambio(valor)
# print(valor)            ## Modificando dentro de la funcion, no modificamos el valor que esta fuera.

#------------------------------------------------------------------------------------------------------------------------------------------

# PASO POR REFERENCIA
## La funcion puede modificar el valor

# def cambio(dato_compuesto):
    # dato_compuesto.pop()            ## El 'pop' si no le paso nada me elimina el ultimo valor de la lista.
    # print(dato_compuesto)

# dato_compuesto = [15, True, 'otro valor']
# cambio(dato_compuesto)              ## Aca si la funcion me modifica el valor que esta afuera.
# print(dato_compuesto)
# cambio(dato_compuesto[:])           ## El '[:]' genera una copia lo cual es equivalente a que pase por valor y la funcion no modifica el valor.
# print(dato_compuesto)
# datos_compuestos2 = dato_compuesto
# datos_compuestos2 = dato_compuesto[:]
# cambio(datos_compuestos2)
# print(datos_compuestos2)

#------------------------------------------------------------------------------------------------------------------------------------------


# def cambio():
#     global valor            ## Le digo que use el valor que esta por fuera.
#     valor = 'pepe'

# valor = 15
# cambio()
# print(valor)

# ## Simular uno con el otro

# def cambio():
#     valor = 'otro valor'
# # completar

#=====================================================================
#                  FUNCIONES INTEGRADAS (BUILT-IN)
#=====================================================================

# int

#round  Para redondear numeros
# print(round(1.4))

#help()  Nos dice para que sirve un comando.

#=====================================================================
#                  ARGUMENTOS INDETERMINADOS
#=====================================================================

# ARGS
## NOS DEVUELVE UNA TUPLA

# def sumar(num1,num2,num3,num4,num5):
#     return sum([num1,num2,num3,num4,num5])          ## A esta funcion solo puedo pasarle 5 parametros.

# suma = sumar(1,5,1,2,3) 
# print(sumar)


# def sumar(*args):               ## Puede ser cualquier palabra, no solo 'args'. Lo importante es el asterisco.
#     print(type(args))
#     print(args)
#     return sum(args)

# suma = sumar(1,5,1,2,3,13,45,67,45,3,23,43,12,67)       ## Puedo sumar la cantidad de valores que quiera
# print(suma)
# suma2 = sumar(1,2,3)
# print(suma2)
# suma3 = sumar(2,2)
# print(suma3)

# OTRO EJEMPLO
## Con strings

# def unir(*valores):
#     print(' '.join(valores))

# unir('Hola', 'Pepe', 'como', 'va', '?')

# OTRO EJEMPLO

# def devuelva_iterable(*args):
#     return args[:15]

# devuelva_iterable(1)
# print(devuelva_iterable(1,1,2,3,4,1,2,3,1,))

#------------------------------------------------------------------------------------------------------------------------------------------

# KWARGS   
## HACE LO MISMO QUE ARGS PERO CON DICCIONARIOS.
## ES UN DICCIONARIO.

# def generar_presentacion(nombre='Pepe', apellido='Grillo', edad=80, profesion='MIAMIIIIII'):
#     return f'Buenas, soy{nombre}{apellido}. Tengo {edad} años. Mi profesion es {profesion}'

# # presentacion = generar_presentacion(apellido = 'forti')
# presentacion = generar_presentacion(apellido='Forti', profesion1='MIAMIIIIII', profesion2='MIAMIIIIIII')  ## Genera un error, no le puedo pasar valores que no estan.
# print(presentacion)

# def generar_presentacion(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#     presentacion = f'Buenas, soy {kwargs.get("nombre", "Pepe")} {kwargs.get("apellido", "Grillo")}. Tengo {kwargs.get("edad", "80")} años. Mi profesion es {kwargs.get("profesion", "grillo")}.'
#     # if 'pepe' in kwargs.keys():
#     #     presentacion += kwargs['pepe']
#     return presentacion

# # presentacion = generar_presentacion(apellido='Forti')
# presentacion = generar_presentacion(apellido='Forti', profesion1='MIAAAAAMIIIIIIIIIIIIIII', profesion2='MIAAAAAMIIIIIIIIIIIIIII', profesion='MIAAAAAMIIIIIIIIIIIIIII', profesion3='MIAAAAAMIIIIIIIIIIIIIII', profesion4='MIAAAAAMIIIIIIIIIIIIIII')
# print(presentacion)

#=====================================================================
#                   EJERCICIO - RELOJ
#=====================================================================

# def reloj(*args):           ## args es una tupla, por eso uso len.
#     if len(args) == 1:
#         seg = args[0] % 60
#         min = args[0] // 60     ## Le pongo dos barras asi me quedan los segundos que sobran. La doble barra divide por entero, no toma decimales.
#         hora = min // 60
#         min %= 60               ## Esto es igual a 'min = min % 60'
#         return f'Los segundos {args[0]} equivalen a {hora} horas, {min} minutos y {seg} segundos'
#     elif len(args) == 3:
#         seg_totales = args[2]
#         seg_totales += args[1] * 60
#         seg_totales += args[0] * 60 * 60
#         return f'{args[0]}:{args[1]}:{args[2]} equivalen a {seg_totales} segundos'
#     else:
#         return 'Solo acepto 1 o 3 valores'


# print(reloj(3600))
# print(reloj(1, 5, 5))

#=====================================================================
#                       RECURSIVIDAD
#=====================================================================

# Tema que no se dio en clase.




# ==========================================================================================================================================
#                                                           CLASE 15 - SCRIPTS, MODULOS Y PAQUETES
# ==========================================================================================================================================

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               ENCAPSULAMIENTO
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# class Auto:
#     def __init__(self, modelo, marca, patente, chasis):
#         self.modelo = modelo
#         # self.marca = marca
#         self.patente = patente
#         # self.chasis = chasis
#         self._marca = marca
#         self.__chasis = chasis
    
#     def __arrancar(self):         ## Nos limita el acceso desde afuera.
#         print('Prrmmm!')
        
#     def podemos_arrancar(self):
#         self.__arrancar()
        
#     def get_chasis(self):
#         # return self.__chasis            ## El auto mismo se pide la informacion del chasis.
#         if self._marca == 'fiat':
#             return self.__chasis
#         else:
#             return 'no se puede mostrar, estas limitado'
        
#     def set_chasis(self, nuevo_valor):
#         if self._marca == 'fiat':
#             self.__chasis = nuevo_valor
#         else:
#             print('no se puede mostrar, estas limitado')
            
#     # def set_chasis(self):
#     #     if self._marca == 'fiat':
#     #         self.__chasis = self.__chasis[1:]
#     #     else:
#     #         print('no se puede mostrar, estas limitado')
        

# auto1 = Auto('uno', 'fiat', 'asd 123', 'AUSHDKBuaqw231323')
# auto2 = Auto('K', 'Ford', 'asd 113', 'AUSHDKBuaqw131323')
# # print(auto1.modelo)
# # print(auto1.marca)
# # print(auto1.patente)
# # print(auto1.chasis)
# # print(auto1._marca)
# # print(auto1.__chasis)         ## No puedo acceder a esta informacion.
# # print(auto1._Auto__patente)
# # print(auto1.get_chasis())
# # print(auto2.get_chasis())
# # auto1.__chasis = 123            ## Esta forma no cambia el chasis.
# # print(auto1.get_chasis())
# # auto1.set_chasis(123)
# # print(auto1.get_chasis())
# # # auto1.set_chasis('Nuevo valor de chasis')

# # auto1.__arrancar()
# auto1.podemos_arrancar()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# Otro ejemplo

# class Cuenta:
#     def __no_es_cero(self, valor):
#         return valor == 0

#     def dividir(self, num1, num2):
#         if self.__no_es_cero(num2):
#             return num1 / num2
#         else:
#             return 'El segundo valor no tiene que ser cero.'

# cuenta1 = Cuenta()
# cuenta1.dividir(1,0)

# EL ENCAPSULAMIENTO NOS PERMITE QUE DESDE AFUERA NO SE PUEDA ACCEDER A LA INFORMACION.

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               SCRIPTS, MODULOS Y PAQUETES
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# import sys

# print(sys.argv)             ## Nos da los argumentos.
# print(type(sys.argv))
# lista_de_argumentos = sys.argv
# print(lista_de_argumentos)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               EJERCICIO APROBEMOS
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# import sys

# # listado_de_argumentos = sys.argv[1:]

# if len(sys.argv[1:]) != 0:        ## Si el listado de argumentos tiene algo entra.

#     valor1 = int(sys.argv[1])
#     valor2 = int(sys.argv[2])

#     if valor1 in range(11) and valor2 in range(11):
#         if (valor1 >= 7 and valor2 >= 7):
#             print('Promocionado')
#         elif (valor1 >= 4 and valor2 >= 4):
#             print('Aprobado pero debe rendir final.')
#         elif valor1 == 3:
#             print('Desaprobado. Debe recuperar el primer parcial.')
#         elif (valor1 < 4 or valor2 < 4):
#             print('Desaprobado. Debe recuperar el segundo parcial.')
#         elif (valor1 < 4 and valor2 < 4):
#             print('Desaprobo ambos parciales, debe recursar.')
        
# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               MODULOS
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# NOS SIRVE PARA SEPARAR CIERTAS UTILIDADES POR RUBRO DE CADA UTILIDAD. EJ: UTILIDADES DE CUENTAS.

## Formas de escribirlo
'''
impor modulo
from modulo import algo, otra_cosa
from modulo import algo as algo_llamado_distinto
from modulo import *
'''

# import mis_funcionalidades

# print(mis_funcionalidades.sumar(2,2))

# persona1  = mis_funcionalidades.Persona('Ricardo')
# print(persona1.nombre)
#--------------------------------------------------------------------------------------------------------------------------------
# DE MANERA MAS ESPECIFICA

# from mis_funcionalidades import sumar, Persona

# print(sumar(2,2))

# persona1 = Persona('Ricardo')
# print(persona1.nombre)
#--------------------------------------------------------------------------------------------------------------------------------
# OTRA FORMA
# from mis_funcionalidades import *  # Nos trae todo lo que tiene el modulo. Esto nos puede generar un problema xq puede ser que dentro de mi modulo tenga cosas que se llaman igual que ne mi codigo.

# sumar = 5    # Nos genera un error de esta forma xq estoy importando todo del modulo y ahi dentro ya tengo un sumar. Con este sumar piso el del modulo.

# print(sumar(2,2))

# persona1 = Persona('Ricardo')
# print(persona1.nombre)
# #--------------------------------------------------------------------------------------------------------------------------------
# # OTRA FORMA
# from mis_funcionalidades import sumar, Persona

# sumar = 5  # Aca se sigue pisando xq tiene el mismo nommbre.

# print(sumar(2,2))

# persona1 = Persona('Ricardo')
# print(persona1.nombre)
#--------------------------------------------------------------------------------------------------------------------------------
# OTRA FORMA
# from mis_funcionalidades import sumar as sumar_de_mi_modulo, Persona   ## Con un 'as' no se genera el error anterior.

# sumar = 5 

# print(sumar_de_mi_modulo(2, 2))

# persona1 = Persona('Ricardo')
# print(persona1.nombre)


# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               PAQUETES
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# SON UN CONJUNTO DE MODULOS PARA QUE QUEDEN MAS ORGANIZADOS.
## Creamos una carpeta donde van los modulos

# from matematicas.resta import restar

# print(restar(5, 3))
## Esto se puede hacer de todas las maneras que vimos en el ejemplo anterior.

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               PAQUETES REDISTRIBUIBLES
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# PAQUETES QUE CREAMOS Y OTROS PUEDEN USAR.

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               COLLECTIONS
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# from collections import namedtuple, Counter

# # Pescado = namedtuple('Pescado', ['nombre', 'especie', 'peso'])

# # pescado1 = Pescado('pecesin', 'payaso', 200)

# # print(Pescado)
# # print(pescado1)
# # print(pescado1.nombre)
# # print(pescado1[0])
# # print(pescado1._asdict())
# # print(list(pescado1))

# print(Counter('abcabc123'))
# print(Counter(1,2,3,4,5,3,5,7,8,9,1,1,1,2,2))

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# MATH

# import math

# print(math.pi)
# print(math.sqrt(64))
# print(round(3.8))
# print(math.floor(3.8))   ## Sea lo que sea lo tira para abajo.
# print(math.ceil(3.3))    ## Sea lo que sea lo tira para arriba.

# ------------------------------------------------------------------------------------------------------------------------------------------------------
# RANDOM

# import random

# # print(random.randrange(15, 22, 2))   ## El tercero dice que pega saltos de a dos. En este caso no me da los pares.
# # print(random.randrange(15))
# # print(random.randrange(15, 22))
# # print(random.randrange(15, 22, 1))

# lista = ['hoy', 'corri', '4', 'kilometros']

# # print(random.choice(lista))
# print(random.choices(lista))        ## 'choices' pasa 1 por default.
# print(random.choices(lista, k=2))
# print(random.choices(lista, k=3))   ## Nos devuelve la cantidad que le pasamos en 'k'
# print(random.choices(lista, k=4))


#==========================================================================================================================================
#                                                           CLASE 12 - PROGRMACION ORIENTADA A OBJETOS - I
#==========================================================================================================================================

# ESTO ES PARTE DEL CODIGO DE LA CLASE 13

#=====================================================================
#                           DEFINIENDO E INSTANCIAR UNA CLASE
#=====================================================================



# '''
# class Auto:
#     ... # pass

# auto1 = Auto()
# auto2 = Auto()
# '''

# def funcion():
#     return 'valor'

# valor = funcion()
# print(valor)


# class ClaseAuto:    ## Para las clases se usa PascalCase.
#     ...

# auto1 = ClaseAuto()
# auto2 = ClaseAuto()

# # print(type(2))
# # print(type(auto1))
# # print(type(auto2))
# print(auto1)
# print(auto2)
# print(id(auto1))
# print(id(auto2))

#=====================================================================
#                                   BASE SOBRE METODOS
#=====================================================================

# ACA LOS AUTOS HACEN LO MISMO

# class ClaseAuto:

#     def tocar_bocina(self):        ## 'self' -->  TODO METODO DE INSTANCIA PRECISA QUE TENGA UN 'SELF' PRIMERO.
#         print('Pii pii!')          ## El self genera lo mismo que  --> 'tocar_bocina(auto1)'.

#     def describir_auto(self):      ## El 'self' va a referenciar al objeto que este pidiendo la funcion.
#         return f'Este es un auto.'

# # La 'instancia' se denomina al obejto en si --> Objeto especifico.
# # Una instancia de una clase es un objeto especifico que se creo con esa clase.
# # La clase es la receta, el objeto el resultado.

# auto1 = ClaseAuto()
# auto2 = ClaseAuto()

# auto1.tocar_bocina()
# print(auto1.describir_auto())

# auto2.tocar_bocina()
# print(auto2.describir_auto())

#=====================================================================
#                                   ATRIBUTOS
#=====================================================================

# ATRIBUTOS DE INSTANCIA
## VA RELACIONADO AL OBJETO

# class FordK:
    
#     def __init__(self, color, puertas):   ## El self representa al objeto.
#         self.color = color         ## Si o si necesita definir estos atributos de instancia para saber a quien se lo estoy agregando.
#         self.puertas = puertas

# # auto1 = FordK()  ## Nos va a pedir que le pasemo color y puertas --> Esto pasa xq el metodo '__init__' se llama constructor.
# # auto2 = FordK()  ## Nos va a pedir que le pasemo color y puertas --> Esto pasa xq el metodo '__init__' se llama constructor.

# #SIN EL __INIT__ TODO ESTO GENERA UN ERROR.

# auto1 = FordK('Negro', 4)
# print(auto1)
# print(f'Color: {auto1.color}')
# print(f'Cantidad de puertas: {auto1.puertas}')

# auto2 = FordK('Rojo', 2)
# print(auto2)
# print(f'Color: {auto2.color}')
# print(f'Cantidad de puertas: {auto2.puertas}')

# Para poder crear atributos de instancia necesitamos el constructor(__init__).





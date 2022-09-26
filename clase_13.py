# ==========================================================================================================================================
#                                                           CLASE 13 - PROGRMACION ORIENTADA A OBJETOS - II
# ==========================================================================================================================================

# DEFINIENDO E INSTANCIAR UNA CLASE

# '''
# class Auto:
#     ...#pass

# auto1 = Auto()
# auto2 = Auto()
# '''

# def funcion():
#     return 'valor'

# valor = funcion()
# print(valor)

# =====================================================================
#                           ATRIBUTOS DE INSTANCIA                                  
# =====================================================================

# '''
# class Auto:
#     def __init__(self,modelo,marca):
#         self.modelo = modelo
#         self.marca = marca
# '''



# VALORES POR DEFECTO                                  


# class FordK:

    # def __init__(self, color = 'verde', puertas = 5):  ## No necesariamente tengo que pasarle un color o puertas. Mirar linea abajo.
    # def __init__(self, color, puertas):     
    #     self.color = color
    #     self.puertas = puertas

#     def tocar_bocina(self, *sonidos):    ## Aca tiene un *kwargs
#         print("pi piii")

#     def describir_autos(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas = 2)
# auto4 = FordK('Rojo')
# auto5 = FordK()
# auto6 = FordK(input('ingrese un color: '), 2)

# print(auto1.color, auto1.puertas)
# print(auto2.color, auto2.puertas)
# print(auto3.color, auto3.puertas)
# print(auto4.color, auto4.puertas)
# print(auto5.color, auto5.puertas)
# print(auto6.color, auto6.puertas)

# =====================================================================
#                           ATRIBUTOS DE CLASE                                 
# =====================================================================

# ES UN ATRIBUTO QUE son iguales para todos.

# class FordK:

#     cant_ruedas = 4    ## Este es el atributo de clase. Todos mis autos creados van a tener esta informacion.

#     def __init__(self, color = 'verde', puertas = 5):
#         self.color = color
#         self.puertas = puertas   ## Con el self es exclusivo del objeto.

#     def tocar_bocina(self):    
#         print("pi piii")

#     def describir_autos(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

# auto1 = FordK('Negro', 4)
# auto2 = FordK('Rojo', 2)
# auto3 = FordK(puertas = 2)
# auto4 = FordK('Rojo')
# auto5 = FordK()

# print(auto1.color, auto1.puertas, auto1.cant_ruedas)
# print(auto2.color, auto2.puertas, auto2.cant_ruedas)
# print(auto3.color, auto3.puertas, auto3.cant_ruedas)
# print(auto4.color, auto4.puertas, auto4.cant_ruedas)
# print(auto5.color, auto5.puertas, auto5.cant_ruedas)

# print(FordK.cant_ruedas)  ## Este si me lo devuelve xq todos los objetos creados lo tienen.
# print(FordK.color)   ## El color no me lo da xq es especifico de cada objeto.


# =====================================================================
#                                   METODOS                                 
# =====================================================================

# class FordK:

#     cant_ruedas = 4    ## Este es el atributo de clase. Todos mis autos creados van a tener esta informacion.

#     def __init__(self, color = 'verde', puertas = 5):
#         self.color = color
#         self.puertas = puertas 
#         self.metros_recorridos = 0
#         self.fabricar()                 ## Dentro de un metodo puede llamar a otro metodo
#         self.toco_bocina = False        ## Aca esta bien. Si quiero tener un atributo, tiene que estar en el constructor.

#     def tocar_bocina(self):    
#         print("pi piii")
#         # self.toco_bocina = True        ## Aca esta mal

#     def describir_auto(self):
#         return f'Este auto tiene {self.puertas} puertas y es de color {self.color}'

#     def __str__(self):    ## Me muestra lo que yo le defini y no le determinado por python.
#         return self.describir_auto()

#     def fabricar(self):
#         print(f'Se fabrico un ford k {self.color} de {self.puertas} puertas.')

#     def avanzar(self, metros):
#         print(f'El auto avanzo {metros} metros')
#         self.metros_recorridos += metros

# auto1 = FordK('Negro', 4)
# print(auto1)
# # print(auto1.toco_bocina)
# # auto1.tocar_bocina()
# # print(auto1.describir_auto())


# auto1 = FordK('Negro', 4)
# auto1.tocar_bocina()
# auto1.avanzar(15)
# print(auto1.metros_recorridos)

# LOS ATRIBUTOS SE INICIALIZAN SIEMPRE EN EL CONSTRUCTOR.


# =====================================================================
#                                   EJ 1 - Mi primer clase                                 
# =====================================================================

# =====================================================================
#                                   MAGIC METHODS                                 
# =====================================================================

# NUESTRO EJEMPLO

# # Repaso diccionarios

# dicc = {
#     'llave1': 'valor1',
#     'llave2': 'valor2',
#     'llave3': 'valor3',
#     'llave4': 'valor4',
# }

# print(type(dicc))
# print(dicc)
# # print(len(dicc))
# # print(dicc['llave2'])
# # dicc['llave2'] = 'valor nuevo de la llave 2'
# # print(dicc['llave2'])

# # for llave, valor in dicc.items():
# #     print(f'La llave {llave} contiene el valor {valor}')
# print('===='*20)

# class MiDic:

#     def __init__(self, **kwargs):     ## Le paso el kwargs para poder hacerlo con varias cosas.
#         self.llaves = []
#         self.valores = []
#         if len(kwargs) > 0:   ## Para saber si el diccionario tiene valores guardados.
#             for llave, valor in kwargs.items():   ## El 'items' de un diccionario me devuelve una tupla que tenia un llave y el valor.
#                 self.llaves.append(llave)
#                 self.valores.append(valor)

    
#     def __str__(self):   ## self xq es un metodo de instancia. 'str' me permite que mi clase se vea como yo quiero y no me muestra lo predefinido por python.
#         return f'MiDic'

#     def __len__(self):   ## Me devuelve el largo de mi clase.
#         return  len(self.llaves) ## Xq mi cantidad de llaves es igual a mi cantidad de valores.

#     def __getitem__(self, llave):   ## Este metodo necesita el 'self' y un parametro. El parametro me ubica la informacion que quiero obtener.
#         index_valor = self.llaves.index(llave)  ## A mi colleccion de llaves busco en que indice esta la llave que me piden que devuelva.
#         return self.valores[index_valor]

#     def __setitem__(self, llave, valor_nuevo): ## No necesita tener un return xq es para configurar. Necesita el 'self', dsps el indice y por ultimo el valor nuevo.
#         index_valor = self.llaves.index(llave)  ## Me permite saber en que indice esta el valor que quiero modificar.
#         self.valores[index_valor] = valor_nuevo

#     def __iter__(self): ## Solo necesita el self
#         for llave in self.llaves:
#             yield llave    ## Nos permite devolver un valor pero quedo como estancado. Arranca desde donde habia quedado y sigue al proximo ciclo.
#             ## Devuelve cada valor del 'for' sin cortarlo como si haria un 'return'.
#             ## El 'yield' queda esperando en el ultimo valor que tomo y luego sigue al proximo en la iteracion.


# midic1 = MiDic(
#     llave1 = 'valor1',
#     llave2 = 'valor2',
#     llave3 = 'valor3',
#     llave4 = 'valor4'
# )

# print(midic1)
# print(len(midic1))
# print(midic1['llave2'])
# midic1['llave2'] = 'valor nuevo de la llave 2.'
# print(midic1['llave2'])

# for llave in midic1:
#     print(f"La llave '{llave}' contiene el valor '{dicc[llave]}'")


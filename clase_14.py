# ==========================================================================================================================================
#                                                           CLASE 14 - HERENCIAS
# ==========================================================================================================================================

# LA CLASE PADRE PUEDE UTILIZAR TODO LO QUE TIENE LA CLASE HIJA.

# LOS ATRIBUTOS DE INSTANCIA SE DEFINEN DENTRO DE LOS METODOS(CONSTRUCTOR).


# class NombreClase:
#     ...

# class Vehiculo(): ## Poner paresntesis vacios es lo mismo que no poner nada. Los parentesis estan para definir la herencia --> Ver si la clase es hija de otra.
#     pass

# class Auto(Vehiculo):  ## La clase padre de 'auto' es 'vehiculo'.
#     pass

# ESTO NOS SIRVE PARA QUE NUESTRA CLASE HIJA TENGA TODO LO QUE TIENE EL PADRE --> ES UNA MANERA DE REDUCIR EL CODIGO.

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               DRY
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# class Auto():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Moto():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# auto = Auto('Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('Mercedes')
# print(moto.marca)
# moto.descripcion()

# QUIERO CREAR UNA CLASE QUE NO REPITA LO MISMO EN AMBAS.
# Con herencia pasaria a ser asi...

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Auto(Vehiculo):
#     ...

# class Moto(Vehiculo):
#     ...
    
# class Lancha(Vehiculo):
#     ...

# vehiculo = Vehiculo('Scania')
# print(vehiculo.marca)
# vehiculo.descripcion()
# auto = Auto()             ## Me genera un error xq a auto no le estoy pasando nada. Le falta el argumento de marca que tiene el padre.
# auto = Auto('Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('BMW')
# print(moto.marca)
# moto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)
# lancha.descripcion()

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               AGREGAR A LAS PARTICULARIDADES HEREDADAS.
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# DE UN HIJO PODEMOS PISAR FUNCIONALIDADES QUE TIENE UN PADRE

# class Vehiculo():
#         self.marca = marca
#     def __init__(self, marca):

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Auto(Vehiculo):
#     # ...
#     def __init__(self, marca, alarma):   ## Aca auto va a usar primero su constructor y no el del padre. Pisa el metodo del padre.
#         self.marca = marca               ## Si el metodo del hijo tiene el mismo nombre que el del padre, el del hijo siempre va a tener prioridad.
#         self.alarma = alarma
    
# class Lancha(Vehiculo):
#     def anclarse(self):
#         print(f'Anclaje efectuado')
        
#     def descripcion(self):               ## Este pisa el 'descricion' del padre xq se llaman iguales y tiene la prioridad el hijo.
#         print(f'Soy una lancha')

# auto = Auto('Ford', True)
# print(auto.marca)
# print(auto.alarma)
# auto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)
# # print(lancha.alarma)
# lancha.descripcion()
# lancha.anclarse()
# # auto.anclarse()  ## Va a dar un error xq anclarse pertenence a lancha.

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               SUPER
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# COMO HACER PARA NO PISAR LAS FUNCIONALIDADES DENTRO DE LOS HIJOS

# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca
        
#     def arrancar(self):
#         print('Prrrrumm!')
        
#     def avanzar(self, distancia):
#         ...
        
#     def tocar_bocina(self):
#         ...
#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class Auto(Vehiculo):
#     # FORMA 1
#     # def __init__(self, color, asientos, marca):
#     #     self.color = color
#     #     self.asientos = asientos
#     #     self.marca = marca
#     #     self.arrncar()

#     # FORMA 2
#     def __init__(self, color, asientos, marca):
#         super().__init__(marca)
#         self.color = color
#         self.asientos = asientos
#         self.arrancar()
    
#     def descripcion(self):
#         super().descripcion()                   ## El 'super' le dice que vaya al padre y ejecute 'descripcion'. Va con los paretesis.
#         print(f'Soy un {type(self).__name__}')
    
# class Moto(Vehiculo):
#         ...

# auto = Auto('Negro', 4, 'Ford')
# print(auto.marca)
# auto.descripcion()
# moto = Moto('BMW')
# print(moto.marca)
# moto.descripcion()

# print(auto.marca, auto.color, auto.asientos)
# print(moto.marca, moto.color, moto.asientos)

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               HERENCIA MULITPLE
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# HAY DOS FORMAS DE HERENCIA MULTIPLE.
## FORMA 1
'''
class Clase1:
    pass
class Clase2:
    pass
class Clase3(Clase1, Clase2):
    pass
'''
## FORMA 2
'''
class Clase1:
    pass
class Clase2(Clase1):
    pass
class Clase3(Clase2):
    pass
'''
# NOS PERMITE GENERALIZAR Y ESPECIALIZAR.
# IR DE CLASES MUY GENERALES(ABUELOS) A LAS MAS ESPECIFICIAS(HIJOS).


# class Vehiculo():
#     def __init__(self, marca):
#         self.marca = marca

#     def descripcion(self):
#         print(f'Vehiculo: {type(self).__name__}')

# class VehiculoTerrestre(Vehiculo):
#     # def __init__(self, alarma, cant_ruedas, marca):
#     #     super().__init__(marca)
#     # def __init__(self, alarma, cant_ruedas, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#         self.alarma = alarma
#         self.cant_ruedas = cant_ruedas

# class Auto(VehiculoTerrestre):       ## Auto hereda de VehiculoTerrestre y este de Vehiculo.
#     ...

# class Lancha(Vehiculo):
#     ...

# auto = Auto(True, 4, marca='Ford')
# # auto = Auto(alarma=True, cant_ruedas=4, marca='Ford')
# print(auto.marca, auto.alarma, auto.cant_ruedas)
# auto.descripcion()
# lancha = Lancha('Mercedes')
# print(lancha.marca)

#--------------------------------------------------------------------------------------------------------------------------------------------

# class Animal:
#     def descripcion(self):
#         print('Soy lo que soy')
#         # return 'Soy un animal'

# class Mamifero (Animal):
#     ...

# class Terrestre:        ## No hereda de nada.
#     def trotar(self):
#         print(f'{type(self).__name__} trotando')
        
#     def descripcion(self):   
#         print('Soy terrestre')
#         # return 'Soy terrestre'

# class Acuatico:
#     def nadar(self):
#         print(f'{type(self).__name__} nadando')
        
#     def descripcion(self):
#         print('Soy acuatico')  
#         # return 'Soy acuatico'
    
# class Gato(Mamifero, Terrestre):    ## Revisa siempre de izq a derecha. En este caso revisa primero 'Mamifero'.
#     # def descripcion(self):        
#     #     return 'Soy un gato'
#     ...
    
# class Delfin(Acuatico, Mamifero):
#     ...


# gato = Gato()
# delfin = Delfin()
# gato.descripcion()
# gato.trotar()
# delfin.descripcion()
# # delfin.trotar()
# delfin.nadar()

# MRO
## Nos permite saber el orden en que lee las clases.

# print(Gato.__mro__)
# print(Delfin.__mro__)

#-------------------------------------------------------------------------------------------------------------------------------------
# POR DEFECTO UNA CLASE HEREDA DE UNA QUE SE LLAMA 'OBJECT'. LA CLASE OBJECT ES LA CLASE PADRE DE TODOS. TODAS LAS CLASES HEREDAN
# DE OBJECT. 
#-------------------------------------------------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                               DUCK TYPING
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# POLIMORFISMO
## Es la posibilidad de llamar diferentes cosas para que hagan lo mismo pero cada cosa lo hace a su manera.

# class Animal:
#     def __init__(self, nombre):
#         self.nombre = nombre
    
#     def caminar(self):
#         print('Soy un animal caminando')

# class Perro(Animal):
#     def caminar(self):
#         print('El perro esta caminando.')
    
# class Gato(Animal):
#     def caminar(self):
#         print('Soy un gato que anda caminando por la calle')
    
# class Chancho(Animal):
#     ...

# class Persona:
#     def caminar(self):
#         print('Cuidado, persona caminando')
    
# animal = Animal()
# perro = Perro()
# gato = Gato()
# chancho = Chancho()
# persona = Persona()

# animal.caminar()
# perro.caminar()
# gato.caminar()
# chancho.caminar()
# persona.caminar()  


# Variacion 1

# def animal_caminando(animal):
#     animal.caminar()

# perro = Perro()
# gato = Gato()
# chancho = Chancho()
# persona = Persona()

# for animal in [perro, gato, chancho, persona]:
#     animal_caminando(animal)
    

# Variacion 2
# def animal_caminando(clase_de_animal):
#     animal = clase_de_animal(input('Ingrese nombre de un animal: '))
#     animal.caminar()

# for clase_de_animal in [Perro, Gato, Chancho]:   ## En la lista estan las clases.
#     animal_caminando(clase_de_animal)

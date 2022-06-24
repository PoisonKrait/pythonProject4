class Vehiculo:
   def __init__(self, color, ruedas, puertas):
       self.color = color
       self.ruedas = ruedas
       self.puertas = puertas


class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindros):

        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindros = cilindros

#class Rebuild(Coche):
#    def __init__(self, color, ruedas, puertas, velocidad, cilindros,
#                 modColor,
#                 modRuedas,
#                 modPuertas,
#                 modVelocidad,
#                 modCilindros):

#        super().__init__(color, ruedas, puertas, velocidad, cilindros)
#        self.modColor = modColor
#        self.modRuedas = modRuedas
#        self.modPuertas = modPuertas
#        self.modVelocidad = modVelocidad
#        self.modCilindros = modCilindros

coche = Coche(color= input('Introduce el color del coche: '),
              ruedas=int(input('Introduce el numero de ruedas: ')),
              puertas=int(input('Introduce el numero de puertas: ')),
              velocidad=int(input('Introduce la velocidad maxima')),
              cilindros=int(input('Introduce los cilindros: ')))

print('El Coche es de color: ', coche.color)
print('Tiene: ', coche.ruedas, ' ruedas')
print('Tiene: ', coche.puertas, ' puertas')
print('Su velocidad maxima es de: ', coche.velocidad, ' KM/H')
print('Tiene: ', coche.cilindros, ' cilindros')


#modificar = input('Deseas modificar el vehiculo? si/no: ')

#if modificar == 'si':
#    opciones = input('Ingresa la opcion a modificar: \n'
#                     '1 Modificar Color \n'
#                     '2 Modificar Ruedas \n'
#                     '3 Modificar Puertas \n'
#                     '4 Modificar Velocidad Maxima \n'
#                     '5 Modificar Cilindros \n'
#                     'Ingresa el numero de la opcion: ')
#    print(opciones)

#    escogerOpcion = opciones
#    if escogerOpcion == '1':



#else: print('Felicidades tu vehiculo se fabricara acorde tus especificaciones')






    #modificar = print(input('¿Deseas modificar tu vehiculo? (si/no)'))

    #if modificar == 'si':
     #   print('1 Modificar Color \n',
    #        '2 Modificar Ruedas \n',
    #          '3 Modificar Puertas \n',
     #         '4 Modificar Velocidad Maxima \n',
      #        '5 Modificar No. De Cilindros \n')
#
 #       opciones = print(int(input('Introduce el numero de la opcion')))

  #      if opciones == '1':
   #         print(Rebuild.)
    #    elif opciones == '2':
     #       print(Rebuild.modRuedas)
      #  elif opciones == '3':
       #     print(Rebuild.modPuertas)
        #elif opciones == '4':
         #   print(Rebuild.modVelocidad)
        #elif opciones == '5':
         #   print(Rebuild.modCilindrada)

    #else:
     #   print('Felicidades tu vehiculo pronto sera fabricado')


class Alumno:
    def inicializar (self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print('El nombre del alumno es: ', self.nombre)
        print('La nota del alumno es: ', self.nota)

    def resultado(self):
        if self.nota < 5.0:
            print('El alumno a reprobado')
        else:
            print('El alumno a aprobado')

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar(nombre=input('Introduce el nombre del alumno: '),
                nota=float(input('Introduce la nota del alumno')))
alumno2.inicializar(nombre=input('Introduce el nombre del alumno: '),
                nota=float(input('Introduce la nota del alumno')))

alumno1.imprimir()
alumno1.resultado()

alumno2.imprimir()
alumno2.resultado()

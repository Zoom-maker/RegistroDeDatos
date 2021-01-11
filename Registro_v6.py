#----------------------------- NOTAS:

# Para el Char by CHar investigar el modulo split de python
# Usar - len(Datos) - para el tamaño de la lista en numero
# Path.seek(32) - Para leer el archivo a partir de que byte, de 8 en 8, cada 8 bytes una linea

#----------------------------- MODULOS:

import sys
import os
import os.path as path
import re
from getpass import getpass
import msvcrt

#-----------------------------  INSTRUCCIONES:

# V1:
# Solo capturar
# Cedula: 546546
# Nombres: 4646
# Edad: 564
# Grabar? Y/N

# V2:
# v1 + Listado + Busqueda (Cedula)

#V3:
#v2 + Edicion + Eliminar

#V4:
# Read Char by Char
#----------------------------- CLASES:
class Usuario:
    
    def __init__(self, cedula, name, ahorros, passw, bit):

        self.__ID = cedula
        self.__name_lastname = name
        self.__savings = ahorros
        self.__passw = passw
        self.__bit = bit

    @property
    def cedula(self):
        return self.__ID

    @property
    def name(self):
        return self.__name_lastname
        
    @property
    def ahorros(self):
        return self.__savings
        
    @property
    def contra(self):
        return self.__passw
        
    @property
    def bits(self):
        return self.__bit

#----------------------------- FUNCIONES:

def Agrupar(cedula, name, ahorros, passw, bits):
    
    Datos.append('\n' + str(cedula) + ", " + str(name) + ", " + str(ahorros) + ", " + str(passw) + ", " + str(bits))
    return Escribir(Datos)

def decode(bit):

   #==================================== SEXO:

    if bit & 1 > 0:
        sex = "Masculino"
    else:
        sex = "Femenino"

    #==================================== ESTADO CIVIL:

    if (bit >> 1) & 1 > 0:
        estadoC = "Casado"

    else:
        estadoC = "Soltero"

    #==================================== EDAD:

    edad = (bit >> 2) & 127

    #==================================== GRADO ACADEMICO:

    if (bit >> 9) & 3 == 0:

        gradoAc = "Inicial"

    elif (bit >> 9) & 3 == 1:

        gradoAc = "Media"

    elif (bit >> 9) & 3 == 2:
    
        gradoAc = "Grado"

    if (bit >> 9) & 3 == 3:
    
        gradoAc = "Postgrado"

    return (sex + ", " + estadoC + ", " + str(edad) + ", " + gradoAc)

def Escribir(list = []):
     
    Path = open(File, "a+")
    for x in range(len(Datos)):

        Path.write(Datos[x])

    Path.close()

def Buscar(param):


    Listado = open(File, "r")

    comp = r'' + param

    for line in Listado:

        find = re.findall(comp, line)
        result = "".join(find)

        if result == param:
            list3 = line.split(", ")
            bit = int(list3[len(list3) - 1])

            print(line)
            print("Decodificado: " + decode(bit))

    Listado.close()

def binarizar (a):
    

    binario = ''    # El numero binario sera un tipo string.

    while (a // 2) != 0:    # // significa el resultado de la division sin el .00, osea el resultado entero. 

        binario = str(a % 2) + binario      # Agregamos los restos de la division.

        a = a // 2

    return str(a) + binario     # Concatenamos el ultimo resultado de la division entera al numero binario 

#----------------------------- 

args,(File)= sys.argv                                   # Obtener nombre del archivo por la linea de comando
File = ("/Users/Dell/Desktop/" + File + ".txt")         # Indica la ruta y el nombre del archivo que se creará

#          0        1        2        3        4        5        6        7        8        9        .
list= [b'\x30', b'\x31', b'\x32', b'\x33', b'\x34', b'\x35', b'\x36', b'\x37', b'\x38', b'\x39', b'\x2e']

Path = open(File, "a") #Abro el archivo. La 'w' indica que es para escribir, osea "Write".
Path.close() # Verificar si elimino esta parte 
Path = open(File, "r") # Verificar si se puede escribir open(File, "ar")
content = Path.read()

if content == '':

    Path = open(File, "w")
    Path.write("Cedula ---- Nombre y apellido ---- Ahorros ---- Password")
    Path.close()


#----------------------------- 

bits = 0
Opt = int(input("(1) Capturar" + '\n' + "(2) Listar " + '\n' + "(3) Busqueda" + '\n' + "(4) Edicion " + '\n' + "(5) Eliminar" + '\n' ))

#----------------------------- CAPTURAR:
if Opt == 1:

    while True:
        
        #----------------------------- CEDULA:
       
        print("Ingrese la Cedula: ")
        list_2 = []     
        while True:
                
            char = msvcrt.getch()
            
            for x in list:

                if char == x:
                    
                    f = char.decode()
                    list_2.append(f)
        
                    for i in range(len(list_2)):
                        print(list_2[i], end="")
                    print("", end ='\r')
                    break

            if char == b'\r':
                cedula = "".join(list_2)
                break
        print()
        #----------------------------- NOMBRE Y APELLIDO:
        
        print("Introduce tu nombre y apellido: ")
        list_2 = []
        while True:

            char = msvcrt.getch()

            cont = True

            for x in list:

                if char == x:
                    cont = False
    
            if cont == True:
        
               
                if char != b'\r':
                    f = char.decode()
                    list_2.append(f)    
        
                for i in range(len(list_2)):
                    print(list_2[i], end="")
                print("", end ='\r')
    
            if char == b'\r':
                name = "".join(list_2)
                break

        print()
        #----------------------------- SEXO (1 bit):
        
        print("Ingrese el sexo (m/f): ")
        list_2 = []
        while True:

            char = msvcrt.getch()

            cont = True

            for x in list:

                if char == x:
                    cont = False
    
            if cont == True:
        
                if char != b'\r':

                    if (char == b'\x6d') | (char == b'\x66'): 
                        f = char.decode()
                        list_2.append(f)    

                for i in range(len(list_2)):
                    print(list_2[i], end="")
                print("", end ='\r')

            if char == b'\r':
         
                sex = "".join(list_2)

                if sex == 'm':
                    sex = 1
                    bits = sex | bits

                break

        print()
        #----------------------------- ESTADO CIVIL (1 bit):
        
        print("Ingrese su estado civil (c/s): ")
        list_2 = []
        while True:

            char = msvcrt.getch()

            cont = True

            for x in list:

                if char == x:
                    cont = False
    
            if cont == True:
        
                if char != b'\r':

                    if (char == b'\x63') | (char == b'\x73'): 
                        f = char.decode()
                        list_2.append(f)    

                for i in range(len(list_2)):
                    print(list_2[i], end="")
                print("", end ='\r')

            if char == b'\r':
         
                estadoC = "".join(list_2)

                if estadoC == 'c':
    
                    estadoC = 1
                    estadoC = estadoC << 1 
                    bits = bits | estadoC

                break

        print()
        #----------------------------- EDAD:
        
        print("Ingresa tu edad (7 - 120): ")
        list_2 = []     
        while True:
                
            char = msvcrt.getch()
            
            for x in list:

                if char == x:
           
                    f = char.decode()
                    list_2.append(f)
        
                    for i in range(len(list_2)):
                        print(list_2[i], end="")
                    print("", end ='\r')
                    break

            if char == b'\r':
                age = "".join(list_2)
                age = int(age)
                
                if (age > 6) & (age < 121):
                    age = age << 2
                    bits = bits | age
                    break
                else: 
                    print("El numero ingresado no esta en el rango. \n Vuelve a ingresar tu edad:")
                    list_2 = []
                
        print()
        
        #----------------------------- GRADO ACADEMICO (2 bits):
        
        print("Ingrese su grado academico (i/m/g/p): ")
        list_2 = []
        while True:

            char = msvcrt.getch()

            cont = True

            for x in list:

                if char == x:
                    cont = False
    
            if cont == True:
        
                if char != b'\r':

                    if (char == b'\x69') | (char == b'\x6d') | (char == b'\x67') | (char == b'\x70'): 
                        f = char.decode()
                        list_2.append(f)    

                for i in range(len(list_2)):
                    print(list_2[i], end="")
                print("", end ='\r')

            if char == b'\r':
         
                gradoAc = "".join(list_2)

                if gradoAc == 'i':
                    gradoAc = 0
                    gradoAc = gradoAc << 9
                    bits = bits | gradoAc

                elif gradoAc == 'm':
                    gradoAc = 1
                    gradoAc = gradoAc << 9
                    bits = bits | gradoAc

                elif gradoAc == 'g':
                    gradoAc = 2
                    gradoAc = gradoAc << 9
                    bits = bits | gradoAc

                elif gradoAc == 'p':
                    gradoAc = 3
                    gradoAc = gradoAc << 9
                    bits = bits | gradoAc

                break

        print()
        #----------------------------- AHORROS:
        print("Ingresa tus ahorros: ")
        list_2 = []  
        while True:
                    
            char = msvcrt.getch()
                
            for x in list:

                if char == x:
                        
                    f = char.decode()
                    list_2.append(f)
        
                    for i in range(len(list_2)):
                        print(list_2[i], end="")
                    print("", end ='\r')
                    break

            if char == b'\r':
                ahorros = "".join(list_2)
                break
        print()
        #----------------------------- CONTRASEÑA:
        while True:
            
            print("Ingresa tu contraseña: ")
            list_2 = []
            while True:
                    
                char = msvcrt.getch()
        
                if char != b'\r':
                    f = char.decode()
                    list_2.append(f) 

                for i in range(len(list_2)):
                    print('*', end="")
                print("", end ='\r')

                if char == b'\r':
                    passw = "".join(list_2)
                    break

            print("Ingresa tu contraseña nuevamente: ")
            list_2 = [] 
            while True:
                    
                char = msvcrt.getch()
                
                if char != b'\r':
                    f = char.decode()
                    list_2.append(f) 

                for i in range(len(list_2)):
                    print('*', end="")
                print("", end ='\r')

                if char == b'\r':
                    passw2 = "".join(list_2)
                    break        
            if passw != passw2:
                print("Las contraseñas no coinciden! Ingresela de nuevo")
            else: 
                break
        #-----------------------------
        user = Usuario(cedula, name, ahorros, passw, bits)
        
        Datos = []              # Esta es una lista

        choise = input("Deseas guardar los datos? (y/n): ")

    #----------------------------- CONDICIONES:

        if choise == 'y':
       
            Agrupar(user.cedula, user.name, user.ahorros, user.contra, user.bits)

            print("Datos guardados!")


        elif choise == 'n':

            print("Datos no guardados!")

        else: 
            print("Respuesta no aceptada")
#----------------------------- AGREGAR MAS DATOS:

        Continue = input("Desea Agregar mas datos? (y/n): ")

        if Continue == 'n':

            Path.close()
            break
#----------------------------- LISTAR:

elif Opt == 2: 
    
    Listado = open(File, "r")
    
    for lines in Listado:
       
        print(lines)

    Listado.close()


#----------------------------- BUSQUEDA:

elif Opt == 3:

    ced = str(input("Ingrese la cedula que se va a buscar: "))

    Buscar(ced)

#----------------------------- EDICION:

elif Opt == 4:

    Listado = open(File, "r")

    Datos = []
    cond = True

    ced = str(input("Que informacion desea editar? (ingresar cedula): "))

    comp = r'' + ced

    for line in Listado:

        find = re.findall(comp, line) 
        result = "".join(find) 

        if result != ced:

            Datos.append(line)

        else:

            cond = False
            print("Ingrese los datos nuevos: ")
            print()
           
            #----------------------------- CEDULA:
       
            print("Ingrese la Cedula: ")
            list_2 = []     
            while True:
                
                char = msvcrt.getch()
            
                for x in list:

                    if char == x:
                    
                        f = char.decode()
                        list_2.append(f)
        
                        for i in range(len(list_2)):
                            print(list_2[i], end="")
                        print("", end ='\r')
                        break

                if char == b'\r':
                    cedula = "".join(list_2)
                    break
            print()
            #----------------------------- NOMBRE Y APELLIDO:
        
            print("Introduce tu nombre y apellido: ")
            list_2 = []
            while True:

                char = msvcrt.getch()

                cont = True

                for x in list:

                    if char == x:
                        cont = False
    
                if cont == True:
        
                    if char != b'\r':
                        f = char.decode()
                        list_2.append(f)    

                    for i in range(len(list_2)):
                        print(list_2[i], end="")
                    print("", end ='\r')
    
                if char == b'\r':
                    name = "".join(list_2)
                    break

            print()
            
            #----------------------------- SEXO (1 bit):
        
            print("Ingrese el sexo (m/f): ")
            list_2 = []
            while True:

                char = msvcrt.getch()

                cont = True

                for x in list:

                    if char == x:
                        cont = False
    
                if cont == True:
        
                    if char != b'\r':

                        if (char == b'\x6d') | (char == b'\x66'): 
                            f = char.decode()
                            list_2.append(f)    

                    for i in range(len(list_2)):
                        print(list_2[i], end="")
                    print("", end ='\r')

                if char == b'\r':
         
                    sex = "".join(list_2)

                    if sex == 'm':
                        sex = 1
                        bits = sex | bits

                    break

            print()
        #----------------------------- ESTADO CIVIL (1 bit):
        
            print("Ingrese su estado civil (c/s): ")
            list_2 = []
            while True:

                char = msvcrt.getch()

                cont = True

                for x in list:

                    if char == x:
                        cont = False
    
                if cont == True:
        
                    if char != b'\r':

                        if (char == b'\x63') | (char == b'\x73'): 
                            f = char.decode()
                            list_2.append(f)    

                    for i in range(len(list_2)):
                        print(list_2[i], end="")
                    print("", end ='\r')

                if char == b'\r':
         
                    estadoC = "".join(list_2)

                    if estadoC == 'c':
    
                        estadoC = 1
                        estadoC = estadoC << 1 
                        bits = bits | estadoC

                    break

            print()
        #----------------------------- EDAD:
        
            print("Ingresa tu edad (7 - 120): ")
            list_2 = []     
            while True:
                
                char = msvcrt.getch()
            
                for x in list:

                    if char == x:
           
                        f = char.decode()
                        list_2.append(f)
        
                        for i in range(len(list_2)):
                            print(list_2[i], end="")
                        print("", end ='\r')
                        break

                if char == b'\r':
                    age = "".join(list_2)
                    age = int(age)
                
                    if (age > 6) & (age < 121):
                        
                        bits = bits | (age << 2)
                        
                        break
                    else: 
                        print("El numero ingresado no esta en el rango \n Vuelve a ingresar tu edad:")
                        list_2 = []
                
            print()
        #----------------------------- GRADO ACADEMICO (2 bits):
        
            print("Ingrese su grado academico (i/m/g/p): ")
            list_2 = []
            while True:

                char = msvcrt.getch()

                cont = True

                for x in list:

                    if char == x:
                        cont = False
    
                if cont == True:
        
                    if char != b'\r':

                        if (char == b'\x69') | (char == b'\x6d') | (char == b'\x67') | (char == b'\x70'): 
                            f = char.decode()
                            list_2.append(f)    

                    for i in range(len(list_2)):
                        print(list_2[i], end="")
                    print("", end ='\r')

                if char == b'\r':
         
                    gradoAc = "".join(list_2)

                    if gradoAc == 'i':
                        gradoAc = 0
                        gradoAc = gradoAc << 9
                        bits = bits | gradoAc

                    elif gradoAc == 'm':
                        gradoAc = 1
                        gradoAc = gradoAc << 9
                        bits = bits | gradoAc

                    elif gradoAc == 'g':
                        gradoAc = 2
                        gradoAc = gradoAc << 9
                        bits = bits | gradoAc

                    elif gradoAc == 'p':
                        gradoAc = 3
                        gradoAc = gradoAc << 9
                        bits = bits | gradoAc

                    break

            print()
            #----------------------------- AHORROS:

            print("Ingresa tus ahorros: ")
            list_2 = []  
            y = 0    
            while True:
                    
                char = msvcrt.getch()
                
                for x in list:

                    if char == x:
                        
                        y += 1
                        f = char.decode()
                        list_2.append(f)
        
                        for i in range(0, y):
                            print(list_2[i], end="")
                        print("", end ='\r')
                        break

                if char == b'\r':
                    ahorros = "".join(list_2)
                    break
            print()
            
            #----------------------------- CONTRASEÑA:
            while True:
            
                print("Ingresa tu contraseña: ")
                list_2 = []
                y = 0      
                while True:
                    
                    char = msvcrt.getch()
        
                    y += 1

                    if char != b'\r':
                        f = char.decode()
                        list_2.append(f) 

                    for i in range(len(list_2)):
                        print('*', end="")
                    print("", end ='\r')

                    if char == b'\r':
                        passw = "".join(list_2)
                        break

                print("Ingresa tu contraseña nuevamente: ")
                list_2 = [] 
                y = 0     
                while True:
                    
                    char = msvcrt.getch()
       
                    y += 1

                    if char != b'\r':
                        f = char.decode()
                        list_2.append(f) 

                    for i in range(len(list_2)):
                        print('*', end="")
                    print("", end ='\r')

                    if char == b'\r':
                        passw2 = "".join(list_2)
                        break        
                if passw != passw2:
                    print("Las contraseñas no coinciden! Ingresela de nuevo")
                    y = 0        
                else: 
                    break
        #-----------------------------
        
            user = Usuario(cedula, name, ahorros, passw, bits)
            Datos.append(str(user.cedula) + ", " + str(user.name) + ", " + str(user.ahorros) + ", " + str(user.contra) + ", " + str(user.bits) + '\n')
           
    Listado = open(File, "w")

    for x in range(len(Datos)):

        Listado.write(Datos[x])
    
    if cond == True:
        print("Datos no encontrados.")
    else:
        print("Datos actualizados correctamente!")

    Listado.close()

#----------------------------- ELIMINAR:

if Opt ==5:

    Listado = open(File, "r")

    Datos = []

    ced = str(input("Que informacion desea editar? (ingresar cedula): "))

    comp = r'' + ced

    for line in Listado:

        find = re.findall(comp, line) 
        result = "".join(find) 

        if result != ced:

            Datos.append(line)


    Listado = open(File, "w")

    for x in range(len(Datos)):

        Listado.write(Datos[x])
    
    print("Datos eliminados correctamente!")

    Listado.close()
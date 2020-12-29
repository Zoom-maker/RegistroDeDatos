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

#----------------------------- FUNCIONES:

def Agrupar(cedula, name, age, ahorros, passw):
    
    Datos.append('\n' + str(cedula) + ", " + str(name) + ", " + str(age)+ ", " + str(ahorros) + ", " + str(passw))
    return Escribir(Datos)

def Escribir(list = []):
     
    Path = open(File, "a+")
    for x in range(len(Datos)):

        Path.write(Datos[x])

    Path.close()

def Buscar(a):

    Listado = open(File, "r")

    comp = r'' + a

    for line in Listado:

        find = re.findall(comp, line)
        result = "".join(find)

        if result == a:

            print(line)

    Listado.close()
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
    Path.write("Cedula ---- Nombre y apellido -- Edad ---- Ahorros ---- Password")
    Path.close()


#----------------------------- 
 
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
        y = 0
        while True:

            char = msvcrt.getch()

            cont = True

            for x in list:

                if char == x:
                    cont = False
    
            if cont == True:
        
                y += 1
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
        #----------------------------- EDAD:
        
        print("Ingresa tu edad: ")
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

        Datos = []              # Esta es una lista

        choise = input("Deseas guardar los datos? (y/n): ")

    #----------------------------- CONDICIONES:

        if choise == 'y':
    
            Agrupar(cedula, name, age, ahorros, passw)

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

    ced = str(input("Que informacion desea editar? (ingresar cedula): "))

    comp = r'' + ced

    for line in Listado:

        find = re.findall(comp, line) 
        result = "".join(find) 

        if result != ced:

            Datos.append(line)

        else:

            print("Ingrese los datos nuevos: ")
            print()
           
            #----------------------------- CEDULA:
       
            print("Ingrese la Cedula: ")
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
                    cedula = "".join(list_2)
                    break
            print()
            #----------------------------- NOMBRE Y APELLIDO:
        
            print("Introduce tu nombre y apellido: ")
            list_2 = []
            y = 0
            while True:

                char = msvcrt.getch()

                cont = True

                for x in list:

                    if char == x:
                        cont = False
    
                if cont == True:
        
                    y += 1
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
            #----------------------------- EDAD:
        
            print("Ingresa tu edad: ")
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
                    age = "".join(list_2)
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
            Datos.append(str(cedula) + ", " + str(name) + ", " + str(age)+ ", " + str(ahorros) + ", " + str(passw) + '\n')

    Listado = open(File, "w")

    for x in range(len(Datos)):

        Listado.write(Datos[x])
    
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
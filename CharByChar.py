import msvcrt

#----------------------------- NOTAS:

# b'\r' = Enter

#----------------------------- INSTRUCCIONES:

# Read char by char:

#    Nombres y Apellidos (strings)
#    Edad (solo enteros)
#    Ahorros (moneda / decimal)
#    Password y Password Confirm

#----------------------------- 

#          0        1        2        3        4        5        6        7        8        9        .
list= [b'\x30', b'\x31', b'\x32', b'\x33', b'\x34', b'\x35', b'\x36', b'\x37', b'\x38', b'\x39', b'\x2e']

#----------------------------- NOMBRES Y APELLIDOS:

print("Introduce tu nombre y apellido: ")
list_2 = []

while True:

    char = msvcrt.getch()

    cont = True

    for x in list:

        if char == x:
            cont = False
    
    if cont == True:
        
        f = char.decode()
        print(f)
        list_2.append(f)
    
    if char == b'\r':

        name = "".join(list_2)
        print("Nombre y apellido: ", name)
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
            print(f)
            list_2.append(f)

    if char == b'\r':
        age = "".join(list_2)
        print("Edad: ", age)
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
            print(f)
            list_2.append(f)

    if char == b'\r':
        ahorros = "".join(list_2)
        print("Ahorros: ", float(ahorros))
        break
print()
#----------------------------- PASSWORD:    

    
while True:
        
    print("Ingresa tu contraseña: ")
    list_2 = []      
    while True:
                    
        char = msvcrt.getch()
        
        f = char.decode()
        print('*')
        list_2.append(f)

        if char == b'\r':
            passw = "".join(list_2)
            break

    print("Ingresa tu contraseña nuevamente: ")
    list_2 = []      
    while True:
                    
        char = msvcrt.getch()
                
        f = char.decode()
        print('*')
        list_2.append(f)

        if char == b'\r':
            passw2 = "".join(list_2)
            break        
    if passw != passw2:
        print("Las contraseñas no coinciden! Ingresela de nuevo")
                
    else: 
        break
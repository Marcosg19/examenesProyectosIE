from random import randint
import psycopg2
#Conexión a base de datos
try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "marcos2001",
        dbname = "proyectosIE"  
    )
    print('Conexión exitosa con la base de datos')
except psycopg2.Error as e:
    print('Ocurrió un error en la conexión')
    print('Verifique los parametros')


cursor = conexion.cursor()


def opciones():
    detenerop = False
    num = 0
    while not detenerop:
        try:
            detenerop = True    
            num = int(input('\nIngrese una opción: '))
        except ValueError:
            print('\nSeleccione una opción valida')
    return num

def datos_persona():
    año_actual = 2022
    mes_actual = 2
    dia_actual = 24

    detener_d1 = True
    detener_d2 = True
    detener_d3 = True  
    while detener_d1:
        try:
            a=int(input('\nIngrese año de nacimiento: '))
            detener_d1 = False
            if a <= 0:
                print('Ingrese un día valido... ')
                detener_d1 = True
        except ValueError:
            print('Caracter invalido...')
            detener_d1 = True
        

    while detener_d2:
        try:
            m=int(input('\nIngrese mes de nacimiento: '))
            detener_d2 = False
            if m <= 0:
                print('Ingrese un mes valido... ')
                detener_d2 = True
            if m > 12:
                print('Ingrese un mes valido... ')
                detener_d2 = True
        except ValueError:
            print('Caracter invalido...')
            detener_d2 = True    

    while detener_d3:
        try:
            d=int(input('\nIngrese día de nacimiento: '))
            detener_d3 = False
            if d <= 0:
                print('Ingrese un día valido... ')
                detener_d3 = True
            if m == 1: 
                if d > 31:
                    print('Ingrese un día valido... ')
                    detener_d3 = True
            if m == 3: 
                if d > 31:
                    print('Ingrese un día valido... ')
                    detener_d3 = True

            if m == 5: 
                if d > 31:
                    print('Ingrese un día valido... ')
                    detener_d3 = True

            if m == 7: 
                if d > 31:
                    print('Ingrese un día valido... ')
                    detener_d3 = True
            
            if m == 8: 
                if d > 31:
                    print('Ingrese un día valido... ')
                    detener_d3 = True

            if m == 10: 
                if d > 31:
                    print('Ingrese un día valido... ')
                    detener_d3 = True

            if m == 12: 
                if d > 31:
                    print('Ingrese un día valido... ')
                    detener_d3 = True
            
            if m == 4: 
                if d > 30:
                    print('Ingrese un día valido... ')
                    detener_d3 = True

            if m == 6: 
                if d > 30:
                    print('Ingrese un día valido... ')
                    detener_d3 = True  

            if m  == 9: 
                if d > 30:
                    print('Ingrese un día valido... ')
                    detener_d3 = True

            if m == 11: 
                if d > 30:
                    print('Ingrese un día valido... ')
                    detener_d3 = True       

            if m == 2: 
                if d > 28:
                    print('Ingrese un día valido... ')
                    detener_d3 = True   

        except ValueError:
            print('Caracter invalido...')
            detener_d3 = True

    edad = año_actual - a
    if m > mes_actual :
        edad = edad - 1

    else:
        if m == mes_actual:
            if d > dia_actual:
                edad = edad - 1
            if d == dia_actual:
                print('\nEstá persona esta cumpliendo',str(edad) +' años hoy')
                cursor.execute("INSERT INTO datos_persona(dia, mes, anio, edad) VALUES(%s,%s,%s,%s);",(d,m,a,edad))
                conexion.commit()


    if m > mes_actual:
        print('\nEsta persona cumple',str(edad) + ' años este año y esta persona no ha cumplido años aun')
        cursor.execute("INSERT INTO datos_persona(dia, mes, anio, edad) VALUES(%s,%s,%s,%s);",(d,m,a,edad))
        conexion.commit()

    if m == mes_actual:
        if d < dia_actual:
            print('\nEsta persona cumplió',str(edad) + ' años este año ')
            cursor.execute("INSERT INTO datos_persona(dia, mes, anio, edad) VALUES(%s,%s,%s,%s);",(d,m,a,edad))
            conexion.commit()
        if d > dia_actual:
            print('\nEsta persona cumple',str(edad) + ' años este año y esta persona no ha cumplido años aun')
            cursor.execute("INSERT INTO datos_persona(dia, mes, anio, edad) VALUES(%s,%s,%s,%s);",(d,m,a,edad))
            conexion.commit()

    if m < mes_actual:
        print('\nEsta persona cumplió',str(edad) + ' años este año')
        cursor.execute("INSERT INTO datos_persona(dia, mes, anio, edad) VALUES(%s,%s,%s,%s);",(d,m,a,edad))
        conexion.commit()


def angulo():
    detener_t1 = True
    detener_t2 = True
    while detener_t1:
        try:
            a=float(input('\nIngrese primer ángulo: '))
            detener_t1 = False
            if a < 0:
                print('Ingresar un número positivo... ')
                detener_t1 = True
            if a == 0:
                print('No puede ser 0...')
                detener_t1 = True
        except ValueError:
            print('Caracter invalido...')
            detener_t1 = True
        

    while detener_t2:
        try:
            b=float(input('\nIngrese segundo ángulo: '))
            detener_t2 = False
            if b < 0:
                print('Ingresar un número positivo... ')
                detener_t2 = True
            if b == 0:
                print('No puede ser 0...')
                detener_t2 = True
        except ValueError:
            print('Caracter invalido...')
            detener_t2 = True 

    print('\nEl tercer ángulo es: ', (180-(a+b)))
    cursor.execute("INSERT INTO angulos(angulo1,angulo2,angulo3) VALUES(%s,%s,%s);",(a,b,180-(a+b)))
    conexion.commit()


def udc():
    detener_t1 = True
    while detener_t1:
        try:
            a=int(input('\nIngrese primer número: '))
            detener_t1 = False
            if a < 0:
                print('Ingresar un número válido... ')
                detener_t1 = True
            if a > 999:
                print('Ingresar un número válido... ')
                detener_t1 = True

        except ValueError:
            print('Caracter invalido...')
            detener_t1 = True
        
    unidades= a%10
    a = a/10
    decenas= a%10
    a = a/10
    centenas= a%10

    print('El número tiene: ')
    print('Centenas: ',int(centenas))
    print('Decenas: ',int(decenas))
    print('Unidades: ',int(unidades))
    cursor.execute("INSERT INTO cdu(centenas,decenas,unidades) VALUES(%s,%s,%s);",(int(centenas),int(decenas),int(unidades)))
    conexion.commit()

def juego():
    detener_juego = True
    while detener_juego:
        a=randint(1,6)
        print('Dado 1: ',a)
        input()
        b=randint(1,6)
        print('Dado 2: ',b)
        input()
        if (a+b) ==8:
            print('Ganaste')
            cursor.execute("INSERT INTO juego(dado1,dado2,mensaje) VALUES(%s,%s,'Ganaste');",(a,b))
            conexion.commit()
            input()
            detener_juego = False
        elif (a+b) ==7:
            print('Perdiste')
            cursor.execute("INSERT INTO juego(dado1,dado2,mensaje) VALUES(%s,%s,'Perdiste');",(a,b))
            conexion.commit()
            input()
            detener_juego = False
        else:
            detener_juego = True

        
def menu_datos():
    detenertr= True
    while detenertr:
        print('\n\tDatos de persona')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opciontr = opciones()

        if opciontr == 1:
            print('\nDatos persona')
            datos_persona()
            input()

        elif opciontr == 2:
            cursor.execute('SELECT*FROM datos_persona;')
            valorestr = cursor.fetchall()
            print()
            print(valorestr)
            input()

        elif opciontr == 3:
            print('\nRegresando...')
            detenertr = False

        else:
            print('\nIngrese una opción válida')
            input()   

def menu_angulo():
    detenertr= True
    while detenertr:
        print('\n\tAngulos de un triangulo')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opciontr = opciones()

        if opciontr == 1:
            print('\nAngulos de un triangulo')
            angulo()
            input()

        elif opciontr == 2:
            cursor.execute('SELECT*FROM angulos;')
            valorestr = cursor.fetchall()
            print()
            print(valorestr)
            input()

        elif opciontr == 3:
            print('\nRegresando...')
            detenertr = False

        else:
            print('\nIngrese una opción válida')
            input() 

def menu_udc():
    detenertr= True
    while detenertr:
        print('\n\tCentenas, decenas y unidades')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opciontr = opciones()

        if opciontr == 1:
            print('\nCentenas, decenas y unidades')
            udc()
            input()

        elif opciontr == 2:
            cursor.execute('SELECT*FROM cdu;')
            valorestr = cursor.fetchall()
            print()
            print(valorestr)
            input()

        elif opciontr == 3:
            print('\nRegresando...')
            detenertr = False

        else:
            print('\nIngrese una opción válida')
            input() 

def menu_juego():
    detenertr= True
    while detenertr:
        print('\n\tJuego simulado del gran 8')
        print('\nOpciones')
        print('1. Abrir programa ')
        print('2. Historial')
        print('3. Regresar')

        opciontr = opciones()

        if opciontr == 1:
            print('\nJuego simulado del gran 8')
            juego()
            input()

        elif opciontr == 2:
            cursor.execute('SELECT*FROM juego;')
            valorestr = cursor.fetchall()
            print()
            print(valorestr)
            input()

        elif opciontr == 3:
            print('\nRegresando...')
            detenertr = False

        else:
            print('\nIngrese una opción válida')
            input() 


detenerprogramas= True
while detenerprogramas:
    print('\n\tPROGRAMAS DE EXAMEN PARCIAL 1')
    print('\nMENÚ')
    print('\n1. Datos de persona')
    print('2. Ángulos de un triángulo')
    print('3. Unidades, decenas y centenas')
    print('4. Juego')
    print('5. Salir')  

    opcion = opciones()

    if opcion == 1:
        menu_datos()
 

    elif opcion == 2:
        menu_angulo()

    elif opcion == 3:
        menu_udc()

    elif opcion == 4:
        menu_juego()

    elif opcion == 5:
        print('\n>>>>>>CERRANDO PROGRAMAS DE EXAMEN PARCIAL<<<<<<\n')
        detenerprogramas = False

    else:
        print('\nIngrese una opción válida')
        input()

cursor.close()
conexion.close()
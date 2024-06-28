import math
import random

def mos_menu_us():
    menu_us="""Menu de Usuario
1.- Registrar Alumno
2.- Listar todos los alumnos
3.- Buscar alumnos por nivel
4.- Calcular la nota promedio de los alumnos
5.- Salir del programa y guardar un archivo .txt

Ingresa tu opcion: """
    print(menu_us, end="")

def opcion_us():
    while True:
        try:
            op=int(input())

            if op>=1 and op<=5:
                return op
            else:
                raise ValueError
        except:
            print("Opcion no valida, intenta nuevamente: ",end="")

def registrar_alumnos():
    nombre=input("Ingrese el nombre del alumno: ")
    apellido=input("Ingrese el apellido del alumno: ")
    edad=int(input("Ingrese la edad del alumno: "))
    nivel=int(input("Ingrese el nivel del alumno: "))
    #notas=
    
    res={"nombre":nombre,"apellido":apellido,"edad":edad,"nivel":nivel,}#"notas":notas}
    return res

def listar_alumnos(lista):
    for i in range(len(lista)):
        print(f"ALUMNO {i+1}:")
        print(f"Nombre: {lista[i]["nombre"]}")
        print(f"Apellido: {lista[i]["apellido"]}")
        print(f"Edad: {lista[i]["lista"]}")
        print(f"Nivel: {lista[i]["nivel"]}")
        #print(f"Notas: {lista[i]["notas"]}")
        print("-------------------------------------------")

def buscar_alumnos(lista):
    nivel_usuario =input ("Ingrese el nivel del alumno: ")
    encontrado= False
    for i in range(len(lista)):
        if nivel_usuario==lista[i]["nivel"]:
            res=lista[i]
            encontrado=True
    if encontrado:
        print(f"Nombre: {res["nombre"]}")
        print(f"Apellido: {res["apellido"]}")
        print(f"Edad: {res["edad"]}")
        print(f"Nivel: {res["nivel"]}")
        #print(f"Notas: {res["notas"]}")
    else:
        print("Nivel incorrecto")

#def promedio_alumnos(lista):

def crear_archivo(lista):
    with open ("alumnos_ingresados.txt","w") as archivo:
        for i in lista:
            res= i["nombre"]+", "+i["apellido"]+", "+i["edad"]+", "+i["nivel"]+", "+i["notas"]+"\n"
            archivo.write(res)



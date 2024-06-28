import math
import Utilidades
import random

op=0
alumnos=[]

while op !=5:
    Utilidades.mos_menu_us()
    op=Utilidades.opcion_us()

    if op ==1:
        alumnos.append(Utilidades.registrar_alumnos())

    elif op ==2:
        Utilidades.listar_alumnos(alumnos)

    elif op ==3:
        Utilidades.buscar_alumnos(alumnos)

    #elif op ==4:
        Utilidades.promedio_alumnos(alumnos)

Utilidades.crear_archivo(alumnos)




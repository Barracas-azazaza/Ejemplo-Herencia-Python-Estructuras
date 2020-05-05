'''@author cbarragan uniempresarial 5/5/2020
    Ejemplo herencia'''
from Empleado import Empleado
from Administrador import Administrador
from Desarrollador import Desarrolador
class Principal:
    A1: Administrador = Administrador(0,"Camilo", "Barragán", 18, "Administrador", "Administrativo")
    print(A1)
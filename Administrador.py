from Empleado import Empleado
class Administrador(Empleado):
    def __init__(self, codigo_: int, nombre_: str, apellidos_: str, edad_: float, cargo_: str, departamento_: str):
        Empleado.__init__(self, codigo_, nombre_, apellidos_, edad_, cargo_, departamento_)
    def administrar(self)->str:
        return "Comienza a administrar"
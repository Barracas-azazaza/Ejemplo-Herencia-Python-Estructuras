from Empleado import Empleado
class Desarrolador(Empleado):
    def __init__(self, codigo_: int, nombre_: str, apellidos_: str, edad_: float, cargo_: str, departamento_: str):
        Empleado.__init__(self, codigo_, nombre_, apellidos_, edad_, cargo_, departamento_)
    def desarrollo(self)->str:
        return "Comienza a programar"
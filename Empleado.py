class Empleado:
    __codigo: int
    __nombre: str
    __apellidos: str
    __edad: float
    __cargo: str
    __departamento: str
    #Constructor
    def __init__(self, codigo_: int, nombre_: str, apellidos_: str, edad_: float, cargo_: str, departamento_: str):
        self.__codigo = codigo_
        self.__nombre = nombre_
        self.__apellidos = apellidos_
        self.__edad = edad_
        self.__cargo = cargo_
        self.__departamento = departamento_
    #Métodos código empleado
    def getCodigo(self)->int:
        return self.__codigo
    def setCodigo(self, newCodigo: int)->None:
        self.__codigo = newCodigo
    #Métodos nombre empleado
    def getNombre(self)->str:
        return self.__nombre
    def setNombre(self, newNombre: str)->None:
        self.__nombre = newNombre
    #Métodos apellidos empleado
    def getApellidos(self)->str:
        return self.__apellidos
    def setApellidos(self, newApellidos: str)->None:
        self.__apellidos = newApellidos
    #Métodos edad empleado
    def getEdad(self)->float:
        return self.__edad
    def setEdad(self, newEdad:float)->None:
        self.__edad = newEdad
    #Métodos de Cargo
    def getCargo(self)->str:
        return self.__cargo
    def setCargo(self, newCargo: str)->None:
        self.__cargo = newCargo
    #Métodos de Departamento
    def getDepartamento(self)->str:
        return self.__departamento
    def setDepartamento(self, newDepartamento: str)->None:
        self.__departamento = newDepartamento
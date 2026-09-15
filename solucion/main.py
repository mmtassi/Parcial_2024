from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, apellido, dni , relacion_dependencia, sueldo):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.relacion_dependencia = relacion_dependencia
        self.sueldo = sueldo

    @abstractmethod
    def calcular_sueldo(self):
        pass


class Contratados(Empleado):
    def __init__(self, nombre, apellido, dni , relacion_dependencia, sueldo, horas_trabajadas):
        super().__init__(nombre, apellido, dni , relacion_dependencia, sueldo)
        self.horas_minimas_dia = 8
        self.horas_trabajadas = horas_trabajadas

    def horas_trabajadas_dia(self):
        return self.horas_trabajadas / 20  # Suponiendo 20 días hábiles en un mes

    def calcular_sueldo(self):
        return self.sueldo * self.horas_trabajadas

class EmpleadoPlanta(Empleado):
    def __init__(self, nombre, apellido, dni , relacion_dependencia, sueldo, antiguedad):
        super().__init__(nombre, apellido, dni , relacion_dependencia, sueldo)
        self.antiguedad = antiguedad

    def calcular_sueldo(self):
        return self.sueldo + (self.antiguedad * 100)  # Sueldo base más un bono por antigüedad
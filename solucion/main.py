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
    def __init__(self, nombre, apellido, dni , relacion_dependencia, sueldo, horas_trabajadas, valor_hora):
        super().__init__(nombre, apellido, dni , relacion_dependencia, sueldo)
        self.horas_minimas_dia = 8
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def horas_trabajadas_dia(self):
        return self.horas_trabajadas

    def calcular_sueldo(self):
        return self.valor_hora * self.horas_trabajadas

class EmpleadoPlanta(Empleado):
    def __init__(self, nombre, apellido, dni , relacion_dependencia, sueldo, nivel):
        super().__init__(nombre, apellido, dni , relacion_dependencia, sueldo)
        self.nivel = nivel

    def calcular_sueldo(self):
        return self.sueldo
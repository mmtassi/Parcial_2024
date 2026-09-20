from abc import ABC, abstractmethod

class Empleado:
    def __init__(self, nombre, apellido, dni, dependencia):
        self._nombre = nombre
        self._apellido = apellido
        self._dni = dni
        self._dependencia = dependencia
        self._horas_trabajadas = []

    def agregar_horas(self, horas):
        if horas < 0:
            raise ValueError("Las horas trabajadas no pueden ser negativas.")
        self._horas_trabajadas.append(horas)

    def sueldo(self):
        return self._dependencia.calcular_sueldo(self._horas_trabajadas)

class RelacionDependencia(ABC):
    @abstractmethod
    def calcular_sueldo(self, horas_trabajadas):
        pass

class Contratado(RelacionDependencia):
    def __init__(self, horas_minimas, precio_hora):
        self._horas_minimas = horas_minimas
        self._precio_hora = precio_hora

    def calcular_sueldo(self, horas_trabajadas):
        sueldo = 0
        for horas in horas_trabajadas:
            if horas >= self._horas_minimas:
                sueldo += self._horas_minimas * self._precio_hora  # Sueldo por horas mínimas

        return sueldo

class Planta(RelacionDependencia):
    def __init__(self, nivel):
        self._nivel = nivel

    def calcular_sueldo(self, horas_trabajadas):
        total_horas = sum(horas_trabajadas)
        horas_extras = max(0, total_horas - 200)
        if total_horas >= 200:
            return self._nivel.valor_hora() * 200 + self._nivel.valor_hora() * horas_extras * 2
        return 0
class Nivel(ABC):
    def __init__(self, sueldo_base):
        self._sueldo_base = sueldo_base

    @abstractmethod
    def valor_hora(self):
        pass

class Operativo(Nivel):

    def valor_hora(self):
        return self._sueldo_base * 1.25

class Tecnico(Nivel):

    def valor_hora(self):
        return self._sueldo_base * 1.50

class Especialista(Nivel):

    def valor_hora(self):
        return self._sueldo_base * 1.75
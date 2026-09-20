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
    def __init__(self, sueldo_base, nivel):
        self._sueldo_base = sueldo_base
        self._nivel = nivel

    def calcular_sueldo(self, horas_trabajadas, nivel):
        return self.

class Nivel(ABC):
    @abstractmethod
    def calcular_sueldo(self, horas_trabajadas):
        pass

class Operativo(Nivel):

    def calcular_sueldo(self, horas_trabajadas):
        sueldo = 0
        if sum(horas_trabajadas) >= 200:
            sueldo = 200 * self._sueldo_base * 1.25 + (sum(horas_trabajadas) - 200) * self._sueldo_base * 1.25 * 2
        return sueldo

class Tecnico(Nivel):

    def calcular_sueldo(self, horas_trabajadas):
        sueldo = 0
        if sum(horas_trabajadas) >= 200:
            sueldo = 200 * self._sueldo_base * 1.50 + (sum(horas_trabajadas) - 200) * self._sueldo_base * 1.50 * 2
        return sueldo

class Especialista(Nivel):

    def calcular_sueldo(self, horas_trabajadas):
        sueldo = 0
        if sum(horas_trabajadas) >= 200:
            sueldo = 200 * self._sueldo_base * 1.75 + (sum(horas_trabajadas) - 200) * self._sueldo_base * 1.75 * 2
        return sueldo
from abc import ABC, abstractmethod

class Empresa:
    def __init__(self):
        self._empleados = []

    def agregar_empleado(self, empleado):
        self._empleados.append(empleado)

    def total_sueldos_a_pagar(self):
        sueldo = 0
        for empleado in self._empleados:
            sueldo += empleado.sueldo()
        return sueldo

    def optimizar_sueldos(self, horas_minimas, precio_hora):
        for empleado in self._empleados:
            empleado.optimizar(horas_minimas, precio_hora)

    def mejor_sueldo(self):
        if not self._empleados:
            return 0
        return max(empleado.sueldo() for empleado in self._empleados)

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

    def efectivizar(self, nivel):
        self._dependencia = self._dependencia.efectivizar(nivel)

    def precarizar(self, horas_minimas, precio_hora):
        self._dependencia = self._dependencia.precarizar(horas_minimas, precio_hora)

    def optimizar(self, horas_minimas, precio_hora):
        self._dependencia = self._dependencia.optimizar(horas_minimas, precio_hora)

class RelacionDependencia(ABC):

    @abstractmethod
    def calcular_sueldo(self, horas_trabajadas):
        pass

    @abstractmethod
    def efectivizar(self, nivel):
        pass

    @abstractmethod
    def precarizar(self, horas_minimas, precio_hora):
        pass

    @abstractmethod
    def optimizar(self, horas_minimas, precio_hora):
        pass

class Contratado(RelacionDependencia):
    def __init__(self, horas_minimas, precio_hora):
        if horas_minimas < 0:
            raise ValueError("Las horas mínimas no pueden ser negativas.")
        if precio_hora < 0:
            raise ValueError("El precio por hora no puede ser negativo.")
        self._horas_minimas = horas_minimas
        self._precio_hora = precio_hora

    def calcular_sueldo(self, horas_trabajadas):
        sueldo = 0
        for horas in horas_trabajadas:
            if horas >= self._horas_minimas:
                sueldo += self._horas_minimas * self._precio_hora  # Sueldo por horas mínimas

        return sueldo

    def efectivizar(self, nivel):
        return Planta(nivel)

    def precarizar(self, horas_minimas, precio_hora):
        raise ValueError("El empleado ya es contratado.")

    def optimizar(self, horas_minimas, precio_hora):
        return self

class Planta(RelacionDependencia):
    def __init__(self, nivel):
        self._nivel = nivel

    def calcular_sueldo(self, horas_trabajadas):
        total_horas = sum(horas_trabajadas)
        horas_extras = max(0, total_horas - 200)
        if total_horas >= 200:
            return self._nivel.valor_hora() * 200 + self._nivel.valor_hora() * horas_extras * 2
        return 0

    def efectivizar(self, nivel):
        raise ValueError("El empleado ya es de planta.")

    def precarizar(self, horas_minimas, precio_hora):
        return Contratado(horas_minimas, precio_hora)

    def optimizar(self, horas_minimas, precio_hora):
        return Contratado(horas_minimas, precio_hora)

class Nivel(ABC):

    @abstractmethod
    def valor_hora(self):
        pass

class Operativo(Nivel):

    def valor_hora(self):
        return 100

class Tecnico(Nivel):

    def valor_hora(self):
        return 150

class Especialista(Nivel):

    def valor_hora(self):
        return 200
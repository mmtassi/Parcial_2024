import pytest
from solucion.clases import *


def test_sueldo_contratado():
    dependencia = Contratado(8, 100)

    pepe = Empleado("pepe", "argento", 33888999, dependencia)
    pepe.agregar_horas(10)
    pepe.agregar_horas(8)
    pepe.agregar_horas(7)
    pepe.agregar_horas(7)
    pepe.agregar_horas(8)
    pepe.agregar_horas(8)
    pepe.agregar_horas(8)
    pepe.agregar_horas(8)
    pepe.agregar_horas(8)
    pepe.agregar_horas(8)
    pepe.agregar_horas(8)

    assert pepe.sueldo() == 7200

def test_sueldo_planta():
    dependencia = Planta(Operativo())

    pepe = Empleado("pepe", "argento", 33888999, dependencia)

    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)


    assert pepe.sueldo() == 20000
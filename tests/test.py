import pytest
from solucion.clases import *

def test_incorporar_empleado():
    empresa = Empresa()
    dependencia = Contratado(8, 100)

    pepe = Empleado("pepe", "argento", 33888999, dependencia)

    lionel = Empleado("lionel", "messi", 12345678, Planta(Operativo()))

    empresa.agregar_empleado(lionel)
    empresa.agregar_empleado(pepe)

    assert len(empresa.empleados) == 2
    assert empresa.empleados[0].nombre == "lionel"
    assert empresa.empleados[0].apellido == "messi"
    assert empresa.empleados[0].dni == 12345678

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

def test_total_sueldos():
    empresa = Empresa()
    pepe = Empleado("Pepe", "Argento", 33888999, Contratado(8, 100))
    empresa.agregar_empleado(pepe)

    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(200)
    pepe.agregar_horas(5)

    matias = Empleado("Matias", "Tassi", 37355549, Planta(Especialista()))
    empresa.agregar_empleado(matias)

    matias.agregar_horas(10)
    matias.agregar_horas(10)
    matias.agregar_horas(10)
    matias.agregar_horas(200)
    matias.agregar_horas(5)

    assert empresa.total_sueldos_a_pagar() == 4000 + 40000 + 14000


def test_mejor_sueldo():
    empresa = Empresa()
    pepe = Empleado("Pepe", "Argento", 33888999, Contratado(8, 100))
    empresa.agregar_empleado(pepe)

    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(200)
    pepe.agregar_horas(5)

    matias = Empleado("Matias", "Tassi", 37355549, Planta(Especialista()))
    empresa.agregar_empleado(matias)

    matias.agregar_horas(10)
    matias.agregar_horas(10)
    matias.agregar_horas(10)
    matias.agregar_horas(200)
    matias.agregar_horas(5)

    assert empresa.mejor_sueldo() == 54000


def test_efectivizar():
    empresa = Empresa()
    pepe = Empleado("Pepe", "Argento", 33888999, Contratado(8, 100))
    empresa.agregar_empleado(pepe)

    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(10)
    pepe.agregar_horas(200)
    pepe.agregar_horas(5)

    pepe.efectivizar(Operativo())

    assert pepe.sueldo() == 29000


def test_precarizar():

    empresa = Empresa()
    matias = Empleado("Matias", "Tassi", 37355549, Planta(Especialista()))
    empresa.agregar_empleado(matias)

    matias.agregar_horas(10)
    matias.agregar_horas(10)
    matias.agregar_horas(10)
    matias.agregar_horas(200)
    matias.agregar_horas(5)

    matias.precarizar(8, 100)
    assert matias.sueldo() == 3200

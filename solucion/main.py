from solucion.clases import *

empresa = Empresa()
pepe = Empleado("pepe", "argento", 33888999, Contratado(8, 100))
empresa.agregar_empleado(pepe)

pepe.agregar_horas(10)
pepe.agregar_horas(10)
pepe.agregar_horas(10)
pepe.agregar_horas(10)
pepe.agregar_horas(200)
pepe.agregar_horas(5)

print(pepe.sueldo())

pepe.efectivizar(Operativo())

print(pepe.sueldo())
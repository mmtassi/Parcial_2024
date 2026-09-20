from solucion.clases import *

empresa = Empresa()
pepe = Empleado("Pepe", "Argento", 33888999, Contratado(8, 100))
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

matias = Empleado("Matias", "Tassi", 37355549, Planta(Especialista()))
empresa.agregar_empleado(matias)

matias.agregar_horas(10)
matias.agregar_horas(10)
matias.agregar_horas(10)
matias.agregar_horas(200)
matias.agregar_horas(5)

print(matias.sueldo())

for empleado in empresa._empleados:
    print(f"{empleado._nombre} {empleado._apellido} - Sueldo: {empleado.sueldo()}")
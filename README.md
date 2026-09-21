Preguntas teóricas
Responder las siguientes preguntas sin realizar ningún código:
1. ¿Es necesario realizar cambios sobre la lógica inicial del método total_sueldos_a_pagar cuando se agreguen nuevos tipos de empleados? Justificar conceptualmente.
    Respuesta: No, no es necesario porque el metodo total_sueldos_a_pagar trabaja directamente con empleados, empresa esta totalmente desacoplada de los tipos de empleados, por lo que no se ve afectada si agrego nuevos tipos de empleados. 
2. ¿Qué concepto del paradigma orientado a objetos se rompería al utilizar IF en el método optimizar_sueldos? Justificar conceptualmente.
    Respuesta: Se rompe el polimorfismo, porque si uso IF preguntaria cada tipo de empleado, entonces no estarian comportandose segun su estado cada objeto, sino que se estaria preguntando por su tipo, lo cual rompe el principio de polimorfismo.
                     
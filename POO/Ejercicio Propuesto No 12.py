"""Un empleado trabaja 48 horas en la semana a razón de $5.000 hora. El porcentaje de
retención en la fuente es del 12,5% del salario bruto. Se desea saber cuál es el salario bruto,
la retención en la fuente y el salario neto del trabajador. """

Horas = 48
Valor_Hora = 5000
retencion = 0.125
Salario_Bruto = Horas * Valor_Hora
Retencion_Fuente = Salario_Bruto * retencion
Salario_Neto = Salario_Bruto - Retencion_Fuente
print ("El Salario Bruto es:", Salario_Bruto)
print ("La Retención en la Fuente es:", Retencion_Fuente)
print ("El Salario Neto es:", Salario_Neto)
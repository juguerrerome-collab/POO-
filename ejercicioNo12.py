# El empleado trabaja 48 horas a la semana y gana 5000$ por hora
#retencion en la fuente 12,5% 
#calcular salario bruto, retencion en la fuente y el salario neto del trabajador
print ("----------------------------------------------------")
horas = 48;
valor_hora = 5000;
retencion = 0.125;
salario_bruto = horas * valor_hora;
valor_retencion = salario_bruto * retencion;
salario_neto = salario_bruto - valor_retencion;

print (f"el salario bruto es : {salario_bruto}$");
print (f"el valor de la retencion en la fuente es : {valor_retencion}$")
print (f"el salario neto es : {salario_neto}$");
print ("----------------------------------------------------")
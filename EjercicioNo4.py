# la mama de juan tiene 3 hijos
#preguntarle la edad a juan 
#Alberto tendra 2/3 de la edad de juan
#Ana debe tener 3/4 de la edad de juan 
# la edad de la mama es la suma de las tres edades
print ("----------------------------------------------------")
edad_juan = int(input(" Hola Juan, ¿cuantos años tienes? : "))
print (f"la edad de juan es : {edad_juan} años");
edad_alberto = int(edad_juan*2/3)
print (f"la edad de alberto es : {edad_alberto} años");
edad_ana = int(edad_juan*3/4)
print (f"la edad de ana es : {edad_ana} años");     
edad_mama = int(edad_juan + edad_alberto + edad_ana)
print (f"la edad de la mama es : {edad_mama} años");



# funcion keys y values como matrices separadas 

agenda = {
"pedro": 35,
"antonio": 26,
"lucas": 19,
"claudia": 25,
"esteban": 24,
"pablo": 30
}
 # matrices separadas 
llave= agenda.keys()
valor = agenda.values()
print(llave, valor,)

 # orden alfabetico de las keys con susrespectivos values
orden =  sorted(llave)
ordentotal = {}
for key in orden:
    ordentotal[key] = agenda[key]

print(ordentotal) 
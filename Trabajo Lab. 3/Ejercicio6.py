#EJERCICIO 6
#Alejandro Nava Castillo
anr=input("Ingrese Tiempo(en an~os)")
while anr<0:
    print "No hay edades negativas"
    anr=input("Ingrese Tiempo(en an~os)")
if anr<3:
    anp=anr*10.5
if anr>=3:
    anp=((anr-3)*4)+(3*10.5)
print anr, "an~os es igual a", anp, "an~os perro"

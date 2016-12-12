#EJERCICIO 1
#Alejandro Nava Castillo
tn=raw_input('Ingrese Su Archivo De Texto(sin extension) ')
t=tn+".txt"
cumple=0
try:
    archivo=open(t)
    archivo.close()
    cumple=0
except:
    cumple=1
while cumple==1:
    print"Su archivo no se encuentre en el directorio de ejecucion"
    tn=raw_input('Por favor, ingrese otro nombre ')
    t=tn+".txt"
    try:
        archivo=open(t)
        archivo.close()
        cumple=0
    except:
        cumple=1
tex=open(t, "r")
arc=tex.readline()
N=input("Ingrese el numero de lineas que quiere leer ")
while N<0:
    print"No hay lineas negativas"
    N=input("Por favor ingrese otro valor ")
n=range(0,N)
for i in n:
    print ""
    print arc
    arc=tex.readline()

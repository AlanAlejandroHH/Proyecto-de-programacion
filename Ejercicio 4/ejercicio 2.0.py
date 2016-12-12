#EJERCICIO 1
#Alejandro Nava Castillo
N=input("Cuantos archivos desea analizar? ")
n=range(0,N)
tn=[]
t=[]
cumple=0
def verificacion(xn,x):
    try:
        archivo=open(x)
        archivo.close()
        cumple=0
        tm=t
    except:
        cumple=1
    while cumple==1:
        print"Su archivo no se encuentre en el directorio de ejecucion"
        xn=raw_input('Por favor, ingrese otro nombre ')
    try:
        x=xn+".txt"
        archivo=open(x)
        archivo.close()
        cumple=0
        x=xn+".txt"
    except:
        cumple=1
lista=[]
arc=[]
for i in n:
    xni=raw_input('Ingrese Su Archivo De Texto(sin extension) ')
    xi=xni+".txt"
    verificacion(xni,xi)
    lista.append(xi)
print lista

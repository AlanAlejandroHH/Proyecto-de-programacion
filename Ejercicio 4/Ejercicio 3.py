#EJERCICIO 3
#Alejandro Nava Castillo
#Solo correr en python, no ipython
tn=raw_input('Ingrese Su Archivo De Texto(sin extension) ')
t=tn+".txt"
def verificacion(xn,x):
    cumple=0
    try:
        archivo=open(x)
        archivo.close()
        cumple=0
    except:
        cumple=1
    while cumple==1:
        print"Su archivo no se encuentre en el directorio de ejecucion"
        xn=raw_input('Por favor, ingrese otro nombre ')
        x=xn+".txt"
        try:
            archivo=open(x)
            archivo.close()
            cumple=0
        except:
            cumple=1
verificacion(tn,t)
pn=raw_input('Ingrese Su Archivo De Salida(sin extension) ')
p=pn+".txt"
tex=open(t, "r")
arc=tex.readline()
N=(len(tn)+1)
N2=(len(tn))
n=range(0,N)
n2=range(0,N2)
arc=[]
tex.close()
tex=open(t,'r')
arc=tex.readlines()
lista=[]
for i in n:
    print (i+1),")",arc[i]
newtex=open(p,'w')
newtex.close()
newtex=open(p,'w+')
lineas=newtex.readlines()
for i in n:
    newtex.write(str(i+1)+") "+arc[i])
newtex.close()

#EJERCICIO 2
#Alejandro Nava Castillo
N=input("Cuantos archivos desea analizar? ")
gg=raw_input('Nombre del nuevo archivo ')
g=gg+".txt"
n=range(0,N)
lista=[]
tex=[]
def verificacion(t,tn):
    cumple=0
    try:
        archivo=open(t)
        cumple=0
    except:
        cumple=1
        while cumple==1:
            print"Su archivo no se encuentre en el directorio de ejecucion"
            tn=raw_input('Por favor, ingrese otro nombre ')
            t=tn+".txt"
            try:
                archivo=open(t)
                cumple=0
            except:
                cumple=1
    return t
    return tn
for i in n:
  tni=raw_input('Ingrese Su Archivo De Texto(sin extension) ')
  ti=tni+".txt"
  ti=verificacion(ti,tni)
  lista.append(ti)
print lista
#(En consideracion) print nuevoarchivo,"Contiene elementos de los archivos",lista
ran=range(0,len(lista))
new=open(g,'w+')
def agregaralista(x):
    for i in ran:
        new.write(lista[i])
        new.write('\n')
agregaralista(lista)

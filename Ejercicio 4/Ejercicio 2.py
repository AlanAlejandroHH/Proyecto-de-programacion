#EJERCICIO 2
#Alejandro Nava Castillo
N=input("Cuantos archivos desea analizar? ")
gg=raw_input('Nombre del nuevo archivo ')
nuevoarchivo=gg+".txt"
n=range(0,N)
lista=[]
tex=[]
cumple=0
def verificacion(xn,x):
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
for i in n:
  cn=raw_input('Ingrese Su Archivo De Texto(sin extension) ')
  c=cn+".txt"
  verificacion(cn,c)
  lista.append(c)
#(En consideracion) print nuevoarchivo,"Contiene elementos de los archivos",lista
contlista=range(0,len(lista))
new=open(nuevoarchivo,'w+')
def agregaralista(x):
    abierto=open(x,'r')
    abierto2=abierto.readlines()
    kk=range(0,len(abierto2))
    for i in kk:
        new.write(abierto2[i])
    new.write('\n')
for i in contlista:
    agregaralista(lista[i])

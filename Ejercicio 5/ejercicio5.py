#Practica 5
#Alejandro Nava Castillo
import csv
tp=open('periodicTable.csv')
lns=csv.reader(tp,delimiter=';')
for line in lns:
    no_atom=line[0]
print no_atom

#EJERCICIO 7
#Alejandro Nava Castillo
n=raw_input('Ingrese nombre' ).title()
s=map(str,n)
v=('a','e','i','o','u','A','E','I','O','U')
if n[0]==v[0] or n[0]==v[1] or n[0]==v[2] or n[0]==v[3] or n[0]==v[4]:
    new=n.lower()
elif n[0]==v[5] or n[0]==v[6] or n[0]==v[7] or n[0]==v[8] or n[0]==v[9]:
    new=n.lower()
else:
    new=n[1:]
    if n[1]==v[0] or n[1]==v[1] or n[1]==v[2] or n[1]==v[3] or n[1]==v[4]:
      new=new
    elif n[1]==v[5] or n[1]==v[6] or n[1]==v[7] or n[1]==v[8] or n[1]==v[9]:
      new=new
    else:
      new=new[1:]
print n+"!"
print n+",",n,"bo B"+new,"Bonana fanna fo F"+new,"Fee fy mo M"+new +",", n+"!"

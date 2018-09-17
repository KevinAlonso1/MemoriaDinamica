__author__='Kevin Alonso'
numeros=[6, 8, 9, 12, 23, 19, 65, 33, 78, 89, 26, 45, 31]
print(numeros)
c=0
for i in range(int(len(numeros)/2)):
    c=c-1
    x=numeros[i]
    numeros[c]=x
print(numeros)

def invertirArreglo_1(list, a, z):
    if(int(len(list)/2)):
        return list


logitud=int(len(numeros))-1
a=int(0)
while((logitud-a)>a):
    aux=numeros[a]
    numeros[a]=numeros[logitud-a]
    numeros[logitud-a]=aux
    a=a+1

print(numeros)
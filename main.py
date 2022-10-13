#1) Realiza un programa que lea tres números por teclado y permita evaluar lo siguiente:
a=int(input('Introduce un numero: '))
b=int(input('Introduce otro: '))
c=int(input('Introduce un tercero: '))

#Evaluar el orden de los números
if a == 0:
  print('Error porque el primer numero es 0')
elif c>b>a:
  print('Los numeros estan en orden ascendente')
else:
  print('Los numeros NO estan en orden ascendente')

print('')
#2) Realiza el ejercicio anterior pero introduciendo los numeros en una lista:
lista=[]
for x in range(3):
  numeros=int(input("Introduce un numero:"))
  lista.append(numeros)

i=0
while i < len(lista): 
  if (lista[i] == 0):
    print('Error porque el primer numero es 0')
  elif(lista[i] < lista[i - 1]): 
    print ('Los numeros estan en orden ascendente') 
  else : 
    print ('Los numeros NO estan en orden ascendente') 
  break

print('')
#3) Realiza un programa que lea letras y cuente con una variable contador las letras "a" que se introducen. Para salir del programa, introducir el carácter ".". Al finalizar mostrar el número de veces que se ha pulsado la letra "a".
letras=input('Introduce una letra:')
while letras!='.':
  lista.append(letras)
  letras=input('Introduce una letra:')

contador=lista.count('a')
print('La letra a aparece', contador, 'veces')

print('')
#4) Crea una lista de palabras, recorre la lista y muestra cada palabra junto con su longitud. Al final, indicar cual fue la palabra con más caracteres.
colores=['morado','azul','amarillo','gris','verde','granate','negro']
longitudes=[len(colores[0]),len(colores[1]),len(colores[2]),len(colores[3]),len(colores[4]),len(colores[5]),len(colores[6])]


respuesta={}
for color in colores:
  for longitud in longitudes:
    respuesta[color]=longitud
    longitudes.remove(longitud)
    break

print(respuesta)

max_value=max(colores)
print('la palabra mas larga es',max_value)
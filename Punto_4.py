myArray = [1,2,2,3,3,3,4,4,4,4,5]
secu = []

repeticiones = {}
for I in myArray:
  if I in repeticiones:
    repeticiones[I] += 1
  else:
    repeticiones[I] = 1

print(repeticiones)
print("   ")

ID = int(0)
Sec = int(0)

for I in range(len(myArray)):
  if(ID != myArray[I]):
    ID = myArray[I]
    Sec = 0
    for J in range(I, len(myArray)):
      if (ID == myArray[J]):
        Sec += 1
      else:
        break
    secu.append(str(ID) +" con secuencia de "+ str(Sec)+"")
print(secu)
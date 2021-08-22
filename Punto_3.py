
def es_simentrica(myArray,orden):
    simetrica=True
    for i  in range (orden):
        for j in range (orden):
            if (myArray[i][j] != myArray[j][i]):
                simetrica=False
        return simetrica

def main():
    myArray = ['a', 'b', 'c', 'd', 'd', 'c', 'b', 'a']

    respuesta=es_simentrica(myArray,len(myArray))
    if (respuesta==True):
        print("Symmetric")
    else:
        print("Asymmetric")

main()





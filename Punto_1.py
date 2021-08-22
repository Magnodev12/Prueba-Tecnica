n=5

def cruz(n):
    resultado=""
    if n == 0:
        print("ERROR")
    else:
        for i in range(n):
            for j in range(n):
                resultado += "X" if (j==i or j==n-i-1) else "_"
        resultado += "\n"
    return resultado
print(cruz(n))
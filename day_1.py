with open("input.txt", "r", encoding="utf-16") as archivo:
    matriz = [list(map(int, linea.split())) for linea in archivo]



def processLists(matriz):
    result = 0;
    matriz1 = []
    matriz2 = []
    pos = 0
    print(matriz)
    for i in matriz:
        matriz1.append(i[0])
    for j in matriz:
        matriz2.append(j[1])

    matriz1 = sorted(matriz1)
    matriz2 = sorted(matriz2)
    for m1 in range(len(matriz1)):
        print(abs(matriz1[m1] - matriz2[m1]))
        result += (abs(matriz1[m1] - matriz2[m1]))
    print(result)
        


processLists(matriz)

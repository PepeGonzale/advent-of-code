with open("input.txt", "r", encoding="utf-16") as archivo:
    matriz = [list(map(int, linea.split())) for linea in archivo]



def processLists(matriz):
    result = 0;
    matriz1 = []
    matriz2 = []
    pos = 0
    for i in matriz:
        matriz1.append(i[0])
    for j in matriz:
        matriz2.append(j[1])

    matriz1 = sorted(matriz1)
    matriz2 = sorted(matriz2)
    
    for m1 in range(len(matriz1)):
        result += (abs(matriz1[m1] - matriz2[m1]))        
    return result
def checkRepeatedNumbers(matriz):
    total_sum = 0
    current_sum = 0
    matriz1 = []
    matriz2 = []
    pos = 0
    for i in matriz:
        matriz1.append(i[0])
    for j in matriz:
        matriz2.append(j[1])
    # iterar por el primero, llevar un contador con la sum
    for i in range(len(matriz1)):
        print(matriz1[i -1], current_sum)
        total_sum += (matriz1[i - 1] * current_sum)
        current_sum = 0
        for j in range(len(matriz2)): 
            if (matriz1[i] == matriz2[j]):
                current_sum += 1
  

    return total_sum

result = processLists(matriz)
result2 = checkRepeatedNumbers(matriz)

print(result2)

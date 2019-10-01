from sys import stdin
import sys
sys.setrecursionlimit(1000000)
##Anderson Laverde
##8923082
#Codigo de Honor : Como miembro de la comunidad Academica de la pontificia
##Universidad Javeriana cali me comprometo a seguir los mas altos estandare
#de integridad academica.
stop=[44721361, 181714, 12449, 2608, 950, 473, 286, 197, 148, 119, 100, 87, 78, 72, 67, 63, 61, 59, 57, 56, 55, 54, 54, 54, 54, 54]
dictionary={}
def combinatoria(n,k):
    up = 1
    down = 1
    for i in range(n,n-k,-1):
        up = up*i
    for j in range(k,0,-1):
        down = down*j
    return up//down
def binarySearch(m):  
    dictionary[m]=[(m,1)]
    sentinel= True
    low=2
    hight = m
    level = 2
    rep=0
    while (low+1)!= hight and rep<3 and sentinel:
        mid =low+((hight-low)// 2)
        midClevel=combinatoria(mid,level)
        print("(",mid,",",level,")",midClevel)
        if midClevel == m:
            temp = (mid,level)
            dictionary[m].append(temp)
            sentinel=False
            print(dictionary)
            rep+=1
            level+=1
        if midClevel< m:
            low = mid + 1
        else:
            hight = mid - 1


def main():
    """
    Funcion que me genera la salida con el formato propuesto para la respuesta
    """
    
    cases = int(stdin.readline())
    for case in range(cases):
        target= int(stdin.readline())
        ans=solve(target)
        print(len(ans))
        for pos in range(len(ans)):
            print("("+str(ans[pos][0])+","+str(ans[pos][1])+")",end=" ")
        print("")


binarySearch(28)


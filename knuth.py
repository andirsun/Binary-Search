from sys import stdin
import sys
sys.setrecursionlimit(1000000)
##Anderson Laverde
## Colaboradores: Santiago Coca Rojas,bryan vera,Antonio Yu,jeison santacruz


def insertar(permutacion, index,letra):
    return permutacion[:index] + letra + permutacion[index:]

def solve(line,respuesta,contador,restemporal):
    restemporal=[]
    contador+=1
    letraAdd=line[contador]
    restemporal=respuesta
    respuesta=[]
    for permutacion in restemporal:
        for posicion in range(len(permutacion)+1):
            copia= permutacion
            variable=insertar(permutacion,posicion,letraAdd)
            respuesta.append(variable)
    if (len(line)-contador) == 1:
        return respuesta
        
    return solve(line,respuesta,contador,restemporal)
        
                   
def main():
    contador=0
    global respuesta
    line = list(stdin.readline().strip())
    while line!=[]:
        if len(line)==1:
            print(line[0])
            print()
        else:
            respuesta=[line[0]]
            restemporal=[]
            ans=solve(line,respuesta,contador,restemporal)
            print(*ans,sep='\n')
            print()
        line = list(stdin.readline().strip())
        

main()


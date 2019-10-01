from sys import stdin
import sys
sys.setrecursionlimit(1000000)
##Anderson Laverde
## Colaboradores: jeison santacruz
def solve(target,tamano,indice,respuesta,lista):
    i=indice+1
    cont=lista[i-1]
    tmp=[]
    tmp.append(cont)
    if tmp[0] == target:
        respuesta.append(tmp)
    if indice == tamano-1:
        return respuesta
    while i<tamano:
        if cont == target:
            indice+=1
            return solve(target,tamano,indice,respuesta,lista)
        elif cont+lista[i]> target:
            i+=1
        else: 
            cont+=lista[i]
            tmp.append(lista[i])
            if sum(tmp) == target:
                respuesta.append(tmp)
            i+=1        
    indice+=1
    return solve(target,tamano,indice,respuesta,lista)
def main():
    line = list(stdin.readline().split())
    line = list(map(int, line)) ## vuelto lista de string a integers
    while line!=[0,0]:
        respuesta = []
        tamano = line[1]
        target=line[0]
        lista=line[2:]
        if tamano==0:
            print("Sums of",str(target)+":")
            print("NONE")
        else:
            ans= solve(target,tamano,0,respuesta,lista)
            print("Sums of",str(target)+":")
        
            if len(ans)!=0:
                for res in ans:
                    string=""
                    for indice in res:
                      string+=str(indice)+"+"
                    print(string[:len(string)-1])
            else:
                print("NONE")
        line = list(stdin.readline().split())
        line = list(map(int, line))
main()

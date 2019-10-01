from sys import stdin

def solve(A, M):
  low = 1
  hight = sum(A) ## Este es mi hi para poder contemplar desde el caso base que es cuando el recipiente valga A[final]
  mejoropcion = 0
  while low <= hight:
    mid = ((hight-low)//2)+low ## Suma segura para hallar la mitad
    #print("Mid",mid)
    if llenar(mid,A,M)==1:
      hight = mid-1
      mejoropcion = mid
    else:
      low = mid+1
  return mejoropcion

def llenar(topeMax,A,M):
  numRecipientes=0
  capcontenedor=0
  for vasija in A:
    if vasija > topeMax: ## Por si se desfaza
      return 0
    if capcontenedor+ vasija > topeMax:
      capcontenedor = 0
    if capcontenedor == 0:
      numRecipientes = numRecipientes+1
      #print("Aumente a otro recipiente")
    if numRecipientes > M:
      return 0
    capcontenedor = capcontenedor + vasija
    ##print("Hecho el contenedor :",vasija,"En el contenedor")
  return 1
    
    
def main():
  line = stdin.readline()
  while len(line)!=0:
    n,M = [ int(x) for x in line.split() ]
    A = [ int(x) for x in stdin.readline().split() ]
    print(solve(A, M))
    line = stdin.readline()

main()

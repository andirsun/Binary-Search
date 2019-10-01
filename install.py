from sys import stdin
from math import *
##Anderson Laverde Gracia
## Colaboradores : Santiago Coca, Yan carlos certuche, Jeison Santacruz

def solve(A,cobertura,islas):
  islas.sort(key=lambda island: island[0])##ordeno las tuplas por la coordenada x
  sumatoria= 0
  for i in range(0,len(islas)):
    if (i == 0):
      count = 1
      x1 = sqrt(cobertura*cobertura - islas[i][1]*islas[i][1])
      lx = islas[i][0] - x1
      rx = islas[i][0] + x1
    else:
      x1 = sqrt(cobertura * cobertura - islas[i][1] * islas[i][1]);
      llx = islas[i][0] - x1;
      rrx = islas[i][0] + x1;
      if (llx <= rx and rrx >= lx):
        lx = llx if (lx < llx) else lx
        rx = rrx if (rx > rrx) else rx
      else:
        sumatoria = sumatoria + 1
        lx = llx
        rx = rrx
  return sumatoria+1
  
def main():
  line=stdin.readline()
  case=1
  while line!='0 0\n':
    ok=False    
    if len(line)!=0 and line!='\n':
      L,G=[int(i) for i in line.split()] ##L son las islas y G la distancia de cobertura de los radares
      X=[0 for i in range(L)]
      R=[0 for i in range(L)]
      islas=[0 for i in range(L)]
      for i in range (L):
        ins=stdin.readline().split()
        x1,y1=int(ins[0]),int(ins[1])
        if y1>G:
          ok=True
        if ok==False:
          islas[i]= (x1,y1)
      if ok==False: 
        ans=solve(0,G,islas)
        print('Case {0}: {1}'.format(case,ans))
      else:
        print('Case {0}: {1}'.format(case,-1))
      case+=1
      line=stdin.readline()
    else:
      line=stdin.readline()
main()

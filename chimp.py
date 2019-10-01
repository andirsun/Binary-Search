from sys import stdin
##ADNERSON LAVERDE GRACIAa
def solve(ladies,x):
  malo = "X"
  menor = 0
  mayor = 0
  tamaño=len(ladies) # para comparar despues 
  low=0
  hight = tamaño -1 ##el tope del arreglo 
  while low<= hight:
    mid =(low+hight)// 2 ## obtengo la mitad del arreglo
    if ladies[mid] == x:
      return solve2(ladies,mid-1,mid+1,x)
    if ladies[mid]< x:
      low = mid + 1
    else:
      hight = mid - 1
  return solve2(ladies,hight,low,x) ##esto es por si nunca lo encuentra

def solve2(lst,menor,mayor,x):
  malo="X"
  minimo= 0
  maximo=0
  ##print(mayor,x)
  if x>lst[len(lst)-1]: ##caso cuando se va muy a la derecha
    print(lst[len(lst)-1],malo)
    return lst[len(lst)-1],malo
  if menor<0: ## desborda por izquierda
    maximo= lst[mayor]
    print(malo,maximo)
    return (malo,maximo)
  if x==lst[len(lst)-1]: ## desborda ala derecha
    minimo =lst[len(lst)-2]
    print(minimo,malo)
    return minimo,malo
  else:
    print(lst[menor],lst[mayor])
    return lst[menor],lst[mayor]
  
  
  
def main():
  inp = stdin
  inp.readline()
  ladies = [ int(x) for x in inp.readline().split() ]
  inp.readline()
  queries = [ int(x) for x in inp.readline().split() ]
  for x in queries:
    solve(ladies, x)

main()



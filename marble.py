from sys import stdin

marble,lenm = None,None
##anderson laverde
def solve(marble, l, r, x): 
    if r >= l: # caso base
        mid = l + (r - l)//2
        #Si esta en la mitad del arreglo
        if marble[mid] == x: 
            return mid 
        elif marble[mid] > x: 
            return solve(marble, l, mid-1, x) 
        else: 
            return solve(marble, mid+1,r,x) 
    else: 
        return -1 ##si no esta
    
def main():
  global marble,lenm
  case = 1
  lenm,lenq = [ int(x) for x in stdin.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(stdin.readline()) for i in range(lenm) ]
    marble.sort() ## ordeno el arreglo 
    print('CASE# {0}:'.format(case))
    for q in range(lenq):
      x = int(stdin.readline())
      ans = solve(marble,0,len(marble),x)
      if ans==-1 or marble[ans]!=x:
        print('{0} not found'.format(x))
      else:
        print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in stdin.readline().split() ]
    case += 1

main()

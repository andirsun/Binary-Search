"""
There are some processes that need to be executed. Amount of a load that process causes on a server that runs it, is being represented by a single integer. Total load caused on a server is the sum of the loads of all the processes that run on that server. You have at your disposal two servers, on which mentioned processes can be run. Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.



Write a function that, given an array A of N integers, of which represents loads caused by successive processes, the function should return the minimum absolute difference of server loads.



For example, given array A such that:

  A[0] = 1

  A[1] = 2

  A[2] = 3

  A[3] = 4

  A[4] = 5



your function should return 1. We can distribute the processes with loads 1, 2, 4 to the first server and 3, 5 to the second one, so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.



Assume that:

N is an integer within the range [1..1,000]

the sum of the elements of array A does not exceed 100,000


In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
"""
import sys

def loadToFirst(server1,server2,number):
    server1.append(number)
    return abs(sum(server2)-sum(server1))    
    
def loadToSecond(server1,server2,number):
    server2.append(number)
    return abs(sum(server2)-sum(server1))
def solution(A):
    server1 = []
    server2 = []
    server1.append(A[0])
    server1.append(A[1])
    for i in A[2:len(A)]:
        load1 = sum(server1)
        load2 = sum(server2)
        if(loadToFirst(server1,server2,i)<=loadToSecond(server1,server2,i)):
            server1.append(i)
        else:
            server2.append(i)
    return abs(sum(server2)-sum(server1))

def main():
  """Read from stdin, solve the problem, write answer to stdout."""
  input = sys.stdin.readline().split()
  A = [int(x) for x in input[0].split(",")]
  sys.stdout.write(str(solution(A)))


if __name__ == "__main__":
  main()

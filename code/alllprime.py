
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def printprime(n):
    for i in range(2,n+1):
        if(isprime(i)):
            print(i,end=" ")
        
n=int(input())
printprime(n)
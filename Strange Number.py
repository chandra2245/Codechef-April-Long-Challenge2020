def find(num): 
    su=[]
      
    # Find factors of number 
    # and add to the sum 
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            su.append( i) 
            num=num//i 
        i += 1
    if num!=1:
        su.append(num) 
      
    # Return sum of numbers 
    # having minimum product 
    return su
t=int(input())
def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if(n%i==0 or n%(i+2)==0): 
            return False
        i=i+6
    return True
while t>0:
    t-=1
    x,k=map(int,input().split())
    count=0
    fac=find(x)
    print(fac)
    for i in fac:
        if isPrime(i)==True:
            count+=1
    if k<=count:
        print(1)
    else:
        print(0)

test_case=int(input())
while test_case>0:
    test_case-=1
    n=int(input())
    min_pair=n//2
    if n==1:
        print(min_pair+1)
        print(1,1)
    elif n%2>0:
        print(min_pair)
        print(3,1,2,n)
        for itera in range(3,n,2):
            print(2,itera,itera+1)
    else:
        print(min_pair)
        for itera in range(1,n+1,2):
            print(2,itera,itera+1)

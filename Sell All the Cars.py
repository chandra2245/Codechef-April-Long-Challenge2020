test_case=int(input())
while test_case>0:
    test_case-=1
    final=0
    n=int(input())
    #flag value storing index
    flag=None
    array=list(map(int,input().split()))
    array.sort()
    array.reverse()
    #iterating
    for iters in range(n):
        if array[iters]<iters:
            flag=iters-1
            break
        final+=array[iters]
    if flag!=None:
        temp_fin=(flag*(flag+1))//2
        final-=temp_fin
        print(final%1000000007)
        #if not none
    else:
        n=n-1
        temp_fin=(n*(n+1))//2
        final-=temp_fin
        print(final%1000000007)
        #if none

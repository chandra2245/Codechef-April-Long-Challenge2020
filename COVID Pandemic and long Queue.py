test_case=int(input())
#no. of test cases
for _ in range(test_case):
    flag=0
    n=int(input())
    position=map(int,input().split())
    position=list(position)
    first_person=position.index(1)
    start=first_person+1
    #strt iteraion
    for iters in range(start,n):
        if position[iters]==1:
            gap=iters-first_person
            if gap<6:
                flag=1
                #breaking as condition fullflled
                break
            gap=0
            first_person=iters
    #printing final output
    if flag==1:
        print("NO")
    else:
        print("YES")

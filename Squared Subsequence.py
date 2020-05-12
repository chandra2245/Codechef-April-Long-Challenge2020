t=int(input())
while t>0:
    t-=1
    n=int(input())
    ar=list(map(int,input().split()))
    pos=0
    c,flag,count,ec=0,0,0,None
    for i in range(n):
        c+=1
        if ar[i]%4==2:
            ec=1
            if flag==0:
                pos=c
                c=0
                flag=1
                #print("go")
            else:
                #print(c)
                l=pos-1
                r=c-1
                x=min(l,r)
                ct=l+r+1
                count=count+((l+r+1)+(((x)*((2*(ct-2))+(x-1)*(-2)))//2))
                #print("here",ar[i],l,r,count)
                c=0
                pos=r+1
        elif ar[i]%4!=2 and ar[i]%2==0:
            ec=0
            if flag==1:
                l=pos-1
                r=c-1
                x=min(l,r)
                ct=l+r+1
                count=count+((l+r+1)+(((x)*((2*(ct-2))+(x-1)*(-2)))//2))
                #print("he",ar[i],l,r,count)
                c=0
                pos=r+1
                flag=0
            else:
                c=0
    tot=(n*(n+1))//2
    if ec==1:
        l=pos-1
        r=c
        #print(l,r)
        x=min(l,r)
        ct=l+r+1
        count=count+((ct)+(((x)*((2*(ct-2))+(x-1)*(-2)))//2))
    print(tot-count)
                

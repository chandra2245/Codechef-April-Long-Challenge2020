from collections import Counter
test_case=int(input())
for _ in range(test_case):
    ans=[]
    n,m,k=map(int,input().split())
    for i in range(n):
        ar=Counter(list(map(int,input().split())))
        ans.append(str(max(ar, key=ar.get)))
    print(" ".join(ans))

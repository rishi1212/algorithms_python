#geekforgeeks
t=int(input())
for i in range(0,t):
    n=int(input())
    copy=n
    while(copy>0):
        print copy,
        copy-=5
    while(copy<=n):
        print copy,
        copy+=5
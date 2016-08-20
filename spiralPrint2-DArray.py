def print_spiral(a,m,n):
    t=0
    b=m-1
    l=0
    r=n-1
    direction=0
    while(t<=b and l<=r):
        if(direction==0):
            for i in range(l,r):
                print (a[t][i])
            t+=1
        elif(direction==1):
            for i in range(t,b):
                print (a[i][r])
            r-=1
        elif (direction == 2):
            for i in range(r, l,-1):
                print (a[b][i])
            b -= 1
        elif (direction == 3):
            for i in range(b, t,-1):
                print (a[i][l])
            l += 1
        direction=(direction+1)%4

a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

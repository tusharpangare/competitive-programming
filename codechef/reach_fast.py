# https://www.codechef.com/problems/REACHFAST

for _ in range(int(input())):
    x,y,k=map(int,input().split())
    rem=(abs(y-x))%k
    if x==y:
        print("0")
    else:
        out=(abs(y-x))//k
        if rem!=0:
            out+=1
        print(out)    
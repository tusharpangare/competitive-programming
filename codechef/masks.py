# https://www.codechef.com/problems/CMASKS

# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    print("Cloth" if y*10<=x*100 else "Disposable")
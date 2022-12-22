# https://www.codechef.com/problems/CUTPAPER
# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    temp=n//k
    print(temp**2)
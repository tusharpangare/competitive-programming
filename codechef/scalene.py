# https://www.codechef.com/problems/SCALENE
for _ in range(int(input())):
    if len(set(map(int,input().split())))==3:
        print("YES")
    else:
        print("NO")
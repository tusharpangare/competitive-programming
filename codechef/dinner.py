# https://www.codechef.com/problems/CHEFDINE
'''
Input:
4
3 1
1 2 3
2 1 3
8 3
1 3 2 2 4 1 3 5
3 3 0 1 2 4 1 4
1 1
5
1
5 3
1 1 2 2 1
1 1 0 3 5

Output:
1
3
1
-1'''
'''
for _ in range(int(input())):
    n,k=map(int,input().split())
    category=list(map(int, input().split()[:n]))
    time=list(map(int, input().split()[:n]))
    dict={}

    for i in range(len(category)):
        temp=category[i]
        if temp in dict.keys():
            if dict[temp]>time[i]:
                dict[temp]=time[i]
        else:
            dict[temp]=time[i]

    if len(dict.keys())<k:
        print("-1")     
    else:
        dict_val=sorted(dict.values())
        print(sum(dict_val[:k]))'''


for _ in range(int(input())):
    n,k=map(int,input().split())
    category=list(map(int, input().split()[:n]))
    time=list(map(int, input().split()[:n]))
    
    time_sorted=sorted(set(time[:k]))
    print(sum(time_sorted))



'''
input:
3
4
1 2 3 4
4
1 -5 1 -5
6
-5 -1 -1 2 -2 -3

output:
1 1 1 1
4 3 2 1
1 1 3 2 1 1
'''

def check_dif(a,b):
    if (a>0 and b<0) or (a<0 and b>0):
        return True
    return False    

def main():
    for _ in range(int(input())):
        n=int(input())
        arr=list(map(int, input().split()))
        
        for x in range(n):
            i=x
            count=1
            while i<n-1:
                if check_dif(arr[i],arr[i+1]):
                    count+=1
                    i+=1
                    continue
                else:
                    i+=1
                    break    
                    
            print(count, end=" ")     
        print()       

main()


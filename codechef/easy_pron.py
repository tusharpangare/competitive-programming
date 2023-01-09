'''# cook your dish here
for _ in range(int(input())):
    n=int(input())
    word=input()
    vowels=["a","e","i","o","u"]
    ct=0
    flag=True
    for i in range(n-1):
        if word[i]  not in vowels and word[i+1] not in vowels:
            ct+=1  
        if ct>=4:
            flag=False
            break
    if flag:
        print("YES")
    else:
        print("NO")'''

        

'''
for _ in range(int(input())):
    n = int(input())
    s = input()
    if n<=3:
        print("YES")
    else:
        for i in range(n-3):
            string = s[i:i+4]
            vow1 = 'a' in string or 'e' in string or 'i' in string 
            vow2 = 'o' in string or 'u' in string 
            if not vow1 and not vow2:
                print("NO")
                break 
        else:
            print("YES")
        
    '''
        


for _ in range(int(input())):
    n=int(input())
    word=input()
    vowels=["a","e","i","o","u"]
    ct=1
    i=0
    while ct<4 and i<n-1:
        if word[i]  not in vowels and word[i+1] not in vowels:
            ct+=1  
        else:
            ct=1
        i+=1

    if ct>=4:
        print("NO")
    else:
        print("YES")

                   
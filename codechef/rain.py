'''# cook your dish here
for _ in range(int (input())):
    rainVal=int(input())
    if(rainVal <3):
        print("LIGHT")
    elif(rainVal>=3 and rainVal<7):
        print("MODERATE")
    elif(rainVal>=7):
        print("HEAVY")        '''

l=[1,1,2]
l.pop(1)
print(l)
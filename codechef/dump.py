n,k=8,3
category=[1,3,2,2,4,1,3,5]
time=[3,3,0,1,2,4,1,4]
dict={}

for i in range(len(category)):
    temp=category[i]
    if temp in dict.keys():
        if dict[temp]>time[i]:
            dict[temp]=time[i]
    else:
        dict[temp]=time[i]

print(dict)
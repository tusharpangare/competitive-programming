for _ in range(int(input())):
    n,x=map(int,input().split())
    freshness=list(map(int, input().split()[:n]))
    cost=list(map(int, input().split()[:n]))

    total_cost=0
    for i in range(n):
        if freshness[i]>=x:
            total_cost+=cost[i]
    print(total_cost)

    '''total_cost= sum([i for i in cost if freshness[cost.index(i)]>=x])
    print(total_cost)'''

    '''total_cost=0
    my_dict=dict(zip(freshness,cost))
    for i in my_dict.keys():
        if i>=x:
            total_cost+=my_dict[i]
    print(total_cost)    '''    


    
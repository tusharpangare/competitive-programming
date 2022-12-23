# https://www.codechef.com/problems/MTYFRI
for _ in range(int(input())):
    n,k=map(int,input().split())
    sequenceA=list(map(int, input().split()[:n]))
    motu=[sequenceA[i] for i in range(n) if i%2==0 ]
    tomu=[sequenceA[i] for i in range(n) if i%2==1 ]
    while k>0:
        if sum(tomu)>sum(motu):
            break
        else:
            m_max=max(motu)
            t_min=min(tomu)
            motu[motu.index(m_max)]=t_min
            tomu[tomu.index(t_min)]=m_max
        k-=1
    
    if sum(tomu)>sum(motu):
        print("YES")
    else:
        print("NO")            

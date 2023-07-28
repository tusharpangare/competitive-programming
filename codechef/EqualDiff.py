# some test cases have failed
# Problem not yet solved
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    freq = {}  # Dictionary to store the frequency of each integer
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    
    max_freq = max(freq.values())  # Maximum frequency of any integer in the array
    min_deletions = len(arr) - max_freq  # Minimum deletions = Total elements - Maximum frequency
    
    print(min_deletions)
    
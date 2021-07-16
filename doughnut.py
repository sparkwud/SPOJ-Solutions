t = int(input())
for step in range(t):    
    c, k, w = map(int, input().split())       
    print("yes") if (c * w <= k) else print("no")






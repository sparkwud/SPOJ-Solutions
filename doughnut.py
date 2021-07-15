t = int(input())
for step in range(t):    
    c, k, w = map(int, input().split())       
    print("yes") if (c * w <= k) else print("no")





for step in range(int(input("Enter the number of steps: "))):
    c, k, w = [int(input()) for num in range(3)]
    print("yes") if k >= c * w else print("no")







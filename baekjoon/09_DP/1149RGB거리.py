import sys
si = sys.stdin.readline

n = int(si())
cost = [list(map(int, si().split())) for _ in range(n)] # red, green, blue

for i in range(1,n):
    #red, green, blue
    cost[i][0] = min(cost[i-1][1],cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0],cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0],cost[i-1][1]) + cost[i][2]

print(min(cost[n-1]))
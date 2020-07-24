def getP(n,grid):           #Get the position of the Princess
    i=0
    j=0
    while i<n:
        while j<n:
            if grid[i][j]=='p':
                return i,j
            else:
                j+=n-1
        i+=n-1
        j=0


def displayPathtoPrincess(n,grid):
    pr,pc=getP(n,grid)
    r,c=(n-1)//2,(n-1)//2             #Bot is in the Centre
    if pr<r and pc<c:
        for _ in range(r,pr,-1):
            print("UP")
        for _ in range(c,pc,-1):
            print("LEFT")
    elif pr<r and pc>c:
        for _ in range(r, pr, -1):
            print("UP")
        for _ in range(c, pc):
            print("RIGHT")
    elif pc<c and pr>r:
        for _ in range(r,pr):
            print("DOWN")
        for _ in range(c,pc,-1):
            print("LEFT")
    else:
        for _ in range(r, pr):
            print("DOWN")
        for _ in range(c, pc):
            print("RIGHT")

m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
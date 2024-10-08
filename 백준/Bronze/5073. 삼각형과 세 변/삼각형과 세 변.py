import sys

def input():
    return sys.stdin.readline().rstrip()

over = False

while not over:
    tri = list(map(int, input().split()))
    if tri[0] == 0:
        over = True
        break
        
    else:
        tri.sort()
        if tri[2] >= tri[0] + tri[1]:
            print("Invalid")

        else:
            if tri[0] == tri[1] and tri[1] == tri[2]:
                print("Equilateral")
            elif tri[0] == tri[1] or tri[1] == tri[2]:
                print("Isosceles")
            else:
                print("Scalene")

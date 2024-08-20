N, M = map(int, input().split())
rec = []

for _ in range(N):
    rec.append(list(map(int, list(input()))))

largest_square_width = min(N, M)

result = 1

def check(rectangle, width):
    # start, end point -> 왼쪽 위
    for i in range(len(rectangle)-width+1):
        for j in range(len(rectangle[0])-width+1):
            if (rectangle[i][j], 
                rectangle[i+width-1][j],
                rectangle[i][j+width-1], 
                rectangle[i+width-1][j+width-1]).count(rectangle[i][j]) == 4:
                return True

    return  False
for i in range(largest_square_width, 1, -1):
    if check(rec, i):
        print(i*i)
        break
else:
    print(result)
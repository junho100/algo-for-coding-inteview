N = int(input())

result = 0
for i in range(N+1):
    for j in range(60):
        for k in range(60):
            string = str(i) + str(j) + str(k)
            if ("3" in string):
                result += 1

print(result)
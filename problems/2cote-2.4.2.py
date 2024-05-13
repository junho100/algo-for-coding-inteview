# a = input()
# y = ord(a[0]) - 96
# x = int(a[1])

# arr = []
# for _ in range(9):
#     arr.append([0 for _ in range(9)])

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# result = 0
# # 0 1    2, 3
# for i in range(4):
#     for j in range(2):
#         if (i == 0 or i == 1):
#             nx = x + dx[i]*2
#             ny = y + dy[j+2]

#             if (nx < 1 or nx > 8 or ny < 1 or ny > 8):
#                 continue

#             result += 1
#         if (i == 2 or i == 3):
#             nx = x + dx[j]
#             ny = y + dy[i]*2

#             if (nx < 1 or nx > 8 or ny < 1 or ny > 8):
#                 continue

#             result += 1
# print(result)
###

result = 0
a = input()
x = int(a[1])
y = ord(a[0]) - ord('a') + 1

steps = [(-2, 1), (2, 1), (-2, -1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

for step in steps:
    nx = x + step[0]
    ny = y + step[1]

    if (nx < 1 or ny < 1 or nx > 8 or ny > 8):
        continue

    result += 1

print (result)
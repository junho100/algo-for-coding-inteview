first_str, second_str = input().split(',')
first = list(map(int, first_str.split()))
second = list(map(int, second_str.split()))


def get_tier(cards):
    first_element = cards[0]

    if cards.count(first_element) == 5:
        return 6

    cards.sort()
    for i in range(4):
        if cards[i] + 1 != cards[i + 1]:
            break
    else:
        return 5

    candidates = list(set(cards))
    for can in candidates:
        if cards.count(can) == 4:
            return 4

    if len(candidates) == 2:
        a = cards.count(candidates[0])
        b = cards.count(candidates[1])

        if (a == 2 and b == 3) or (a == 3 and b == 2):
            return 3

    if len(candidates) == 3:
        a = cards.count(candidates[0])
        b = cards.count(candidates[1])
        c = cards.count(candidates[2])

        if (a == 2 and b == 2) or (a == 2 and c == 2) or (b == 2 and c == 2):
            return 2

    return 1


first_tier = get_tier(first)
second_tier = get_tier(second)

if first_tier > second_tier:
    print('First')
elif first_tier < second_tier:
    print('Second')
else:
    print('Draw')

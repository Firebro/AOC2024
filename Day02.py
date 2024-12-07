File = open("InputDay02.txt")
input = File.read()

def check_order(level) -> bool:
    order_counter = 0

    for item in level:
        if level.index(item) != len(level)-1:

            if item < level[level.index(item)+1]:
                order_counter += 1
            elif item > level[level.index(item)+1]:
                order_counter -= 1

    return len(level)-1 == abs(order_counter)

# 1 1 4 4 3
# +1 -1 0 +1 = 2 = len-1 +-1

def check_dist(level) -> bool:
    isSafe = True

    for item in level:
        if level.index(item) != len(level)-1:
            if abs(item - level[level.index(item)+1]) not in [1, 2, 3]:
                isSafe = False
    return isSafe


## main
counter = 0
levels = input.split("\n")

for level in levels:
    level = level.split(" ")
    for item in range(len(level)):
        level[item] = int(level[item])

    order_safe = check_order(level)
    dist_safe = check_dist(level)


    if order_safe and dist_safe:
        counter += 1
    else:
        for i in range(len(level)):
            temp_lvl = []
            temp_lvl.extend(level)
            temp_lvl.pop(i)

            if check_order(temp_lvl) and check_dist(temp_lvl):
                counter+=1
                break

print(counter)
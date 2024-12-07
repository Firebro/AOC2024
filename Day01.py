File = open("InputDay01.txt")
input = File.read()

left_list = []
right_list = []

for line in input.split("\n"):
    left_list.append(int(line.split("   ")[0]))
    right_list.append(int(line.split("   ")[1]))

'''
#Teil 1:
diff_list = []

for i in range(len(left_list)):
    left_min = min(left_list)
    right_min = min(right_list)

    diff_list.append(max([left_min-right_min, right_min-left_min])) #abs(right_min-left_min)
    left_list.remove(left_min)
    right_list.remove(right_min)

sum = sum(diff_list)
print(sum)
'''

#Teil 2:
counter_list = []

for left_item in left_list:
    item_counter = 0
    for right_item in right_list:
        if left_item == right_item:
            item_counter += 1
    counter_list.append(left_item * item_counter)

print(sum(counter_list))
import re

File = open("InputDay03.txt")
input = File.read()

product_list = []

def add_mul_to_list(inputString):
    product_list_local  = []
    mul_pattern = re.compile('mul\(\d{1,3},\d{1,3}\)')
    mul_result = re.findall(mul_pattern, inputString)

    int_pattern = re.compile('\d{1,3},\d{1,3}')

    int_result = []

    for word in mul_result:
        int_result.append(re.findall(int_pattern, word))

    for mul in int_result:
        for word in mul:
            num_list = word.split(",")
            product = int(num_list[0]) * int(num_list[1])
            product_list_local.append(product)

    return product_list_local

def split_string_dont (string) -> [str,str]:
    word = "don't()"
    str_before = string[:string.find(word)]
    str_after = string[string.find(word)+len(word):]
    return [str_before,str_after]

def split_string_do (string) -> str:
    #str_before = string[:string.find("don't()")]
    str_after = string[string.find("do()")+len("do()"):]
    return str_after

end_reached = False
new_str = input
while not end_reached:
    split_dont = split_string_dont(new_str)
    product_list.extend(add_mul_to_list(split_dont[0]))
    new_str = split_string_do(split_dont[1])

    if new_str.find("do()") == -1 or new_str.find("don't()") == -1:
        end_reached = True

print(sum(product_list))
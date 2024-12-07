import re

File = open("InputDay04.txt")
input = File.read()

lines = input.split("\n")
xmas = re.compile("XMAS")

counter = 0

def check_xmas (line) -> int:
    hor_res_list = re.findall(xmas, line)
    hor_bckw_list = re.findall(xmas, line[::-1])

    return len(hor_res_list)+ len(hor_bckw_list)


vert_lines = []
for letter in lines[0]:
    vert_lines.append("")
for line in lines:
    for letter in range(len(line)):
        vert_lines[letter] += line[letter]

print(len(lines[0]))

#counter += check_xmas(line)

print(counter)
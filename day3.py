import re

def process_memory(file_path):
    pattern = r"mul\(\s*(\d+)\s*,\s*(\d+)\s*\)"
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(pattern,line)
            for x,y in matches:
                total_sum += int(x)*int(y)
    return total_sum

file_path = r"D:\Advent of Code\day3.txt" 
result = process_memory(file_path)
print(result)
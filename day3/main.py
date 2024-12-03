import re

def calculate_mul(mul_string):
    numbers_with_parenthesis = mul_string.replace('mul', '')
    cleaned = numbers_with_parenthesis.strip("()")
    parts = cleaned.split(",")
    first_number, second_number = (int(parts[0]), int(parts[1]))
    return first_number * second_number

mul_matches = []
with open("input.txt", "r") as input:
    content = input.read()
    pattern = r"mul\(\d+,\d+\)"
    mul_matches = re.findall(pattern, content)

sum = 0
for match in mul_matches:
    sum = sum + calculate_mul(match)
print(sum)
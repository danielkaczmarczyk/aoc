#!/usr/bin/python3

def parse_binary_string(binary_string):
    return list(map(lambda x: int(x), list(binary_string.strip())))


totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('./2021/03/input') as file:
    numbers = list(map(parse_binary_string, file.readlines()))

for binary_number in numbers:
    for i in range(len(binary_number)):
        totals[i] += binary_number[i]

gamma_rate = ''
epsilon_rate = ''


for number in totals:
    if number > len(numbers) / 2:
        gamma_rate += '1'
        epsilon_rate += '0'
    else:
        gamma_rate += '0'
        epsilon_rate += '1'

print(len(numbers))
print(totals)
print(gamma_rate, epsilon_rate)

gamma_int = int(gamma_rate, 2)
epsilon_int = int(epsilon_rate, 2)

print(gamma_int, epsilon_int)
print(gamma_int * epsilon_int)

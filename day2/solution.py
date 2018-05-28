#!/usr/bin/env python3

def part1(sheet):
    total = 0
    for line in sheet:
        line = line.strip()
        numbers = list(map(int, line.split('\t')))
        total += max(numbers) - min(numbers)
    return total


def find_divisors(numbers):
    for i in range(0, len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if numbers[j] % numbers[i] == 0:
                return numbers[j] // numbers[i]


def part2(sheet):
    total = 0
    for line in sheet:
        line = line.strip()
        numbers = list(map(int, line.split('\t')))
        numbers.sort()
        total += find_divisors(numbers)
    return total


with open('input.txt', mode='rt') as f:
    spreadsheet = f.readlines()

print(part1(spreadsheet))

print(part2(spreadsheet))

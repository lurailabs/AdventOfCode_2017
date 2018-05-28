#!/usr/bin/env python3

def inverse_captcha(captcha, step):
    captcha = list(map(int,captcha))
    total = 0
    for i in range(0, len(captcha)):
        if captcha[i] == captcha[(i + step) % len(captcha)]: total += captcha[i]

    return total

with open('input.txt', mode='rt') as f:
    input_captcha = f.read()


print(inverse_captcha(input_captcha, 1))

print(inverse_captcha(input_captcha, len(input_captcha)//2))


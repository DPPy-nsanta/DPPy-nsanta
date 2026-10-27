#!/usr/bin/env python3
number = int(input("Enthe a number:\n"))
i = 0 
while i <= 9:
    result = i * number
    print(f"{i} * {number} = {result}")
    i += 1
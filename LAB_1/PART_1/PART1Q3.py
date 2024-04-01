def string_to_int(s):
    if len(s) == 0:
        return 0
    return int(s[0]) * 10**(len(s) - 1) + string_to_int(s[1:])

print(string_to_int('13531'))

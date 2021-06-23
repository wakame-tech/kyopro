s = input()

def is_palin(s):
    return s == s[::-1]

def is_strong_palin(s):
    n = len(s)
    return is_palin(s) and is_palin(s[0:(n - 1) // 2]) and is_palin(s[(n + 3) // 2 - 1:])

print('Yes' if is_strong_palin(s) else 'No')
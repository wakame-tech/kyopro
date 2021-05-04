s = input()

def is_easy(s):
    for i, c in enumerate(s):
        if i % 2 == 0:
            if not c.islower():
                return False
        else:
            if not c.isupper():
                return False

    return True

print('Yes' if is_easy(s) else 'No')

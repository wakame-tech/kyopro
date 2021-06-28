def debug(func):
    def inner(*args):
        res = func(*args)
        print(f'[@debug] {func.__name__}{args} = {res}')
        return res
    return inner

@debug
def f(x):
    return x ** 2

if __name__ == "__main__":
    f(2)
    f(5)
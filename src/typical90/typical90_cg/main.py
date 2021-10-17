def divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


if __name__ == "__main__":
    k = int(input())
    divs = divisors(k)
    # print(divs)
    ans = set()
    for i in range(len(divs)):
        for j in range(i, len(divs)):
            a, b = divs[i], divs[j]
            if a * b > k:
                continue
            if k % (a * b) != 0:
                continue
            # print(a, b, k // (a * b))
            ans.add(tuple(sorted([a, b, k // (a * b)])))
    print(len(ans))

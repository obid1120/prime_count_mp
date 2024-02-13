from math import sqrt


def prime_count(m: int, n: int):
    
    m = m + 1 if m % 2 == 0 else m
    ls = []
    s = 0

    for i in range(m, n, 2):
        for j in range(3, int(i/2), 2):
            if i % j == 0:
                break
        else:
            ls.append(i)
            s += 1
    if ls[0] == 1:
        ls[0] = 2
    print(s)
    print(ls)


if __name__ == "__main__":
    m = int(input("m: "))
    n = int(input("n: "))
    prime_count(m, n)

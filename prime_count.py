from math import sqrt
from time import perf_counter
from multiprocessing import Process


def prime_count(m: int, n: int):

    m = m + 1 if m % 2 == 0 else m
    # ls = []
    s = 0

    for i in range(m, n, 2):
        for j in range(3, int(i/2), 2):
            if i % j == 0:
                break
        else:
            # ls.append(i)
            s += 1
    # if ls[0] == 1:
    #     ls[0] = 2
    print(f"In interval [{m}-{n}] has {s} prime count")
    # print(ls)


if __name__ == "__main__":

    processes = []
    start = perf_counter()
    for i in range(1, 10_000_001, 2_500_000):
        process = Process(target=prime_count, args=[i, i+2_499_999])
        processes.append(process)
        process.start()

    for j in processes:
        j.join()
    end = perf_counter()
    print(f"Runtime: {end-start}")

    # m = int(input("m: "))
    # n = int(input("n: "))
    # prime_count(m, n)

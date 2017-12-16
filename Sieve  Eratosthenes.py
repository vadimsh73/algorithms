# -*-coding:UTF-8-*-


def sieve_eratosthenes():
    n = int(input("n = "))
    a = [True] * n
    a[0] = a[1] = False
    for i in range(2, n):
        if a[i]:
            for j in range(2*i, n, i):
                a[j] = False

    for i in range(n):
        print(i, "-", "Простое" if a[i] else "Составное")

sieve_eratosthenes()
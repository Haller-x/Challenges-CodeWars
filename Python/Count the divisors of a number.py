def divisors(n):
    lista = []
    for i in range(1, n + 1, 1):
        if n % i == 0:
            lista.append(i)
    return len(lista)

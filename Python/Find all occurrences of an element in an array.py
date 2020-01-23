def find_all(array, n):
    teste = []
    for i in range(len(array)):
        if array[i] == n:
            teste.append(i)
    return teste
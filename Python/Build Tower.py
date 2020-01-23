def tower_builder(n_floors):
    res = []
    for i in range(n_floors):
        l = " "
        m = "*"
        x = int((n_floors * 2)-1)
        y = int(n_floors -i -1)
        res.append(y * l + m * (2  * i + 1) + y * l)
    return res
def isValidWalk(walk):
    x = 0
    y = 0
    for i in walk:
        if i == 'n':
            y += 1
        if i == 's':
            y -= 1
        if i == 'w':
            x -= 1
        if i == 'e':
            x += 1
        print("result"+str(x)+","+str(y))
    if len(walk)==10 and x == 0 and y ==0:
        return 0<1
    else:
        return 0>1
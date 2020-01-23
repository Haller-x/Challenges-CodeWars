def bonus_time(salary, bonus):
    if bonus == True:
        t = salary * 10
        return "$" + str(t)
    else:
        return "$" + str(salary)
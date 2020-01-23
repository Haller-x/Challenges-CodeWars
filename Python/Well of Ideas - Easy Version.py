def well(x):
    # your code here
    for i in range(len(x)):
        if x.count("good") > 2:
            return "I smell a series!"
        elif x.count("good") == 1 or x.count("good") == 2:
            return "Publish!"
        else:
            return "Fail!"
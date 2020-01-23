def solution(string, ending):
    if (ending == ''):
        return True
    elif string.endswith(ending) == True:
        return True
    else:
        return False
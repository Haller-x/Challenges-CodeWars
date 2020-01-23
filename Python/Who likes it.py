def likes(names):
    ppl = len(names)
    if ppl == 0:
        return("no one likes this")
    elif ppl == 1:
        return(names[0]+" likes this")
    elif ppl == 2:
        return(names[0]+" and "+ names[1]+" like this")
    elif ppl == 3:
        return(names[0]+", "+names[1]+" and "+names[2]+" like this")
    elif ppl == 4 or ppl > 4:
        return(names[0]+", "+names[1]+" and "+str(ppl-2)+" others like this")
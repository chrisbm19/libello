from random import randint as ri

def coin():
    return ri(1, 2)

def d4():
    return ri(1, 4)

def d6():
    return ri(1, 6)

def d8():
    return ri(1, 8)

def d10():
    return ri(1, 10)

def d12():
    return ri(1, 12)

def d20():
    return ri(1, 20)

def adv():
    return max(d20(), d20())

def disadv():
    return min(d20(), d20())

def d100():
    return ri(1, 100)

def twod6():
    return sum([d6() for i in range(2)])

def threed6():
    return sum([d6() for i in range(3)])

def xd6(x):
    return sum([d6() for i in range(x)])
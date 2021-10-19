

def power(base,exponenet):
    if exponenet == 0:
        return 1
    if exponenet == 1:
        return base
    return base * power(base,exponenet-1)


power(2,4)

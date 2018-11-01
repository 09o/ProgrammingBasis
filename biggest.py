######################
#  求三个数中的最大值  #
######################

# Method 1
def biggest(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

# Method 2
def bigger(a, b):
    if a > b:
        return a
    else:
        return b

def biggist(a, b, c):
    return bigger(bigger(a, b), c)


# Method 3
max(a, b, c)
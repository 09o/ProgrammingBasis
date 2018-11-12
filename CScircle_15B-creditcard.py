import time
start =time.clock()

def check(S):
    res = True
    idx = 4
    space = 0
    sum = 0
    if S != '':
        item = S.split()
        for i in range(len(item)-1):
            if S[idx] == ' ':
                space += 1
            idx += 5      
        if space != 3:
            S = 0
            res = False
        if S != 0:
            lst = S.split()
            for i in lst:
                if i.isdigit():
                    for n in i:
                        sum+=int(n)
                else:
                    res = False
                    break
            if sum % 10 != 0 or sum == 0:
                res = False
    else:
        res = False
    
    return res

print check('2768 3424 2345 2358')
print check('9384 3495 3297 0121')
print check('0000000000000000')
print check('1876 0954 325009182')
print check(' 5555 5555 5555 5555')
print check('0000 0000 0000 000')
print check('0 0 0 0000000000000')
print check('')
print check('0000 0000')
print check('0123 4567 8902 4568')
print check('0123 4567 89AB EFGH')
print check('0000 000000000000') 

end = time.clock()
print('Running time: %s ms'%((end-start)*1000))

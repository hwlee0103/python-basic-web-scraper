#basic function
def plusA(a, b):
    return a + b

#infinite amount of args
print("a","a","a","a","a","a")

def plus_inf(a, b, *args, **kwargs):
    print(args, kwargs)
    return a + b

plus_inf(1, 2, 1, 1, 1, 1, 1, 1, 1, a=True, b=True, c=True)


#infinite calculator
def plus(*args):
    result = 0
    for number in args:
        result += number
    print(result)
    return result
    
plus(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
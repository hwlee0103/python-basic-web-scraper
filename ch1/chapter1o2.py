#if-else
def check_num_plus(a, b):
    if type(b) is str:
        return None
    else:
        return a + b

print(check_num_plus(12, "10"))

def check_num_plus2(a, b):
    if type(b) is int or type(b) is float:
        return a + b
    else:
        return None

print(check_num_plus2(12, "10"))
print(check_num_plus2(12, 1.2))
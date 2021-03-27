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

#if else and or
def age_check(age):
    print(f"you are {age}")
    if age < 18:
        print("you cant drink")
    elif age == 18:
        print("you are new to this!")
    elif age > 20 and age < 25:
        print("you are still kind of young")
    else:
        print("enjoy your drink")

age_check(18)
age_check(23)
age_check(29)
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

#for loop
days = ("Mon", "Tue", "Wed", "Thu", "Fri")

for x in days:
    print(x)
    
for day in [1, 2, 3, 4, 5]:
    print(day)

#break
for day in days:
    if day is "Wed":
        break
    else:
        print(day)

#strings are also sequence
for letter in "Nicolas":
    print(letter)

#import
#import math
#from math import ceil, fsum
#print(math.ceil(1.2))
#print(math.fabs(-1.2))
#print(ceil(1.2))
from math import fsum as first_sum
#print(fsum([1, 2, 3, 4, 5, 6, 7]))
print(first_sum([1, 2, 3, 4, 5, 6, 7]))

#import calculator.py
from ch1.calculator import plus, minus
print(plus(1, 2), minus(1, 2))
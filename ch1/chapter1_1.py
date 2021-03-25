#functions
def say_hello():
    print("hello")
print("bye")

#function call
say_hello()

#arguments
def say_hello_to(who):
    print("hello", who)

say_hello_to("Nicolas")

def plus(a, b):
    print(a + b)

plus(2, 5)

#with default value
def minus(a, b = 0):
    print(a-b)

minus(9, 3)
minus(10)

def say_hello_to_someone(name = "anonymous"):
    print("hello", name)

say_hello_to_someone("Nicolas")
say_hello_to_someone()

#returns
def p_plus(a, b):
    print(a + b)

def r_plus(a, b):
    return a + b
    print("is this print in the function?")

p_result = p_plus(2, 3)
r_result = r_plus(2, 3)

print(p_result, r_result)

#keyword arguments
def r_minus(a, b):
    return a - b

r_m_result = r_minus(b = 30, a = 1)
print(r_m_result)

def r_say_hello(name, age, are_from, fav_food):
    return f"Hello {name} you are {age} years old and you are from  {are_from} you like {fav_food}"
    #return "Hello " + name + " you are " + age + " years old"
hello = r_say_hello("nico", "12", "colombia", "kimchi")
print(hello)
hello = r_say_hello(age = "12", name="nico", fav_food="kimchi", are_from="colombia")
print(hello)
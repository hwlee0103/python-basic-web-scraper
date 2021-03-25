#variables
a_number = 2
a_float = 3.12
a_string = "like this"
a_boolean = False
a_none = None
#False = 0, True = 1
print(type(a_number))
print(type(a_float))
print(type(a_string))
print(type(a_boolean))
print(type(a_none))

#list
days = "Mon, Tue, Wed, Thur, Fri"
print(days)

day_one = "Mon"

days_list = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_list)
print(type(days_list))
print("Mon" in days_list)
#result = True
print("Man" in days_list)
#result = False

print(days_list[3])
print(len(days_list))

#list is mutable
print(days_list)
days_list.append("Sat")
print(days_list)
days_list.reverse()
print(days_list)

#Tuple
days_list2 = ("Mon", "Tue", "Wed", "Thur", "Fri")
print(type(days_list2))

#variables
name="Nico"
age = 29
korean = True
fav_food = ["Kimchi", "Sashimi"]

#dictionary
nico = {
    "name" : "Nico",
    "age":29,
    "korean":True,
    "fav_food":["kimchi", "sashimi"]
}
print(nico)
print(nico["name"])
nico["handsome"] = True
print(nico)

#built-in functions
age = "18"
print(type(age))
n_age = int(age)
print(type(n_age))
print(n_age)
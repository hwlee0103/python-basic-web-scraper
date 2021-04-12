#class
class Car():
    #wheels = 4
    #doors = 4
    #windows = 4
    #seats = 4

    #make __init__
    def __init__(self, *args, **kwargs):
        #print(kwargs)
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    #override __str__ method
    def __str__(self):
        #return "lalalalalala"
        return f"Car with {self.wheels} wheels"

    #method
    def start(self):
        print(self.doors)
        print("I started")

    #convertable car as an example
    #def take_off(self):
     #   return "taking off"

#extend class
class Convertible(Car):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"
    
    def __str__(self):
        return f"Car with no roof"

#extend class
class Something(Convertible):
    pass


#make porche as an example
#porche = Car(color="green", price="$40")
porche = Convertible(color="green", price="$40")
#porche.color = "Red"
print(porche)
print(porche.color, porche.price)
porche.take_off()
print(porche.wheels)
#print(porche.windows)
#print(porche.color)

#ferrari = Car()
#ferrari.color = "Yellow"

#porche.start()

#function
#def start():
#    print("I started")

#other methods
print(dir(Car))

#check default
mini = Car()
print(mini.color, mini.price)

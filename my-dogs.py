import random

# from dog import *
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
import dog
my_other_dog = dog.Dog("Annie:", " Super Dog")
print(my_other_dog.name)
print(my_other_dog.breed)
my_other_dog.bark()
print("                                      ")

my_dog = dog.Dog("Rex:", " Mega Dog")
print(my_dog.name)
print(my_dog.breed)
my_dog.bark()
print("                                      ")

my_other_dog1 = dog.Dog("Sam:", ' Ultra Dog')
print(my_other_dog1.name)
print(my_other_dog1.breed)
my_other_dog1.sit()
print("                                      ")

my_other_dog2 = dog.Dog("Trish:", ' Omni Dog')
print(my_other_dog2.name)
print(my_other_dog2.breed)
my_other_dog2.rollOver()
print("                                      ")
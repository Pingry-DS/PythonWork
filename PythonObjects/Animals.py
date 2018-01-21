'''An Introduction to objects in Python'''

class Human:

    primary_attribute = "Having Thumbs"

    def __init__(self):
        weight = 160

    def speak(self):
        print "blah blah blah"


#Name of your class. Does not have to match file name. You can
#have more than one class in a file. THERE ARE NO RULES.
class Man(Human):

    #Only declare instance variables here if they are the same
    #for ALL instances of the class!
    primary_attribute = "Greedy"

    def __init__(self):
        height = 6

    #Taking self as a parameter is what distinguishes a method as a
    #class method (think static vs non-static).
    def speak(self):
        print "But I am the most important animal!"

class Bear():

    def speak(self):
        print "Roar!"

class Pig():

    def speak(self):
        print "Oink!"

class ManBearPig(Man, Bear, Pig):

    def __init__(self):
        height = 100

    def speak(self):
        print "I am ManBearPig!"




adam = ManBearPig()
adam.speak()

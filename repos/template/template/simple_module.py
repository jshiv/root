import numpy as np
import random



#its easy to make a function
def first_function(words):
    print words


#python functions are very flexable
def simple_function(x, y = 3, letter = 'b', tf = True, none = None, *args, **kwargs):
    '''also comments are cool! try tabbing in ipyhton to see
    what a comment in a function says'''
    print 'x = ' + str(x)
    print 'x*y = ' + str(x*y)
    print 'the letter is: ' + letter
    if tf:
        print 'the boolean variable is True :-)'
    else:
        print 'the boolean variable is was not True :-('
    if none is not None:
        print 'none is not None'
        print 'none is : '+str(none)
    print "also...."
    print args
    print kwargs
    return x*y


#classes are also easy to build
class die:
	#     first every class needs an __init__ method
	#     __init__ gets run automatically when you instantiate an object
    def __init__(self, sides = 6):
        '''die represents a single die with the property of sides and the methods of roll and rolln'''
        self.sides = sides
        
    def roll(self):
        self.rolled = random.randint(1,self.sides)
        print self.rolled
    def rolln(self, n = 10):
        self.rolled = [random.randint(1,self.sides) for x in range(n)]
        print self.rolled



#here is a very genral class that you can use in lots of places
class general:
    
    def __init__(self, param1, param2 = 'string', param3 = None, namedMethod = 'firstMethod', **kwargs):
        '''param1 is required
        param2 is default to the value "string"
        param3 is default to None
        namedMethod will run general.firstMethod() by default
        or you can give it the name of some other method you want to run!
        **kwargs along with the initParam method will 
        let you intantiate any parameter by the name you give it...
        obj = general(param1 = 1, x = 1, y = 2, z = 4)
        x, y, z will now exist as properties of the instance obj'''
        
        self.initParam(kwargs)
        self.param1 = param1
        self.param2 = param2
        if param3 is not None:
            self.param3 = param3
        self.runMethod(method = namedMethod) #this will run the method named in namedMethod
        
    def initParam(self, kwargs):
        '''initalize the given argument structure as properties of the class
        to be used by name in specific query execution'''
        self.argList = []
        for key, value in kwargs.items():
            self.argList.append(key)
            setattr(self,key,value)

    def runMethod(self, method):
        '''call the query method by name during the initialization procedure'''
        methodToCall = getattr(self, method)
        result = methodToCall()
        
    def firstMethod(self):
        '''this method will run by default by calling the runMethod from
        the namedMethod argument'''
        #do stuff!
        print "stuff got did!"
        

if __name__ == '__main__':
	z = simple_function(x = 1, none = 15)
	#instantiate the object 'myDie', overriding the default #sides
	myDie = die(24)

	#run the 'roll' function under the object which rolls and prints result
	myDie.roll()
	#run the 'rolln' function under the object which rolls n times and prints results
	myDie.rolln(5)

	#make a general object
	obj = general(param1 = 1, x = 1, z = 3, milkBone = 'MMMM thats good stuff')
	print obj.argList
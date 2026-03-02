# class Human:
#     Name: None  #----state(variables)
#     Age: None    #----state 
#     Weight: None  #----state
#     blood_group=None  #----state

#     def sleep(self):  #behaviour(function)
#         print(self.Name+"is sleeping")

# person=Human()
# person.Name="sarumathi v"
# person.Age=23
# person.Weight=59
# person.blood_group="A+ve"

# print(person.Name)
# print(person.Age)
# person.sleep()
# person.blood_group()

# person1=Human

# PASS --EMPTY CLASS OR EMPTY METHOD - TO FULLFILL WITHOUT ANTY ERROR WE USE PASS
# class Human:
#     # pass
# Name: None  #----state(variables)
# Age: None    #----state 
# Weight: None  #----state
# blood_group=None  #----state

# person=Human()
# Name="sarumathi_vasu"
# print(Name)
# Got an error as Expected indented block - here we command pass so we need to declare variable or method with in the class


# Constructor -  to initialize the object by setting up its attributes or state
# __init__ : Initializes the instance.

# static vs dynamic => why used to save memory so we used
# if we declare static then it automatically takes
# in static we cannot able to access the self in 51 line if we use self it got an error 
class person:
    s_time=8
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.s_time=10
    @staticmethod
    def sleep():
        print("the person is slepping",person_1.s_time,"hours")

print(person.s_time)
person_1=person(name="saru",age=23)
print(person_1.s_time)
person.sleep()

# therfore: staticmethod : class level variables
# classmethod(dynamic) : instance (object) level variables
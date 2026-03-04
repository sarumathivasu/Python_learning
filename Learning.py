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
# class person:
#     s_time=8
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         self.s_time=10
#     @staticmethod
#     def sleep():
#         print("the person is slepping",person_1.s_time,"hours")

# print(person.s_time)
# person_1=person(name="saru",age=23)
# print(person_1.s_time)
# person.sleep()

# therfore: staticmethod : class level variables
# classmethod(dynamic) : instance (object) level variables

# inheritance -- where one class can acquire the properties and methods of another class
# parent class -> common properties and methods also called as super class or base class
# child class -> inherties the parent class - also called as sub class or dervied class
# class grandparent:
#     def __init__(self):
#         print("swimming")

# class parent:

#     def sing (self):
#         print("singing")
#     def __init__(self):
#         self.networth_of_parent= 50000000

# class child(parent):
#     def dancing(self):
#         print("dancing")

# child1=child()
# child1.sing()
# print(child1.networth_of_parent)

# single level - class parent - class child
# multi-level - class grand parent , class parent, class child
# multiple-level - class grand parent , class parent(no relation with grandparent), class child(relation with both parent and child)
# hierarchical - single parent - multiple child - class grandparent - childs are both class parent and class child.
# hybrid - combinations of above four.

# super keyword
class parent:
    def drive(self, speed):
        print("parent is driving at the spped of", speed)

class child(parent):
    def drive(self, speed):
        super().drive(speed)
        # self.drive
        print("child is driving at ", speed-30)
        # return super().drive()
child1=child()

# child2=parent()
# child2.drive()
child1.drive(500)

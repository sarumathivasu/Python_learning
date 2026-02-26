class Human:
    Name: None  #----state(variables)
    Age: None    #----state 
    Weight: None  #----state
    blood_group=None  #----state

    def sleep(self):  #behaviour(function)
        print(self.Name+"is sleeping")

person=Human()
person.Name="sarumathi v"
person.Age=23
person.Weight=59
person.blood_group="A+ve"

print(person.Name)
print(person.Age)
person.sleep()
person.blood_group()

person1=Human

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

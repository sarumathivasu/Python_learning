class Human:
    Name: None  #----state
    Age: None    #----state 
    Weight: None  #----state
    blood_group=None  #----state

    def sleep(self):  #behaviour
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
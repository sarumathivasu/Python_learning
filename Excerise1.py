class Students:
    def __init__(self,name,subject1,subject2,subject3,subject4,subject5):
        self.Name=name
        self.Subject1=subject1
        self.Subject2=subject2
        self.Subject3=subject3
        self.Subject4=subject4
        self.Subject5=subject5
    def sumofsubjects(self):
        total= (self.Subject1+self.Subject2+self.Subject3+self.Subject4+self.Subject5)
        print(self.Name + "is total marks= "+str(total))

    def maximumnumber(self):
        maxi=max(self.Subject1,self.Subject2,self.Subject3,self.Subject4,self.Subject5)
        print("maximumno=", maxi)

    def manimumnumber(self):
        mini=min(self.Subject1,self.Subject2,self.Subject3,self.Subject4,self.Subject5)
        print("minimumno=", mini)

studentof_1=Students("sarumathi", 90,80,100,89,100)
studentof_2=Students("madhu",100,100,89,99,99)

studentof_1.sumofsubjects()
studentof_1.maximumnumber()
studentof_1.manimumnumber()
studentof_2.sumofsubjects()

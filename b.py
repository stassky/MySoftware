class Person:
    def __init__(self, Fname, Lname):
        self.firstName = Fname
        self.lastName = Lname

    def printName(self):
        print(self.firstName, self.lastName)

class student (Person):
    def __init__(self, Fname, Lname, Result):
        Person.__init__(self, Fname, Lname)
        self.studentScore = Result

x = student("Mike", "Olson",1975)
print (x.studentScore)
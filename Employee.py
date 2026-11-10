class employee():
    def __init__(self, role,salary, age,gender,name) :
        self.name = name
        self.gender = gender
        self.age = age
        self.role = role
        self.salary = salary

    def showDetails(self):
        print("Name :"+ self.name)
        print("Gender : " + self.gender)
        print("Age : "+ str(self.age))
        print("Role : " + self.role)
        print("Salary : " + self.salary)
    def UpdateDetails(self):
        Name = input("What is your name: ")
        Gender = input("What is your gender: ")
        Age = input("What is your current age: ")
        Role = input("What is your current role: ")
        Salary = input("What is your current salary: ")
        self.name = Name
        self.gender = Gender
        self.age = Age
        self.role = Role
        self.salary = Salary 
s1 = employee("name","Gender","age","role","salary")
s1.UpdateDetails()
s1.showDetails()



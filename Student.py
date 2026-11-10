class student():
    def __init__(self, name, gender, age, grade,username,password) :
        self.name = name
        self.gender = gender
        self.age = age
        self.grade = grade
        self.username = username
        self.password = password

    def showDetails(self):
        print("Name :"+ self.name)
        print("Gender : " + self.gender)
        print("Age : "+ str(self.age))
        print("Grade : " + self.grade)
    def UpdateAge(self):
        self.age+=1
    def Login(self):
        user = input("Enter the username: ")
        grade = int(input("Enter your mark: "))
        if user == self.username:
            print("Correct, Move on to Password")
            password1 = input("Enter the password: ")
            if password1 == self.password:
                print("Correct! You have successfully logged in!")
            else:
                print("Incorrect! Try Again Later")
        else:
            print("Incorrect Username!")
        if grade >= 90:
            self.grade = 'A'
        elif grade >= 70:
            self.grade = 'B'
        else:
            self.grade = 'C'
    def UpdatePassword(self):
        NewPassword = input("Enter the new password: ")
        self.password = NewPassword

s1 = student("Shivansh","M",14,"class 10","Shivansh","Shivansh@123")
s2 = student("Johncy","F",12, "class 8","Johncy","J")
s2.UpdatePassword()
s2.Login()
s2.showDetails()



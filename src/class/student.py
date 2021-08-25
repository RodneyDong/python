class Person:
    name = "John"
    ssn = "111-22-3333"
    age = 15  # field 2

    def sayHello(self):
        print("Hello the world!")

class Student(Person): # class name is 'Student', Student class inherits from Person, so every thing person has, the student will also have
    id = 1111 # field 3

    def turnInHomework(self):
        print(f"{self.name} is turning homework...")

    def practice(self):
        print("I am running...")

if __name__ == '__main__':
    student1 = Student()
    student1.turnInHomework()
    student1.practice()
    print(student1.ssn)
    student1.sayHello()

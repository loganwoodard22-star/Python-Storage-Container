class UniversityMember:
    def __init__(self,name,id_number):
        self.name=name
        self.id_number=id_number

    def displayinfo(self):
        return 0
    
class Student(UniversityMember):
    def __init__(self,name, id_number, major,gpa):
        UniversityMember.__init__(self,name, id_number)
        self.major=major
        self.gpa=gpa

    def displayinfo(self):
        return f"Student Information\nName: {self.name}\nId Number: {self.id_number}\nMajor: {self.major}\nGpa: {self.gpa}"
    
class Professor(UniversityMember):
    def __init__(self,name,id_number,department,salary):
        UniversityMember.__init__(self,name,id_number)
        self.department=department
        self.salary=salary

    def displayinfo(self):
        return f"Professer Information\nName: {self.name}\nId Number: {self.id_number}\nDepartment: {self.department}\nSalary: {self.salary}"
    

student_list=[]
professor_list=[]

student1 = Student("Alice Johnson", "S1001", "Computer Science", 3.85)
student2 = Student("Brian Lee", "S1002", "Mathematics", 3.60)

student_list.append(student1)
student_list.append(student2)

professor1 = Professor("Dr. Smith", "P2001", "Computer Science", 72000)
professor2 = Professor("Dr. Brown", "P2002", "Physics", 68000)

professor_list.append(professor1)
professor_list.append(professor2)

print("University Member Information")
print("-----------------------------")
for item in student_list:
    print(item.displayinfo())
    print("")

for item in professor_list:
    print(item.displayinfo())
    print("")
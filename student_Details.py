#create an student details method in class.it take fname,lastname,age,gender
#it will return fname+lastname with if male it is it should return Mr.fname+lastname,if it is female it should return ms.fname+lastname 
class StudentData:
    def __init__(self):
        self.students = []

    def add_student(self, fname, lname, age, gender=""):
        student = {
            "fname": fname,
            "lname": lname,
            "age": age,
            "gender": gender
        }
        self.students.append(student)
#Student Details
    def get_details(self, name):
        found = False
        for student in self.students:
            full_name = student["fname"] + " " + student["lname"]
            if student["fname"].lower() == name.lower() or student["lname"].lower() == name.lower() or full_name.lower() == name.lower():
                found = True
                if student["gender"].lower() == 'male':
                    print("Mr. " + full_name)
                elif student["gender"].lower() == 'female':
                    print("Mss. " + full_name)
                else:
                    print(full_name)
        if not found:
            print("No details found")

def main():
    # Example usage
    n = int(input("Enter how many members' details you want to enter: "))
    student_data = StudentData()
    for _ in range(n):
        fname = input("Enter the firstname: ")
        lname = input("Enter the lastname: ")
        gender = input("Enter the gender (either Male/Female): ")
        age = int(input("Enter the age: "))
        student_data.add_student(fname, lname, age, gender)

    name_to_search = input("Enter the name to search for details: ")
    student_data.get_details(name_to_search)
if __name__=="__main__":
    main()
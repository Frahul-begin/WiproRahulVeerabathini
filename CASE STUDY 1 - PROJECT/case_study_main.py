from abc import ABC, abstractmethod
import json
import csv
import time

# Decorators
def admin_only (func):
    def wrapper(*args, **kwargs):
        if kwargs.get("role") != "admin":
            print("Access denied: You are not an administrator.")
            return
        return func(*args, **kwargs)
    return wrapper

def log_execution(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Method {func.__name__} executed successfully.")
        return result
    return wrapper

def performance_timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] {func.__name__} took {end - start:.4f} seconds.")
        return result
    return wrapper

#Descriptors
class MarksDescriptor:
    def __get__(self, instance, owner):
        return instance._marks
    def __set__(self, instance, value):
        if not isinstance(value, dict):
            raise ValueError("Marks must be a dictionary")
        if any(m < 0 or m > 100 for m in value.values()):
            raise ValueError("Value must be between 0 and 100.")
        instance._marks = value

class SalaryDescriptor:
    def __get__(self, instance, owner):
        raise PermissionError("Access denied: Salary is confidential")
    def __set__(self, instance, value):
        instance._salary = value


#AbstractBASE CLASS

class Person(ABC):
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass

    def __del__(self):
        print(f"Deleting resources {self.name}")

# STUDENT CLASS

class Student(Person):
    marks = MarksDescriptor()
    def __init__(self, sid, name, department, sem, marks):
        super().__init__(sid, name, department)
        self.sem = sem
        self.marks = marks
        self.courses = []

    def get_details(self):
        print("\n")
        print("Student details:")
        print(f"Name     : {self.name}")
        print(f"Role     : Student")
        print(f"Department: {self.department}")

    #Calculation(Avg & Grade)
    @performance_timer
    @log_execution
    def calculate_performance(self):
        avg = sum(m for m in self.marks.values()) / len(self.marks)
        grade = "A" if avg >= 90 else "B" if avg >= 80 else "C"
        return avg, grade

    def __gt__(self, other): #Operator overloading
        return sum(self.marks.values()) > sum(other.marks.values())


#FACULTY CLASS

class Faculty(Person):
    salary = SalaryDescriptor()
    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        print("\n")
        print("Faculty details:")
        print(f"Name     : {self.name}")
        print(f"Role     : Faculty")
        print(f"Department: {self.department}")

#Course & Iterators

class CourseIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        value = self.students[self.index]
        self.index += 1
        return value

class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)
        student.courses.append(self)

    def __add__(self, other):
        return self.credits + other.credits

    def __iter__(self):
        return CourseIterator(self.students)

#Genarators
def student_generator(students):
    print("Student generator")
    for s in students:
        yield f"{s.id} - {s.name}"

#File Handling
#json File
def save_students_json(students):
    data = []
    for s in students:
        data.append({
            "id": s.id,
            "name": s.name,
            "department": s.department,
            "sem": s.sem,
            "marks": s.marks,
        })
    with open("students.json", "w") as f:
        json.dump(data, f, indent=2)
    print("Students saved to students.json")

#csv File
def generate_csv_report(students):
    with open("students.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "NAME", "DEPARTMENT", "Average", "GRADE"])
        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.id, s.name, s.department, round(avg, 2), grade])

    print("CSV Report Generated: students.csv")


# Main Program

students = []
faculty = []
courses = []

try:
    s1 = Student(
        "S101",
        "Rahul",
        "Electronics",
        4,
        {
            "Maths": 95,
            "Python": 87,
            "DSA": 90,
            "OS": 92,
            "Networks": 89
        }
    )
    students.append(s1)

    f1 = Faculty("F201", "Saritha", "Electronics", 60000)
    faculty.append(f1)

    c1 = Course("CS401", "Python-Selenium", 4, f1)
    courses.append(c1)

    c1.enroll_student(s1)
    print("\nEnrollment Successful")
    print("\nStudent Details:")
    print(f"Student Name: {s1.name}")
    print(f"Course Name: {c1.name}")

    avg, grade = s1.calculate_performance()

    print("\nStudent Performance Report:")
    print(f"Student Name: {s1.name}")
    print("Marks   :", s1.marks)
    print("Grade   :", grade)
    print("Average  :", round(avg, 2))

    s1.get_details()
    f1.get_details()

    s2 = Student(
        "S102",
        "Rohit",
        "Computer Science",
        4,
        {
            "Maths": 70,
            "Python": 75,
            "DSA": 80,
            "OS": 72,
            "Networks": 78
        }
    )
    print("\nCompare Two Students (> operator)")
    print(f"{s1.name} > {s2.name} :", s1 > s2)

    c2 = Course("CS402", "Algorithms", 3, f1)
    print("\nMerge Course Credits (+ operator)")
    print("Total Credits After Merge :", c1 + c2)
    print("\nStudent Record Generator")
    for record in student_generator([s1, s2]):
        print(record)

    #File operations
    save_students_json(students)
    generate_csv_report(students)

#Exception Handling
except ValueError as ve:
    print("Invalid Marks")
    print("Error:", ve)

except PermissionError as pe:
    print("Permission Denied")
    print("Error:", pe)

except FileNotFoundError:
    print("Error: File Not Found")

except Exception as e:
    raise

finally:
    print("\nFinished, Thank you!")


























import json
import os




class Person:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

class Student(Person):
    def __init__(self, name,fname, student_class,ask_department,roll_no, marks=None):
        super().__init__(name)
        self.fname = fname
        self.student_class = student_class
        self.ask_department = ask_department
        self.roll_no = roll_no
        self.marks = marks if marks else {}

    def to_dict(self):
        return {
            "name": self.name,
            "fname":self.fname,
            "class": self.student_class,
            "marks": self.marks,
            "department":self.ask_department,
            "rollno": self.roll_no
        }

class Teacher(Person):
    def __init__(self, name, subject,ask_gradu,classnumber):
        super().__init__(name)
        self.subject = subject
        self.ask_gradu = ask_gradu
        self.classnumber = classnumber

    def to_dict(self):
        return {
            "name": self.name,
            "subject": self.subject,
            "degree":self.ask_gradu,
            "classnumber":self.classnumber
        }


class SchoolManagementSystem:

    def __init__(self):
        self.student_file = "students.json"
        self.teacher_file = "teachers.json"
        self.login_file = "login.json"
        self.create_files()

    def create_files(self):
        for file in [self.student_file, self.teacher_file, self.login_file]:
            if not os.path.exists(file):
                with open(file, "w") as f:
                    if file == self.login_file:
                        json.dump({"admin": "1234"}, f)
                    else:
                        json.dump([], f)

    def login(self):
        with open(self.login_file, "r") as f:
            users = json.load(f)

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in users and users[username] == password:
            print("Login successful!\n")
            return True
        else:
            print("Invalid credentials!\n")
            return False

    def add_student(self):
        SUBJECT = ["English","Ss", "Hindi", "Science", "Math"]
        DEPARTMENT = ["Science", "Commerce", "Arts"]
        SCIENCE = ["Chemistry", "Physics", "Math", "Biology", "Pt"]
        COMMERCE = ["Account", "Business", "Economics", "English", "Pt"]
        ARTS = ["English", "History", "Geography", "Political Sci", "Sociology"]
        CHILD = [1,2,3,4,5,6,7,8,9,10]
        SENIOR = [11,12]
        BACHE = CHILD + SENIOR
        # print(BACHE)
        
        while True:
            roll_no = 1
            with open(self.student_file, "r") as f:
                Students = json.load(f)
                
            name = input("Enter student name: ").title()
            if not name.isalpha():
                print("invalid answer")
                continue

            fname = input("enter your father name: ").title()
            if not fname.isalpha():
                print("invalid answer")
                continue

            student_class = input("Enter class: ")
            if not student_class.isdigit():
                print("plz input only number")
                continue
            student_class = int(student_class)
            
            for person in Students:
                if person["class"] == student_class:
                    roll_no += 1

  
            
            if student_class in CHILD:
                print("is a child now")
                ask_department = "only for senior student"
                student = Student(name,fname, student_class, ask_department, roll_no)
                with open(self.student_file, "r") as f:
                        students = json.load(f)
                students.append(student.to_dict())
                with open(self.student_file, "w") as f:
                    json.dump(students, f, indent=4)
                print("Student added successfully!\n")
                more_student = input("enter in 'Y'-'N': ").title()
                if more_student in ["Y", "N"]:
                    if more_student == "Y":
                        continue
                    else:
                        with open(self.student_file, "w") as f:
                            json.dump(students,f, indent=4)      
                        break
                else:
                    print("invalid input")

            elif student_class in SENIOR:
                print(DEPARTMENT)
                ask_department = input("enter your department: ").title()
                if ask_department not in DEPARTMENT:
                    print("try again")
                    continue
                if ask_department in DEPARTMENT:
                    student = Student(name, fname, student_class, ask_department,roll_no)
                    with open(self.student_file, "r") as f:
                        students = json.load(f)
                    students.append(student.to_dict())
                    with open(self.student_file, "w") as f:
                        json.dump(students, f, indent=4)

                    print("Student added successfully!\n")
                    more_student = input("enter in 'Y'-'N': ").title()
                    if more_student in ["Y", "N"]:
                        if more_student == "Y":
                            continue
                        else:
                            with open(self.student_file, "w") as f:
                                json.dump(students,f, indent=4)      
                            break
                    else:
                        print("invalid input")
            
            else:
                print("invalid input")

    def remove_student(self):
        
        while True:
            name = input("Enter student name to remove: ").title()
            if not name.isalpha():
                print("what are you doing type name properly")
                continue

            classnumber = input("enter your class: ")
            if not classnumber.isdigit():
                print("need only number brother")
                continue
            classnumber = int(classnumber)

            rollno = input("enter your rollno: ")
            if not rollno.isdigit():
                print("need only number brother")
                continue
            rollno = int(rollno)

            with open(self.student_file, "r") as f:
                students = json.load(f)

            updated = []
            
            for s in students:
                if not (name == s['name'] and rollno == s['rollno'] and classnumber == s["class"]) :
                    updated.append(s)
            if len(updated) == len(students):
                print("Student not found")
            else:
                with open(self.student_file, "w") as f:
                    json.dump(updated, f, indent=4)
                print("Student removed successfully")
   
    def add_teacher(self):
        SUBJECT = ["English","Ss", "Hindi", "Science", "Math"]
        DEPARTMENT = ["Science", "Commerce", "Arts"]
        SCIENCE = ["Chemistry", "Physics", "Math", "Biology", "Pt"]
        COMMERCE = ["Account", "Business", "Economics", "English", "Pt"]
        ARTS = ["English", "History", "Geography", "Political Sci", "Sociology"]
        CHILD = [1,2,3,4,5,6,7,8,9,10]
        SENIOR = [11,12]
        while True:
            with open(self.teacher_file, "r") as f:
                Teachers = json.load(f)
            name = input("Enter teacher name: ").title()
            if not name.isalpha():
                print("invalid answer")
                continue

            classnumber = input("Enter classnumber: ")
            if not classnumber.isdigit():
                print("invalid answer")
                continue
            classnumber = int(classnumber)
            if classnumber in SENIOR:
                    print(DEPARTMENT)
                    ask_department = input("enter your department: ").title()
                    if ask_department not in DEPARTMENT:
                        print("try again")
                        continue
                    if ask_department in DEPARTMENT:
                        if ask_department == "Science":
                            print("select subject", SCIENCE)
                            subject = input("Enter subject: ").title()
                            if not subject.isalpha():
                                print("invalid answer")
                                continue
                            if subject not in SCIENCE:
                                print("try again")
                                continue
                            if subject in SCIENCE:
                                print("Nice")   
                            for Person in Teachers:
                                if Person["subject"] == subject and Person["classnumber"] == classnumber:
                                    print("teacher already exist")
                                    return                     
                        elif ask_department == "Commerce":
                            print("select subject", COMMERCE)
                            subject = input("Enter subject: ").title()
                            if not subject.isalpha():
                                print("invalid answer")
                                continue
                            if subject not in COMMERCE:
                                print("try again")
                                continue
                            if subject in COMMERCE:
                                print("Nice")
                            for Person in Teachers:
                                if Person["subject"] == subject and Person["classnumber"] == classnumber:
                                    print("teacher already exist")
                                    return   
                        elif ask_department == "Arts":
                            print("select subject", ARTS)
                            subject = input("Enter subject: ").title()
                            if not subject.isalpha():
                                print("invalid answer")
                                continue
                            if subject not in ARTS:
                                print("try again")
                                continue
                            if subject in ARTS:
                                print("Nice")
                            for Person in Teachers:
                                if Person["subject"] == subject and Person["classnumber"] == classnumber:
                                    print("teacher already exist")
                                    return   
            elif classnumber in CHILD:
                    print("select subject", SUBJECT)
                    subject = input("Enter subject: ").title()
                    if not subject.isalpha():
                        print("invalid answer")
                        continue
                    if subject not in SUBJECT:
                        print("try again")
                        continue
                    if subject in SUBJECT:
                        print("Nice")
                    for Person in Teachers:
                        if Person["subject"] == subject and Person["classnumber"] == classnumber:
                            print("teacher already exist")
                            return
         
            ask_gradu = input("have degree ?: ").title()
            if ask_gradu in ["Yes", "No"]:
                if ask_gradu == "Yes":
                    print("Nice")
                else:
                    print("okay!")
            else:
                print("invalid input")
            teacher = Teacher(name, subject, ask_gradu,classnumber)                                               

            with open(self.teacher_file, "r") as f:
                teachers = json.load(f)

            teachers.append(teacher.to_dict())

            with open(self.teacher_file, "w") as f:
                json.dump(teachers, f, indent=4)

            print("Teacher added successfully!\n")

            more_teacher = input("enter in 'Y'-'N': ").title()
            if more_teacher in ["Y", "N"]:
                if more_teacher == "Y":
                    continue
                else:
                    with open(self.teacher_file, "w") as f:
                        json.dump(teachers,f, indent=4)      
                    break
            else:
                print("invalid input")

    def remove_teacher(self):
        while True:
            name = input("Enter teacher name to remove: ").title()
            if not name.isalpha():
                print("kya kar raha hai bhai sahi naam dal")
                continue
            classnumber = input("enter the class number: ")
            if not classnumber.isdigit():
                print("kya kar raha hai bhai sahi naam dal")
                continue
            classnumber = int(classnumber)

            with open(self.teacher_file, "r") as f:
                teachers = json.load(f)

            updated = []
            for t in teachers:
                if not (name == t['name'] and classnumber == t['classnumber']):
                    updated.append(t)
            if len(updated) == len(teachers):
                print("teacher not found")
            else:
                with open(self.teacher_file, "w") as f:
                    json.dump(updated, f, indent=4)
                print("teacher removed successfully")

    def update(self):
        print("Update:")
        print("1. Student")
        print("2. Teacher")

        choice = input("Enter choice (1-2): ")

        if choice == "1":
            self.update_student()
        elif choice == "2":
            self.update_teacher()
        else:
            print("Invalid choice!\n")

    def update_student(self):
        SUBJECT = ["English","Ss", "Hindi", "Science", "Math"]
        DEPARTMENT = ["Science", "Commerce", "Arts"]
        SCIENCE = ["Chemistry", "Physics", "Math", "Biology", "Pt"]
        COMMERCE = ["Account", "Business", "Economics", "English", "Pt"]
        ARTS = ["English", "History", "Geography", "Political Sci", "Sociology"]
        CHILD = [1,2,3,4,5,6,7,8,9,10]
        SENIOR = [11,12]
        while True:
            name = input("Enter student name: ").title()
            if not name.isalpha():
                print("name dal sahi se")
                continue

            rollno = input("enter roll number: ")
            if not rollno.isdigit():
                print("number de sahi se")
                continue
            rollno = int(rollno)

            classnumber = input("enter class number: ")
            if not classnumber.isdigit():
                print("number de sahi se")
                continue
            classnumber = int(classnumber)
            with open(self.student_file, "r") as f:
                students = json.load(f)

            found = False

            for s in students:
                if s["name"] == name and s['class'] == classnumber and s["rollno"] == rollno:
                    print("1. Name")
                    print("2. Class")

                    field = input("Enter field to update (1-2): ")

                    if field == "1":
                        s["name"] = input("Enter new name: ").title()
                    elif field == "2":
                        s["class"] = int(input("Enter new class: "))
                        if classnumber in SENIOR:
                            print(DEPARTMENT)
                            ask_department = input("enter your department: ").title()
                            if ask_department not in DEPARTMENT:
                                print("try again")
                                return
                            s["department"] = ask_department

                    else:
                        print("Invalid field!")
                        return

                    found = True
                    break

            if found:
                with open(self.student_file, "w") as f:
                    json.dump(students, f, indent=4)
                print("Student updated successfully!\n")
                break
            else:
                print("Student not found!\n")

            more_teacher = input("enter in 'Y'-'N': ").title()
            if more_teacher in ["Y", "N"]:
                if more_teacher == "Y":
                    continue
                else:
                    with open(self.student_file, "w") as f:
                        json.dump(students,f, indent=4)      
                    break
            else:
                print("invalid input")

    def update_teacher(self):
        while True:
            name = input("Enter teacher name: ").title()
            if not name.isalpha():
                print("name dal sahi se")
                continue

            classnumber = input("enter class number: ")
            if not classnumber.isdigit():
                print("number de sahi se")
                continue
            classnumber = int(classnumber)

            with open(self.teacher_file, "r") as f:
                teachers = json.load(f)

            found = False

            for t in teachers:
                if t["name"] == name and t["classnumber"] == classnumber:
                    print("1. Name")
                    print("2. Subject")

                    field = input("Enter field to update (1-2): ")

                    if field == "1":
                        t["name"] = input("Enter new name: ")
                    elif field == "2":
                        t["subject"] = input("Enter new subject: ")
                    else:
                        print("Invalid field!")
                        return

                    found = True
                    break

            if found:
                with open(self.teacher_file, "w") as f:
                    json.dump(teachers, f, indent=4)
                print("Teacher updated successfully!\n")
            else:
                print("Teacher not found!\n")

            more_teacher = input("enter in 'Y'-'N': ").title()
            if more_teacher in ["Y", "N"]:
                if more_teacher == "Y":
                    continue
                else:
                    with open(self.teacher_file, "w") as f:
                        json.dump(teachers,f, indent=4)      
                    break
            else:
                print("invalid input")

    def add_result(self):
        SCIENCE = ["Chemistry", "Physics", "Math", "Biology", "Pt"]
        COMMERCE = ["Account", "Business", "Economics", "English", "Pt"]
        ARTS = ["English", "History", "Geography", "Political Sci", "Sociology"]
        SUBJECT = ["English","Ss", "Hindi", "Science", "Math"]
        DEPARTMENT = ["Science", "Commerce", "Arts"]
        CHILD = [1,2,3,4,5,6,7,8,9,10]
        SENIOR = [11,12]
        while True:
            with open(self.student_file, "r") as f:
                students = json.load(f)
            name = input("Enter student name: ").title()
            if not name.isalpha():
                print("nam sahi se dal lala")
                continue
            classnumber = input("enter class number: ")
            if not classnumber.isdigit():
                print("number dal sahi se")
                continue
            classnumber = int(classnumber)
            rollno = input("enter rollno number: ")
            if not rollno.isdigit():
                print("number dal sahi se")
                continue
            rollno = int(rollno)
            found = False
            for s in students:
                if s["name"] == name and s["class"] == classnumber and s["rollno"] == rollno:
                    marks = {}
                    if classnumber in CHILD:
                        print("Enter marks for subjects:", SUBJECT)
                        for sub in SUBJECT:
                            score = int(input(f"Enter {sub} marks: "))
                            marks[sub] = score
                    elif classnumber in SENIOR:
                        print("Select department:", DEPARTMENT)
                        ask_department = input("Enter department: ").title()
                        if ask_department != s["department"]:
                            print("Department mismatch")
                            return
                        if ask_department == "Science":
                            print("Enter marks for subjects:", SCIENCE)
                            for sub in SCIENCE:
                                score = int(input(f"Enter {sub} marks: "))
                                marks[sub] = score
                        elif ask_department == "Commerce":
                            print("Enter marks for subjects:", COMMERCE)
                            for sub in COMMERCE:
                                score = int(input(f"Enter {sub} marks: "))
                                marks[sub] = score
                        elif ask_department == "Arts":
                            print("Enter marks for subjects:", ARTS)
                            for sub in ARTS:
                                score = int(input(f"Enter {sub} marks: "))
                                marks[sub] = score
                        s["marks"] = marks
                        found = True
                        break
            if found:
                with open(self.student_file, "w") as f:
                    json.dump(students, f, indent=4)
                print("Result added successfully!\n")
            else:
                print("Student not found!\n")
            more = input("Add result for another student? (Y/N): ").upper()
            if more != "Y":
                break

    def view_result(self):
        name = input("Enter student name: ")

        with open(self.student_file, "r") as f:
            students = json.load(f)

        for s in students:
            if s["name"] == name:
                if not s.get("marks"):
                    print("No result available.\n")
                    return

                total = sum(s["marks"].values())
                percentage = total / len(s["marks"])

                print("\n----- Result -----")
                for sub, mark in s["marks"].items():
                    print(f"{sub}: {mark}")

                print("Total:", total)
                print("Percentage:", round(percentage, 2), "%")

                if percentage >= 40:
                    print("Status: PASS\n")
                else:
                    print("Status: FAIL\n")
                return

        print("Student not found!\n")

    def menu(self):
        while True:
            print("------ School Management System ------")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. Add Teacher")
            print("4. Remove Teacher")
            print("5. Update")
            print("6. Add Result")
            print("7. View Result")
            print("8. Exit")

            choice = input("Enter choice (1-8): ")

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.remove_student()
            elif choice == "3":
                self.add_teacher()
            elif choice == "4":
                self.remove_teacher()
            elif choice == "5":
                self.update()
            elif choice == "6":
                self.add_result()
            elif choice == "7":
                self.view_result()
            elif choice == "8":
                print("Exiting system... Thank you!")
                break
            else:
                print("Invalid choice!\n")


system = SchoolManagementSystem()

if system.login():
    system.menu()
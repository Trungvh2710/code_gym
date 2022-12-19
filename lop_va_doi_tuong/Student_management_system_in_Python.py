class Student:
    def __init__(self, student_id, name, dob, address, cls):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.address = address
        self.cls = cls
        
    def print_information(self):
        print("Information of the student:")
        print("id =", self.student_id)
        print("name =", self.name)
        print("date of birth =", self.dob)
        print("address =", self.address)
        print("class =", self.cls, "\n")

class StudentList:
    def __init__(self):
        self.student_list = []  #list chứa các đối tượng student
    #In thông tin sinh viên
    def print_student(self):
        for student in self.student_list:
            student.print_information()
    
    #Thêm sinh viên mới
    def add_student(self):
        print("Please input student information")
        student_id = int(input("Student_id: "))
        name = input("name: ")
        dob = input("dob: ")
        address = input("address: ")
        cls = input("class: ")
        new_student = Student(student_id, name, dob, address, cls)
        self.student_list.append(new_student)
        
    #Cập nhập thông tin sinh viên
    def update_student_information(self, name, dob, address, cls):
        student_id = int(input("Input student id: "))
        for student in self.student_list:
            if student.student_id == student_id:
                student.name = name
                student.dob = dob
                student.address = address
                student.cls = cls
            else:
                print("Không có sinh viên này")
                
    #Xóa thông tin sinh viên theo id:
    def delete_student(self):
        student_id = int(input("Input student id: "))
        index = -1
        for i in range (len(self.student_list)):
            if self.student_list[i].student_id == student_id:
                index = i
                break
        if index == -1:
            print("Not found student id")
        else:
            del self.student_list[index]
    
    #Tìm kiếm thông tin sinh viên
    def find_student_by_id(self):
        student_id = int(input("Input student id: "))
        index = -1
        for i in range (len(self.student_list)):
            if self.student_list[i].student_id == student_id:
                index = i
                break
        if index == -1:
            print("Not found student id")
        else:
            return self.student_list[i]
    
    #Sắp xếp sinh viên
    def sort_student(self):
        #sort by name
        return sorted(self.student_list, key = lambda x: x.name)

#Tạo đối tượng của lớp Student_List để sử dụng
studentlist = StudentList()
while True:
    option = int(input("Select function:\n \
                        1. View student\n \
                        2. Add new students\n \
                        3. Update students\n \
                        4. Delete students\n \
                        5. Find students \n\
                        6. Sort student \n"))
    if option == 1:
        studentlist.print_student()
    elif option == 2:
        studentlist.add_student()
    elif option == 3:
        print("Please input student information:")
        name = input("name: ")
        dob = input("dob: ")
        address = input("address: ")
        cls = input("class: ")
        studentlist.update_student_information(name, dob, address, cls)
    elif option == 4:
        studentlist.delete_student()
    elif option == 5:
        studentlist.find_student_by_id()
    elif option == 6:
        studentlist.student_list = studentlist.sort_student()
    else:
        print("Bạn nhập không đúng yêu cầu")
    y_o_n = input("Bạn muốn tiếp tục(Y/N)?: ")
    if y_o_n.upper() == "N":
        break
        print("Kết thúc")    
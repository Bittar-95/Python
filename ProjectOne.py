from functools import reduce
# =============================================================================
#                               Person Class
# =============================================================================
class Person:
    def __init__(self,name,address):
        self._name =name
        self._address =address
        
    def get_name(self):
        return self._name
    
    def set_name(self , new_name):
        self._name = new_name
        
    def get_address(self):
        return self._address
    
    def set_address(self,new_address):
        self._address = new_address
        
    def __del__(self):
        print("I have been deleted")

# =============================================================================
#                                 Employee Class
# =============================================================================
class Employee(Person):
    def __init__(self, employee_number, name, address, salary, job_title, loan):
        super().__init__(name, address)
        self.employee_number = int(employee_number)
        self.__salary = float(salary)
        self.__job_title = str(job_title)
        self.__loan = list(loan)
        
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, changed_salary):
        self.__salary = changed_salary
    
    def get_job_title(self):
        return self.__job_title
    
    def set_job_title(self, changed_job_title):
        self.__job_title = changed_job_title
    
    def get_total_loans(self):
        if len(self.__loan) !=0: 
            summation = reduce(lambda acc , loan : acc + loan , self.__loan)
            return summation
        
    def get_max_loan(self):
        if len(self.__loan) !=0: 
            max_loan = reduce(lambda max_loan , current_loan : max_loan if max_loan > current_loan else current_loan ,self.__loan )
            return max_loan
        return 0
        
    
    def get_min_laon(self):
        if len(self.__loan) !=0: 
            min_loan = reduce(lambda min_loan , current_loan : min_loan if min_loan < current_loan else current_loan ,self.__loan )
            return min_loan
        return 0
        
    def set_loans(self,changed_loans):
        self.__loan = changed_loans
        
        
    def get_loans(self):
        return self.__loan
        
    def print_info(self):
        print("Employee Information :-\n" + "Name : " + self._name, "\nAddress : " + self._address, "\nEmployee Number : "+str(self.employee_number), "\nSalary : "+ str(self.__salary), "\nJop Title : " +self.__job_title,"\nTotal Loans : " +str(self.get_total_loans()) , end="\n")
        
        
    def __del__(self):
        print('I have been deleted')

# =============================================================================
#                               Student Class
# =============================================================================
class Student(Person): 
    def __init__(self, student_number,name,address, subject, marks):
        super().__init__(name,address)
        self.student_number = int(student_number)
        self.__subject = str(subject)
        self.__marks = dict(marks)
        
    def get_subject(self):
        return self.__subject
    
    def set_subject(self, changed_subject):
        self.__subject = changed_subject
        
    def get_marks(self):
        return self.__marks
    
    def set_marks(self, change_marks):
        self.__marks = change_marks
        
    def get_average(self):
        avg = reduce(lambda acc, mark: acc + mark,self.__marks.values()) / len(self.__marks)
        return avg
        
    def get_list_grade_marks(self):
        list_grades = {}
        for key,value in self.__marks.items():
            if value >= 90:
                list_grades.update({key:value})
        return list_grades
    
    def print_info(self):
        print("Student Information :-", "\nStudent Number : ", self.student_number, "\nName : ", self._name, "\nAddress : ", self._address, "\nSubject : ", self.__subject, "\nAverage", self.get_average(), "\nMarks : ", str(self.__marks));
        
    def __del__(self):
        print("I have been deleted")
        
# =============================================================================
#                               Extr Methods
# =============================================================================
def total_objects_method(objects_list , message):
        print(message , len(objects_list))
        
def maximium_loan(objects_list):
    return reduce(lambda acc , employee : employee if employee.get_max_loan() > acc.get_max_loan() else acc,objects_list)
       
def minimum_loan(objects_list):
   return reduce(lambda acc ,loan : acc  if acc.get_min_laon()==0 or loan.get_min_laon()==0 else loan if loan.get_min_laon()<acc.get_min_laon() else acc , objects_list)

def extract_dectionary(employee_list):
    list_employee_dectionary = {};
    for emlist in employee_list:
        list_employee_dectionary.update({str(emlist.employee_number):emlist.get_loans()})
#        temp = {str(emlist.employee_number):emlist.get_loans()}
#        list_employee_dectionary.append(temp)
    return list_employee_dectionary

def highest_loans_by_dictionary(employee_list):
    
    def reduce_employee(acc , loan):
        nested_reduce =reduce(lambda nested_acc , nested_loan:nested_acc if nested_acc>nested_loan else nested_loan,loan)
        if(acc >nested_reduce):
            return acc
        else:
            return nested_reduce
        
        
    
    highest_loan = reduce(reduce_employee, employee_list.values(),0)
    return highest_loan;
   

def lowerst_loans_by_dictionary(employee_list):
    
    def reduce_employee(acc , loan):
        nested_reduce =reduce(lambda nested_acc , nested_loan:nested_acc if nested_acc<nested_loan else nested_loan,loan)
        if(acc <nested_reduce):
            return acc
        else:
            return nested_reduce
        
        
    
    lowest_loan = reduce(reduce_employee, employee_list.values(),99999999999999999)
    return lowest_loan;

def get_students_info(list_objects):
    for std in list_objects:
        print("Name: ",std.get_name())
        subjects = std.get_list_grade_marks();
        print("Subjects :")
        print(subjects)
        
def highest_salary(employee_list):
    max_salary = 0;
    for employee in employee_list:
        if  employee.get_salary()>max_salary:
            max_salary = employee.get_salary()
    return max_salary

def lowest_salary(employee_list):
    min_salary = 1000000000000000;
    for employee in employee_list:
        if  employee.get_salary()<min_salary:
            min_salary = employee.get_salary()
    return min_salary

def total_salary(employee_list):
    sum_salary = 0;
    for employee in employee_list:
        sum_salary+=employee.get_salary()
    return sum_salary

def remove_objects(obects_list):
    for objects in obects_list:
       del objects

            
            
    
  
            
    
        
    
    
# =============================================================================
#                           Instance of Employee Class
# =============================================================================
first_employee = Employee(1000, "Ahmed Yazan", "Amman, Jordan", 500, "HR Consultant", [434, 200, 1020])
second_employee = Employee(2000, "Hala Rana", "Aqaba, Jordan", 750, "Department Manager", [150, 3000,1520202, 250])
third_employee = Employee(3000, "Mariam Ali", "mafraq, Jordan", 600, "HR S Consultant", [304, 1000, 250, 300, 500, 235])
fourth_employee = Employee(4000, "Yasmeen Mohammad", "Karak, Jordan", 865, "Director", [])

#=================================== 1 ====================================#
print("-------------------------1------------------------")
employee_list = [first_employee ,second_employee,third_employee]

#=================================== 3 ====================================#
print("-------------------------3------------------------")
total_objects_method(employee_list , "Total Number Of Employee : ")

#=================================== 14 ====================================#
print("=========================14===============")
print(highest_salary(employee_list))


#=================================== 15 ====================================#
print("=========================15===============")
print(lowest_salary(employee_list))


#=================================== 16 ====================================#
print("=========================16===============")
print(total_salary(employee_list))

#=================================== 5 ====================================#
print("-------------------------5------------------------")
for employee in employee_list:
    employee.print_info()
    print("Your Loans",employee.get_loans())
    print("*********************************************************")

#=================================== 8 ====================================#
    print("-------------------------8------------------------")
print("Maximum Loan :-", maximium_loan(employee_list).get_max_loan())


#=================================== 9 ====================================#
print("-------------------------9------------------------")
print("Minimum Loan :-", minimum_loan(employee_list).get_min_laon())

#=================================== 10 ====================================#
print("-------------------------10------------------------")
for employee in employee_list:
    print(employee.get_name(),employee.get_loans() , "Total Loans Is: ",len(employee.get_loans()),"Summation Loans Is: ",sum(employee.get_loans()),end="\n");

#=================================== 11 ====================================#
print("-------------------------11------------------------")
print(extract_dectionary(employee_list))


#=================================== 12 ====================================#
print("-------------------------12------------------------")
highest = highest_loans_by_dictionary(extract_dectionary(employee_list))
print("The Highest Loan Between All Emplooies is : ",highest ,end=" ")

lowest = lowerst_loans_by_dictionary(extract_dectionary(employee_list)) 
print("The Lowest Loan Between All Emplooies is : ",lowest , end=" ")





# =============================================================================
#                           Instance of Student Class
# =============================================================================
first_student = Student(20191000, "Khalid Ali", "Irbid, Jordan", "History", {"English" : 80, "Arabic" : 90, "Art" : 95, "Management" : 75})
second_student = Student(20182000, "Reem Hani", "Zarqa, Jordan", "Software Eng", {"English" : 80, "Arabic" : 90, "Management" : 75, "Calculus" : 85, "OS" : 73, "Programming" : 90})
third_student = Student(20161001, "Nawras Abdullah", "Amman, Jordan", "Arts", {"English" : 83, "Arabic" : 92, "Art" : 90, "Management" : 70})
fourth_student = Student(20172030, "Amal Read", "Tafelah, Jordan", "Computer Eng", {"English" : 83, "Arabic" : 99, "Calculus" : 80, "OS" : 79, "Programming" : 91})

#=================================== 2 ====================================#
print("-------------------------2------------------------")
students_list=[first_student,second_student, third_student, fourth_student]

#=================================== 13 ====================================#
print("=====================================13============================")
get_students_info(students_list)
#=================================== 4 ====================================#
print("-------------------------4------------------------")
total_objects_method(students_list,"Total Number Of Students : ")

#=================================== 6 ====================================#
print("-------------------------6------------------------")
for student in students_list:
        student.print_info()
        print("*********************************************************")
        
#=================================== 7 ====================================#
print("-------------------------7------------------------")
highst_average = reduce(lambda acc,student:student if student.get_average() >  acc.get_average() else acc, students_list)        
print("------------------------------------------")
print("The Student INFO That have highst AVG :")
highst_average.print_info()


#=================================== 17 ====================================#
print("-------------------------17------------------------")
remove_objects(employee_list)
remove_objects(students_list)






        
    
        


        
    



        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
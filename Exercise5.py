class Employee:
    def __init__(self , en , name,address,salary,jt):
        self.EmployeeNumber = en
        self.__Name = name
        self.__Address = address
        self.__Salary = salary
        self.__JobTitle = jt
    def getName(self):
        return self.__Name
    def getAddress(self):
        return self.__Address
    def setAddress(self,address):
        self.__Address = address
    def getSalary(self):
        return self.__Salary
    def getJobTitle(self):
        return self.__JobTitle
    def printResultHorizantal(self):
        print("Employee Information :""Employee Number = ",self.EmployeeNumber ,"Name = ", self.__Name ,"Address = ", self.__Address , "Salary = " , self.__Salary , "Job title = ",self.__JobTitle)
      
    def printResultVretical(self):
        print("Employee Information :","\nEmployee Number = ",self.EmployeeNumber ,"\nName = ", self.__Name ,"\nAddress = ", self.__Address , "\nSalary = " , self.__Salary , "\nJob title = ",self.__JobTitle)
        
    def __del__(self):
        print(self.__Name + " has been deleted")

Employee1 = Employee(1,"Mohammad Khaled" , "Amman,Jordan" , 500,"Consultant")
Employee2 = Employee(2,"Hala Rana" , "Aqaba,Jordan" , 750,"Manager")
Employee1.setAddress("USA")
Employee1.printResultHorizantal()
print("---------------")
Employee1.printResultVretical()
print("Employee1 New Address :",Employee1.getAddress())
print("---------------")

del Employee1
del Employee2
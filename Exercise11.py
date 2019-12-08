# Python Project Three
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sqlite3
# DATABASE
connection = sqlite3.connect('OrgDB.db')
db = connection.cursor()
db.execute('''create table if not exists Employees
		   (Number int, Name text, Gender text, Nationality text, DateOfBirth text, Address text, Department text, Salary real)''')
#==============================================================================
#==============================================================================
#==============================================================================
# WINDOWS
def addEmployee():
	def add():
		global students
		number = int(numberValue.get()); numberValue.set('')
		name = nameValue.get(); nameValue.set('')
		gender = genderValue.get(); genderValue.set('')
		nationality = nationalityValue.get(); nationalityValue.set('')
		dateOfBirth = dateOfBirthValue.get(); dateOfBirthValue.set('')
		address = addressValue.get(); addressValue.set('')
		department = departmentValue.get(); departmentValue.set('')
		salary = float(salaryValue.get()); salaryValue.set('')
		
		query = f"insert into Employees values ({number}, '{name}', '{gender}', '{nationality}', '{dateOfBirth}', '{address}', '{department}', {salary})"
		db.execute(query)
		connection.commit()
		
		msgValue.set('Employee '+ str(number) +' has been added successfully.')
		
	addEmployeeWindow = Toplevel(company)
	addEmployeeWindow.title('Add Employee')
	addEmployeeWindow.geometry('800x600')
	
	xLabel = 250
	xInput = xLabel + 175
	
	yLabel = 225
	yInput = yLabel + 7
	
	numberValue = StringVar()
	nameValue = StringVar()
	genderValue = StringVar()
	nationalityValue = StringVar()
	dateOfBirthValue = StringVar()
	addressValue = StringVar()
	departmentValue = StringVar()
	salaryValue = StringVar()
	msgValue = StringVar()
	
	numberLabel = Label(addEmployeeWindow, text = 'Number: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel)
	nameLabel = Label(addEmployeeWindow, text = 'Name: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+25)
	genderLabel = Label(addEmployeeWindow, text = 'Gender: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+50)
	nationalityLabel = Label(addEmployeeWindow, text = 'Nationality: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+75)
	dateOfBirthLabel = Label(addEmployeeWindow, text = 'Date Of Birth: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+100)
	addressLabel = Label(addEmployeeWindow, text = 'Address: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+125)
	departmentLabel = Label(addEmployeeWindow, text = 'Department: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+150)
	salaryLabel = Label(addEmployeeWindow, text = 'Salary: ', font=('arial', 12, 'bold')).place(x=xLabel ,y=yLabel+175)
	
	numberInput = Entry(addEmployeeWindow, textvariable=numberValue).place(x=xInput ,y=yInput)
	nameInput = Entry(addEmployeeWindow, textvariable=nameValue).place(x=xInput ,y=yInput+25)
	genderInput = Entry(addEmployeeWindow, textvariable=genderValue).place(x=xInput ,y=yInput+50)
	nationalityInput = Entry(addEmployeeWindow, textvariable=nationalityValue).place(x=xInput ,y=yInput+75)
	dateOfBirthInput = Entry(addEmployeeWindow, textvariable=dateOfBirthValue).place(x=xInput ,y=yInput+100)
	addressInput = Entry(addEmployeeWindow, textvariable=addressValue).place(x=xInput ,y=yInput+125)
	departmentInput = Entry(addEmployeeWindow, textvariable=departmentValue).place(x=xInput ,y=yInput+150)
	salaryInput = Entry(addEmployeeWindow, textvariable=salaryValue).place(x=xInput ,y=yInput+175)
	
	addEmployeeButton = Button(addEmployeeWindow, text='Add Employee', command=add).place(x=xLabel+100 ,y=yLabel+225)

	msg = Label(addEmployeeWindow, textvariable=msgValue).place(x=xLabel+30 ,y=yLabel+275)
#==============================================================================
#==============================================================================
def viewEmployees():
	viewEmployeesWindow = Toplevel(company)
	viewEmployeesWindow.title('View Employees')
	viewEmployeesWindow.geometry('800x600')
	
	information = ScrolledText(viewEmployeesWindow, width=111, height=54)		
	
	data = db.execute('select * from Employees')
	result = 'EMPLOYEES INFORMATION:\n'
	for row in data:
		result = result + f'''Number:        {row[0]}
Name:          {row[1]}
Gender:        {row[2]}
Nationality:   {row[3]}
Date of Birth: {row[4]}
Adress:        {row[5]}
Department:    {row[6]}
Salary:        {row[7]}\n\n\n'''
	
	information.insert(END, result + '\n')
	information.grid(column=0,row=0)
#==============================================================================	
#==============================================================================
#==============================================================================
# MAINLOOP	
company = Tk()
company.title('Company Profiles')
company.geometry('800x600')

addEmployeeButton = Button(company, text='Add Employee', command=addEmployee).place(x=260,y=260)
viewEmployeesButton = Button(company, text='View Employees', command=viewEmployees).place(x=420,y=260)
exitButton = Button(company, text='Exit', command=company.destroy).place(x=370,y=300)

company.mainloop()

# =============================================================================
#Q1
#from sympy import *
#x,y,i,n,z= symbols('x y i n z')
#expr = x**2+x**3+21*x**4+10*x+1
#print(expr.subs(x,7))
#ex = expand((x+y)**2)
#print(ex)
#simp = simplify('4*x**3+21*x**2+10*x+12')
#print(simp)
#
#lim = Limit(1/(x**2),x,sym.oo)
#print(lim)
#
#summ = summation(2*i+i-1,(i,5,n))
#print(summ)
#
#integ = integrate(sin(x) + exp(x) * cos(x)+ tan(x),x)
#print(integ)
#
#fac = factor(x**3+12*x*y*z+2*y**2*z)
#print(fac)
#
#solv =solveset(x-4,x)
#print(solv)
#
#mat = Matrix([[5,12,40],[30,70,2]]) * Matrix([2,1,0])
#print(mat)
#
#plot(x**3+3,(x,-10,10))
#
#plot3d(x**2*y**3 , (x,-6,6),(y,-6,6))
#
#
# =============================================================================


import xlsxwriter, xlrd

print('\n\nEXERCISE 2')
workbook = xlsxwriter.Workbook('exercise2.xlsx')
worksheet = workbook.add_worksheet()

str1 = 'This is Example'
str2 = 'My first export examlpe'

format1 = workbook.add_format({
		'bold': True,
		'font_color': 'red',
		'font_size': 18
		})

format2 = workbook.add_format({
		'font_size': 20
		})

worksheet.write('A1', str1, format1)
worksheet.write('A2', str2, format2)
worksheet.write('A3', 1, format2)
worksheet.write('A4', 2, format2)
worksheet.write('A5', 3, format1)

workbook.close()
#==============================================================================
print('\n\nEXERCISE 3')
wb = xlrd.open_workbook('exercise3.xlsx')

for s in wb.sheets():
	print('Sheet:', s.name)
	for row in range(s.nrows):
		values=[]
		for col in range(s.ncols):
			values.append(s.cell(row, col).value)
			
		print(values)
		
	print()
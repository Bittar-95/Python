import numpy
# =============================================================================
# Q1
zeros= numpy.zeros(10)
ones= numpy.ones(10)
fives= numpy.ones(10) * 5
# =============================================================================


# =============================================================================
# Q2
array_numbers = numpy.arange(30,71,1)
print(array_numbers)
# =============================================================================


# =============================================================================
# Q3
array_numbers = numpy.arange(30,71,2)
print(array_numbers)
# =============================================================================

# =============================================================================
# Q4
array_numbers = numpy.array([[15,20,30],[15,20,30],[30,50,20]])
for array in array_numbers:
    for item in array:
        print(item)
# =============================================================================

# =============================================================================
# Q5
random_number = numpy.random.normal(0 , 1)
print(random_number)
# =============================================================================


# =============================================================================
# Q6
array_numbers = numpy.arange(48).reshape(3,4,4)

for numbers in array_numbers:
    for number in numbers:
        for item_number in number:
            print(item_number)

# =============================================================================


# =============================================================================
# Q7
array_numbers = numpy.arange(0,21)
array_numbers[9:16]*=-1
print(array_numbers)
# =============================================================================


# =============================================================================
# Q8
x = [1,8,3,5]
y = numpy.random.randint(0,11,4)
multiply = x * y;
print(multiply)

# =============================================================================


# =============================================================================
# Q9
two_dimension_array = numpy.array([[15,20,30,20],[20,30,2,3]])
print(two_dimension_array.shape , two_dimension_array , end="\n")

# =============================================================================


# =============================================================================
# Q10
three_dimension_array =numpy.random.randint(0,10,size=(3,3,3))
for one_dimension_array in three_dimension_array:
    print(one_dimension_array)
# =============================================================================

# =============================================================================
# Q11
a = numpy.array([9,-1,2,5])
b = numpy.array([1,-6,0,10])
c = numpy.array([[1,8,2,5],[3,1,7,9]])

print("a-b:",a-b)
print("a*b:" ,a*b)
print("a.dot(b):" ,a.dot(b))
print("a*2:", a*2)
print("np.sin(a):", numpy.sin(a))
print("a<3:" ,a<3)
print("a.sum():" ,a.sum())
print("a.sum(axis = 0):", a.sum(axis = 0))
print("c.sum():", c.sum())


print("c.sum(axios = 0):", c.sum(axis = 0))
print("a.min():", a.min())
print("a.max():", a.max())
print("a.mean():", a.mean())
print("a.average:", numpy.average(a))
print("a.median():", numpy.median(a))
print("a.std():", a.std())
print("a.var():", a.var())
print("c.cumsum():", c.cumsum())
print("a[1:2]:", a[1:2])
print("a[2:]:", a[2:])
print("c[-1]:", c[-1])

# =============================================================================





# =============================================================================
# Q12
import matplotlib.pyplot as plt
x = range(1,50)
y = [len(x) * 3]
plt.plot(x)
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Draw a line")
plt.show()
# =============================================================================



# =============================================================================
# Q13
#x1 = [10,20,30]
#y1 = [20,40,10]
#x2=[10,20,30]
#y2=[40,10,30]
#plt.figure()
#plt.plot(x1,y1, label = r"line 1")
#plt.plot(x2,y2, label = r"line 2")
#plt.title("Two or more lines on same plot with suitable legends")
#plt.xlabel("x-axis") ; plt.ylabel("Skill")
#plt.legend(loc='upper left')
#plt.show
# =============================================================================


# =============================================================================
# Q14
t = numpy.arange(0., 5., 0.2)
plt.plot(t, t, 'g--', t, t**2, 'bs', t, t**3,'r^')
plt.show()
# =============================================================================

# =============================================================================
# Q15
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

objects = ('Python','Java', 'Php', 'javascript', 'C#' , "C++")
y_pos = np.arange(len(objects))
performance = [22.2,17.6,8.8,8,7.7,6.7]

plt.bar(y_pos, performance, align='center' , color =('red','black','green','blue','yellow' , 'lightblue'))
plt.xticks(y_pos, objects)
plt.ylabel('Popularity')
plt.title('Popularity of Programming language')

plt.show()
# =============================================================================

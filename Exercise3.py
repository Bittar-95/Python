#Q1------------------------------------------
testList = [1,2,3,4,5];
for item in testList:
    print(item)
#Q1------------------------------------------
    
    
#Q2------------------------------------------
testList = [1,2,3,4,5];
print("The Value Is : ",sum(testList))
#Q2------------------------------------------


#Q3------------------------------------------
testList = [1,2,3,4,5];
print("The Max Value Is : ",max(testList))
#Q3------------------------------------------

#Q4------------------------------------------
testList = [1,2,3,4,5,5];
testList =list(dict.fromkeys(testList));
print(testList)
#Q4------------------------------------------


#Q5------------------------------------------
testList = [1,2,3,4,5,5];
print("True" if len(testList)!=0 else "False")
#Q5------------------------------------------

#Q6------------------------------------------
testTuple = (15,20,30,10,2);
for toupleItem in testTuple:
    print(toupleItem)
#Q6------------------------------------------
    
    
#Q7------------------------------------------
num_set = set([0, 1, 2, 3, 4, 5,6])
for item in num_set:
    print(item)
#Q7------------------------------------------
    
    
#Q8------------------------------------------
num_set = {0, 1, 2, 3, 4, 5,6}
num_set_two = {0,5,3,6,9,20,4}
numSetInterSection = num_set & num_set_two
print(numSetInterSection)
print("Test")
#Q8------------------------------------------


#Q9------------------------------------------
#(Green , Blue Yellow)
#Q9------------------------------------------

#Q10------------------------------------------
#6
#Q10------------------------------------------


#Q11------------------------------------------
dic1 = {1:10 , 2:20}
dic2 = {3:30 , 4:40}
dic3 = {5:50 , 6:60}
dic4 = {}
for d in (dic1 , dic2,dic3):
    dic4.update(d);
print(dic4)
#The Output is {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#Q11------------------------------------------




#Q12------------------------------------------
#H
#llo
#orl
#12
#hello, world!
#Jello,World!

#Q12------------------------------------------
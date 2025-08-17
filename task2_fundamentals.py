# below program shows the addition 
#num_1=20
#num_2=30
#add=num_1+num_2
#print(add)
""" i  have taken a two variables and i assigned values to those variables and i perform addition operation by using the operator+ later display the information on the screen"""

#  i Declare two variables, one storing an integer and the other a string. Print their values
name="sradha"
age=25
print(name)
print(age)

#i perform small task
''' this program prints a simple right angl triangle pattern using stars
each row adds one more star then previous'''
row=4
for i in range(1,row+1):
    print("*" * i)

#create a variables of different data types (int,float,str)and print their values
employee_name="suraj"
age=27
salary=25000.0
print(employee_name)
print(age)
print(salary)

#print  type of value assigned in to the variable
discount=20
print(discount)
print(type(discount))

#display the memory addresses
employee_id=10
person_age=10
print(id(employee_id))
print(id(person_age))

#type conversion
#str--->int
age="35"
print(type(age))
print(age)
int_conversion=int(age)
print(type(int_conversion))
print(age)


#implicit conversion(automatic)
num_1=20
num_2=2.5
result=(num_1)+(num_2)
print(result)

#cocatenate two strings
name="ravan"
company=" at ibm"
print(name+company)

'''
--> Operators:
1)Arthimetic operator - Addition,Substraction,Modular value,Multiplication,Expontial 
+,-,%,*z,**

2)Assignment operator - Equal to, Plus equal to,minus equal to,
=,+=,-=,%=,*==,**=,&=,

3)Comparision operator = ==,!=,>=,<=,etc

4)Logical Operators = And( Should satisfy both conditions ) ,or ( Should Satisfy any one Condition) , not (Reverse the output)

5)Identity Operators = is(Used to check the object(Memory allocation), is not( Used to check the object not same)

Note : Difference between is and == is is checks the object(Memory) and it checks the value

6)Membership operators = To check the item's availability ) - in, not in( Reverse the output of in)

7)Bitwise operators = & - Bitwise and  ,| Bitwise or ,^ Bitwise xor,~,<<,>>(ex - 5 - 0101,3 - 0011 )



num01 = 90
num02 = 7
num03 = 48
print(num01 + num02 + num03)


int1 = 8
int2 = 7
print(int1 - int2 )

digit_x = 789
digit_y = 897
print(digit_x % digit_y == 0)


num1 = 89
num2 = 98
print(num1 * num2)
print(num1 ** num2)
print(num1 // num2)



num = 9
num += 77
print(num)

Marks = 90
Marks -= 70
print(Marks)


Digit_01 = 90
Digit_01 %= 70
print(Digit_01)


y = 90
y *= 70
print(y)

dy = 9
dy **= 89
print(dy)


a= 69
b = 90
print(a > 70 and b > 70)


day1_Collections = 6000
day2_Collections = 9000
day3_Collections = 1000
print(day1_Collections >1000 or day2_Collections > 1000 or day3_Collections > 1000)


mkg = 90
mhj = 678
print(not( mkg > mhj))'''


x = 98
y = 98
print( x is y)

list_ = [1,5,6]
list_2= [4,8,9]
list_3 = list_2
print(list_3 is list_)

list_x = [1,5,6]
list_y= [4,8,9]
list_z = list_y
print(list_z is not list_x)


Math_Score = [98,80,90,99,67]
Eng_Score  = [98,96,0,100,68]
print(Math_Score in Eng_Score)
print(100 in Eng_Score)
print(Math_Score not in Eng_Score)


print(5 & 3)
'''(5 - 0101,3 - 0011 and 11 - 1  )'''
print(5 | 3)
'''(5 - 0101,3 - 0011 and 00 - 0  )'''

print(5 ^ 3)
'''(5 - 0101,3 - 0011 and same - 0  )'''



























































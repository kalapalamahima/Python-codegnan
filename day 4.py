'''--> Datatypes - 2 types:
1) Mutable - Can be modify directly on the variable which the data type is assigned.
ex- List,Dict,
2) Immutable - Can not be modified directly on the variable which the data type is assigned.
ex - int,str,Tuple,Set

--> Int    : Storing a number or digit in the variable
--> Float  : Storing a decimal value in the variable
--> String : Collection of characters represented with ' ' or " "

Methods         - Can be changed but not modified
1)Replace()     - This method is used to change the old sub string with a new sub string

2)Indexing()    - It access the string from 0,1,.... positions for each character which used to get the
                  particular substring,item from start {variable[Index position]}
                  
3)Cancatenation - It is used add 2 or more a strings,tuples and lists with the same data type

4)Split         - Used to seperate the string using a dsubstring and it will sploit into list such as before the
                  substring is one index and after the substring is another index.

5)Strip        - It removes the sub string either the first or last
6)Join         -  It joins the string with any special character given
7)Count()
8)Capitalize()
9)is alpha()
10)is alnum()
11)isdigit()
12)isdecimal()



Split()
joint()


Digit_01 = 9
Digit_02 = 9
print(Digit_01 + Digit_02)'''


#Methods: replace(variable.replace('old str','new str') 

my = 'Python is a programming language'
print(my.replace('Python','C'))

#indexing:
my = 'Python is a programming language'
print(my[5])
# Cancatenation:
g = ('Hello')
print(g + ' Mahima')

# Split: 
m = 'Honesty is the best policy'
print(m.split('best'))

# Strip:
m = 'Honesty is the best policy'
print(m.strip('Honesty'))

# join
a = 'Honesty is the best policy'
print('-'.join(a))

# f :

num = int(input('enter a number: '))
print(f'{num} is a even number')


a = "I am going to clg"
b = a.split()
print(len(b))


time = '22:43'
print(time.split())
print(index(0))







      
 























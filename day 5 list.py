'''--> List: It is a collection of different datatypes and it is represented by [] seperated by comma.
It is a mutable data type.

*Methods:Variable_name.Method()

1)Append() - It is used to add new item into list at the last position of the list.(only 1 argument is passed but as a list we can add more then 1) even int included
2)Extend () - Its is used to add new item into list but it adds as each position to each index in the list,It only takes iterables (List,str,tuple).int excluded
3)Pop()     - It removes the index position's value,if nothing is mentioned it will remove last index position
4)Remove()  - It removes directly the item given.
5)Slicing() - It is used to get particular part of the list,string or tuple,this is based on the index positions (Inclusive:Exclusive)
6)Len()     - It is used to find the number of items present in the list 

'''
any = [1,'Python is a  language',67,68,[34,['This is python class'],78,'Im looking for good bat'],[2,'this is 5th class',3],56]
print(any[4] [1] [0] [-6])


# Immutable data type:
c = 'Java is a Language'
print(c.replace('java','Python'))
print(c)

# Append: Mutable  
a = [1,3,4,6]
print(a.append(56))
print(a)
a.append([9,0])
print(a)

#Extend:(List,str,tuple)
b = [2,5,7,0]
b.extend([5,7,'good'])
print(b)

#Pop:
nm = [2,6,8]
nm.pop(2)
nm.pop()
print(nm)

#Remove()
n = [2,5,78,90]
n.remove(78)
print(n)

#Slice()
po = [45,7,8,9,0,5,6]
print(po[2:5])

#Len()
y = 'Good Girl'
print(len(y))











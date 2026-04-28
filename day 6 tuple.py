''' --> Tuple: It is a collection of ifferent data types which are represented by ()
--> And the items in the tuple is seperated by comma.
---> They r worked with indexing
---> It is immutable


---> Dictionaries : (Important)
===> Allows any the immutable datatypes(int,str,tuple)
===> Dict is a colection of key:value pairs.
---> Duplicates r not allowed,if given it takes only the last occurance of it


---> Methods :
 1) ceys() - Used to access only keys in the dict (dict.keys())
 2) values() - Used to access only values in the dict (dict.values())
 3) items() - Used to access key value pairs into tuples 
 4) clear() - Used to delete all the items
 5) Update() - Used to add new key:value


'''
#Tuple
so = (1,'Python',[2,5],[4,5])
print(so[1])

#Concetanation
m = (2,3,4,5)
print(so + m)

#Dictionary
hm = {'Name' : 'Maahi','age': '22'}
print(hm)

#Methods
#Keys()
print(dict.keys(hm))
print(dict.values(hm))
print(dict.values(hm))

#print(22 in hm['age']) - only for string


#print('Maahi' in hm['Name'])

hm.update({'Edu' : 'B.tech'})
print(hm)

#1)Create a tuple with different data types,Print the second element?

k = (1,4,'fish')
print(k[1])

#2) Access the last element using indexing

m = (10,20,30,40)
print(m[-1])

#3) Create two tuples , Concatenate them and print result
kl = (4,6,7)
ml = ('j','ukl')
print(kl + ml)

#4)Slice and print elements from index 1 to 3
x = (1,2,3,4,5)
print(x[1:3])

#6) Create a dictionary with keys: name, age, city Print the dictionary

n = {'name':'Ram','age':'25','city':'Hyderabad'}
print(n['name'])







































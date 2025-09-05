name = "prakhar aditya"
print(name[2])#index 2
print(name[0:14:3])#index 0 to 14 (n-1)
# [0:14] means 0th letter to last letter 14th and [:3] means every 3rd letter\
name1="anmol";
print(name1[:4])
name2="anmol";
print(name2[2:])
name3="anmol";
print(name3[:-1])

print("anmol"in name3)#value is true and it is case sensitive.


print("Anmol"in name3)#value is false and it is case sensitive.
print("Anmol"not in name3)#value is true and it is case sensitive.
print(len(name3))#answer is 5 baeacuse "len" is used to find length of a string.


#tuple is immutable because they have different id 
data= ("Shubham",19,3.14)

print(id(data))

print(data[1])#to find the specific value at a certain index

data= (True) reinitialize is not allowed because it is immutable
print(id(data))


data1=("shubham",19,3.14,(4,6,7))#to access (4,6,7)you have to come first on index of parenthesis data and then on elemnet data. 

data2=(78)
print(type(data2))#int show int because tuble have comma after its first element other wise it is not tuple
# for check type use type fxn 



data3=(78,"shubham")#now it show tuble because it have commma / element after its first element
print(type(data3))

data4 =3,4,5,"rahul" #it is also a tuple you can also use tuple without any parenthesis.
print(type(data4))
sum=data3+data4 #it is use for concatination
print(sum)


#youncan also pritn tuble with another data type
print(f"{(data2)},{(data3)}")

sum=data3+data4 #it is use for concatination
print(sum)
print(sum[0])
print(sum[3:-1])#-1 or ending element is not include in slice while printing
print(sum[3:-3])#-1 or ending element is not include in slice while printing thats why result is blank 
print(sum[3:0])#  slice while printing thats why result is blank 
print(sum[-3:0])#  slice while printing thats why result is blank 


data5=78,
print((data5[0])*3)#it is use to multiply tuple number

data6=78,"shubham"
print((data6)*3)#it is use to print tuble multiple times 


data7=78,
print((data7)*3)#it is use to print number multiple time



data8="shubham", #it is use to print element multiple times 

print((data8)*3)


data8="shubham"   #it is use to print index value multiple time 
print((data8[0])*3)

a,b,c,d=data4  #this is clalled unpacking in which you can assign a variable for each value of data 2 
print(a,b,c,d)

data8=1,2,4,5,8,5,6,5,5,5,4,4,4,5,6,2,4,8,5,8,4,4
print(data8.count(4))#.count fxn is use to print a count of a value .



# <------------------------list--------------------------->\
#list is mutable and can be change or reinitialize

list1=[1,2,3,4,5,6,7.95,True,"shubham",(6,7,"90"),[3,40]]
print(list1[9][1])
print(list1[-1][-1])#----------------/
                                      #both output are same
print(list1[-1][1])#----------------/



list1=[1,2,3,4,5]
list1.append("shubham")#append is use for add value in list 
print(list1)



list1=[1,2,3,4,5]
list1.insert(4,10)#insert is use for add  value on certain index in list 
print(list1)


list1=[1,2,3,4,5]
list1.remove(3)#rremove  is use for remove value on certain index in list 
print(list1)



 

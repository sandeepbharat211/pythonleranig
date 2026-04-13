#numerical data type
a=10
print(a,type(a)) #integer data type
a=6.8
print(a,type(a)) #float data type
a=6+3j
print(a,type(a)) #complex data type

#Sequensial data type
s="Hello"
print(s,type(s))
s='hello 89778'
print(s,type(s))
s='''hello my name is sandeep 
my coures is fullsatck python'''
print(s) #ther is all string data type

x=[10,3,9,50,3,9]
x[0]=8
print(x,type(x)) #List data type

x=(66,56,8j,'hello')
print(x,type(x)) #tuple muteble data type
x=(10)
print(x,type(x)) #this is count integer

#dictinory data type
a={ 'cource':'python',
  'corce_duresion': "7 months"} #dict data type
print(a,type(a))

a={23,40,6,8,9,6}
#a[3]=3  # set is inmuteble data type
print(a,type(a)) #set data type

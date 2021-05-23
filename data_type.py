num = 2.5 # 'float' data type
print(num)
print(type(num))
num = 5 # 'int' data type
print(num)
print(type(num))
num = 6+9j # 'complex' data type
type(num)
print(num)
print(type(num))
a = 5.6 #value is 'float'
print(a)
b = int(a) #but we can convert it into 'int'.
print(b)
print(type(b))
k = float(b) # b is in 'int' format convert it into 'float'.
print(k)
k = 6
c = complex(b,k)
print(c)
print(b<k) # ans comes true.
print(type(b<k)) # class comes 'bool'. so in this bool data type we find the value i.e true or false.
print(b>k)
print(int(True)) #value of 'True' is 1.
print(int(False)) # value of 'False' is 0.
a = [25,36,45,12]
print(type(a)) # 'list' data type.
a = {25,36,45,15,12,25}
print(type(a)) # 'set' data type.
t = (25,36,4,57,12)
print(type(t)) # 'tuple' data type.
a = "Omkar"
print(type(a)) # 'string' data type.
print(range(10)) # it will shows(0, 10). This is the 'range' data type.
print(list(range(10))) # it will shows (0,1,2,3 upto 10).
d = {'narendra':'redmi','omkar':'nokia','akshay':'iphone','sneha':'oneplus'}
print(d)
print(d.keys()) #this is 'Dictionary' data type. keys are names.
print(d.values()) # this  shows values in dictionary.
print(d.get('akshay')) # this get function shows a specific value which we want to find.
a = {'omkar':'berozgaar','narendra':'8lpa','akshay':'7.5lpa','sneha':'8.5lpa'}
print(a)
print(a.keys())
print(a.get('omkar'))
print(a.get('narendra'))


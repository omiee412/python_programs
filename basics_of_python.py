print('omkar')
x = 2
y = 3
print (x+y)
print ("omkar's laptop")
print(r'omkar\'s laptop') #backslash (\') is the meaning of escape character
print("omkar's laptop")
name = 'youtube' # "name 'youtube'" does not work bcz of name is variable and youtube is string, concatenation cannot occur like this.
print('/home/omkar') # in linux we use (/), intstead of (\) in windows.
print('/home/\nomkar') # (\n) is for new line .
print(r'/home/\nomkar') # (r') is denotes Raw string, to treat (\) as a normal character.
print('omkar' + 'omkar') #add or concatenate two strings.
x = 2
print(x + 3)
y = 3
print(x + y) # for mathematical purpose.
print(name +  ' rocks') #concatenation of strings using variable.
print(name[0]) # in [] '0' is the first character of 'youtube' prints 'y'.
print(name [4]) #in [] '4' is the fifth character of 'youtube' prints 'u'.
print(name[6]) #in [] '6' is the seventh character of 'youtube' prints 'e'.
print(name[0:4]) #in [] '0:4' is the 'string slicing' eg. 0=y to 4=t i.e 'yout'.
print(name[1:6]) #in [] '1:6' is the 'string slicing' eg. 1=o to 6=b i.e 'outub'.
print(name [3:])#in [] '3:' is the 'string slicing' eg. 3=t to the end of the string i.e 'tube'.
print(name [-6:])#in [] '-6:' is -ve index. -1 is the last character of string i.e 'e' and so on -2 is 'b'...
myname = 'Omkar Potdar' # myname is varible.
print(myname)
print(len(myname)) #len is length of the string. 
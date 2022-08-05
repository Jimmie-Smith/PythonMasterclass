#print('today is a good to learn python')
#print('python is fun')
#print("python's strings are easy to use")
#print('we can even use "quotes" in strings')
#print("Hello" + " World")
greeting = "Hello"
name = "jimmie"
print(greeting + name)

# If we want a space, we can add that too! input prompts a command taken and stored into a variable

#print(greeting + ' ' + name)

#print("C:\\Users\\tim\\notes")

#print(r"C:\Users\tim\notes")

age = 24
age = "2 years"
floater = 25.5
print(age)
print(name +  " is " + age +  " years old")



print(type(greeting))
print('This is the new age type', type(age))

age = 27

print("i am {0} years old".format(age))

for i in range(1, 10):
    print("No {0} is {1} squared, and {2} cubed.".format(i, i ** 2, i ** 3))
    
print(f"Jimmie is {age} years old")

for i in range(1,10):
    print(f"number {i} is {i ** 2}, and {i **3} is {i} cubed")
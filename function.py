# example of simple function

# def greet():
#     print("hello,welcome to python")

# greet()
# greet()
# greet()

 #function with parameter
# def greet(name):
#     print(f"hello,{name}")

# greet("Anu") #"anu"->arguments
# greet("Ram")


# fuunctin add two numbers
def add(num1,num2):
    print(num1+num2)
    #return num1+num2


add(2,5)
add(40,10)
x=10
y=60
add(x,y)
print(add(x,y))    
 

 # functin with return value

def add(num1,num2):
   return num1+num2

x=add(3,5)
print(f"x={x}")
print(f"sum:{add(10,40)}")
res=add(6,7)
print("res:",res)
print(add(2,6))
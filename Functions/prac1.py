# square of a number
def f(n,m):
    return n**m
ans=f(3,5)
print(ans)

#write a function to return area and circumference
import math
def fcalculate(radius):
    area=round(math.pi*radius**2,2)
    circumference=round(2*math.pi*radius,2)
    return area,circumference
a,c=fcalculate(3)
print("area is: ",a,"and" ,"circumference is: ",c)

# write a function to return  a default value if not any value is given
def greet(name="riya"):
    return "hello "+ name+"!"
print(greet("aditya"))

# how lambda function work
cube=lambda x:x**3
print(cube(3))

# how sum(args) method work

def sum_all(*args):
    return sum(args)
print(sum_all(1,2))
print(sum_all(1,2,3,4))

# how we can take more argument in one funtion
def print_list(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}=>{value}")
print_list(name="riya",branch="ece",year="3rd")
print_list(name="riya",branch="ece")

# how yieling work
## yield is used inside a function to make it a generator instead of a normal function.
# Think of it as a "pause and resume" keyword:
#return → ends the function and sends back a value.
#yield → sends back a value but keeps the function's state so it can continue from where it left off next time you call it.

def even_generator(limit):
    for i in range(2,limit+1,2):
        yield i
    
for num in even_generator(10):
    print(num)
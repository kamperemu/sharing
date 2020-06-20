# getting started with python

# q9
x = int(input("Enter x coordinate: "))
y = int(input("Enter y coordinate: "))

dist = (x**2 + y**2)**(1/2)
dartHit = False
if dist <=10:
    dartHit = True
print(dartHit)

# q10
Celsius = int(input("Enter the temperature(in Celsius): "))
Fahrenheit = ((Celsius*9)/5)+32
print("The temperature in Fahrenheit is",Fahrenheit)

# q11
P = int(input("Enter money lent: "))
R = int(input("Enter rate of interest per annum (in %): "))
T = int(input("Enter time (in years): "))

Amount = P + ((P*R*T)/100)
print("Amount payable is",Amount)

# q12
x = int(input("Number of days of work for person A: "))
y = int(input("Number of days of work for person B: "))
z = int(input("Number of days of work for person C: "))

team = (x*y*z)/(x*y+y*z+x*z)
print("The job takes",team,"days to complete the work together.")

# q13
x = int(input("Enter x: "))
y = int(input("Enter y: "))

add = x + y
sub = x - y
mul = x * y
div = x / y

print("x + y = ",add)
print("x - y = ",sub)
print("x * y = ",mul)
print("x / y = ",div)

# q14
x = int(input("Enter x: "))
y = int(input("Enter y: "))
swap = x
x = y
y = swap
print("x = ",x)
print("y = ",y)

# q15
x = int(input("Enter x: "))
y = int(input("Enter y: "))
x,y = y,x
print("x = ",x)
print("y = ",y)

# q16
n = int(input("Enter n:"))
for i in range(n):
    print("GOOD MORNING")

# q17
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = int(input("Enter z: "))

avg = (x+y+z)/3

print("The average of the three numbers is",avg)

# q18
r1 = 7
vol1 = (4*22*(r1**3))/(3*7)
r2 = 12
vol2 = (4*22*(r2**3))/(3*7)
r3 = 16
vol3 = (4*22*(r3**3))/(3*7)

print("Volume of sphere with radius",r1,"cm is",vol1,"cm^3")
print("Volume of sphere with radius",r2,"cm is",vol2,"cm^3")
print("Volume of sphere with radius",r3,"cm is",vol3,"cm^3")

# q19
name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = 2020+100-age
print(name,"will be 100 years old in the year",year)

# q20
m = int(input("Enter mass of object (in kg): "))
E = m * (3 * 10**8)**2
print("The energy of the object is",E,"Joules.")


# q21
import math
ladder = int(input("Enter length of ladder: "))
angle = int(input("Enter angle made by ladder: "))
height = ladder * math.sin(math.radians(angle))
print("Height reached by the ladder is",height)














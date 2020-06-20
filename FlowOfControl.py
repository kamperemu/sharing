# Flow Of Control

# python code 1
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(name," is eligible for applying for driving license")
else:
    print(name," is not eligible for applying for driving license")


# python code 2
n = int(input("Enter the table you want: "))

for i in range(1,11):
    print(str(n)+" x "+str(i)+" = "+str(n*i))

# python code 3
a = int(input("Enter value 1: "))
b = int(input("Enter value 2: "))
c = int(input("Enter value 3: "))
d = int(input("Enter value 4: "))
e = int(input("Enter value 5: "))
nums = [a,b,c,d,e]
maxnum = a
minnum = a
for i in nums:
    if maxnum < i:
        maxnum = i
    if minnum > i:
        minnum = i

print("MAXIMUM:",maxnum)
print("MINIMUM:",minnum)


# python code 4
year = int(input("Enter the year: "))
if year % 4 == 0:
    print(year," is a leap year.")
else:
    print(year," is not a leap year.")


# python code 5
n = int(input("Enter a number: "))
i = 5

while i <= n:
    if (i % 10) == 0:
        num = i
    else:
        num = -i

    if i == (n//10)*10:
        print(num)
    else:
        print(num, end=",")

    i+=5
        
print()
# python code 6

n = int(input("Enter n: "))
sum = 0
for i in range(1,n+1):
    sum += (1/(i**3))
print("SUM: ",sum)


# python code 7
n = int(input("Enter n: "))
total = 0
while(n>0):
    digit=n%10
    total=total+digit
    n=n//10
print("SUM:",total)




# python code 8
n=int(input("Enter number:"))
temp=n
r=0
while(n>0):
    digit=n%10
    r=r*10+digit
    n=n//10
if(temp==r):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")



# python code 9 (i)
n = 5
for i in range(1,n+1,2):
    for j in range(n,i,-2):
        print(end=" ")
    for j in range(0,i):
        print("*",end="")
    print()
for i in range(n-2,0,-2):
    for j in range(i,n,2):
        print(end=" ")
    for j in range(i,0,-1):
        print("*",end="")
    print()

# python code 9 (ii)
n=5
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(end="  ")
    for j in range(i,0,-1):
        print(j,end=" ")
    for j in range(2,i+1):
        print(j,end=" ")
    print()
# python code 9 (iii)
n=5
for i in range(n,0,-1):
    for j in range(n,i,-1):
        print(end="  ")
    for j in range(1,i+1):
        print(j,end = " ")
    print()

# python code 9 (iv)
n = 5
for i in range(1,n+1,2):
    for j in range(n,i,-2):
        print(end=" ")
    for j in range(0,i):
        if j==0 or j==i-1:
            print("*",end="")
        else:
            print(end=" ")
    print()
for i in range(n-2,0,-2):
    for j in range(i,n,2):
        print(end=" ")
    for j in range(i,0,-1):
        if j==i or j==1:
            print("*",end="")
        else:
            print(end=" ")
    print()


# python code 10
percent = int(input("Enter percentage of marks:"))
if percent>90:
    print("GRADE: A")
elif percent>80:
    print("GRADE: B")
elif percent>70:
    print("GRADE: C")
elif percent>60:
    print("GRADE: D")
else:
    print("GRADE: E")

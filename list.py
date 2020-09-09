'''
# code 2(a)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))

print(l)

# code 2(b)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(input("Enter no: "))

print(l)

# code 2 (c)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))

for i in l:
    if i%2==0:
        print(i, end = " ")

# code 2 (d)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))
sum = 0
for i in l:
    if i%2 == 1:
        sum+=i

# code 2 (e)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))
for i in l:
    if i%5==0:
        print(i, end = " ")

# code 2 (f)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))
for i in l:
    if i%3==0 and i%7==0:
        print(i, end = " ")

# code 2 (g)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))

pro = 1
for i in l:
    if i%10 == 0:
        pro*=i
print(pro)

# code 2 (h)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))
for i in l:
    if i%10==3:
        print(i, end = " ")

# code 2 (i)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))
for i in range(len(l)):
    if i%2 == 0:
        print(l[i],end=" ")

# code 2 (j)
l = []
n = int(input("Enter n: "))
for i in range(0,n):
    l.append(int(input("Enter no: ")))

print("First 3:",end=" ")
for i in range(0,3):
    print(l[i],end = " ")
print()
print("Last 3:",end=" ")
for i in range(-1,-4,-1):
    print(l[i],end=" ")
print()


test = input("Enter String: ")
count = len(test.split())
print("no of words: ",count)

test = input("Enter String: ")
test_list = test.split()
count = len(test_list)
print("no of words: ",count)


# python code
test = input("Enter a string: ")
L = list(test)
str1=""
for i in L:
    if(i=='a'):
        i="A"
    str1+=i
print(str1)
'''
# python code
list1 = [5,10,15,20,25,50,20]
for i in range(len(list1)):
    if list1[i]==50:
        list1[i]=200
        break

print(list1)

# python code
list1 = [5,20,15,20,15,50,15]
i=0
while i<len(list1):
    if list1[i] == 15:
        list1.pop(i)
    else:
        i+=1
print(list1)

# python code
L1 = [10,20,30,40]
L2 = [111,222,333,444]
for i in range(len(L1)):
    print(L1[i],end=" ")
    print(L2[i])
for i in range(len(L1)):
    print(L1[i],end=" ")
    print(L2[-i-1])
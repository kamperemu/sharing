# options of series for user to choose from
print("There are 4 different types of series:")
print("1) 1,2,3,4,5,6,7...n")
print("2) 1 2 4 8 16...n ")
print("3) -100 -96 -92...n ")
print("4) 1 10 100 1000...n ")
print("5) 2+4+6+8+10+...n ")
print("6) 10+20+30+...n ")
print("7) 4+8+12+...n ")
print("\nPress 0 to exit\n")


loop = True
while loop:

    choice = int(input("Enter your choice : "))

    # printing series according to choice of the user
    if choice == 1:
        # 1,2,3,4,5,6,7,...n
        n = int(input("Enter a number: "))

        for i in range(1, n):
            print(i, end=",")
        print(i+1)
    elif choice == 2:
        # 1 2 4 8 16 ...n
        n = int(input("Enter a number: "))
        i=1

        while i<=n:
            print(i, end=" ")
            i*=2
    elif choice == 3:
        # -100 -96 -92 -88 -84 ... n
        n = int(input("Enter a number: "))

        for i in range(-100, n+1, 4):
            print(i, end=" ")
    elif choice == 4:
        # 1 10 100 ... n
        n = int(input("Enter a number: "))
        i = 1
        while i<=n:
            print(i, end=" ")
            i*=10
    elif choice == 5:
        # 2+4+6+8+...n
        n=int(input("Enter a number: "))
        sum=0
        for i in range(2,n+1,2):
            sum+=i
        print("Sum: ",sum)
    elif choice == 6:
        # 10+20+30+40+...n
        n=int(input("Enter a number: "))
        sum=0
        for i in range(10,n+1,10):
            sum+=i
        print("Sum: ",sum) 
    elif choice == 7:
        # 4+8+12+16+...n
        n=int(input("Enter a number: "))
        sum=0
        for i in range(4,n+1,4):
            sum+=i
        print("Sum: ",sum)
    elif choice==0:
        print("\n\nexiting")
        loop=False
    else:
        print("Invalid input")

    print("\n")



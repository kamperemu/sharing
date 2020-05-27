print("Select the series you want from these")
print("1. 2 4 6 8")
print("2. 2 4 6 8 ...n")
print("3. 3 6 9 ...n")
print("\nPress 0 to exit\n")


loop = True

while loop:
    series = int(input("Enter the number of the series you want:"))
    if series==1:
        for i in range(2,9,2):
            print(i, end=" ")
    elif series==2:
        n = int(input("Enter n: "))
        for i in range(2,n+1,2):
            print(i, end=" ")
    elif series==3:
        n = int(input("Enter n: "))
        for i in range(3,n+1,3):
            print(i, end=" ")
    elif series==0:
        print("\n\nexiting")
        loop=False
    print("\n")

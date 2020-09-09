def ques(A,B):
    if B in (A+A) and len(A)>=len(B):
        return True
    else:
        return False
A = input("String A: ")
B = input("String B: ")
print(ques(A,B))
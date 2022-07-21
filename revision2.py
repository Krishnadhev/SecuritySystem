# n=int(input("Enter a value to check if it prime or not: "))
# factors=0
# for i in range(1,n+1):
#     if n%i==0:
#         factors=factors+1
# if factors==2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

# 4. Write a program in Java to open 3 arrays of name A, P & N. 
# Store 15 numbers in array A. 
# Shift all the positive even numbers in array P and all the negative odd numbers in array N. 
# Finally print the array P & N.

A=[17,18,-20,-21,41,-87,44,66,-110,-95,12,26,-73,78,91]
P=[None] * 15
N=[None] * 15
Pposition=0
Nposition=0
for i in A:
    if i%2==0 and i>=0:
        P[Pposition]=i
        Pposition=Pposition+1
    if i%2==1 and i<=0:
        N[Nposition]=i
        Nposition=Nposition+1
print(P)
print(N)
        
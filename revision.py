#Write a program and display all the evens numbers from te list
A=[17,23,37,82,90,4]
for i in A:
    if i%2==0:
        print(i)

#WAP to make a list of random numbers and find the sum of oddnumbers
sum=0
A=[17,23,37,82,90,4]
for i in A:
    if i%2==1:
        sum=sum+i
print(sum)

#WAP to display only those numbers that are in the odd position and are even
A=[17,23,37,82,90,4]
for i in range(0,6):
    if A[i]%2==0 and i%2==1:
        print(A[i])

#WAP to make a list of random numbers. 
#Transfer all the even numbers to array A and all the odd numbers to array B.
C=[12,14,16,18,20,21,23,5,17,19]
evenposition=0
oddposition=0
A=[None] * 5
B=[None] * 5
for i in C:
    if i%2==0:
        A[evenposition]=i
        evenposition=evenposition+1
    else:
        B[oddposition]=i
        oddposition=oddposition+1
print(A)
print(B)

#WAP to make a list of random numbers and reverse all the numbers.
C=[12,14,16,18,20,21,23,56,17,19]
for i in C:
    firstnumber=i//10
    lastnumber=i%10
    reverse=(lastnumber*10)+firstnumber
    print(reverse)


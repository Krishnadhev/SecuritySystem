# n=int(input("Enter a number: "))
# lastnumber=n%10
# firstnumber=n//10
# print(firstnumber)
# print(lastnumber)
# reverse=lastnumber*10+(firstnumber*1)
# print(reverse)

# list=[19,17,29,81,93]
# for i in list:
#     firstnumber=i//10
#     lastnumber=i%10
#     reverse=lastnumber*10+(firstnumber*1)
#     print(reverse)

# 1. Accept 10 numbers into an array and then calculate the sum of numbers present in odd positions and even positions respectively.

# list=[97,66,54,12,5,112,17,31,24,45]
# oddsum=0
# evensum=0
# for i in range(0,10):
#     if i%2==0:
#         evensum=evensum+list[i]
#     else:
#         oddsum=oddsum+list[i]
# print(evensum)
# print(oddsum)

# 2. Accept 10 numbers into an array and then calculate the sum of even numbers present in odd positions.

# list=[17,29,37,49,53,173,192,126,289,00]
# sum=0
# for i in range(0,10):
#     if i%2==1 and list[i]%2==0:
#         sum=sum+list[i]
# print(sum)

# Create two arrays A and B of size 5 and C of size 10. 
# Accept numbers in two arrays A and B. Fill the array
#  C in such a way that the all odd positions occupy the numbers
#  present in array A and all even positions occupy the numbers present in array B.
# A=[29,49,173,126,19]
# B=[17,37,53,192,289]
# C=[None] * 10
# oddposition=1
# evenposition=0
# for i in A:
#     C[oddposition]=i
#     oddposition=oddposition+2
# for i in B:
#     C[evenposition]=i
#     evenposition=evenposition+2

 #4. Create three arrays A, B and C both of size 5.
 #  Accept numbers in two arrays A and B. 
 # Fill all the elements of array C with the sum of numbers
 #  present in appropriate element of array A and B.

# A=[29,49,173,126,19]
# B=[17,37,53,192,289]
# C=[None] * 5
# for i in range(0,5):
#     C[i]=A[i]+B[i]
# print(C)



 #Create two arrays A and B of size 5 and C of size 10. 
 # Accept numbers in two arrays A and B. 
 # Fill the array C in such a way that the first five positions occupy the numbers
 #  present in array A and rest of five positions occupy the numbers present in array B.

# A=[29,49,173,126,19]
# B=[17,37,53,192,289]
# count=5
# C=[None] * 10
# for i in range(0,5):
#     C[i]=A[i]
#     C[count]=B[i]
#     count=count+1
# print(C)

# Create two arrays A and B of size 5 and C of size 10. 
# Accept numbers in two arrays A and B. 
# Fill the array C in such a way that the all odd positions occupy the 
# numbers present in array A and all even positions occupy the numbers present in array B.

# A=[29,49,173,126,19]
# B=[17,37,53,192,289]
# oddcount=1
# evencount=0
# C=[None] * 10
# for i in range(0,5):
#     C[oddcount]=A[i]
#     C[oddcount-1]=B[i]
#     oddcount=oddcount+2
#     evencount=evencount+2
# print(C)

#12. Accept the name, physics, chemistry and math marks of 25 students. 
#Then display a list of the given data with Total and Average.

# Physics=[98,87,89,94,91,100,101,72,53,67,85,73,86,82,96,32,17,63,55,56,57,58,59,60,61]
# Chemistry=[98,87,89,94,91,100,101,72,53,67,85,73,86,82,96,32,17,63,55,56,57,58,59,60,61]
# Math=[98,87,89,94,91,100,101,72,53,67,85,73,86,82,96,32,17,63,55,56,57,58,59,60,61]
# Total=[None] * 25
# Average=[None] * 25
# print(len(Physics))
# print(len(Chemistry))
# print(len(Math))
# print(len(Total))
# for i in range(0,26):
#     Total[i]=Physics[i]+Chemistry[i]+Math[i]
#     Average[i]=Total[i]/3
# print(Total)
# print(Average)

# Write a program to find from the following data: 17, 20, 24, 29, 16, 87, 19, 52
# Product of the odd numbers
# sum of the even numbers
#The largest and smallest element

l=[17,20,24,29,16,87,19,52]
product=1
sum=0
for i in range(0,8):
    number=l[i]
    if number%2==1:
        product=product*number
    else:
        sum=sum+number
print(product)
print(sum)
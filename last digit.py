# Write a program to accept n number from user and display the last digit of all those n numbers.

# n= int(input("Enter n numbers: "))


# for i in range(1,n+1):
#     a= int(input("Enter a number: "))
#     print(a%10)


# a2 + a2 / 2 + a2 / 3 + …… + a2 / 10
# a=int(input("Enter a value for a: "))
# sum=0
# for i in range(1,11):
#     sum=sum+((a**2)/(i))
# print(sum)

# x^1 - x^2 + x^3 - x4 + x5 - ………… - x20; where x = 2

sum=0
x=2
for i in range(1,21):
    if i%2==0:
        sum=sum-x**i
    else:
        sum=sum+x**i

print(sum)

# 1, 2, 4, 7, 11, 



    
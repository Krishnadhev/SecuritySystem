n=int(input("Enter a value to find if it is prime or not: "))
for i in range(2,n):
    if n%i!=0:
        a=2
if a==2:
    print("Prime Number")
   
else:
    print("Not a Prime")
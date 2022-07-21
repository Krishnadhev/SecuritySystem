m=int(input("Enter a number for m: "))
n=int(input("Enter a number for n: "))
count=0
count1=0
for i in range(1,m+1):
    if m%i==0:
        count=count+1
for i in range(1,n+1):
    if n%i==0:
        count1=count1+1
if count==2 and count1==2 and n-m==2:
    print("Twin Numbers")
else:
    print("Single Number")
        
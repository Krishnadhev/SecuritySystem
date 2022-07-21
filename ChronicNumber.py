n=int(input("Enter a number to find the chronic numbers of it: "))
flag=0
for i in range(1,n+1):
    if i*(i+1)==n and i*(i+1)<=n:
        flag=1
        break
if flag==1:
    print("Chronic number")
else:
    print("Not a Chronic number")
        
        
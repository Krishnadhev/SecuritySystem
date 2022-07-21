n= int(input("Enter a number: "))
negsum=0
posoddsum=0
posevensum=0
list= []
for i in range(1,n+1):
    a= int(input("Enter a number: "))
    list.append(a)
for i in list:
    if i<0:
        negsum=negsum+i
    if i>0 and i%2==1:
        posoddsum=posoddsum+i
    if i>0 and i%2==0:
        posevensum=posevensum+i
print("Sum of positive even numbers" +str(posevensum))
print("Sum of positive odd numbers" + str(posoddsum))
print("Sum of negative numbers" + str(negsum))







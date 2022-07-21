# Write a program to make a list of some random numbers and input a searching #.
# Search the number in the list and if the number exists then print search succesful else not search not succesful.
list= [7,9,-9,-7,0]
searchingnum= int(input("Enter a searching number: "))
flag=0
for i in list:
    if searchingnum==i:
        flag=1
        break
if flag==1:
    print("Search Succesful")

else:
    print("Search Unsuccesful")
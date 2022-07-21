# 1,11,111,1111
# number=0
# for i in range(1,6):
#     number=number*10+1
#     print(number)
# 5,55,555,5555
# 0.5,0.55,0.555,0.5555,0.55555
# number=0
# power=1
# for i in range(1,6):
#     number=number*10+5
#     denominator=10**power
#     power=power+1
#     print(number/denominator)

 # 1.0,1.1 , 1.11 , 1.111 ..n terms
n=int(input("Enter a value for n: "))
number=0
power=0
for i in range(1,n+1):
    number=number*10+1
    denominator=10**power
    power=power+1
    print(number/denominator)

    
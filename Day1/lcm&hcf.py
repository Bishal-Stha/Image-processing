num1 = int(input("Enter the value of number: "))
num2 = int(input("Enter the value of number: "))
hcf = 1
big = 0

if num1 >num2:
    big = num2
else:
    big = num1

for i in range(2,big+1):
    if num1%i==0 and num2%i==0:
        hcf = i

lcm = (num1*num2)//hcf
print(hcf)
print(lcm)
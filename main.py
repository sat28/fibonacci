# fibonacci series - 0 1 1 2 3 5 8 11 .......
# until 100
num1, num2 = 0, 1
# for(i=2; i<=100;i++)
print(num1, num2)
for i in range(2, 101):
    num3 = num1 + num2
    num1 = num2 
    num2 = num3 # 1 -> 1
    print(num3)



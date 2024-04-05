# Jordan Ash

# 4/4/2024

# P4LAB2

# Output Range with increment of 5 

num1 = int(input())
num2 = int(input())

if num2 < num1:
    print("Second integer can't be less than the first.")
else:
    print(num1, end=' ')

    while num1 + 5 <= num2:
        num1 += 5
        print(num1, end=' ')
print()


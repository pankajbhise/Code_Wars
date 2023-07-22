# Question 2

# Example 1:
num = 56
sum = 0
rev = 0


while num != 0:
    num1 = num%10
    sum = sum + num1
    num = num//10

print("Sum of digits is:", sum)
    

temp = sum
while sum > 0:

    digit = sum%10
    rev = (rev*10)+digit
    sum = sum//10

if(temp == rev):
    print("1")
else:
    print("0")




# Example 2:
num = 98
sum = 0
rev = 0


while num != 0:
    num1 = num%10
    sum = sum + num1
    num = num//10

print("Sum of digits is:", sum)
    
    
temp = sum
while sum > 0:

    digit = sum%10
    rev = (rev*10)+digit
    sum = sum//10

if(temp == rev):
    print("1")
else:
    print("0")

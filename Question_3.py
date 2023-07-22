# Question 3

# Example 1:
num = 555
rev = 0
temp = num
while num > 0:
    digit = num%10
    rev = (rev*10)+digit
    num = num//10

if(temp == rev):
    print("Yes it is palindrome number")
else:
    print("No it is not a palindrome number")



# Example 2:
num = 123
rev = 0
temp = num
while num > 0:
    digit = num%10
    rev = (rev*10)+digit
    num = num//10

if(temp == rev):
    print("Yes it is palindrome number")
else:
    print("No it is not a palindrome number")
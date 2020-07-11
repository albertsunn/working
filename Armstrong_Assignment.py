number = input("Enter an integer number :")

while number.isdigit() == False :
    number = input("Don't use non-numeric, float, or negative values!. Enter again :")
    
number = int(number)
number1 = int(number)
wrt = str(number)
n = len(wrt)
i = 0
sum = 0
while i < n :
    a = number // 10 ** (n-1)
    number = number % 10 ** (n-1)
    sum += a ** len(wrt)
    n -= 1
if sum == number1:
    print(number1, "is an Armstrong number")
else :
    print(number1, "is NOT an Armstrong number")

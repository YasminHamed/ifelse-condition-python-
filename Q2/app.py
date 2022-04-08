# Python program to find the largest number among the three input numbers

#Enter three numbers to find the largest of them
firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
thirdNumber = float(input("Enter third number: "))
 
#Finding the largest number by if else condition
if firstNumber > secondNumber and firstNumber > thirdNumber:
   largest = firstNumber
elif secondNumber > firstNumber and secondNumber > thirdNumber:
   largest = secondNumber
else:
   largest = thirdNumber

#final result(the largest number)
print("The largest number is",int(largest))
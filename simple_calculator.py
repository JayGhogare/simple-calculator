print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor")
print("6. Modulus")
print("7. Exponent")

Choice = int(input(" Enter your Choice :"))
Num1 = int(input("Enter 1st Number :"))
Num2 = int(input("Enter 2nd Number :"))

Addition = ( Num1 + Num2)
Substraction = ( Num1 - Num2)
Multiplication = ( Num1 * Num2)
Divison = ( Num1 / Num2)
Floor = ( Num1 // Num2)
Modulus = ( Num1 % Num2)
Exponent = ( Num1 ** Num2)
if Num2 == 0 :
    print("Cannot divide by zero")
if Choice == 1 :
    print("Result =", Addition)
elif Choice == 2 :
    print("Result =", Substraction)
elif Choice == 3 :
    print("Result =", Multiplication)
elif Choice == 4 :
    print("Result =", Divison)
elif Choice == 5 :
    print("Result =", Floor) 
elif Choice == 6 :
    print("Result =", Modulus)   
elif Choice == 7 :
    print("Result =", Exponent)
else :
    print("Invalid Choice")    
#1. Positive, Negative or Zero

n = int(input("Enter number: "))

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#2. Even or Odd

n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#3. Greatest of Two Numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("A is greatest")
else:
    print("B is greatest")

#4. Greatest of Three Numbers

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a > b and a > c:
    print("A is greatest")
elif b > c:
    print("B is greatest")
else:
    print("C is greatest")

#5. Eligible for Voting

age = int(input("Enter age: "))

if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

#6. Leap Year

year = int(input("Enter year: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not leap year")

#7. Vowel or Consonant

ch = input("Enter character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")

#8. Divisible by 5 and 11

n = int(input("Enter number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible")
else:
    print("Not divisible")

#9. Multiple of 3 and 7

n = int(input("Enter number: "))

if n % 3 == 0 and n % 7 == 0:
    print("Multiple of 3 and 7")
else:
    print("Not multiple")

#10. Grade Based on Marks

marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

#11. Uppercase or Lowercase

ch = input("Enter character: ")

if ch.isupper():
    print("Uppercase")
else:
    print("Lowercase")

#12. Alphabet is Vowel

ch = input("Enter alphabet: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Not vowel")

#13. Triangle Formation

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if a+b > c and a+c > b and b+c > a:
    print("Triangle can form")
else:
    print("Triangle cannot form")

#14. Type of Triangle

a = int(input("Enter side A: "))
b = int(input("Enter side B: "))
c = int(input("Enter side C: "))

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

#15. Largest Among Four Numbers

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))
d = int(input("Enter D: "))

if a >= b and a >= c and a >= d:
    print("A is greatest")
elif b >= c and b >= d:
    print("B is greatest")
elif c >= d:
    print("C is greatest")
else:
    print("D is greatest")

#16. Three-Digit Number

n = int(input("Enter number: "))

if 100 <= abs(n) <= 999:
    print("Three digit number")
else:
    print("Not three digit")

#17. Electricity Bill


units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
else:
    bill = units * 10

print("Bill =", bill)

#18. Income Tax

income = int(input("Enter income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
else:
    tax = income * 0.10

print("Tax =", tax)

#19. Student Pass or Fail

m1 = int(input("Enter subject 1 marks: "))
m2 = int(input("Enter subject 2 marks: "))
m3 = int(input("Enter subject 3 marks: "))

if m1 >= 35 and m2 >= 35 and m3 >= 35:
    print("Pass")
else:
    print("Fail")

#20. Number Within Range

n = int(input("Enter number: "))

if 10 <= n <= 50:
    print("Within range")
else:
    print("Out of range")

#21. Simple Calculator

a = int(input("Enter A: "))
b = int(input("Enter B: "))
op = input("Enter operator (+,-,*,/): ")

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    if b != 0:
        print(a/b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")

#22. Century Leap Year

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Century leap year")
elif year % 100 == 0:
    print("Century year")
else:
    print("Not a century year")

#23. Season Based on Month

m = int(input("Enter month number: "))

if m in [3, 4, 5, 6]:
    print("Summer")
elif m in [7, 8, 9, 10]:
    print("Rainy")
elif m in [11, 12, 1, 2]:
    print("Winter")
else:
    print("Invalid month")

#24. Number of Days in a Month

m = int(input("Enter month: "))

if m == 2:
    print("28 or 29 days")
elif m in [4, 6, 9, 11]:
    print("30 days")
elif 1 <= m <= 12:
    print("31 days")
else:
    print("Invalid month")

#25. Password Validation

password = input("Enter password: ")

if len(password) >= 8 and any(ch.isdigit() for ch in password):
    print("Valid password")
else:
    print("Invalid password")

#26. Ticket Price Based on Age


age = int(input("Enter age: "))

if age < 5:
    print("Free ticket")
elif age <= 18:
    print("Ticket Rs. 50")
else:
    print("Ticket Rs. 100")

#27. Discount Based on Purchase

amount = int(input("Enter purchase amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 2000:
    discount = amount * 0.10
else:
    discount = 0

print("Discount =", discount)
print("Final amount =", amount-discount)

#28. Driving License Eligibility

age = int(input("Enter age: "))
eye = input("Eyesight normal? (yes/no): ")

if age >= 18 and eye == "yes":
    print("Eligible")
else:
    print("Not eligible")

#29. Login System

username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful")
else:
    print("Invalid username or password")

#30. Menu-Driven Calculator

while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 5:
        print("Exit")
        break

    a = int(input("Enter A: "))
    b = int(input("Enter B: "))

    if ch == 1:
        print("Result =", a+b)
    elif ch == 2:
        print("Result =", a-b)
    elif ch == 3:
        print("Result =", a*b)
    elif ch == 4:
        if b != 0:
            print("Result =", a/b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

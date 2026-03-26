# Basic if
age = 20
if age >= 18:
    print("Eligible to vote")

print("-----")

# if-else
marks = 40
if marks >= 50:
    print("Pass")
else:
    print("Fail")

print("-----")

# if-elif-else
score = 75
if score >= 90:
    print("Grade A")
elif score >= 70:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Fail")

print("-----")

# Logical operators
temp = 28
is_raining = False

if temp > 25 and not is_raining:
    print("Go outside")

if temp > 35 or is_raining:
    print("Stay inside")

print("-----")

# String condition
user = "admin"

if user == "admin":
    print("Welcome Admin")
else:
    print("Access Denied")
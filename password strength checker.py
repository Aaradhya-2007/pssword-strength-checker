password = input("Enter your password: ")

length = len(password)
has_upper = False
has_lower = False
has_digit = False
has_special = False
score = 0 

if length < 6:
    print("password is too short")
elif length <= 10:
    print("password is okay")
else:
    print("Your password is long")

for x in password:
    if x.isupper():
        has_upper = True
    elif x.islower():
        has_lower = True
    elif x.isdigit():
        has_digit = True
    else:
        has_special = True


print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Digit:", has_digit)
print("Special:", has_special)

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score <= 2:
    print("Password strength: Weak")
elif score <= 4:
    print("Password strength: Medium")
else:
    print("Password strength: Strong")


print("your password is", password)

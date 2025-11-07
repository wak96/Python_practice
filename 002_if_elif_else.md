# 🧠 Python if, elif, else Examples (বাংলা ব্যাখ্যাসহ)

## 🧩 উদাহরণ–১: ধনাত্মক, ঋণাত্মক, না শূন্য সংখ্যা

```python
num = int(input("Enter a number: "))

if num > 0:
    print("ধনাত্মক সংখ্যা")
elif num < 0:
    print("ঋণাত্মক সংখ্যা")
else:
    print("শূন্য")
```

🔹 **ব্যাখ্যা:**
`if` শর্ত প্রথমে পরীক্ষা করে — তারপর না মিলে গেলে `elif`, সবশেষে `else`।


## 🧩 উদাহরণ–২: বয়স অনুযায়ী ক্যাটাগরি নির্ধারণ

```python
age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")
```

🔹 **ব্যাখ্যা:**
এখানে বয়সের রেঞ্জ অনুযায়ী ভিন্ন আউটপুট দেওয়া হচ্ছে।

---

## 🧩 উদাহরণ–৩: পরীক্ষার ফলাফল (Grade System)

```python
marks = int(input("Enter marks: "))

if marks >= 80:
    print("A+")
elif marks >= 70:
    print("A")
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print("B")
elif marks >= 40:
    print("C")
else:
    print("Fail")
```

🔹 **ব্যাখ্যা:**
এইভাবে `elif` ব্যবহার করে **multiple conditions** চেক করা যায়।

---

## 🧩 উদাহরণ–৪: সংখ্যা জোড় না বিজোড়

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

🔹 **ব্যাখ্যা:**
সংখ্যাটি ২ দিয়ে ভাগ করলে ভাগশেষ ০ হলে সেটি জোড়, নইলে বিজোড়।

---

## 🧩 উদাহরণ–৫: সবচেয়ে বড় সংখ্যা বের করা

```python
a = 15
b = 20
c = 10

if a > b and a > c:
    print("A সবচেয়ে বড়")
elif b > a and b > c:
    print("B সবচেয়ে বড়")
else:
    print("C সবচেয়ে বড়")
```

🔹 **ব্যাখ্যা:**
এখানে `and` ব্যবহার করা হয়েছে একাধিক শর্ত একসাথে পরীক্ষা করতে।

---

## 🧩 উদাহরণ–৬: লগইন চেক

```python
username = "kawsar"
password = "1234"

user_input = input("Username: ")
pass_input = input("Password: ")

if user_input == username and pass_input == password:
    print("Login successful ✅")
elif user_input == username:
    print("Password ভুল ❌")
else:
    print("Username ভুল ❌")
```

🔹 **ব্যাখ্যা:**
লগইন সফল হবে তখনই, যখন ইউজারনেম এবং পাসওয়ার্ড দুটোই মিলে যায়।

---

## 🧩 উদাহরণ–৭: তাপমাত্রা অনুযায়ী বার্তা

```python
temp = float(input("Enter temperature in Celsius: "))

if temp >= 35:
    print("খুব গরম দিন ☀️")
elif temp >= 25:
    print("মনোরম আবহাওয়া 🌤️")
elif temp >= 15:
    print("সামান্য ঠান্ডা 🌥️")
else:
    print("খুব ঠান্ডা 🥶")
```

🔹 **ব্যাখ্যা:**
তাপমাত্রার উপর নির্ভর করে বার্তা পরিবর্তন হচ্ছে।

---

## 🧩 উদাহরণ–৮: বছর লিপ ইয়ার কিনা

```python
year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")
```

🔹 **ব্যাখ্যা:**
লিপ ইয়ার নির্ধারণে `elif` দরকার কারণ শর্তগুলো ধারাবাহিকভাবে যাচাই করতে হয়।

---

## 🧩 উদাহরণ–৯: গাড়ির স্পিড চেক

```python
speed = int(input("Enter car speed: "))

if speed > 120:
    print("Too Fast! Fine imposed 🚓")
elif speed >= 80:
    print("Fast but acceptable 🚗")
elif speed >= 40:
    print("Normal speed 🚙")
else:
    print("Too slow 🐢")
```

🔹 **ব্যাখ্যা:**
স্পিডের রেঞ্জ অনুযায়ী সতর্কবার্তা দেখায়।

---

## 🧩 উদাহরণ–১০: Nested if (if এর ভিতরে if)

```python
age = int(input("Enter your age: "))
citizen = input("Are you a citizen? (yes/no): ")

if age >= 18:
    if citizen == "yes":
        print("You can vote ✅")
    else:
        print("You are not a citizen ❌")
else:
    print("You are under 18 ❌")
```

🔹 **ব্যাখ্যা:**
একটি `if` ব্লকের ভিতরে আরেকটি `if` — একে বলে **nested if**।


---

# 🧠 Python if–elif–else Examples (Part–2)

## 🧩 উদাহরণ–১১: Discount Calculation
```python
price = float(input("Enter total price: "))

if price >= 1000:
    discount = price * 0.20
elif price >= 500:
    discount = price * 0.10
else:
    discount = price * 0.05

print("Discount:", discount)
print("Final Price:", price - discount)
```

**ব্যাখ্যা:** ক্রয়ের পরিমাণ অনুযায়ী ডিসকাউন্ট নির্ধারণ।


## 🧩 উদাহরণ–১২: Password Strength Checker

```python
password = input("Enter password: ")

if len(password) >= 12:
    print("Strong Password 💪")
elif len(password) >= 8:
    print("Moderate Password 😐")
else:
    print("Weak Password ⚠️")
```

**ব্যাখ্যা:** পাসওয়ার্ডের দৈর্ঘ্যের ওপর ভিত্তি করে স্ট্রেংথ দেখায়।

---

## 🧩 উদাহরণ–১৩: Student Attendance Check

```python
attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:
    print("Allowed for exam ✅")
else:
    print("Not allowed ❌")
```

**ব্যাখ্যা:** উপস্থিতি ৭৫% এর কম হলে পরীক্ষায় অংশ নেওয়া যাবে না।

---

## 🧩 উদাহরণ–১৪: Electricity Bill Calculator

```python
unit = int(input("Enter electricity units: "))

if unit <= 100:
    bill = unit * 5
elif unit <= 300:
    bill = unit * 7
else:
    bill = unit * 10

print("Total Bill:", bill, "Tk")
```

**ব্যাখ্যা:** ইউনিট বাড়লে রেটও বাড়ে।

---

## 🧩 উদাহরণ–১৫: Month Name from Number

```python
month = int(input("Enter month number (1-12): "))

if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
else:
    print("Other Month")
```

**ব্যাখ্যা:** সংখ্যার মাধ্যমে মাস নির্ধারণ।

---

## 🧩 উদাহরণ–১৬: BMI Category

```python
bmi = float(input("Enter BMI value: "))

if bmi < 18.5:
    print("Underweight")
elif bmi < 24.9:
    print("Normal")
elif bmi < 29.9:
    print("Overweight")
else:
    print("Obese")
```

**ব্যাখ্যা:** BMI মান অনুযায়ী শারীরিক অবস্থা।

---

## 🧩 উদাহরণ–১৭: Simple Calculator

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == '+':
    print("Result:", a + b)
elif op == '-':
    print("Result:", a - b)
elif op == '*':
    print("Result:", a * b)
elif op == '/':
    print("Result:", a / b)
else:
    print("Invalid operator ❌")
```

**ব্যাখ্যা:** ব্যবহারকারীর ইনপুট অনুযায়ী গাণিতিক কাজ সম্পন্ন করে।

---

## 🧩 উদাহরণ–১৮: Exam Result with Bonus

```python
marks = int(input("Enter marks: "))
bonus = input("Got bonus marks? (yes/no): ")

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
else:
    grade = "C"

if bonus == "yes":
    print("Final Grade:", grade, "+ Bonus 🎁")
else:
    print("Final Grade:", grade)
```

**ব্যাখ্যা:** মূল গ্রেডের সঙ্গে বোনাস থাকলে আলাদা বার্তা দেয়।

---

python
ch = str(input("Enter any keyword: "))

## 🧩 উদাহরণ–১৯: Check if any vowel exists inside the word
ch = input("Enter any word: ")
vowels = ["a", "e", "i", "o", "u"]
found = False

for v in vowels:
    if v in ch.lower():
        found = True
        break
if found:
    print("There is vowels")
else:
    print("No vowels found")

or

ch = str(input("Enter any keyword: "))

if any(vowel in ch.lower() for vowel in "aeiou"):
    print("It's vowel")
else:
    print("It's not")

# it cheecks only words
# used lower() function
ch = str(input("Enter any keyword: "))

if ch.lower() in "aeiou":
    print("It's vowil")
else:
    print("It's not")

#used upper()function

ch = input("Enter any keyword: ")

if ch.upper() in "aeiou":
    print("It's vowel")
else:
    print("It's not")



## 🧩 উদাহরণ–২০: সংখ্যা ৩ দিয়ে ও ৫ দিয়ে বিভাজ্য কিনা

```python
num = 15

if num % 3 == 0 and num % 5 == 0:
    print("৩ এবং ৫ দুটো দিয়েই বিভাজ্য ✅")
elif num % 3 == 0:
    print("শুধু ৩ দিয়ে বিভাজ্য")
elif num % 5 == 0:
    print("শুধু ৫ দিয়ে বিভাজ্য")
else:
    print("কোনোটাতেই নয় ❌")
```

## 🧩 উদাহরণ–২১: ব্যবহারকারীর স্কোর অনুযায়ী লেভেল নির্ধারণ

```python
score = 450

if score >= 1000:
    level = "Pro Gamer"
elif score >= 500:
    level = "Intermediate"
elif score >= 100:
    level = "Beginner"
else:
    level = "Newbie"

print("Your level:", level)
print(f"your level: {level}")
```

---

## 🧩 উদাহরণ–২২: লগইন + এক্সেস লেভেল (Nested)

```python
username = "admin"
password = "1234"
access = "super"

if username == "admin" and password == "1234":
    if access == "super":
        print("Super Access Granted ✅")
    else:
        print("Limited Access 🔐")
else:
    print("Login Failed ❌")
```

---

## 🧩 উদাহরণ–২৩: শর্ট হ্যান্ড if-else চেইন

```python
marks = 85
grade = "A+" if marks >= 80 else "A" if marks >= 70 else "F"
print("Grade:", grade)
```

---

## 🧩 উদাহরণ–২৪: বয়স অনুযায়ী টিকেটের দাম (Nested)

```python
age = 10

if age < 5:
    price = 0
elif age < 18:
    price = 50
elif age < 60:
    price = 100
else:
    price = 70

print("টিকেটের দাম:", price, "৳")
```

---

## 🧩 উদাহরণ–২৫: পাসওয়ার্ডের দৈর্ঘ্য চেক

```python
password = "pass123"

if len(password) < 6:
    print("Password খুব ছোটো ❌")
elif len(password) <= 10:
    print("Password ঠিক আছে ✅")
else:
    print("Password খুব বড় 📏")
```

---

## 🧩 উদাহরণ–২৬: তিনটি কন্ডিশনে Nested Decision

```python
age = 25
citizen = True
criminal = False

if age >= 18:
    if citizen:
        if not criminal:
            print("তুমি ভোট দিতে পারবে ✅")
        else:
            print("তোমার অপরাধ রেকর্ড আছে ❌")
    else:
        print("তুমি নাগরিক নও ❌")
else:
    print("অপ্রাপ্তবয়স্ক ❌")
```

---

## 🧩 উদাহরণ–২৭: সময় অনুযায়ী শুভেচ্ছা বার্তা

```python
hour = 14  # ২৪ ঘণ্টা ফরম্যাট

if 0 <= hour < 12:
    print("শুভ সকাল ☀️")
elif 12 <= hour < 18:
    print("শুভ বিকেল 🌤️")
else:
    print("শুভ রাত্রি 🌙")
```

---

## 🧩 উদাহরণ–২৮: শিক্ষার্থীর উপস্থিতি অনুযায়ী রেজাল্ট

```python
marks = 78
attendance = 85

if marks >= 60:
    if attendance >= 75:
        print("পাস ✅")
    else:
        print("অনুপস্থিতির কারণে ফেল ❌")
else:
    print("নম্বরের কারণে ফেল ❌")
```

---

## 🧩 উদাহরণ–২৯: ইউজারের বয়স ও সাবস্ক্রিপশন চেক (Ternary mix)

```python
age = 21
subscribed = True

message = (
    "Full Access ✅" if age >= 18 and subscribed
    else "Limited Access 🔐" if age >= 18
    else "Access Denied ❌"
)

print(message)
```

---


import random

# Question 2
number = int(input("Please enter a number "))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Question 3
name = "Nunya"
age = 22

ageAndName = name + " " + str(age)

print(name)
print(age)

print(ageAndName)


# Question 4
randomNumber = random.randint(1, 5)
guessNumber = 0

guessNumber = int(input("Enter a number: \n"))

while guessNumber != randomNumber:
    guessNumber = int(input("Try again! \n"))

print("Hey, That's absolutely right")


# Question 5
listNumbers = [1, 4, 9, 16, 25]

for i in listNumbers:
    if i % 2 == 0:
        print(i)


# Question 6
age = int(input("Enter your age: \n"))

while age < 0:
    print("Enter your age \n")
sum = 0
i = 0
# use while loop to iterate until zero
while (i < age):
    sum = sum + (i + 1)
    i = i + 1
print(sum, 'years')

print("\n")

MONTHPERYEAR = 12
DAYSPERYEAR = 365
HOURSPERYEAR = 8760

ageAsMonth = age * MONTHPERYEAR
ageAsDays = age * DAYSPERYEAR
ageAsHours = age * HOURSPERYEAR

print("Age in months: " + str(ageAsMonth) + "\n" + "Age in days: " + str(ageAsDays) + "\n" + "Age in hours: " + str(ageAsHours))

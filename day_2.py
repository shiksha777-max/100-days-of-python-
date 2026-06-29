two_digit_number = input("Type a two digit number: ")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

#add two integers together
result = int(first_digit) + int(second_digit)
print(result)


#Body mass index calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2  
print(int(bmi))


age = input("What is your current age? ")
years_remaining = 90 - int(age)
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")


#Tip calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))      
tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people
print(f"Each person should pay: ${bill_per_person:.2f}")



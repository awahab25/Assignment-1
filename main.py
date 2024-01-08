 # Ans 1

# user_salary = int(input("Enter your Salary"))
# service_time = int(input("How many years did you serve?"))
# bonus = (user_salary * 5)/100
# if service_time>5:
#     user_salary += bonus
#     print("Your bonus is" , user_salary)
# else:
#     print("No bonus for you")


#  Ans 2
    
# user_age = int(input("Enter your age"))
# if user_age > 17:
#     print("You are eligible for Voting")
# else:
#     print("You are no Eligible for voting")


# Ans 3

# user_number = int(input("Enter the Number"))
# if user_number%2 == 0:
#     print("Even")
# else:
#     print("Odd")


# Ans 4

# user_number = int(input("Enter the Number"))
# if user_number%7 == 0:
#     print(user_number, "is divisible")
# else:
#     print(user_number, "is not divisible")


# Ans 5

# user_number = int(input("Enter the Number"))
# if user_number/5 == 0:
#     print("Hello")
# else:
#     print("BYE")


# Ans 6

# def calculate_electricity_bill(units):
#     if units <= 100:
#         total_bill = 0
#     elif units <= 300:
#         total_bill = (units - 100) * 5
#     else:
#         total_bill = (200 * 5) + (units - 300) * 10

#     return total_bill

# # Accepting input from the user
# units = int(input("Enter the number of units consumed: "))

# # Calculating the electricity bill
# bill_amount = calculate_electricity_bill(units)

# # Displaying the result
# print(f"Total bill amount for {units} units is Rs.{bill_amount}")


# Ans 7

# number = int(input("Enter a number: "))
# last_digit = number % 10
# print("The last digit of the number is:",last_digit)


# Ans 8

# num_div_3 = int(input("Enter a number"))
# last_digit=num_div_3%10
# if last_digit % 3 == 0:
#     print("The last digit is divisible by 3.")
# else:
#     print("The last digit is not divisible by 3.")


# Ans 9

# length = float(input("Enter the length of the rectangle: "))
# breadth = float(input("Enter the breadth of the rectangle: "))

# if length == breadth:
#     print("It is a square.")
# else:
#     print("It is a rectangle.")


# Ans 10
# value1 = int(input("Enter First Number"))
# value2 = int(input("Enter Second Number"))
# if value1>value2:
#     print(value1)
# else:
#     print(value2)


# Ans 11

# quantity = int(input("Enter the quantity: "))
# unit_cost = 100
# total_cost = quantity * unit_cost

# if total_cost > 1000:
#     discount = 0.10 * total_cost
#     total_cost -= discount

# print("The total cost for the user is ",total_cost)


# Ans 12
# user_marks = float(input("Enter Your Marks:"))
# if user_marks <=25: Grade="F"
# elif user_marks > 25 and user_marks<=45: Grade="E"
# elif user_marks > 46 and user_marks<=50: Grade="D"
# elif user_marks > 51 and user_marks<=60: Grade="C"
# elif user_marks > 61 and user_marks<=80: Grade="B"
# else: Grade= "A"
# print("Your Grade is",Grade)


# Ans 13

# age1 = int(input("Enter age of person 1: "))
# age2 = int(input("Enter age of person 2: "))
# age3 = int(input("Enter age of person 3: "))
# if age1 >= age2 and age1 >= age3:
#     oldest = age1
# elif age2 >= age1 and age2 >= age3:
#     oldest = age2
# else:
#     oldest = age3

# if age1 <= age2 and age1 <= age3:
#     youngest = age1
# elif age2 <= age1 and age2 <= age3:
#     youngest = age2
# else:
#     youngest = age3

# print("Oldest person's age:",oldest)
# print("Youngest person's age:",youngest)
 

# Ans 14

# classes_held = int(input("Enter the number of classes held: "))
# classes_attended = int(input("Enter the number of classes attended: "))
# attendance_percentage = (classes_attended / classes_held) * 100
# if attendance_percentage >= 75:
#     print("Percentage of classes attended",attendance_percentage)
#     print("Student is allowed to sit in the exam.")
# else:
#     print("Student is not allowed to sit in the exam.Bcz it's attendace is less than 75%.")


# Ans 15

# class_held = int(input("Enter the number of classes held: "))
# class_attended = int(input("Enter the number of classes attended: "))
# medical_cause =int(input("How many class you leave due to medical issue:"))
# attendance_percentage =(((class_attended+medical_cause)/class_held)*100)
# if attendance_percentage >= 75:
#     print("Percentage of classes attended:",attendance_percentage)
#     print("Student is allowed to sit in the exam.")
# else:
#     print("Percentage of classes attended:",attendance_percentage)
#     print("Student is not allowed to sit in the exam.") 

# Ans 16

# year = int(input("Enter a year: "))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year," is a leap year.")
# else:
#     print( year,"is not a leap year.")

# Ans 17

# age = int(input("Enter age:"))
# gender = input("Enter gender (M/F):").upper()
# marital_status = input("Enter marital status (Y/N):").upper
# if gender == 'F':
#     print("She will work only in urban areas.")
# elif gender == 'M' and 20 <= age <= 40:
#     print("He may work anywhere.")
# elif gender == 'M' and 40 <= age <= 60:
#     print("He will work in urban areas only.")
# else:
#     print("Error!")
    
    

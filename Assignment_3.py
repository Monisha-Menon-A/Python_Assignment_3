# 1) Program to find month of the year
# def main():
#     months = [
#         "January", "February", "March", "April", "May", "June", 
#         "July", "August", "September", "October", "November", "December"
#     ]
    
#     try:
#         month_number = int(input("Enter the month: "))
        
#         if 1 <= month_number <= 12:
#             print(f"Month {month_number} is {months[month_number - 1]}.")
    
#     except ValueError:
#         print("Error: Invalid input. Please enter an integer.")

# if __name__ == "__main__":
#     main()

# 2) Calculate ticket price
# def calculate_ticket_price():
#     full_price = 6.0
    
#     try:
#         age = int(input("Enter your age: "))
        
#         if age < 16:
#             ticket_price = full_price / 2  
#         elif age >= 60:
#             ticket_price = full_price / 3  
#         else:
#             ticket_price = full_price 
        
#         print(f"Your ticket costs £{ticket_price:.2f}.")
    
#     except ValueError:
#         print("Error: Please enter a valid integer for your age.")

# if __name__ == "__main__":
#     calculate_ticket_price()


# 3) Calculate BMI
# def calculate_bmi():
#     try:
#         weight = float(input("Enter your weight in (kg): "))
#         height = float(input("Enter your height in (m): "))
        
#         if weight <= 0 or height <= 0:
#             print("Error: Weight and height must be positive numbers.")
#             return
        
#         bmi = weight / (height ** 2)
        
#         if bmi < 18.5:
#             status = "Underweight"
#         elif 18.5 <= bmi <= 24.9:
#             status = "Normal"
#         elif 25 <= bmi <= 29.9:
#             status = "Overweight"
#         else:
#             status = "Obese"
        
#         print(f"Your BMI is {bmi:.2f}. You are in the {status} range.")
    
#     except ValueError:
#         print("Error: Please enter valid numeric values for weight and height.")

# if __name__ == "__main__":
#     calculate_bmi()

# 4) Find the greatest number
# def find_greatest():
#     try:
#         num1 = float(input("Enter the first number: "))
#         num2 = float(input("Enter the second number: "))
#         num3 = float(input("Enter the third number: "))
        
#         if num1 >= num2 and num1 >= num3:
#             greatest = num1
#         elif num2 >= num1 and num2 >= num3:
#             greatest = num2
#         else:
#             greatest = num3
        
#         print(f"The greatest number is {greatest}.")
    
#     except ValueError:
#         print("Error: Please enter valid numbers.")

# if __name__ == "__main__":
#     find_greatest()


# 5) Find factorial
# def calculate_factorial():
#     try:
#         num = int(input("Enter a number: "))
        
#         factorial = 1
        
#         for i in range(1, num + 1):
#             factorial *= i
        
#         print(f"The factorial of {num} is {factorial}.")
    
#     except ValueError:
#         print("Error: Please enter a valid integer.")

# if __name__ == "__main__":
#     calculate_factorial()


# 6) Reverse the number
# def reverse_number():
#     try:
#         num = int(input("Enter an integer: "))
        
#         reversed_num = 0

#         while num > 0:
#             digit = num % 10 
#             reversed_num = reversed_num * 10 + digit  
#             num = num // 10  
        
#         print(f"The reversed number is {reversed_num}.")
    
#     except ValueError:
#         print("Error: Please enter a valid integer.")

# if __name__ == "__main__":
#     reverse_number()


# 7) Find multiples
# def find_multiples():
#     try:
#         num = int(input("Enter a number: "))
#         limit = 50
        
#         print(f"Multiples of {num} are:")
        
#         for i in range(1, limit + 1):
#             multiple = num * i
#             if multiple > limit:
#                 break
#             print(multiple, end=" ")
#         print()  
    
#     except ValueError:
#         print("Error: Please enter valid positive integers.")

# if __name__ == "__main__":
#     find_multiples()

# 8) Print the inputted value as it is 
# def echo_until_done():
#     while True:
#         user_input = input("Enter a value: ")
        
#         if user_input == 'done':
#             print("Exiting the loop")
#             break
        
#         print(f"You entered: {user_input}")

# if __name__ == "__main__":
#     echo_until_done()

# 9) Print Fizz and Buzz
# def fizz_buzz():
#     for num in range(1, 11):
#         if num % 3 == 0 and num % 5 == 0:
#             print("FizzBuzz")
#         elif num % 3 == 0:
#             print("Fizz")
#         elif num % 5 == 0:
#             print("Buzz")
#         else:
#             print(num)

# if __name__ == "__main__":
#     fizz_buzz()

# 10) Print pattern
def print_pattern():
    for i in range(5, 0, -1): 
        for j in range(i, 0, -1):  
            print(j, end=" ")  
        print() 

if __name__ == "__main__":
    print_pattern()























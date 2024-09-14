#  Ask the user for their birth year and calculate their age.
##################Basic Approach#################



# Birth_Year = int(input("Enter the birth your"))

# current_year = datetime.now().year

# year = current_year - Birth_Year

# print(f"Your Age {year} old")

# print(current_year)

#################Function Approach##############
# def calculate_age(Birth_Year):

#   current_year = datetime.now().year

#   age = current_year - Birth_Year
#   return age

# Birth_Year = int(input("Enter the Birth Year"))

# age =  calculate_age(Birth_Year)
# print(f"Age::{age}year old")

#######################Handling Invalid Value########################
# from datetime import datetime
# def get_user_value():
#   while True:
#     try:
#       Birth_Year = int(input("Enter birth year"))
#       if Birth_Year>datetime.now().year:
#         print("Birth day cannot given future,Please Enter the year correct")
#       else :
#         return Birth_Year
#     except ValueError:
#       print("Invalid Input please enter valid numeric number")

         
# def calculate_age(Birth_Year):

#   current_year = datetime.now().year

#   age1 = current_year - Birth_Year
#   return age1

# Birth_Year  = get_user_value()
# age1 = calculate_age(Birth_Year)
# print(f"Age{age1}year old")

##################Comprehensive Exception Handling####################
import logging
from datetime import datetime

# Logging setup
logging.basicConfig(
    filename='atm.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

def insert_card():
    try:
        card_inserted = input("Please insert your card (yes/no): ")
        if card_inserted.lower() != 'yes':
            raise ValueError("Your card was not accepted.")
        logging.info("Your card was accepted.")
        return True
    except ValueError as e:
        logging.error(f"Error: {e}")
        print("Your card was not accepted. Please try again or use another card.")
        return False

def enter_pin():
    try:
        pin = input("Please enter your ATM pin: ")
        if pin != "1234":  # Assuming the correct pin is "1234"
            raise ValueError("Incorrect pin entered.")
        logging.info("Correct pin entered.")
        return True
    except ValueError as e:
        logging.error(f"Error: {e}")
        print("You entered an incorrect pin. Please try again.")
        return False

def enter_amount():
    try:
        amount = int(input("Please enter the amount: "))
        available_cash = 9000  # Assuming the ATM has 9000 rupees available
        if amount > available_cash:
            raise ValueError("Insufficient cash available.")
        logging.info("Amount accepted.")
        return amount
    except ValueError as e:
        logging.error(f"Error: {e}")
        print("Sufficient balance not available. Please enter a lower amount.")
        return 0
    except Exception as e:
        logging.error(f"Error: {e}")
        print("Invalid input, please enter a valid number.")
        return 0

def withdraw_amount(amount):
    try:
        if amount == 0:
            raise ValueError("Amount issue.")
        logging.info(f"{amount} rupees debited.")
        print(f"You have withdrawn {amount} rupees.")
    except ValueError as e:
        logging.critical(f"Error: {e}")
        print("Due to a technical issue, you could not withdraw money. Please use another ATM.")

# Start the process
if insert_card():
    if enter_pin():
        amount = enter_amount()
        withdraw_amount(amount)

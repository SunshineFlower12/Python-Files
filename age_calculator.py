import os
import platform

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

while True:
    clear_screen()
    print("🧮 Age in Months, Days, and Weeks Calculator")
    print("Enter 'q' to exit.\n")

    user_input = input("Enter your age in years: ").strip()

    if user_input.lower() == 'q':
        break

    if not user_input.isdigit() or int(user_input) <= 0:
        print("\nInvalid input. Please enter a positive number.")
        input("Press Enter to try again...")
        continue

    age = int(user_input)
    months = age * 12
    days = age * 365
    weeks = days // 7

    print("\nYou have lived approximately:")
    print(f"- {months} months")
    print(f"- {days} days")
    print(f"- {weeks} weeks")

    input("\nPress Enter to continue...")

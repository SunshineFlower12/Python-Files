import os
import platform

def clear_screen():
    """Clears the terminal screen based on the operating system."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def calculate_age_metrics(age_years):
    """Calculate months, days, and weeks for the given age in years."""
    months = age_years * 12
    days = age_years * 365.25  # Account for leap years by using an approximation
    weeks = days // 7
    return months, days, weeks

def get_age_input():
    """Prompt the user for their age and validate the input."""
    while True:
        user_input = input("Enter your age in years (or 'q' to exit): ").strip()

        if user_input.lower() == 'q':
            return None

        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        
        print("\nInvalid input. Please enter a valid positive number or 'q' to exit.")
        continue

def main():
    """Main function to run the age calculator program."""
    while True:
        clear_screen()
        print("🧮 Age in Months, Days, and Weeks Calculator")
        
        age = get_age_input()
        
        if age is None:
            print("Goodbye! 👋")
            break
        
        months, days, weeks = calculate_age_metrics(age)

        print(f"\nYou have lived approximately:")
        print(f"- {months} months")
        print(f"- {days:.0f} days")  # Rounded to a whole number for better UX
        print(f"- {weeks:.0f} weeks")  # Rounded to a whole number for better UX
        
        input("\nPress Enter to calculate again, or type 'q' to exit.")

if __name__ == "__main__":
    main()

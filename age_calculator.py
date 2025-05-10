import os
import platform

# Function to clear the screen based on the OS
def clear_screen():
    """Clear the terminal screen based on the operating system."""
    os.system('cls' if platform.system() == 'Windows' else 'clear')

# Function to calculate age metrics
def calculate_age_metrics(age_years):
    """Calculate months, days, and weeks for the given age in years."""
    months = age_years * 12
    days = age_years * 365.25  # Account for leap years
    weeks = days // 7
    return months, days, weeks

# Function to handle user input and validation
def get_age_input():
    """Prompt the user for their age and validate the input."""
    while True:
        user_input = input("Please enter your age in years (or type 'q' to exit): ").strip()

        # If the user wants to exit, return None
        if user_input.lower() == 'q':  
            return None

        # Ensure the input is a positive number
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)

        # Friendly error message for invalid input
        print("\nOops! That doesn't seem like a valid age. Please enter a positive number (e.g., 25).")
        continue

# Main function to run the age calculator
def main():
    """Main function to run the age calculator program."""
    while True:
        clear_screen()
        print("🧮 **Age Calculator** 🎉\n")
        print("Let's calculate how long you've been alive! Just enter your age in years. 😄\n")

        # Get age input from the user
        age = get_age_input()

        if age is None:  # If the user typed 'q', exit the program
            print("\nThank you for using the Age Calculator! Have a wonderful day! 👋")
            break

        # Calculate the age in months, days, and weeks
        months, days, weeks = calculate_age_metrics(age)

        # Display the results in a friendly manner
        print(f"\nYou have lived for approximately:\n")
        print(f"- {months} months")
        print(f"- {days:.0f} days")  # Rounded for clarity
        print(f"- {weeks:.0f} weeks")  # Rounded for clarity

        print("\nAmazing! Keep enjoying life! 🎉😊\n")

        # Ask the user if they want to calculate again or exit
        user_choice = input("Press Enter to calculate again, or type 'q' to exit. 🌟").strip().lower()

        if user_choice == 'q':
            print("\nThank you for using the Age Calculator! Have a wonderful day! 👋")
            break

if __name__ == "__main__":
    main()

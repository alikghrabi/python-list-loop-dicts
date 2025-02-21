# Input Gathering

salary = float(input("Enter your month salary: "))
month_input = input("Enter the name of the month: ")

# function to check the percentages
def get_percentage(name):
    while True:
        percentage = float(input(f"Enter the percentage for {name}: "))
        if 0 <= percentage <= 100:
            return percentage
        else:
            print("Percentage must be between 0 and 100. Please try again.")

percentages = {
    "savings": get_percentage("savings"),
    "rent": get_percentage("rent"),
    "electricity": get_percentage("electricity")
}

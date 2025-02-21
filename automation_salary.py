# Input Gathering

salary = float(input("Enter your month salary: "))
month_input = input("Enter the name of the month: ")

# function to check the percentages
def get_percentage(percent):
    while True:
        percentage = float(input(f"Enter the percentage for {percent}: "))
        if 0 <= percentage <= 100:
            return percentage
        else:
            print("Percentage must be between 0 and 100. Please try again.")

percentages = {
    "savings": get_percentage("savings"),
    "rent": get_percentage("rent"),
    "electricity": get_percentage("electricity")
}

# Calculations and Allocations

# Converting percentages to dollar amoamnt
savings = salary * (percentages["savings"] / 100)
electricity = salary * (percentages["electricity"] / 100)
rent = salary * (percentages["rent"] / 100)

#Giving  total amount sent from the salary during a specific month
total_allocations = savings + electricity + rent

# Subtracting the whole salary from total allocations to get how much left from the salary
remainder_salary = salary - total_allocations

# Yearly cost estimation
yearly_cost_estimation = electricity * 12 + rent * 12

# Squaring the month salary
square_salary = pow(salary, 2)

# Extra savings
extra_savings = float(input("Enter your extra saving amount: "))
if savings != 0:
    fraction = extra_savings / savings
    print(f"Fraction of extra savings: {fraction}")
else:
    print("Savings amount is zero, cannot calculate fraction.")


# Output Formatting: Summary
print(f"\nSummary for {month_input}")
print(f"Monthly Salary: ${salary:.2f}")
print(f"Savings Allocation: ${savings:.2f}")
print(f"Rent Allocation: ${rent:.2f}")
print(f"Electricity Allocation: ${electricity:.2f}")
print(f"Total Allocated : ${total_allocations:.2f}")
print(f"Remaining Salary : ${remainder_salary:.2f}")
print(f"Yearly Rent Estimate: ${rent * 12:.2f}")
print(f"Yearly Electricity Estimate: ${electricity * 12:.2f}")
print(f"Square of Monthly Salary: {square_salary:.2f}")
print(f"Fraction of Extra Savings: {fraction:.4f}")
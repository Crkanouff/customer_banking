# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input('\nEnter Savings Account Balance: '))
    savings_interest = float(input('Enter Savings Interest Rate: '))
    savings_months = int(input('Enter Savings Months: '))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("\nSavings Account Summary")
    print("Savings Account Interest Earned: $", format(interest_earned_savings, ',.2f'))
    print("Updated Savings Account Balance:  $", format(updated_savings_balance, ',.2f'))

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input('\nEnter CD Account Balance: '))
    cd_interest = float(input('Enter CD Interest Rate: '))
    cd_maturity = int(input('Enter Number of Months until CD Maturity: '))
    
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("\nCD Account Summary")
    print("CD Account Interest Earned: $", format(interest_earned_cd, ',.2f'))
    print("Updated CD Account Balance: $", format(updated_cd_balance, ',.2f'))

if __name__ == "__main__":
    # Call the main function.
    main()

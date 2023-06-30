

from ExpenseTracker.Expense import Expense


def main():
    print(f'Welcomme to Expense Tracker')
    get_user_expense()
    save_expense_to_file()
    summarize_expenses()  # Read file and summarize expenses


def get_user_expense():
    print(f'Getting User Expense')
    expesne_name = input('Enter Expense Name: ')
    # used ot convert amount into float as money is in decimal
    expense_amount = float(input('Enter Expense Amount: '))
    # used format string to print the value of variable inside the string
    print(f"You've entered {expesne_name}, {expense_amount}")

    expense_category = [
        'Food',
        'Clothing',
        'Transportation',
        'Bills',
        'Miscellaneous'
    ]

    while True:
        print('Select a category for your expense: ')
        # used to get a list of tuples with each index and value of expense_category
        for i, category in enumerate(expense_category):
            # i+1 is used to start the index from 1 instead of 0
            print(f'  {i+1}. {category}')

            # used to print the range of values the user can select
            value_length = f' [1 - {len(expense_category)}]'
            selected_index = int(
                input(f'Enter a category number {value_length}: '))
            if selected_index <= 1 and selected_index >= len(expense_category):
                print(
                    f'Please pick a category from 1 to {len(expense_category)}')
            else:
                new_expense = Expense()
                break
        break


def save_expense_to_file():
    print(f'Saving Expense to File')


def summarize_expenses():
    print(f'Summarizing Expenses')


if __name__ == "__main__":  # If this file is run directly, run main()
    main()

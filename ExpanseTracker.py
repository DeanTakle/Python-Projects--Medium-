

from Expense import Expense


def main():
    print(f'Welcomme to Expense Tracker')
    expense_file_path = 'expenses.csv'
    expenses = get_user_expense()
    save_expense_to_file(expenses, expense_file_path)  # Save to fileC
    summarize_expenses(expense_file_path)  # Read file and summarize expenses


def get_user_expense():
    print(f'Getting User Expense')
    expense_name = input('Enter Expense Name: ')
    # used to convert amount into float as money is in decimal
    expense_amount = float(input('Enter Expense Amount: '))
    # used format string to print the value of variable inside the string

    expense_category = [
        'Food',
        'Clothing',
        'Transportation',
        'Bills',
        'Miscellaneous',
    ]

    while True:
        print('Select a category for your expense: ')
        # used to get a list of tuples with each index and value of expense_category
        for i, category_name in enumerate(expense_category):
            # i+1 is used to start the index from 1 instead of 0
            print(f'  {i + 1}. {category_name}')

        # used to print the range of values the user can select
        value_length = f' [1 - {len(expense_category)}]'
        selected_index = int(
            input(f'Enter a category number {value_length}: ')) - 1

        if i in range(len(expense_category)):
            selected_category = expense_category[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print('Invalid Option, Try Again')


def save_expense_to_file(expenses: Expense, expense_file_path):
    print(f'Saving User Expense to File: {expenses} to {expense_file_path}')
    # used to append the file if it exists, f is the file object
    with open(expense_file_path, 'a') as f:
        # used to write the expense to the file. CSV means Comma Separated Values = {},{},{}\n
        f.write(f'{expenses.name}, {expenses.amount}, {expenses.category}\n')


def summarize_expenses(expense_file_path):
    print(f'Summarizing Expenses of File: {expense_file_path}')
    expenses = []
    with open(expense_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            expenses_name, expenses_amount, expenses_category = line.strip().split(
                ',')  # used to split the line and strip the whitespace
            line_expense = Expense(
                name=expenses_name, amount=expenses_amount, category=expenses_category
            )
            print(line_expense)
            # used to append the line_expense to the expenses list
            expenses.append(line_expense)
    print(expenses)


if __name__ == "__main__":  # If this file is run directly, run main()
    main()

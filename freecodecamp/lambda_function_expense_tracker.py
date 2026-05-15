# Function to store new data in the list as a dictionary
def add_expense(expenses, amount, category):
    # This creates a 'record' for each transaction
    expenses.append({'amount': amount, 'category': category})
    
# Function to iterate through the data and display it clearly
def print_expenses(expenses):
    for expense in expenses:
        # Accessing dictionary values by their keys: 'amount' and 'category'
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')
    
# Logic to calculate the sum of all transaction amounts
def total_expenses(expenses):
    # 'map' extracts all the amounts, 'lambda' identifies the key, and 'sum' adds them up
    return sum(map(lambda expense: expense['amount'], expenses))
    
# Logic to isolate specific transactions
def filter_expenses_by_category(expenses, category):
    # 'filter' creates a new list containing only items that match the user's category
    return filter(lambda expense: expense['category'] == category, expenses)
    

def main():
    # Initialize an empty list to act as our temporary database
    expenses = []
    
    # Start the infinite loop for the user interface
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            # Convert input to float to handle decimal numbers (like 10.50)
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            # Display the result of our 'total_expenses' math function
            print('\nTotal Expenses: ', total_expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            # Filter the list and store the temporary result
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            # Break the loop to stop the script
            break

# Run the program
main()
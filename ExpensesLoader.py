from Expense import *


class ExpensesLoader(object):
    """A class for loading expenses from a file.
    """

    # We do not have an __init__ function and will call the default constructor

    def import_expenses(self, expenses, file):
        """Reads data from the given file and stores the expenses in the given expenses dictionary, where the expense
        type is the key and the value is an Expense object with the parameters expense type and total amount for that
        expense type.

        The same expense type may appear multiple times in the given file, so add all the amounts for the same
        expense types.

        Ignore expenses with missing amounts. If a line contains both an expense type and an expense amount,
        they will be separated by a colon (:).

        You can assume that if they exist, expense types are one-word strings and the amounts are numerical and can
        be casted to a float data type.

        Strip any whitespace before or after the expense types and amounts. Blank lines should be ignored.

        Expenses are case-sensitive. "coffee" is different from "Coffee".

        This method will be called twice in the main function in expenses.py with the same dictionary, but different
        files.

        This method doesn’t return anything.  Rather, it updates the given expenses dictionary based
        on the expenses in the given file.

        For example, after loading the expenses from the file, the expenses dictionary should look like
        this: {'food': Expense('food', 5.00), 'coffee': Expense('coffee', 12.40),
               'rent': Expense('rent', 825.00), 'clothes': Expense('clothes', 45.00),
               'entertainment': Expense('entertainment', 135.62), 'music': Expense('music', 324.00),
               'family': Expense('family', 32.45)}

        Note: You are not expected to handle negative numbers in your code
        """
        # open file in read mode
        with open(file, "r") as stream:
            lines = stream.readlines() # read all lines into a list
            for line in lines:
                line = line.strip() # remove leading and trailing spaces on each lines
                if not line: # check if line is empty then continue
                    continue
                parts = line.split(":") # split the line by semicolon
                if len(parts) != 2: # check to see if lenght of after spliting does not contain two parts then continue
                    continue
                expense_type, amount = parts # save parts appropriately to 
                expense_type = expense_type.strip() # remove the leading and trailing spaces 
                try:
                    amount = float(amount.strip()) # use a try-except block to catch valueError and cast amount to float/remove spaces
                except ValueError:
                    continue
                if expense_type in expenses: # check if the expense type exist then add amount
                    expenses[expense_type].amount += amount
                else:
                    expenses[expense_type] = Expense(expense_type, amount) # create a new expense type otherwise
                


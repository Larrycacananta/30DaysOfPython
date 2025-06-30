class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}
        self.expenses = {}
    def add_income(self, description, amount):
        """Add an income entry with description and amount."""
        if description in self.incomes:
            self.incomes[description] += amount
        else:
            self.incomes[description] = amount

    def add_expense(self, description, amount):
        """Add an expense entry with description and amount."""
        if description in self.expenses:
            self.expenses[description] += amount
        else:
            self.expenses[description] = amount

    def total_income(self):
        """Calculate total income."""
        return sum(self.incomes.values())

    def total_expense(self):
        """Calculate total expense."""
        return sum(self.expenses.values())

    def account_balance(self):
        """Calculate the balance = total income - total expense."""
        return self.total_income() - self.total_expense()

    def account_info(self):
        """Return a summary of the account."""
        info = (
            f"Account Holder: {self.firstname} {self.lastname}\n"
            f"Total Income: ${self.total_income():.2f}\n"
            f"Total Expense: ${self.total_expense():.2f}\n"
            f"Account Balance: ${self.account_balance():.2f}\n"
            f"Incomes: {self.incomes}\n"
            f"Expenses: {self.expenses}"
        )
        return info
person = PersonAccount("Larry", "Cacananta")
person.add_income("Salary", 5000)
person.add_income("Freelance", 1200)
person.add_expense("Rent", 1500)
person.add_expense("Groceries", 300)

print(person.account_info())
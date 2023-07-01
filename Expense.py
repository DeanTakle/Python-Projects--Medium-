class Expense:  # Class that represents an expense

    def __init__(self, name, amount, category) -> None:
        self.name = name
        self.amount = amount
        self.category = category

    def __repr__(self):  # prints the object in a string format when called, -> str is used to tell the compiler that the function will return a string
        # return f"<Expense: {self.name}, {self.category}, £{self.amount:.2f}>"
        return "<Expense: {}, {}, £{}>".format(self.name, self.category, self.amount)

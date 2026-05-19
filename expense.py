class Expense:

    def __init__(self, name, category, amount):

        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self):

        return f"<Expense: " f"{self.name}, " f"{self.category}, " f"{self.amount:.2f}>"

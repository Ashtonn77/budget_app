class Category:

    def __init__(self, name):
        self.ledger = []
        self.name = name

    def __str__(self):
        s = len(self.name)
        f = int((30 - s) / 2)
        e = 30 - f - s

        temp = "*" * f + self.name + "*" * e + "\n"

        for i in self.ledger:
            formatted_float = "{:.2f}".format(float(i["amount"]))[0:7]
            n = len(formatted_float)
            m = 30 - len(i["description"][0:23]) - n
            temp += (i["description"][0:23] + " " * m) + formatted_float + "\n"

        temp += ("Total: " + str(self.get_balance()))

        return temp

    def get_balance(self):
        total = 0.0
        for obj in self.ledger:
            total += obj["amount"]

        return total

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def transfer(self, amount, budget_category):
        if self.check_funds(amount):
            budget_category.deposit(
                amount, "Transfer from {}".format(self.name))
            self.withdraw(amount, "Transfer to {}".format(
                budget_category.name))
            return True
        else:
            return False

    def total_spend(self):
        total = 0.0

        for withdrawal in self.ledger:
            if withdrawal["amount"] < 0:
                total += withdrawal["amount"]

        return total


def get_percentage(total, category_amt):
    return (category_amt / total) * 100


def final_percentage(categories, single_cat):
    t = 0
    for i in categories:
        t += i.total_spend()

    t = get_percentage(t, single_cat.total_spend())
    t = t - (t % 10)

    return int(t)


def create_spend_chart(categories):

    temp = temp = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "

    return temp

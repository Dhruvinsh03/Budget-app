class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()
  def deposit(self, amount, description = ""):
    self.ledger.append({"amount":amount,"description":description})

  def withdraw(self, amount, description = ""):
    if self.check_funds(amount):
      self.ledger.append({"amount":-amount,"description":description})
      return True
    else:
      return False
  def get_balance(self):  
      balance = 0
      for item in self.ledger:
        balance += item["amount"]
      return balance
  def transfer(self,amount,category):
    if self.check_funds(amount):
      self.withdraw(amount,"Transfer to " + category.name)
      category.deposit(amount,"Transfer from " + self.name)
      return True
    else:
      return False
  def check_funds(self,amount):
    if amount > self.get_balance():
      return False
    else:
      return True
  def __str__(self):
    title=f"{self.name:*^30}\n"
    items=""
    total=0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
      total += item['amount']
    output = title + items + "Total: " + str(total)
    return output

def create_spend_chart(categories):
    chart = "Percentage spent by category\n"
    spendings = [sum(item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
    total_spent = sum(spendings)

    for i in range(100, -1, -10):
        chart += f"{i:3}|"
        for spending in spendings:
            chart += " o " if spending >= i else "   "
        chart += " \n"

    chart += "    ----------\n     "

    max_len = max(len(category.category) for category in categories)
    for i in range(max_len):
        for category in categories:
            chart += category.category[i] if i < len(category.category) else " "
            chart += "  "
        chart += "\n     "

    return chart.rstrip()
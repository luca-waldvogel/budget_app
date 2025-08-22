class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0
        self.withdrawals = 0

    def deposit(self, amount, description = ''):
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.balance -= amount
            self.withdrawals += amount
            self.ledger.append({'amount': (amount * -1), 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other.name}')
            other.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else: 
            return True

    def title_line(self):
        title_line = ''
        for i in range((30 - len(self.name)) // 2 + (30 - len(self.name)) % 2):
            title_line += '*'
        title_line += self.name
        for i in range((30 - len(self.name)) // 2):
            title_line += '*'
        return title_line
    
    def ledger_items(self):
        ledger_items = ''
        for item in self.ledger:
            counter = 0
            counter += 1

            #description
            count1 = 0
            for i in item['description']:
                count1 += 1
                if count1 > 23:
                    break
                ledger_items += i
            for j in range(23 - len(item['description'])):
                ledger_items += ' '

            #amount
            amount = item['amount']
            amount_str = f'{amount:.2f}'
            count2 = 0
            for j in range(7 - len(amount_str)):
                ledger_items += ' '
            for i in amount_str:
                count2 += 1
                if count2 > 23:
                    break
                ledger_items += i
            
            ledger_items += '\n'
        return ledger_items

    def __str__(self):
        title_line = self.title_line()
        ledger_items = self.ledger_items()
        total_line = f'Total: {self.balance:.2f}'
        return f'{title_line}\n{ledger_items}{total_line}'


def create_spend_chart(categories):
    total_spend = 0
    for cat in categories: total_spend += cat.withdrawals
    output_dict = {'line1': '100| ', 'line2': ' 90| ', 'line3': ' 80| ', 'line4': ' 70| ', 'line5': ' 60| ', 'line6': ' 50| ', 'line7': ' 40| ', 'line8': ' 30| ', 'line9': ' 20| ', 'line10': ' 10| ', 'line11': '  0| ', 'divider_line': '    -'}
    output_str = 'Percentage spent by category'
    longest_category_name = ''
    
    for category in categories:
        if len(category.name) > len(longest_category_name):
            longest_category_name = category.name

        percentage_spend = category.withdrawals / total_spend * 100 // 10 * 10
        percentage = 110
        for i in range(11):
            percentage -= 10
            line = f'line{i+1}'
            if percentage_spend >= percentage:
                output_dict[line] += 'o  '
            else:
                output_dict[line] += '   '

        output_dict['divider_line'] += '---'

    for i in range(len(longest_category_name)):
        output_dict.update({f'cat_line{i}': '     '})
    
    for category in categories:
        for i, v in enumerate(category.name):
            output_dict[f'cat_line{i}'] += f'{v}  '
        for i in range((len(longest_category_name) - len(category.name))):
                i += len(category.name)
                output_dict[f'cat_line{i}'] += f'   '
    
    for i, v in output_dict.items():
        output_str += '\n'
        output_str += v

    return output_str

food = Category('Food')
food.deposit(2000, 'Initial deposit')
food.withdraw(100, 'Groceries')
food.withdraw(150, 'Restaurant')

clothing = Category('Clothing')
clothing.deposit(2000, 'Initial deposit')
clothing.withdraw(200, 'Jeans')

food.transfer(50, clothing)

print(create_spend_chart([food, clothing]))
print()
print(food)
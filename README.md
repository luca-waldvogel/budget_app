# 💰 Budget App

A simple budgeting app with categories to track deposits, withdrawals, transfers, and spending.  
It also generates a text-based **spend chart** showing the percentage spent by each category.

It was created as part of my **Scientific Computing with Python Certification**.  
👉 [View my certification here](https://freecodecamp.org/certification/lucawaldvogel/scientific-computing-with-python-v7)

---

## 🚀 Features

- Create budget categories (e.g. Food, Clothing, Entertainment)
- Deposit money with optional description
- Withdraw money (with fund checks)
- Transfer money between categories
- View category balance and ledger
- Nicely formatted string representation of category ledgers
- Generate a **spending percentage chart** across categories

---

## 🧩 Classes & Functions

### `Category`
Represents a single budget category.

**Methods**
- `deposit(amount, description='')` → Adds money
- `withdraw(amount, description='')` → Withdraws if funds available
- `get_balance()` → Returns current balance
- `transfer(amount, other_category)` → Moves money between categories
- `check_funds(amount)` → Ensures balance is sufficient
- `__str__()` → Returns a formatted ledger view

### `create_spend_chart(categories)`
Generates a vertical percentage chart of spending distribution across given categories.

---

## 📖 Examples

### Basic usage
```python
food = Category('Food')
food.deposit(2000, 'Initial deposit')
food.withdraw(100, 'Groceries')
food.withdraw(150, 'Restaurant')

clothing = Category('Clothing')
clothing.deposit(2000, 'Initial deposit')
clothing.withdraw(200, 'Jeans')

food.transfer(50, clothing)

print(food)
```

### Output
```python
*************Food*************
Initial deposit        2000.00
Groceries              -100.00
Restaurant             -150.00
Transfer to Clothing    -50.00
Total: 1700.00
```

### Spend chart
```python
print(create_spend_chart([food, clothing]))
```

### Output
```python
Percentage spent by category
100|       
 90|       
 80|       
 70|
 60| o
 50| o
 40| o  o
 30| o  o
 20| o  o
 10| o  o
  0| o  o
    -------
     F  C
     o  l
     o  o
     d  t
        h
        i
        n
        g
```

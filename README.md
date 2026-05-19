# 💰 Expense Tracker (Python)

A simple command-line Expense Tracker built using Python.  
This project helps users add expenses, store them in a JSON file, and view spending summaries based on categories and budget.

---

# 🚀 Features

- Add expenses
- Store data in JSON format
- View expense summary
- Category-wise expense tracking
- Budget tracking
- Simple menu-driven interface
- Object-Oriented Programming (OOP) implementation

---

# 📂 Project Structure

```bash
expense-tracker/
│
├── main.py
├── expense.py
├── expenses.json
└── README.md
```

---

# 🛠 Technologies Used

- Python
- JSON
- File Handling
- OOP Concepts

---

# 📌 How It Works

The program follows this flow:

```text
Start Program
      ↓
Display Menu
      ↓
Take User Input
      ↓
Save Expense to JSON
      ↓
Read Expenses
      ↓
Generate Summary
```

---

# 📄 expense.py

Contains the `Expense` class.

```python
class Expense:
```

The class stores:

- Expense name
- Expense category
- Expense amount

---

# 📄 main.py

Contains the main logic of the application:

- Menu system
- Adding expenses
- Saving data
- Reading JSON
- Summarizing expenses

---

# 📦 JSON Storage Example

Expenses are stored in `expenses.json`

Example:

```json
[
    {
        "name": "Pizza",
        "category": "Food",
        "amount": 250
    },
    {
        "name": "Shoes",
        "category": "Shopping",
        "amount": 1200
    }
]
```

---

# ▶️ How to Run

## Step 1

Clone the repository

```bash
git clone <repository-link>
```

---

## Step 2

Open project folder

```bash
cd expense-tracker
```

---

## Step 3

Run the program

```bash
python main.py
```

---

# 📋 Menu Options

```text
1. Add Expense
2. View Expense Summary
3. Exit
```

---

# 🧠 Concepts Used

This project covers:

- Variables
- Functions
- Loops
- Conditional Statements
- Lists
- Dictionaries
- Classes & Objects
- File Handling
- JSON Handling
- Exception Handling

---

# ⚠️ Current Limitations

- No delete expense feature
- No edit expense feature
- No input validation for invalid numbers
- Entire JSON file rewrites after every save
- No database integration

---

# 🔥 Future Improvements

Possible upgrades:

- Add expense deletion
- Add expense editing
- Monthly reports
- Data visualization
- SQLite database integration
- GUI version using Tkinter
- Web version using Flask or FastAPI

---

# 📚 Learning Outcome

This project is useful for beginners learning:

- Python basics
- File handling
- JSON
- OOP
- Program structure
- Data flow in applications

---

# 👨‍💻 Author

Created as a beginner Python learning project on 18th May.



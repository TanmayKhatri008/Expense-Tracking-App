# 🧾 Expense Tracker

A simple command-line Expense Tracker built using Python.  
This project allows users to add expenses, save them into a CSV file, and view spending summaries based on categories and total budget.

The project was created while learning Python fundamentals and focuses on understanding real programming concepts through a practical project.

---

# 🚀 Features

- Add new expenses
- Categorize expenses
- Save expenses into a CSV file
- View category-wise spending summary
- Calculate total spent amount
- Track remaining budget
- Simple menu-driven interface
- Beginner-friendly project structure

---

# 🛠️ Technologies Used

- Python
- File Handling
- Object-Oriented Programming (OOP)
- CSV Storage

---

# 📂 Project Structure

```bash
expense-tracker/
│
├── main.py
├── expense.py
├── expenses.csv
└── README.md
```

---

# 📘 Concepts Used

This project covers several important Python concepts:

- Functions
- While Loops
- For Loops
- Match Case Statements
- Lists
- Dictionaries
- Classes and Objects
- File Handling
- String Formatting
- Type Conversion
- User Input Handling

---

# ⚙️ How the Project Works

## 1. User Selects an Option

The program displays a menu:

```bash
===== Expense Tracker =====
1. Add Expense
2. View Expense Summary
3. Exit
```

---

## 2. Add Expense

The user enters:
- Expense name
- Expense amount
- Expense category

Example:

```bash
Enter expense name: Pizza
Enter the amount: 300
```

---

## 3. Save Expense

The expense is saved into `expenses.csv`.

Example stored data:

```csv
Pizza,Food,300
Movie,Fun,500
```

---

## 4. View Summary

The program:
- Reads all expenses from the CSV file
- Calculates category-wise totals
- Calculates total spending
- Shows remaining budget

Example:

```bash
Expenses By Category:

Food: $300.00
Fun: $500.00

Total Spent: $800.00
Remaining Budget: $1200.00
```

---

# ▶️ How to Run the Project

## Step 1 — Clone the Repository

```bash
git clone <your-repository-link>
```

---

## Step 2 — Open Project Folder

```bash
cd expense-tracker
```

---

## Step 3 — Run the Program

```bash
python main.py
```

---

# 🧠 What I Learned From This Project

This project helped me understand:
- How real programs are structured
- How data is stored using files
- How functions work together
- How objects and classes are used
- How loops and conditions control program flow

---

# 📸 Sample Output

```bash
This expense tracker was created on 18th May
Running the Expense Tracker

===== Expense Tracker =====
1. Add Expense
2. View Expense Summary
3. Exit

Enter your choice:
```

---

# 👨‍💻 Author

Created as a beginner Python project while learning programming fundamentals and building hands-on projects.

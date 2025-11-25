# Student Budget & Expense Tracker — Project Statement

## Problem Statement
Students often struggle to manage their monthly spending because they do not track day-to-day expenses. As a result, they frequently overspend without realizing it.  
There is a need for a simple digital tool that allows students to record expenses, categorize them, compare total expenses with their preset monthly budget, and get basic spending insights.

---

## Scope of the Project
The scope of this project includes:
- Allowing a student to set or update a monthly budget
- Adding and storing daily expenses
- Viewing all expenses in a structured list
- Generating a summary that shows:
  - Total money spent  
  - Remaining budget  
  - Percentage of budget used  
  - Category-wise spending totals  

Out of scope:
- Multi user login  
- Bank/payment integration  
- Online syncing    

The focus is on building a **simple, modular, file based CLI application**.

---

## Target Users
- College and university students  
- Hostellers and day scholars  
- Young adults or beginners who want a basic expense tracker  
- Anyone needing a lightweight budgeting tool  

---

## Features
- Set monthly budget  
- Add expenses with date, amount, category & description  
- View all recorded expenses  
- View monthly summary  
- Category wise spending breakdown  
- JSON file used for persistent storage  
- Modular Python code (5 separate modules)  
- Beginner friendly command line interface  

---

## Modules Overview
- **main.py** – Application menu & navigation  
- **storage.py** – Handles saving & loading of data (JSON)  
- **budget.py** – Budget creation and update functions  
- **expenses.py** – Add and view expenses  
- **reports.py** – Summary & analytics  

---

## Conclusion
This project provides a simple and effective digital solution to help students track their expenses and manage their monthly budget.  
With clean module separation and JSON-based storage, it is easy to understand, run, and extend.


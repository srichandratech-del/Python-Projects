# 💰 Financial Calculator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/7%20Expense%20Categories-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Dictionary%20Based%20Tracker-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Live%20Expense%20Display-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**Financial Calculator** is a Python command-line expense tracker that lets you record costs across **7 spending categories** — from Food and Health to Entertainment and Transportation — storing each entry in a dictionary for a live running summary.

Built as part of my **Python learning journey**, this project reinforced dynamic dictionary updates, list-driven menus, and float input handling in a practical, real-world budgeting context.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📂 **7 Expense Categories** | Personal, Food, Health, Education, Transportation, Entertainment, Miscellaneous |
| 📋 **List-Driven Menu** | Categories generated dynamically from a list — no hardcoded print statements |
| 💾 **Dictionary Tracker** | Each category's cost stored in `prices{}` and updated on every entry |
| 👀 **Live Summary** | Current expenses printed after every entry so you can track progress |
| 🔁 **Session Loop** | Keep adding expenses across categories until you choose to exit |
| 🚪 **Clean Exit** | Option 8 breaks the loop and exits gracefully |

---

## 📂 Expense Categories

| # | Category | Description |
|---|----------|-------------|
| 1 | **Personal** | Personal care, clothing, lifestyle |
| 2 | **Food** | Groceries, dining, beverages |
| 3 | **Health** | Medical, pharmacy, fitness |
| 4 | **Education** | Tuition, books, courses |
| 5 | **Transportation** | Fuel, transit, vehicle costs |
| 6 | **Entertainment** | Streaming, events, hobbies |
| 7 | **Miscellaneous** | Any other expenses |

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/Lists-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Dictionaries-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/while%20Loop-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/for%20Loop%20%2B%20enumerate-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/F--Strings-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Float%20Input-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Conditional%20Statements-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Index--Based%20Selection-✔-blueviolet?style=flat-square"/>
</p>

- **Lists** — `types[]` stores all category names, driving the menu dynamically
- **Dictionaries** — `prices{}` maps each category to its recorded cost, updated on every entry
- **`while True` loop** — keeps the session running until option 8 is chosen
- **`for` loop with index** — `range(len(types))` generates the numbered menu from the list
- **Index-based selection** — `types[choice - 1]` maps user input directly to a category name
- **Float input** — `float(input())` accepts decimal expense values
- **F-strings** — dynamic prompts and confirmation messages per category
- **Conditional range check** — `if choice >= 1 and choice <= 7` validates menu input cleanly

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — pure built-in Python only.

---

## 📁 Project Structure

```
📦 Financial Calculator/
│
├── 📄 Financial_Calculator.py     # Main program file
└── 📄 README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd "Python-Projects/Financial Calculator"
```

### 3. Run the Program

```bash
python Financial_Calculator.py
```

---

## 💻 Example Usage

```
Welcome to the Financial Calculator!

Please select a category:
1. Personal
2. Food
3. Health
4. Education
5. Transportation
6. Entertainment
7. Miscellaneous
8. Exit

Enter your choice: 2
Enter the cost of Food expenses: 3500.50
Food expenses recorded successfully.
Current expenses: {'Food': 3500.5}

Please select a category:
1. Personal
...
Enter your choice: 5
Enter the cost of Transportation expenses: 1200.00
Transportation expenses recorded successfully.
Current expenses: {'Food': 3500.5, 'Transportation': 1200.0}

Please select a category:
...
Enter your choice: 8
Exiting the program.
```

---

## 🔮 Future Improvements

- [ ] 🛡️ Add `try/except` to handle non-numeric input for choice and cost
- [ ] ➕ Allow multiple entries per category (running total instead of overwrite)
- [ ] 📊 Print a final expense summary report with total spend on exit
- [ ] 💹 Add a budget limit per category and warn when exceeded
- [ ] 💾 Save expense records to a `.csv` or `.json` file for history
- [ ] 📅 Add date-stamping to each entry using `datetime`
- [ ] 🖥️ Build a GUI version using Tkinter with a pie chart breakdown

---

## 📚 Learning Outcome

This project reinforced how a **list and a dictionary can work together** as the backbone of a menu-driven data entry tool. Key takeaways:

- Using a `list` to drive a **dynamic, numbered menu** — adding a new category only requires updating `types[]`, not the rest of the code
- How `types[choice - 1]` cleanly converts a 1-based user choice into a 0-based list index
- That `prices[category] = cost` both **creates and updates** a dictionary key in a single line — no separate insert logic needed
- The current version overwrites a category if entered twice — a natural next step is switching to `prices[category] = prices.get(category, 0) + cost` for running totals

---

## 👨‍💻 Author

**Sri Chandra**

<p>
  <img src="https://img.shields.io/badge/GitHub-srichandratech--del-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

> 🌱 *Part of my ongoing Python learning journey — building real projects to solidify programming fundamentals.*

---

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Track-Every%20Rupee-green?style=for-the-badge"/>
</p>

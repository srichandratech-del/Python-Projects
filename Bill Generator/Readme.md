# 🧾 Bill Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-blueviolet?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/File%20I%2FO-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Persistent%20ID%20Counter-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Dictionary%20Based%20Cart-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Formatted%20Bill%20Output-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**Bill Generator** is a Python command-line tool that lets you add items to an order and instantly produces a **formatted bill** — complete with item breakdown, quantities, unit prices, totals, customer name, and a **persistent auto-incremented Bill ID** that survives across program restarts.

Built as part of my **Python learning journey**, this project introduced persistent state through file I/O — using `ID.txt` as a lightweight counter that increments with every new bill, simulating how real billing systems track invoice numbers.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🛒 **Dynamic Order Cart** | Add any number of items with individual quantities and prices |
| 🔢 **Auto Bill ID** | Each bill gets a unique incrementing ID stored in `ID.txt` |
| 💾 **Persistent Counter** | Bill ID persists across sessions — never resets on restart |
| 🧮 **Auto Total** | Calculates per-item subtotals and grand total automatically |
| 🖨️ **Formatted Bill** | Clean, readable bill layout with item × price breakdown |
| ✅ **Done Command** | Type `done` to stop adding items and print the bill |

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/Dictionaries-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/File%20Read%20%26%20Write-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/with%20Statement-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Persistent%20State-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/while%20Loop-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/for%20Loop%20%2B%20.items()-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/F--Strings%20%26%20:.2f-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Float%20%26%20Int%20Input-✔-blueviolet?style=flat-square"/>
</p>

- **Dictionaries** — `order{}` stores each item as a key with `quantity` and `price` as nested values
- **File I/O with `with` statement** — reading the current ID from `ID.txt` at the start and writing the incremented ID at the end
- **Persistent State** — `ID.txt` acts as a lightweight database that keeps the bill counter alive between sessions
- **`while True` loop** — keeps accepting items until the user types `done`
- **`for item, details in order.items()`** — iterating over the cart dictionary to print each line of the bill
- **F-strings with `:.2f`** — formatting all currency values to exactly 2 decimal places
- **Unit price recovery** — `price / quantity` reconstructs the original unit price from the stored total for clean bill display

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — pure built-in Python only.  
> ⚠️ `ID.txt` must exist in the same folder before running. Create it with `0` inside before first use.

---

## 📁 Project Structure

```
📦 Bill Generator/
│
├── 📄 Bill_Generator.py     # Main program file
├── 📄 ID.txt                # Persistent bill ID counter (start with 0)
└── 📄 README.md             # Project documentation
```

---

## ⚙️ First-Time Setup

Before running for the first time, create `ID.txt` in the project folder with just `0` inside:

```bash
echo 0 > ID.txt
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd "Python-Projects/Bill Generator"
```

### 3. Create ID.txt (first time only)

```bash
echo 0 > ID.txt
```

### 4. Run the Program

```bash
python Bill_Generator.py
```

---

## 💻 Example Usage

```
Add items to your order. Type 'done' when finished.
Enter your name: Arjun

Enter item name: Coffee
Enter quantity for Coffee: 2
Enter price for each of Coffee: 120
Coffee added to your order.
--------------------
Current order: {'Coffee': {'quantity': 2, 'price': 240.0}}
--------------------

Enter item name: Sandwich
Enter quantity for Sandwich: 1
Enter price for each of Sandwich: 180
Sandwich added to your order.
--------------------
Current order: {'Coffee': {'quantity': 2, 'price': 240.0}, 'Sandwich': {'quantity': 1, 'price': 180.0}}
--------------------

Enter item name: done

------------------
|    YOUR BILL    |
------------------
ID: 1
Name: Arjun
--------------------
Items Ordered:
Coffee: 2 x ₹120.00 = ₹240.00
Sandwich: 1 x ₹180.00 = ₹180.00
---------------------
Total: ₹420.00
```

> On the next run, the Bill ID automatically increments to `2`, then `3`, and so on.

---

## 🔮 Future Improvements

- [ ] 🛡️ Add `try/except` to handle invalid quantity or price input
- [ ] 🗑️ Allow removing items from the cart before printing the bill
- [ ] 💾 Save each generated bill to a `.txt` or `.csv` file for record-keeping
- [ ] 🧾 Add GST / tax percentage calculation to the total
- [ ] 🔁 Add a loop to generate multiple bills per session
- [ ] 🕐 Add a timestamp (date and time) to each bill using `datetime`
- [ ] 🖨️ Generate a formatted PDF bill using `reportlab`
- [ ] 🗄️ Replace `ID.txt` with a proper database (`sqlite3`) for full order history

---

## 📚 Learning Outcome

This project introduced the concept of **persistent state through file storage** — a pattern that sits at the core of nearly every real-world application. Key takeaways:

- How a simple text file (`ID.txt`) can act as a lightweight counter that survives program restarts — the foundation of how invoice and order IDs work in real systems
- Using `order[item] = {nested dict}` to build a structured cart where each item holds its own data
- Iterating a dictionary with `.items()` to produce a clean, line-by-line bill printout
- Recovering the **unit price** from a stored subtotal with `price / quantity` — a practical data modelling decision
- How `:.2f` formatting ensures all currency values print with consistent decimal places

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
  <img src="https://img.shields.io/badge/Every%20Bill-Counted-green?style=for-the-badge"/>
</p>

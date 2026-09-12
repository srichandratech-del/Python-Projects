# 🧮 Basic Calculator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
  <img src="https://img.shields.io/badge/Input%20Handling-✔-yellowgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/Division%20By%20Zero%20Guard-✔-yellowgreen?style=flat-square"/>
</p>

---

## 🧾 Overview

**Basic Calculator** is a beginner-friendly Python command-line program that performs the four fundamental arithmetic operations — **Addition, Subtraction, Multiplication, and Division** — through a clean and simple user interface.

Built as part of my **Python learning journey**, this project helped me practice user input, conditional branching, operator logic, and basic error handling (division by zero).

---

## ✨ Features

| # | Operation | Accepted Keywords | Symbol |
|---|-----------|-------------------|--------|
| 1 | **Addition** | `Add`, `Addition` | `+` |
| 2 | **Subtraction** | `Sub`, `Subtraction` | `-` |
| 3 | **Multiplication** | `Mul`, `Multiplication` | `*` |
| 4 | **Division** | `Div`, `Division` | `/` |

> ✅ Accepts **multiple input formats** per operation — full name, short name, or symbol  
> 🛡️ **Division by zero** is handled gracefully with an error message

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/Variables%20%26%20Data%20Types-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/User%20Input-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Float%20Conversion-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Conditional%20Statements-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Logical%20Operators-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Error%20Handling-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20Comparison-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Arithmetic%20Operators-✔-blueviolet?style=flat-square"/>
</p>

- **Variables & Data Types** — storing numbers as `float` and operator as `str`
- **User Input** — capturing values and operator choice via `input()`
- **Float Conversion** — converting string input to `float` for decimal support
- **Conditional Statements** — `if`, `elif`, `else` for operation routing
- **Logical Operators** — `or` to accept multiple valid input formats per operation
- **String Comparison** — matching operator keywords typed by the user
- **Arithmetic Operators** — `+`, `-`, `*`, `/` for core calculations
- **Basic Error Handling** — guarding against division by zero with a nested `if`

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — pure built-in Python only.

---

## 📁 Project Structure

```
📦 Basic Calculator/
│
├── 📄 Basic_Calculator.py     # Main program file
└── 📄 README.md               # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd "Python-Projects/Basic Calculator"
```

### 3. Run the Program

```bash
python Basic_Calculator.py
```

---

## 💻 Example Usage

**➕ Addition**
```
------------------------------
| Welcome To Basic Calculator |
------------------------------

Enter First Number: 25
Enter Second Number: 15
Enter operation (add/sub/mul/div): +

------------------------------
Answer =  40.0
------------------------------
```

**➗ Division (valid)**
```
Enter First Number: 100
Enter Second Number: 4
Enter operation (add/sub/mul/div): Division

------------------------------
Answer =  25.0
------------------------------
```

**🚫 Division by Zero (guarded)**
```
Enter First Number: 10
Enter Second Number: 0
Enter operation (add/sub/mul/div): /

Syntax Error
```

**❌ Invalid Operation**
```
Enter operation (add/sub/mul/div): power

Invalid Operation
```

---

## 🔮 Future Improvements

- [ ] 🔁 Add a loop to allow multiple calculations per session
- [ ] 🛡️ Add input validation to reject non-numeric values
- [ ] ➕ Add more operations — modulo `%`, power `**`, floor division `//`
- [ ] 🔤 Make operator input **case-insensitive** (e.g. `ADD` = `add` = `Add`)
- [ ] 📜 Show calculation history within a session
- [ ] 🖥️ Build a graphical interface using Tkinter
- [ ] 🧮 Add a scientific calculator mode

---

## 📚 Learning Outcome

This project gave me a solid foundation in **handling user input and conditional branching** in Python. Key takeaways:

- How to accept and convert different data types from user input
- Using `or` conditions to support multiple valid input formats
- Structuring logic cleanly with `if / elif / else`
- Defending against runtime errors like **division by zero**

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
  <img src="https://img.shields.io/badge/Built%20with-❤️%20%26%20Logic-red?style=for-the-badge"/>
</p>

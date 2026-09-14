# 📅 Calendar Program

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/calendar-module-yellowgreen?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Recursive%20Function-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Multi--Month%20Support-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**Calendar Program** is a minimal Python command-line tool that prints a neatly formatted monthly calendar for any year and month you specify — powered entirely by Python's built-in `calendar` module.

Built as part of my **Python learning journey**, this project introduced me to the `calendar` module, recursive function calls, and building small, clean utility tools with a continuous-use loop.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📆 **Any Month, Any Year** | Print a calendar for any valid year and month combination |
| 🔁 **Multi-Month Session** | After each calendar, choose to print another without restarting |
| 🖨️ **Formatted Output** | Clean bordered display using Python's `calendar.month()` |
| 🛑 **Graceful Exit** | Friendly goodbye message on exit; invalid input terminates cleanly |

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/calendar%20Module-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Functions-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Recursive%20Calls-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/User%20Input-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Conditional%20Statements-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20Methods-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/exit()-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Int%20Conversion-✔-blueviolet?style=flat-square"/>
</p>

- **`calendar` Module** — using `calendar.month(year, month)` to generate a formatted calendar string
- **Functions** — encapsulating the full calendar logic inside `print_calendar()`
- **Recursive Function Calls** — calling `print_calendar()` from within itself to loop without a `while` loop
- **User Input** — capturing year, month, and continue/exit responses
- **Conditional Statements** — `if / elif / else` routing the yes/no response
- **`.lower()`** — normalising user input for case-insensitive comparison
- **`exit()`** — cleanly terminating on unexpected input

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — uses only Python's built-in `calendar` module.

---

## 📁 Project Structure

```
📦 Calendar Program/
│
├── 📄 Calendar.py      # Main program file
└── 📄 README.md        # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd "Python-Projects/Calendar Program"
```

### 3. Run the Program

```bash
python Calendar.py
```

---

## 💻 Example Usage

```
Welcome to the Calendar Program!
============================================================
Enter year: 2025
Enter month: 8

------------------------------------------------------------
   August 2025
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31

------------------------------------------------------------

Do you want to print another calendar? (yes/no): yes

Enter year: 2026
Enter month: 1

------------------------------------------------------------
  January 2026
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

------------------------------------------------------------

Do you want to print another calendar? (yes/no): no
Thank you for using the Calendar Program!
```

---

## 🔮 Future Improvements

- [ ] 🛡️ Add `try/except` for invalid year or month input
- [ ] 📆 Add option to print the **full year** calendar using `calendar.calendar(year)`
- [ ] 🔍 Highlight today's date in the output
- [ ] 📁 Add option to export the calendar to a `.txt` file
- [ ] 🖥️ Build a GUI version using Tkinter with a month picker
- [ ] 🗓️ Add week number display alongside each row

---

## 📚 Learning Outcome

This project introduced me to Python's **`calendar` module** and showed how much a standard library can do with minimal code. Key takeaways:

- How to use a built-in module (`calendar`) to avoid writing logic from scratch
- Using **recursion** as a clean alternative to a `while` loop for repeat-use tools
- How `.lower()` makes input comparisons robust without extra conditions
- Building a complete, usable utility with just one function and one module

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
  <img src="https://img.shields.io/badge/Every%20Month-On%20Demand-blue?style=for-the-badge"/>
</p>

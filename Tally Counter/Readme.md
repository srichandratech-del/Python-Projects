# 🔢 Tally Counter

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
  <img src="https://img.shields.io/badge/Increment%20%7C%20Decrement%20%7C%20Reset-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Live%20Count%20Display-✔-blue?style=flat-square"/>
</p>

---

## 🧾 Overview

**Tally Counter** is a minimal Python command-line tool that simulates a physical tally counter — letting you **increment, decrement, and reset** a running count through a simple interactive menu.

Built as part of my **Python learning journey**, this project reinforced the fundamentals of loops, conditionals, and stateful variables in the most distilled form possible — one variable, one loop, four choices.

---

## ✨ Features

| Option | Action | Result |
|--------|--------|--------|
| `1` | **Increment** | Adds `1` to the current count |
| `2` | **Decrement** | Subtracts `1` from the current count |
| `3` | **Reset** | Sets count back to `0` |
| `4` | **Exit** | Ends the session with a goodbye message |

> 🔁 The menu runs in a continuous loop — the count persists across all operations until you exit or reset

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/Variables-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/While%20Loop-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Conditional%20Statements-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/F--Strings-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Lists-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20join()-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/User%20Input-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Break%20Statement-✔-blueviolet?style=flat-square"/>
</p>

- **Variables** — a single `count` integer holds and updates state throughout the session
- **`while True` Loop** — keeps the menu live until the user explicitly exits
- **Conditional Statements** — `if / elif / else` routing each menu option
- **F-strings** — live count display after every increment or decrement
- **Lists** — storing menu options cleanly for display via `"\n".join()`
- **`str.join()`** — printing the menu list as a formatted block
- **`break`** — cleanly exiting the loop on option `4`

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — pure built-in Python only.

---

## 📁 Project Structure

```
📦 Tally Counter/
│
├── 📄 Tally_Counter.py     # Main program file
└── 📄 README.md            # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd "Python-Projects/Tally Counter"
```

### 3. Run the Program

```bash
python Tally_Counter.py
```

---

## 💻 Example Usage

```
Welcome to the Tally Counter!
Please choose an option:
1. Increment Count
2. Decrement Count
3. Reset Count
4. Exit

Enter your choice (1-4): 1
Count incremented. Current count: 1

Enter your choice (1-4): 1
Count incremented. Current count: 2

Enter your choice (1-4): 1
Count incremented. Current count: 3

Enter your choice (1-4): 2
Count decremented. Current count: 2

Enter your choice (1-4): 3
Count reset to 0.

Enter your choice (1-4): 4
Exiting the Tally Counter. Goodbye!
```

---

## 🔮 Future Improvements

- [ ] 🛡️ Add input validation for non-numeric entries
- [ ] 🚫 Prevent count from going below `0` (no negative tallying)
- [ ] 🔢 Allow custom increment/decrement step sizes (e.g. count by 5)
- [ ] 📜 Show a history log of all operations in the session
- [ ] 💾 Save and load count from a file between sessions
- [ ] 🖥️ Build a GUI version with `+` / `-` / `Reset` buttons using Tkinter

---

## 📚 Learning Outcome

Simple in scope but sharp in focus — this project reinforced the core loop of **state → input → update → display** that sits at the heart of nearly every interactive program. Key takeaways:

- Maintaining a **persistent variable** across many loop iterations
- Cleanly routing user choices with `if / elif / else`
- Using a **list + `join()`** to print menus instead of repeated `print()` calls
- Keeping code minimal, readable, and purposeful

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
  <img src="https://img.shields.io/badge/Count-Everything-orange?style=for-the-badge"/>
</p>

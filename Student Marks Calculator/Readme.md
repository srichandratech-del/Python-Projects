# 📊 Student Marks Calculator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Beginner--Intermediate-yellow?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/time-module-yellowgreen?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Multi--Student%20Support-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Live%20Progress%20Bar-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/CGPA%20%26%20Grade%20System-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**Student Marks Calculator** is a Python command-line tool that collects marks for multiple students across any number of subjects, then generates a clean, formatted academic report for each student — complete with **Total Marks, Percentage, CGPA, and Grade**.

Built as part of my **Python learning journey**, this project brought together loops, lists, input validation, formatted output, and a real-time animated progress bar into one cohesive, practical tool.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 👥 **Multi-Student Support** | Process any number of students in a single session |
| 📚 **Flexible Subject Count** | Each student can have a different number of subjects |
| 📊 **Full Academic Report** | Generates Total Marks, Percentage, CGPA, and Grade per student |
| 🎓 **Grade System** | Auto-assigns grades from `A+` to `F` based on CGPA |
| ⏳ **Animated Progress Bar** | Live `█` block progress bar while report is being calculated |
| 🔁 **Session Loop** | Run multiple batches of students without restarting the program |
| 🛡️ **Input Validation** | Guards against blank names and invalid subject counts |

---

## 🎓 Grading System

| CGPA Range | Grade |
|------------|-------|
| `≥ 9.0` | **A+** — Outstanding |
| `≥ 8.0` | **A** — Excellent |
| `≥ 7.0` | **B** — Good |
| `≥ 6.0` | **C** — Average |
| `≥ 5.0` | **D** — Below Average |
| `< 5.0` | **F** — Fail |

> 📐 **CGPA Formula:** `CGPA = (Total Marks / No. of Subjects) / 10`

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/While%20Loop-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/For%20Loops-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Lists%20%26%20Append-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/F--Strings-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Input%20Validation-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Float%20%26%20Int%20Types-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20Methods-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/time%20Module-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Formatted%20Output-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Conditional%20Grading-✔-blueviolet?style=flat-square"/>
</p>

- **`while True` Loop** — keeps the session alive until the user chooses to exit
- **Nested `for` Loops** — outer loop per student, inner loop per subject
- **Lists & `.append()`** — dynamically storing names, subject counts, and marks
- **`sum()`** — totalling marks across all subjects per student
- **F-strings** — live prompts and formatted report output
- **Input Validation** — blank name guard and positive integer check for subject count
- **`time.sleep()`** — pacing the animated progress bar
- **`\r` + `flush=True`** — overwriting the same terminal line for the live bar effect
- **`.center()`** — centering the report header text
- **`:.2f` Formatting** — rounding percentage and CGPA to 2 decimal places

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — uses only Python's built-in `time` module.

---

## 📁 Project Structure

```
📦 Marks Calculator/
│
├── 📄 Marks_Calculator.py     # Main program file
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
cd "Python-Projects/Marks Calculator"
```

### 3. Run the Program

```bash
python Marks_Calculator.py
```

---

## 💻 Example Usage

**Input Phase**
```
Enter the number of students: 2

------------------------------------------------------------
Enter the name of Student 1: Arjun

Enter the number of subjects for Student 1: 3

Enter marks for Subject 1: 85
Enter marks for Subject 2: 90
Enter marks for Subject 3: 78

------------------------------------------------------------
Enter the name of Student 2: Priya

Enter the number of subjects for Student 2: 3

Enter marks for Subject 1: 95
Enter marks for Subject 2: 92
Enter marks for Subject 3: 98
```

**Animated Progress Bar**
```
Calculating the report...
[████████████████████] 100%
✅ Report generated successfully!
```

**Generated Report**
```
============================================================
              Student Marks and Percentage Report
============================================================
Student name  : Arjun
Total Marks   : 253.00 / 300.00
Percentage    : 84.33%
CGPA          : 8.43
Grade         : A
------------------------------------------------------------

Student name  : Priya
Total Marks   : 285.00 / 300.00
Percentage    : 95.00%
CGPA          : 9.50
Grade         : A+
------------------------------------------------------------

Do you want to continue? (yes/no): no

Exiting the Marks Calculator. Goodbye!.....

Thank you for using the Marks Calculator!
------------------------------------------------------------
```

---

## 🔮 Future Improvements

- [ ] 🛡️ Add `try/except` blocks for robust invalid number input handling
- [ ] 📁 Export the report as a `.txt` or `.csv` file
- [ ] 📊 Add subject-wise mark display in the final report
- [ ] 🔝 Highlight the topper (highest percentage) across all students
- [ ] 📉 Add a class average and lowest score summary
- [ ] 💯 Define a max marks per subject instead of assuming 100
- [ ] 🖥️ Build a GUI version using Tkinter
- [ ] 📄 Generate a formatted PDF report using `reportlab`

---

## 📚 Learning Outcome

This project helped me understand how to build a **data collection and reporting pipeline** using only core Python. Key takeaways:

- How to collect and store **structured data** across multiple students using lists
- Using **nested loops** to handle variable numbers of subjects per student
- Producing a **neatly formatted terminal report** with alignment and separators
- Implementing a **live animated progress bar** using `\r` and `time.sleep()`
- Applying a **grade calculation formula** in a clean, readable conditional chain

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
  <img src="https://img.shields.io/badge/Built%20with-❤️%20%26%20Data-red?style=for-the-badge"/>
</p>

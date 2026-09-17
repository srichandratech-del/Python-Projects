<h1><p align="center"><b>🐍 Python Projects</b></p></h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Projects-9-181717?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/badge/Status-Active-2ea44f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CLI%20Tools-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Text%20Adventure-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Math%20Tools-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Academic%20Tools-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Calendar%20Tools-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/QR%20Code%20Tools-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Password%20Tools-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Streaming%20Apps-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/More%20Coming%20Soon-🔜-orange?style=flat-square"/>
</p>

<p align="center">
A collection of Python projects, experiments, and applications developed while learning and exploring Python.<br/>
This repository is a living record of my programming journey — from small utilities to larger, more complex applications.
</p>

---

## 🧾 About

This repository is primarily focused on **learning Python through practical implementation**.

Rather than limiting learning to tutorials and theory, each project here is an opportunity to **apply, experiment, break, debug, and improve** — covering everything from beginner fundamentals to intermediate logic and application design.

Projects vary in complexity and purpose, but every one represents a real concept, idea, or challenge explored during the journey.

---

## 📦 Projects

| # | Project | Type | Description | Key Concepts |
|--:|---------|------|-------------|--------------|
| 1 | [🧮 Basic Calculator](#-1-basic-calculator) | CLI Tool | Performs the 4 core arithmetic operations via an interactive menu | Conditionals, `or` logic, Float input, Division guard |
| 2 | [📐 Theorem Verifier](#-2-theorem-verifier) | CLI Tool | Verifies theorems and calculates 10 common mathematical formulas | Functions, `math` module, `time` module, Loops |
| 3 | [🚀 Project ICARUS](#-3-project-icarus) | Text Adventure | A deep-space survival RPG with puzzles, riddles, and an oxygen system | Game state, Global vars, `sys` module, Nested logic |
| 4 | [📊 Student Marks Calculator](#-4-student-marks-calculator) | Academic Tool | Calculates marks, percentage, CGPA, and grade for multiple students | Nested loops, Lists, Progress bar, F-strings |
| 5 | [🔢 Tally Counter](#-5-tally-counter) | CLI Utility | A simple interactive counter with increment, decrement, and reset | `while` loop, Conditionals, State variable |
| 6 | [📅 Calendar Program](#-6-calendar-program) | CLI Utility | Prints a formatted monthly calendar for any year and month | `calendar` module, Recursion, `.lower()`, `exit()` |
| 7 | [🔳 QR Code Generator](#-7-qr-code-generator) | CLI Tool | Generates a QR code for any text or URL and exports it as a PNG | `qrcode`, `Pillow`, OOP, File I/O, `pip` |
| 8 | [🔐 Password Generator](#-8-password-generator) | CLI Tool | Generates a secure random password of any length from a full character set | `random`, `try/except`, Recursion, String ops |
| 9 | [🎬 StreamFlix Clone](#-9-streamflix-clone) | CLI App | A streaming service simulation with sign up, login, and subscription plans | Nested dicts, Lists of dicts, `datetime`, Data modelling |
| 🔜 | *More coming soon...* | — | New projects will be added as the journey continues | — |

> 📄 Each project has its own detailed `README.md` inside its directory.

---

## 🗂️ Project Details

---

### 🧮 1. Basic Calculator

<p>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
</p>

A command-line calculator that performs **Addition, Subtraction, Multiplication, and Division** between two numbers.

Accepts multiple input formats per operation — full name (`Addition`), short name (`Add`), or symbol (`+`). Includes a division-by-zero guard.

**Highlights:**
- Multi-format operator input (`Add` / `add` / `+`)
- Division by zero handled gracefully
- Clean `if / elif / else` routing

📁 [View Project →](./Basic%20Calculator)

---

### 📐 2. Theorem Verifier

<p>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
</p>

An interactive theorem verification and formula calculation tool supporting **10 mathematical functions** — from Pythagoras to Heron's Formula and Vector Magnitude.

Driven by a numbered menu, each function is cleanly isolated into its own Python function.

**Highlights:**
- 10 theorems and formulas in one tool
- Modular design — one function per theorem
- Uses Python's `math` and `time` modules

📁 [View Project →](./Theorem%20Verifier)

---

### 🚀 3. Project ICARUS

<p>
  <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-Text%20Adventure%20Game-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
</p>

A full text-based survival RPG set aboard a failing deep-space vessel. Navigate **5 interconnected regions**, solve riddles, crack codes, manage a draining oxygen meter, and defeat a rogue AI mainframe.

The most ambitious project in the repository — featuring global state management, condition-gated navigation, attempt-based puzzles, and a full restart-on-death system.

**Highlights:**
- Live oxygen stat that drains with every mistake
- 5 distinct rooms: Medical Bay → Control Hall → Life Support → Science Lab → Core Control
- Code puzzles, riddles, and a final logic puzzle
- Auto-restart system on death with full state reset

```
[1] Medical Room ──► [2] Main Control Hall
                              │
               ┌──────────────┴──────────────┐
          [3] Life Support          [4] Science Lab
               └──────────────┬──────────────┘
                               │
                    [5] Core Control Room ← FINAL BOSS
```

📁 [View Project →](./Project%20ICARUS)

---

### 📊 4. Student Marks Calculator

<p>
  <img src="https://img.shields.io/badge/Level-Beginner--Intermediate-yellow?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-Academic%20Tool-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
</p>

A report generator that collects marks for multiple students across any number of subjects and produces a formatted academic report — with **Total Marks, Percentage, CGPA, and Grade** — all inside an animated progress bar reveal.

**Highlights:**
- Supports multiple students, each with different subject counts
- Animated `█` block progress bar while report generates
- CGPA and grade auto-calculated (`A+` → `F`)
- Session loop — run multiple batches without restarting

| CGPA | Grade |
|------|-------|
| ≥ 9.0 | A+ |
| ≥ 8.0 | A |
| ≥ 7.0 | B |
| ≥ 6.0 | C |
| ≥ 5.0 | D |
| < 5.0 | F |

📁 [View Project →](./Student%20Marks%20Calculator)

---

### 🔢 5. Tally Counter

<p>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Utility-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
</p>

A minimal interactive counter that simulates a physical tally clicker — increment, decrement, reset, and exit through a simple persistent menu loop.

Small in scope but sharp in focus — demonstrating the core **state → input → update → display** loop at the heart of every interactive program.

**Highlights:**
- Live count display after every action
- Persistent `while True` session loop
- Menu printed using list + `"\n".join()`

📁 [View Project →](./Tally%20Counter)

---

### 📅 6. Calendar Program

<p>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Utility-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
</p>

A clean command-line tool that prints a formatted monthly calendar for any year and month — powered entirely by Python's built-in `calendar` module.

Enter a year and month, view the calendar, then choose to print another or exit — all through a recursive session loop.

**Highlights:**
- Prints any month of any year on demand
- Uses `calendar.month()` for instant formatted output
- Recursive function call keeps the session running without a `while` loop
- Graceful exit with goodbye message; unexpected input terminates cleanly

**Example Output:**
```
   August 2025
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```

📁 [View Project →](./Calendar%20Program)

---

### 🔳 7. QR Code Generator

<p>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/External%20Package-qrcode-red?style=flat-square"/>
</p>

A command-line tool that converts any **text or URL** into a QR code and optionally saves it as a **PNG image file** — the first project in this repository to use an external Python package.

**Highlights:**
- Generates a QR code for any text or URL
- Saves output as a named `.png` with custom black-and-white colours
- First project using `pip` and a third-party library (`qrcode` + `Pillow`)
- Introduces object-oriented usage — instantiating a class and calling its methods

> ⚠️ **Requires external packages:** `pip install qrcode[pil]`

📁 [View Project →](./QR%20Code%20Generator)

---

### 🔐 8. Password Generator

<p>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
</p>

A secure random password generator that builds passwords from a full **88-character pool** — lowercase, uppercase, digits, and symbols — at any length the user specifies.

Features `try/except` error handling for the first time in this repository, and uses `random.sample()` to ensure no character repeats within a single password.

**Highlights:**
- Full character set: `a-z`, `A-Z`, `0-9`, `! @ # $ & /`
- `random.sample()` guarantees no repeated characters per password
- First use of `try / except ValueError` for robust input validation
- Recursive session loop — generate back-to-back passwords without restarting

📁 [View Project →](./Password%20Generator)

---

### 🎬 9. StreamFlix Clone

<p>
  <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/Type-CLI%20App-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square"/>
</p>

A command-line simulation of a streaming subscription service — inspired by Netflix. Users can **sign up** with a plan, **log in** to view their account, and navigate through a persistent session menu.

The most data-driven project in the repository — introducing nested dictionaries, lists of dictionaries as an in-memory user database, and auto-stamped dates at runtime.

**Highlights:**
- 4 subscription plans: Basic (₹299), Standard (₹499), Premium (₹699), Family (₹999)
- Sign-up stores a full user record including plan, payment method, and start date
- Login searches the user list by name with case-insensitive matching
- `datetime.date.today()` auto-stamps the subscription start date

| Plan | Price | Devices |
|------|-------|---------|
| Basic | ₹299 | 1 |
| Standard | ₹499 | 2 |
| Premium | ₹699 | 3 |
| Family | ₹999 | 5 |

📁 [View Project →](./StreamFlix)

---

## 🧠 Learning Focus

The projects in this repository develop practical experience across:

<p>
  <img src="https://img.shields.io/badge/Variables%20%26%20Data%20Types-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Loops%20%26%20Control%20Flow-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Functions%20%26%20Recursion-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Dictionaries%20%26%20Data%20Structures-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/try%2Fexcept%20Error%20Handling-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Input%20Validation-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Game%20State%20Management-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Built--in%20%26%20External%20Modules-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/File%20I%2FO-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Data%20Modelling-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/CLI%20Application%20Design-✔-blueviolet?style=flat-square"/>
</p>

- Python fundamentals — variables, data types, operators
- Conditional statements — `if / elif / else`
- Loops and control flow — `while`, `for`, `break`
- Functions, modular programming, and recursion
- Lists, dictionaries, and nested data structures
- `try / except` — exception and error handling
- Input handling and validation
- Global state management across functions
- Built-in modules — `math`, `time`, `sys`, `calendar`, `random`, `datetime`
- External packages — `qrcode`, `Pillow` via `pip`
- File I/O — saving generated output to disk
- Data modelling — structuring real-world entities as Python data structures
- CLI application design and user experience
- Problem-solving and algorithmic thinking

---

## ⚙️ Development Approach

```text
Learn → Experiment → Build → Debug → Improve
                        ↑          ↓
                        └──────────┘
```

Each project is an opportunity to apply what I've learned and discover something new. Earlier projects are intentionally simple — later ones reflect increasingly complex ideas and problem-solving.

---

## 🚀 Getting Started

### Requirements

```
Python 3.x
Git
```

> ✅ Projects 1–6, 8, 9 use Python's built-in modules only — no extra installation needed.  
> ⚠️ **Project 7 (QR Code Generator)** requires an external package — see below.

### Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### Navigate to the Repository

```bash
cd Python-Projects
```

### Run a Project

Navigate to the project folder and run its Python file:

```bash
cd "Basic Calculator"
python Basic_Calculator.py
```

### QR Code Generator — Extra Step

```bash
cd "QR Code Generator"
pip install qrcode[pil]
python QR_Code_Generator.py
```

Each project directory contains its own `README.md` with full instructions, examples, and notes.

---

## 📁 Repository Structure

```
📦 Python-Projects/
│
├── 📂 Basic Calculator/
│   ├── 📄 Basic_Calculator.py
│   └── 📄 README.md
│
├── 📂 Theorem Verifier/
│   ├── 📄 Theorem_Verifier.py
│   └── 📄 README.md
│
├── 📂 Project ICARUS/
│   ├── 📄 ICARUS.py
│   └── 📄 README.md
│
├── 📂 Student Marks Calculator/
│   ├── 📄 Marks_Calculator.py
│   └── 📄 README.md
│
├── 📂 Tally Counter/
│   ├── 📄 Tally_Counter.py
│   └── 📄 README.md
│
├── 📂 Calendar Program/
│   ├── 📄 Calendar.py
│   └── 📄 README.md
│
├── 📂 QR Code Generator/
│   ├── 📄 QR_Code_Generator.py
│   └── 📄 README.md
│
├── 📂 Password Generator/
│   ├── 📄 Password_Generator.py
│   └── 📄 README.md
│
├── 📂 StreamFlix Clone/
│   ├── 📄 StreamFlix.py
│   └── 📄 README.md
│
├── 📄 LICENSE
└── 📄 README.md
```

> New projects will be added as separate directories as the journey continues.

---

## 🔮 Future Direction

This repository will keep growing alongside my Python learning. Upcoming projects may explore:

- 🤖 Automation scripts
- 📁 File and data handling
- 🗄️ Databases and storage
- 📈 Algorithms and data structures
- 🔌 Python for electronics and engineering (ECE focus)
- 🖥️ GUI applications using Tkinter
- 🌐 Web-based Python tools

---

## 🎯 Purpose of This Repository

This is more than a collection of Python programs.

It is a **record of my progress as I learn to program** — each project represents a problem I attempted to solve, a concept I wanted to understand, or an idea I wanted to turn into working software.

Over time, this repository will reflect not just the projects I have built, but how my thinking, skills, and ambition as a developer have grown.

---

## 👨‍💻 Author

**Sri Chandra**

<p>
  <img src="https://img.shields.io/badge/GitHub-srichandratech--del-181717?style=for-the-badge&logo=github&logoColor=white"/>
</p>

---

<h3><p align="center"><b>Learning by building. 🌱</b></p></h3>

<p align="center">
  <img src="https://img.shields.io/badge/Made%20with-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Journey-Ongoing-orange?style=for-the-badge"/>
</p>

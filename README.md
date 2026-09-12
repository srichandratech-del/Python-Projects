<h1><p align="center"><b>🐍 Python Projects</b></p></h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Projects-5-181717?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/badge/Status-Active-2ea44f?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/CLI%20Tools-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Text%20Adventure-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Math%20Tools-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Academic%20Tools-✔-blue?style=flat-square"/>
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

## 🧠 Learning Focus

The projects in this repository develop practical experience across:

<p>
  <img src="https://img.shields.io/badge/Variables%20%26%20Data%20Types-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Loops%20%26%20Control%20Flow-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Functions-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Lists%20%26%20Data%20Structures-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Input%20Validation-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Game%20State%20Management-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/math%20%26%20sys%20%26%20time%20Modules-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/CLI%20Application%20Design-✔-blueviolet?style=flat-square"/>
</p>

- Python fundamentals — variables, data types, operators
- Conditional statements — `if / elif / else`
- Loops and control flow — `while`, `for`, `break`
- Functions and modular programming
- Lists, data structures, and `append` / `sum` / `join`
- Input handling and validation
- Global state management across functions
- Built-in modules — `math`, `time`, `sys`
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

> ✅ No external dependencies required for any current project — all use Python's built-in modules only.

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
├── 📄 LICENSE
└── 📄 README.md
```

> New projects will be added as separate directories as the journey continues.

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

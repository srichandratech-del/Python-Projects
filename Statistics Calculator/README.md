# 📊 Statistics Calculator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-blueviolet?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Mean-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Median-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Mode-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Frequency%20Distribution-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**Statistics Calculator** is a Python command-line tool that computes the three core measures of central tendency — **Mean, Median, and Mode** — from frequency distribution data entered by the user.

Unlike simple list-based calculators, this tool works with **x values and their corresponding frequencies** — the standard format used in statistics and data analysis — making it practical for academic and real-world data sets.

Built as part of my **Python learning journey**, this project deepened my understanding of list operations, parallel data processing, cumulative frequency logic, and modular function design.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📐 **Mean Calculator** | Computes weighted mean using `Σ(x × f) / Σf` |
| 📍 **Median Calculator** | Finds median via cumulative frequency and N/2 position |
| 🏆 **Mode Calculator** | Identifies the value with the highest frequency |
| 🔁 **Persistent Menu** | `while True` loop lets you run multiple calculations per session |
| 🛡️ **Input Validation** | Checks for mismatched list lengths and empty inputs |
| 📋 **Frequency Display** | Prints frequency and cumulative frequency lists alongside results |

---

## 📐 Formulas Used

| Measure | Formula | Description |
|---------|---------|-------------|
| **Mean** | `Σ(x × f) / Σf` | Sum of products divided by total frequency |
| **Median** | Value at `N/2` in cumulative frequency | First `cf` value ≥ half the total |
| **Mode** | `x` where `f` is maximum | Value with the highest frequency |

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/Functions-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Lists%20%26%20Append-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Parallel%20List%20Processing-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20Split%20%26%20Int%20Cast-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Cumulative%20Frequency-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/max()%20%26%20index()-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/while%20Loop-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Input%20Validation-✔-blueviolet?style=flat-square"/>
</p>

- **Functions** — `mean_calculator()`, `median_calculator()`, `mode_calculator()`, and `main()` cleanly separated
- **Lists & `.append()`** — building `X` and `FR` lists from comma-separated user input
- **`.split(',')` + `int()` cast** — parsing raw string input into usable integer lists
- **Parallel list processing** — iterating `X` and `FR` together using `range(len(X))`
- **Cumulative Frequency** — building `cf[]` with a running total to locate the median position
- **`max()` + `.index()`** — finding the mode by locating the highest frequency and mapping it to `X`
- **`sum()`** — totalling frequency lists for mean and median calculations
- **`while True` loop** — persistent menu routing until exit is chosen
- **Input validation** — length mismatch check and empty list guard before any calculation runs

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — pure built-in Python only.

---

## 📁 Project Structure

```
📦 Statistics Calculator/
│
├── 📄 Statistics_Calculator.py     # Main program file
└── 📄 README.md                    # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd "Python-Projects/Statistics Calculator"
```

### 3. Run the Program

```bash
python Statistics_Calculator.py
```

---

## 💻 Example Usage

**Calculating the Mean**
```
----------------------------------------
| Welcome to the Statistics Calculator |
----------------------------------------
Options:
1. Calculate Median
2. Calculate Mean
3. Calculate Mode
4. Exit
--------------------
Enter your choice (1-4): 2

Enter the values of x separated by commas: 10,20,30,40,50
Enter the values of frequencies separated by commas: 2,3,5,4,1

------------------------------
Frequencies: [2, 3, 5, 4, 1]
Mean: 29.333333333333332
------------------------------
```

**Calculating the Median**
```
Enter your choice (1-4): 1

Enter the values of x separated by commas: 10,20,30,40,50
Enter the values of frequencies separated by commas: 2,3,5,4,1

------------------------------
Cumulative Frequency: [2, 5, 10, 14, 15]
Median: 30
------------------------------
```

**Calculating the Mode**
```
Enter your choice (1-4): 3

Enter the values of x separated by commas: 10,20,30,40,50
Enter the values of frequencies separated by commas: 2,3,5,4,1

------------------------------
Frequencies: [2, 3, 5, 4, 1]
Mode: 30
------------------------------
```

**Input Validation**
```
Enter the values of x separated by commas: 10,20,30
Enter the values of frequencies separated by commas: 2,3

Error: The lengths of x and fr must be the same.
```

**Exiting**
```
Enter your choice (1-4): 4

------------------------------
Exiting the program.
Thank you for using the Statistics Calculator!
------------------------------
```

---

## 🔮 Future Improvements

- [ ] 📈 Add **Range**, **Variance**, and **Standard Deviation** calculations
- [ ] 🛡️ Add `try/except` to handle non-numeric input gracefully
- [ ] 📊 Display a frequency distribution table before results
- [ ] 🖨️ Allow grouped data input (class intervals) for the median formula
- [ ] 💾 Export results to a `.txt` or `.csv` report file
- [ ] 📉 Add a bar chart of frequencies using `matplotlib`
- [ ] 🖥️ Build a GUI version using Tkinter

---

## 📚 Learning Outcome

This project tackled real statistical logic in Python — no shortcuts. Key takeaways:

- How to **process two parallel lists** (values and frequencies) together using index-based loops
- Building **cumulative frequency** manually with a running total — understanding the logic behind the median algorithm
- How `.split(',')` + a list comprehension / `append` loop converts raw string input into a workable data structure
- Why **validating list lengths before processing** is essential when two inputs must be paired
- That `max()` and `.index()` together make finding the mode clean and concise

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
  <img src="https://img.shields.io/badge/Mean%20|%20Median%20|%20Mode-Solved-green?style=for-the-badge"/>
</p>

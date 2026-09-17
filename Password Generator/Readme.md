# 🔐 Password Generator

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Beginner-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-orange?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/random-module-yellowgreen?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/time-module-yellowgreen?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/try%2Fexcept-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Recursive%20Functions-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**Password Generator** is a Python command-line tool that generates a **cryptographically shuffled, random password** of any length — built from a full character set of lowercase, uppercase, digits, and symbols.

Built as part of my **Python learning journey**, this project introduced `try/except` error handling, `random.sample()` for non-repeating character selection, and recursive function calls to keep the session running cleanly.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔡 **Full Character Set** | Combines lowercase, uppercase, numbers, and symbols for strong passwords |
| 📏 **Custom Length** | User defines the exact character length of the password |
| 🔀 **True Randomness** | Uses `random.sample()` — no repeated characters in a single password |
| 🛡️ **Input Validation** | Rejects non-integer and zero/negative length inputs with `try/except` |
| 🔁 **Multi-Session Loop** | Generate back-to-back passwords without restarting the program |
| ✨ **Formatted Output** | Clean bordered display with emoji indicators and a timed reveal |

---

## 🔣 Character Set

| Type | Characters |
|------|-----------|
| Lowercase | `a b c d e f g h i j k l m n o p q r s t u v w x y z` |
| Uppercase | `A B C D E F G H I J K L M N O P Q R S T U V W X Y Z` |
| Numbers | `0 1 2 3 4 5 6 7 8 9` |
| Symbols | `! @ # $ & /` |
| **Total Pool** | **88 characters** |

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/random%20Module-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/time%20Module-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/try%2Fexcept-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Recursive%20Functions-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20Concatenation-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/str.join()-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/F--Strings-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Input%20Validation-✔-blueviolet?style=flat-square"/>
</p>

- **`random` Module** — using `random.sample()` to pick unique characters from the full pool
- **`str.join()`** — assembling the sampled character list into a single password string
- **`try / except ValueError`** — first use of exception handling to catch non-integer input gracefully
- **`time.sleep()`** — brief delay before revealing the generated password for effect
- **Recursive Functions** — `password_generator()` and `Continue()` call each other to loop the session
- **String Concatenation** — building the full character pool by joining four character-set strings
- **F-strings** — displaying the password and its length in a formatted output block
- **Input Validation** — guarding against empty, non-numeric, zero, and negative length values

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — uses only Python's built-in `random` and `time` modules.

---

## 📁 Project Structure

```
📦 Password Generator/
│
├── 📄 Password_Generator.py     # Main program file
└── 📄 README.md                 # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd "Python-Projects/Password Generator"
```

### 3. Run the Program

```bash
python Password_Generator.py
```

---

## 💻 Example Usage

**Generating a password**
```
=======================================================
            🔐 PASSWORD GENERATOR
-------------------------------------------------------
  Create a secure random password in seconds!

=======================================================
  🔢 Enter the length of password: 12
-------------------------------------------------------
  🔐 Generated Password
-------------------------------------------------------
  Password : k#3Tz!Rp9Aw@
  Length   : 12
-------------------------------------------------------

=======================================================
  🔄 Generate another password? (yes/no): yes
=======================================================

  🔢 Enter the length of password: 8
-------------------------------------------------------
  🔐 Generated Password
-------------------------------------------------------
  Password : M5&bXq!v
  Length   : 8
-------------------------------------------------------

=======================================================
  🔄 Generate another password? (yes/no): no

-------------------------------------------------------
  ✨ Thank you for using the Password Generator!
  🔐 Stay secure and keep your passwords strong!
-------------------------------------------------------
```

**Invalid input handling**
```
  🔢 Enter the length of password: abc

  ❌ Invalid input. Please enter a positive integer.

  🔢 Enter the length of password: -5

  ❌ Invalid input. Please enter a positive integer.
```

---

## 🔮 Future Improvements

- [ ] 🔁 Replace recursion with a `while` loop to prevent stack overflow on many iterations
- [ ] 📋 Copy the generated password to clipboard using `pyperclip`
- [ ] ⚙️ Let user choose which character types to include (e.g. symbols only, no numbers)
- [ ] 💯 Add a password strength indicator (Weak / Medium / Strong)
- [ ] 💾 Save generated passwords to a `.txt` log file
- [ ] 🔢 Add a bulk mode — generate multiple passwords at once
- [ ] 🖥️ Build a GUI version using Tkinter with a copy button

---

## 📚 Learning Outcome

This project introduced two important new concepts to the journey. Key takeaways:

- **`try / except`** — how to catch and handle runtime errors (like `ValueError`) gracefully instead of crashing
- **`random.sample()`** — the difference between `random.choice()` (allows repeats) and `random.sample()` (unique picks only), and why the latter produces stronger passwords
- How recursive functions can create a natural flow between program stages without a loop
- Building a **polished CLI experience** with emoji, borders, and timed output using only standard Python

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
  <img src="https://img.shields.io/badge/Stay%20Secure-Always-red?style=for-the-badge"/>
</p>

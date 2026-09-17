# 🎬 StreamFlix Clone

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20App-blueviolet?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/datetime-module-yellowgreen?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Dictionaries-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/User%20Auth%20System-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Subscription%20Management-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**StreamFlix Clone** is a Python command-line simulation of a streaming service — inspired by platforms like Netflix. Users can **sign up** with a subscription plan, **log in** to view their account details, and manage sessions through a persistent main menu loop.

Built as part of my **Python learning journey**, this is the most data-driven project so far — introducing nested dictionaries for structured data, runtime user records stored in a list, and a real-world simulation of an authentication and subscription system.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📝 **Sign Up** | Register with name, age, gender, subscription plan, and payment method |
| 🔑 **Log In** | Retrieve full account details by name from the active session |
| 💳 **4 Subscription Plans** | Basic, Standard, Premium, and Family — each with unique price, duration, and device limit |
| 📅 **Auto Date Stamping** | Subscription start date is automatically set to today using `datetime` |
| 🔁 **Persistent Session Loop** | Main menu runs continuously until the user chooses to exit |
| 🗂️ **In-Memory User Store** | All registered users are stored in a list of dictionaries for the session |

---

## 💳 Subscription Plans

| Plan | Price | Duration | Devices |
|------|-------|----------|---------|
| **Basic** | ₹299 | 1 Month | 1 |
| **Standard** | ₹499 | 1 Month | 2 |
| **Premium** | ₹699 | 1 Month | 3 |
| **Family** | ₹999 | 1 Month | 5 |

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/Nested%20Dictionaries-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Lists%20of%20Dictionaries-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/datetime%20Module-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Functions-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/for%20Loop%20Search-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/while%20Loop-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20Methods-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Data%20Modelling-✔-blueviolet?style=flat-square"/>
</p>

- **Nested Dictionaries** — `subscription_types` stores structured plan data (price, duration, devices) per key
- **Lists of Dictionaries** — `data[]` acts as an in-memory user database, each entry a full user record
- **`datetime` Module** — `datetime.date.today()` auto-captures the sign-up date at runtime
- **Functions** — `sign_up()` and `log_in()` cleanly separate the two core workflows
- **`for` Loop Search** — iterating through `data` to find a matching username for login
- **`.lower()` Comparison** — case-insensitive name matching during log in
- **`while True` Loop** — keeps the main menu alive until exit is chosen
- **Data Modelling** — structuring real-world entities (users, plans) as Python data structures

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — uses only Python's built-in `datetime` module.

---

## 📁 Project Structure

```
📦 StreamFlix Clone/
│
├── 📄 StreamFlix.py        # Main program file
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
cd "Python-Projects/StreamFlix Clone"
```

### 3. Run the Program

```bash
python StreamFlix.py
```

---

## 💻 Example Usage

**Sign Up**
```
==========================
| Welcome to StreamFlix! |
==========================

1. Sign Up
2. Log In
3. Exit

Enter your choice (1/2/3): 1

========================================
          SIGN UP
========================================
Enter your name: Arjun
Enter your age: 21
Enter your gender: Male

Subscription Types:
1. Basic     : Price - ₹299 | Duration - 1 month | Devices - 1
2. Standard  : Price - ₹499 | Duration - 1 month | Devices - 2
3. Premium   : Price - ₹699 | Duration - 1 month | Devices - 3
4. Family    : Price - ₹999 | Duration - 1 month | Devices - 5

Choose your subscription type (1/2/3/4): 3
Enter your payment method (Credit Card/Debit Card/PayPal): Credit Card

========================================
       SIGN UP SUCCESSFUL
========================================
Welcome, Arjun !
Subscription: Premium
Price: ₹699
Payment Method: Credit Card
Start Date: 2026-09-17
Duration: 1 month
Devices: 3
```

**Log In**
```
Enter your choice (1/2/3): 2

========================================
          LOG IN
========================================
Enter your name: arjun

========================================
          WELCOME BACK
========================================
Name: Arjun
Age: 21
Gender: Male
Subscription: Premium
Price: ₹699
Payment Method: Credit Card
Start Date: 2026-09-17
Duration: 1 month
Devices: 3
```

**Exit**
```
Enter your choice (1/2/3): 3
Thank you for using StreamFlix!
```

---

## 🔮 Future Improvements

- [ ] 🔑 Add password-based authentication for secure login
- [ ] 💾 Persist user data to a `.json` or `.csv` file so records survive between sessions
- [ ] ❌ Add account deletion and subscription cancellation
- [ ] 🔄 Allow users to upgrade or downgrade their subscription plan
- [ ] 📅 Calculate and display subscription expiry date
- [ ] 👥 List all registered users (admin view)
- [ ] 🗄️ Integrate with a database (`sqlite3`) for proper persistent storage
- [ ] 🖥️ Build a GUI version using Tkinter

---

## 📚 Learning Outcome

StreamFlix was the most structured and data-rich project built so far. Key takeaways:

- How to model **real-world entities** (users, plans) as Python dictionaries and lists
- Using a **list of dictionaries** as a simple in-memory database
- How `datetime.date.today()` can automatically stamp records at runtime
- Writing a **login search** by iterating a data list and comparing values
- How separating concerns into functions (`sign_up`, `log_in`) makes a program scalable and readable

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
  <img src="https://img.shields.io/badge/Stream-Everything-E50914?style=for-the-badge"/>
</p>

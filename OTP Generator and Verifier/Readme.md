# 🔑 OTP Generator & Verifier

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-CLI%20Tool-blueviolet?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/random-module-yellowgreen?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/time-module-yellowgreen?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/File%20I%2FO-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Cross--File%20Import-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Attempt%20Limiter-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**OTP Generator & Verifier** is a two-file Python system that simulates a real **One-Time Password (OTP) authentication flow** — the same mechanism used by banking apps, login systems, and 2FA services.

`OTP_Generator.py` creates a 5-digit OTP and saves it to a shared file. `OTP_Verifier.py` reads that file and challenges the user to enter the correct OTP within **3 attempts** — with the option to regenerate and retry the full cycle.

This is the first project in this repository to span **two scripts** that communicate via a shared file, and the first to use **cross-module imports** at runtime.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔢 **5-Digit OTP** | Generates a random integer between `10000` and `99999` |
| 💾 **File-Based Handoff** | OTP is written to `otp.txt` by the generator and read by the verifier |
| 🔁 **3-Attempt Limit** | User has exactly 3 tries before verification is locked out |
| ♻️ **Regenerate & Retry** | After a session, user can generate a fresh OTP and verify again |
| 🔗 **Cross-File Import** | Verifier imports `OTP_Generator` at runtime to trigger regeneration |
| ⏱️ **Timed Transition** | `time.sleep()` adds a brief delay between generation and verification |

---

## 🗂️ How the Two Files Work Together

```
┌─────────────────────────┐        writes        ┌──────────────┐
│   OTP_Generator.py      │ ──────────────────►  │   otp.txt    │
│  random.randint(...)    │                       │  e.g. 47391  │
└─────────────────────────┘                       └──────┬───────┘
                                                         │ reads
                                                         ▼
                                                ┌─────────────────────────┐
                                                │   OTP_Verifier.py       │
                                                │  3-attempt verify loop  │
                                                │  imports OTP_Generator  │
                                                │  on regenerate request  │
                                                └─────────────────────────┘
```

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/random%20Module-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/File%20Read%20%26%20Write-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/with%20Statement-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/while%20Loop%20%2B%20Counter-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Cross--Module%20Import-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Recursive%20Functions-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/time%20Module-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20Comparison-✔-blueviolet?style=flat-square"/>
</p>

- **`random.randint()`** — generating a bounded 5-digit random integer
- **File I/O with `with` statement** — writing OTP to disk and reading it back safely with automatic file closing
- **`while` loop + attempt counter** — limiting user to exactly 3 verification attempts
- **Cross-module import** — `OTP_Verifier.py` dynamically imports `OTP_Generator` at runtime to call `generate_otp()`
- **Recursive `Continue()`** — looping the regenerate/verify cycle without a `while` loop
- **`time.sleep()`** — pause between OTP generation and verification prompt
- **String comparison** — OTP from file is read as a string and compared directly to user input

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — uses only Python's built-in `random` and `time` modules.

---

## 📁 Project Structure

```
📦 OTP System/
│
├── 📄 OTP_Generator.py     # Generates OTP and saves to otp.txt
├── 📄 OTP_Verifier.py      # Reads otp.txt runs the 3 attempt verification
├── 📄 otp.txt              # Shared file — created at runtime by generator
└── 📄 README.md            # Project documentation
```

> ⚠️ `otp.txt` is created automatically when `OTP_Generator.py` runs. Do not create it manually.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/srichandratech-del/Python-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd "Python-Projects/OTP System"
```

### 3. Run the Verifier

The verifier automatically triggers the generator first:

```bash
python OTP_Verifier.py
```

> You can also run the generator standalone to create a fresh OTP without verifying:
> ```bash
> python OTP_Generator.py
> ```

---

## 💻 Example Usage

**Successful Verification**
```
========================================
          OTP GENERATOR
========================================
----------------------------------------
✅ OTP GENERATED SUCCESSFULLY!
----------------------------------------
========================================
       OTP READY FOR VERIFICATION
========================================

========================================
        OTP VERIFICATION SYSTEM
========================================
----------------------------------------
Attempts remaining: 3
----------------------------------------
Enter OTP: 47391
----------------------------------------
✅ OTP VERIFIED SUCCESSFULLY!
----------------------------------------
Do you want to generate a new OTP? (yes/no): no
========================================
       ❌ OTP VERIFICATION STOPPED
========================================
Exiting the program. Goodbye!
========================================
```

**Failed Verification — Max Attempts**
```
----------------------------------------
Attempts remaining: 3
----------------------------------------
Enter OTP: 12345
----------------------------------------
❌ INVALID OTP!
----------------------------------------
Attempts remaining: 2
----------------------------------------
Enter OTP: 99999
----------------------------------------
❌ INVALID OTP!
----------------------------------------
Attempts remaining: 1
----------------------------------------
Enter OTP: 00000
----------------------------------------
❌ INVALID OTP!
----------------------------------------
========================================
     ❌ MAXIMUM ATTEMPTS REACHED
       VERIFICATION STOPPED
========================================
Do you want to generate a new OTP? (yes/no): yes
```

---

## 🔮 Future Improvements

- [ ] 🕐 Add OTP expiry — invalidate the OTP after a set time (e.g. 30 seconds)
- [ ] 🔢 Add configurable OTP length (4-digit, 6-digit, 8-digit)
- [ ] 🔒 Hash the OTP in `otp.txt` instead of storing it in plain text
- [ ] 📧 Simulate OTP delivery via email using `smtplib`
- [ ] 📱 Add an SMS simulation layer
- [ ] 🗄️ Replace `otp.txt` with a proper database (`sqlite3`)
- [ ] 🖥️ Build a GUI version using Tkinter with a countdown timer

---

## 📚 Learning Outcome

This project introduced the concept of **two programs communicating through a shared file** — a pattern used in real-world systems. Key takeaways:

- How to use the `with` statement for safe, clean file reading and writing
- That `input()` always returns a string — so storing and comparing the OTP as a string (not int) is intentional and correct here
- How to **import another script as a module** at runtime to reuse its functions
- Building a realistic authentication flow — generation → delivery (file) → verification → lockout — using only core Python

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
  <img src="https://img.shields.io/badge/Verify-Or%20Lockout-red?style=for-the-badge"/>
</p>

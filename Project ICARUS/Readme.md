# 🚀 Project ICARUS

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Type-Text%20Adventure%20Game-blueviolet?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/sys-module-yellowgreen?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Global%20State%20Management-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/Oxygen%20Survival%20System-✔-red?style=flat-square"/>
  <img src="https://img.shields.io/badge/Multi--Room%20Navigation-✔-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/No%20External%20Packages-Required-lightgrey?style=flat-square"/>
</p>

---

## 🧾 Overview

**Project ICARUS** is a Python-powered, text-based survival adventure game set aboard a failing deep-space research vessel.

The hull has been breached. Systems are collapsing. Your oxygen is draining. Navigate through **5 interconnected regions**, crack codes, solve riddles, manage your dwindling oxygen supply, and outwit a rogue AI mainframe — all before you suffocate in the cold vacuum of space.

Built as part of my **Python learning journey**, this project pushed me into advanced territory: global state management, multi-function game loops, condition-gated room navigation, and building a full narrative experience using only Python's core tools.

---

## 🗺️ Game World — Region Map

```
┌─────────────────────────────────────────────────────────┐
│                    ICARUS SHIP LAYOUT                   │
├─────────────────────────────────────────────────────────┤
│                                                         │
│   [1] MEDICAL ROOM  ──►  [2] MAIN CONTROL HALL          │
│        (Start)                    │                     │
│                         ┌─────────┴──────────┐          │
│                         │                    │          │
│                    [3] LIFE             [4] SCIENCE      │
│                    SUPPORT              LAB ROOM         │
│                     ROOM               (Extinguisher)   │
│                   (Oxygen Suit)                          │
│                         │                    │          │
│                         └─────────┬──────────┘          │
│                                   │                     │
│                          [5] CORE CONTROL ROOM           │
│                              (FINAL BOSS)               │
└─────────────────────────────────────────────────────────┘
```

---

## ⚙️ Game Mechanics

| Mechanic | Description |
|----------|-------------|
| 🫁 **Oxygen System** | Starts at `80%`. Drains with every wrong answer and action. Reach `0%` → game over |
| 🔒 **Condition Gates** | Rooms and paths only unlock when you have the right items or stats |
| 🎒 **Inventory** | Carry a Fire Extinguisher — required to clear the path to the final room |
| 💀 **Permadeath** | Run out of oxygen or exhaust all attempts → ship resets, you restart |
| 🔁 **Auto-Restart** | A revival protocol resets all state and sends you back to Room 1 |
| 🧩 **Puzzles** | Pressure calibration, code-cracking, riddles, and a final logic puzzle |

---

## 🏠 Regions & Challenges

### 1️⃣ Medical Room *(Starting Zone)*
- Use a first aid kit to boost Oxygen by `+20%`
- Calibrate pod pressure from **10 PSI → exactly 50 PSI**
- Each pressure adjustment costs `5%` Oxygen
- Wrong commands loop until correct

### 2️⃣ Main Control Hall *(Hub)*
- Central navigation point linking all other rooms
- Fire blocks the path to the Control Room
- Requirements to pass the fire:
  - ✅ Must possess the Fire Extinguisher
  - ✅ Oxygen must be `≥ 90%`

### 3️⃣ Life Support Room *(Code Puzzle)*
- 3-digit security override code locks the Oxygen reserves
- **3 attempts** — each failure: `-10% Oxygen`
- Solve astronomy-based riddles to derive the code
- Success: Oxygen boosted to `200%`
- Fail all 3: room vents atmosphere → restart

### 4️⃣ Science Lab Room *(Dual Riddle Lock)*
- Fire extinguisher locked behind **2 sequential riddles**
- **3 attempts each** — each failure: `-10% Oxygen`
- Riddle 1: *Physics / Space phenomenon*
- Riddle 2: *Wordplay / lateral thinking*
- Fail either riddle: safety gas deployed → restart

### 5️⃣ Core Control Room *(Final Boss)*
- Face the rogue AI mainframe
- Solve the **Master Logic Puzzle**
- **5 attempts** — each failure: `-50% Oxygen` ⚠️
- One correct answer wins the game

---

## 🧠 Concepts Practiced

<p>
  <img src="https://img.shields.io/badge/Global%20Variables-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Functions-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/While%20Loops-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Conditional%20Statements-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Game%20State%20Management-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/sys%20Module-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/String%20Methods-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Attempt%20Counters-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/Recursive%20Room%20Calls-✔-blueviolet?style=flat-square"/>
  <img src="https://img.shields.io/badge/F--Strings-✔-blueviolet?style=flat-square"/>
</p>

- **Global Variables** — tracking `Oxygen`, `has_extinguisher`, `life_room_solved` across all rooms
- **Functions** — one function per room, cleanly separated and self-contained
- **While Loops** — driving puzzle attempt counters and pressure calibration loops
- **Conditional Gate Logic** — item checks and stat checks locking or unlocking paths
- **Game State Management** — full state reset via `restart_game()` on death
- **`sys` Module** — using `sys.exit()` for a clean win-state termination
- **String Methods** — `.strip().lower()` for robust input normalization
- **F-strings** — live status displays showing Oxygen and attempt counts mid-game
- **Recursive Room Calls** — rooms calling themselves or other rooms to maintain flow

---

## 📋 Requirements

```
Python 3.x
```

> ✅ No external packages required — uses only Python's built-in `sys` module.

---

## 📁 Project Structure

```
📦 Project ICARUS/
│
├── 📄 ICARUS.py        # Full game — all rooms, puzzles, and logic
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
cd "Python-Projects/Project ICARUS"
```

### 3. Run the Game

```bash
python ICARUS.py
```

---

## 💻 Game Preview

```
==================================================
          WELCOME TO PROJECT: ICARUS              
==================================================
Emergency Alert: Deep-space research vessel hull breached!
Systems failing. You must survive the lockdown protocols.

=== EMERGENCY PROTOCOL INITIALIZED ===

------------MEDICAL ROOM------------
You see a first aid kit.
Type 'first aid' to use it: first aid
You use the first aid kit and heal yourself.
Your Oxygen level is now: 100

You wake up in a life-support pod. Warning sirens are blaring.
The terminal shows current pressure is at 10 PSI.
To escape the pod, you must calibrate pressure to EXACTLY 50 PSI.

[STATUS] Pressure: 10 PSI | Oxygen: 100%
Enter command ('increase' to add 10 PSI / 'decrease' to drop 10 PSI): increase
...
[SUCCESS] Pressure stabilized at 50 PSI! The pod doors hiss open.
```

```
--- FINAL REGION: CORE CONTROL ROOM ---
[MASTER LOGIC PUZZLE]
A spaceship crew consists of a Captain, an Engineer, and a Pilot.
...
Who is the only person guaranteed to tell the truth right now?

Identify the truthful crew member: captain

==========================================
CORRECT! The mainframe accepts your bypass logic.
YOU HAVE POWERED DOWN THE ROGUE SYSTEM AND WON THE GAME!
==========================================
```

---

## 🧩 Puzzle Spoiler Guide

<details>
<summary>⚠️ Click to reveal puzzle answers (SPOILERS)</summary>

| Room | Puzzle | Answer |
|------|--------|--------|
| Medical Room | Pressure Calibration | Type `increase` 4 times to reach 50 PSI |
| Life Support | 3-Digit Override Code | `290` |
| Science Lab | Riddle 1 | `photon` |
| Science Lab | Riddle 2 | `electricity` |
| Control Room | Master Logic Puzzle | `captain` |

</details>

---

## 🔮 Future Improvements

- [ ] 🗺️ Add more rooms and branching storyline paths
- [ ] 💾 Implement a save/load system for game progress
- [ ] 🎒 Expand the inventory system with multiple collectible items
- [ ] 🔊 Add sound effects using `pygame` or `playsound`
- [ ] 📊 Add a scoring system based on Oxygen remaining at win
- [ ] 🖥️ Build a terminal UI with `curses` for visual room displays
- [ ] 🤖 Add more enemy AI encounters and combat mechanics
- [ ] 🎨 Add color-coded terminal output using `colorama`

---

## 📚 Learning Outcome

Project ICARUS was my most ambitious Python project yet. It taught me how to:

- Maintain and mutate **global game state** cleanly across many functions
- Design **condition-gated navigation** where progress depends on inventory and stats
- Build **retry loops** with attempt counters and live stat feedback
- Handle a **fail-state and full reset** without crashing the program
- Think like a **game designer** — balancing difficulty, pacing, and player feedback

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
  <img src="https://img.shields.io/badge/Survive-Or%20Suffocate-red?style=for-the-badge"/>
</p>

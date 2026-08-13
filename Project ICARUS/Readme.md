# 🚀 Project: Icarus — Sci-Fi Survival Text Adventure

[![Language](https://img.shields.io/badge/Language-Python%203-blue.svg)](https://www.python.org/)
[![Topic](https://img.shields.io/badge/Category-Game%20Dev-orange.svg)](https://github.com/topics/game-development)
[![Platform](https://img.shields.io/badge/Platform-Terminal%20%2F%20Console-lightgrey.svg)](https://en.wikipedia.org/wiki/Text-based_game)

**Project: Icarus** is an immersive, text-based sci-fi survival puzzle game written entirely in Python. The player takes on the role of a surviving crew member aboard the deep-space research vessel *Icarus* following a catastrophic hull breach. With oxygen levels dropping and a rogue mainframe locking down the ship, you must use logic, resource management, and problem-solving to survive and reset the ship's core.

---

## 🕹️ Game Universe & Lore

> *"Emergency Alert: Deep-space research vessel hull breached! Systems failing. Lockdown protocols initiated."*

You awaken inside a pressurized medical pod with sirens blaring. Your suit's oxygen tank is dropping, and the path to the main bridge is blocked by an intense electrical fire. To take back control of the ship, you must navigate through various sectors, manage your oxygen supply, gather vital equipment, and solve the structural and mathematical puzzles left behind by the compromised ship AI.

---

## 🛠️ Key Gameplay & Code Mechanics

This project showcases core programming and game design concepts implemented cleanly in standard Python:

*   **Global State Management:** Tracks real-time player variables including `Oxygen` levels, puzzle completion flags (`life_room_solved`), and key inventory items (`has_extinguisher`).
*   **Dynamic Calibration Loops:** Uses directional conditional logic (`while` loops) in the Medical Pod to let players fine-tune environmental systems interactively.
*   **Non-Linear Progression:** A central node hub (`main_room()`) coordinates access across multiple sectors based on the state of your inventory and current health metrics.
*   **Integrated Fail-Safes:** Includes an automated check step (`check_Oxygen()`) running concurrently prior to actions to capture failure states instantly.

---

## 📂 Game Sectors

| Sector | Primary Objective | Hazards & Mechanics |
| :--- | :--- | :--- |
| **Medical Hall** | Calibrate Pod Pressure to 50 PSI | Continuous Oxygen Drain on movement |
| **Main Control Hall** | Navigate Hub & Assess Fire Hazard | High-heat blocking zone (Requires 90%+ Oxygen) |
| **Life Support** | Crack 3-Digit System Override Code | High-voltage security shocks (-10% Oxygen per fail) |
| **Science Lab** | Solve Dual Crypto-Terminal Riddles | Hazard gas deployment (Hard wipe on 3 failures) |
| **Core Bridge** | Solve Master Logic Puzzle vs. Mainframe AI | Heavy feedback loops (-15% Oxygen per fail) |

---

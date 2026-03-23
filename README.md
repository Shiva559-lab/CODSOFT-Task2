# CODSOFT-Task2
# 🧮 Task 2 — Simple Calculator

![Python](https://img.shields.io/badge/Python-3.7%2B-blue?style=flat-square&logo=python)
![CLI](https://img.shields.io/badge/Interface-CLI-lightgrey?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

A clean, robust **command-line calculator** built with Python. Supports six arithmetic operations with full input validation, error handling, and a loop mode for continuous calculations.

---

## 📸 Preview

```
════════════════════════════════════════
       Simple Python Calculator
════════════════════════════════════════

Enter the first number: 25
Enter the second number: 4

Select an operation:
  1. Addition       (+)
  2. Subtraction    (-)
  3. Multiplication (*)
  4. Division       (/)
  5. Modulus        (%)
  6. Exponentiation (**)

Enter your choice (1-6): 4

────────────────────────────────────────
  Result: 25 / 4 = 6.25
────────────────────────────────────────
```

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕➖✖️➗ **6 Operations** | Addition, subtraction, multiplication, division, modulus, exponentiation |
| ✅ **Input Validation** | Rejects non-numeric entries with helpful messages |
| 🛡 **Error Handling** | Catches division by zero, modulus by zero, and overflow |
| 🔢 **Smart Formatting** | Displays integers cleanly (e.g. `6` not `6.0`), decimals to 6 places |
| 🔄 **Loop Mode** | Prompts to calculate again after each result |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- No external packages required

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-projects.git
cd python-projects/task2-calculator

# Run the application
python calculator.py
```

---

## 🎯 Supported Operations

| Choice | Symbol | Operation | Example |
|---|---|---|---|
| 1 | `+` | Addition | `5 + 3 = 8` |
| 2 | `-` | Subtraction | `10 - 4 = 6` |
| 3 | `*` | Multiplication | `6 * 7 = 42` |
| 4 | `/` | Division | `22 / 7 = 3.142857` |
| 5 | `%` | Modulus | `10 % 3 = 1` |
| 6 | `**` | Exponentiation | `2 ** 8 = 256` |

---

## 🛡 Error Handling

| Scenario | Response |
|---|---|
| Non-numeric input | Re-prompts with "Invalid input" message |
| Division by zero | Prints error, exits gracefully |
| Modulus by zero | Prints error, exits gracefully |
| Result overflow | Prints error, exits gracefully |

---

## 📁 Project Structure

```
task2-calculator/
│
└── calculator.py   # Main application (single file)
```

---

## 🛠 Built With

- **Python 3** — Core language
- No external libraries — pure standard library

---

## 📜 License

This project is licensed under the MIT License.

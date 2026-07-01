# Python Programming Learning Hub

A comprehensive collection of **70+ Python exercises** covering fundamental programming concepts through hands-on practice problems. This repository is designed for learners building core Python skills from the ground up.

## 📚 What's Inside

This project contains structured, progressive exercises organized by topic:

### Core Concepts
- **Operators & Variables** (`start.py`) — Basic arithmetic, data types, string operations
- **Conditionals** (`introduction_to_python.py`) — if/elif/else, logical operators, decision-making
- **Loops** (`loops.py`, `loops_v2.py`–`loops_v5.py`) — while loops, for loops, nested loops, pattern generation
- **String Manipulation** (`string_slicing.py`) — Indexing, slicing, text processing
- **Type Conversion** (`type_conversion.py`) — Converting between data types

### Practical Applications
- Armstrong numbers and special number checks
- Tiered pricing calculations (electricity bills, scoring systems)
- Pattern printing (triangles, pyramids, nested shapes)
- Mathematical operations (factorials, power calculations, digit sums)
- Real-world scenarios (exam eligibility, weather classification, currency breakdowns)
- **Excel Data Validation** (`compare_two_bres.py`) — Cell-by-cell workbook comparison utility

## 🚀 Quick Start

Each exercise file is self-contained and runs independently:

```bash
# Run beginner concepts
python3 start.py

# Run conditional exercises (50+ decision-making problems)
python3 introduction_to_python.py

# Run loop exercises (70+ loop variations and patterns)
python3 loops.py
```

When prompted, provide input values and see the output:
```
$ python3 introduction_to_python.py
# Exercise 1: Enter a number
5
Not Divisible by Seven
```

## 📖 Learning Path

**Beginner** → Start with `start.py` to learn operators, variables, and basic I/O

**Intermediate** → Move to `introduction_to_python.py` for conditional logic and decision-making

**Advanced** → Practice `loops.py` and variants for iteration, patterns, and algorithmic thinking

## 📁 File Guide

| File | Exercises | Focus |
|------|-----------|-------|
| `start.py` | 1–5 | Basic operators, variables, data types, input/output |
| `introduction_to_python.py` | 1–63 | Conditionals, divisibility checks, number properties, real-world decisions |
| `loops.py` | 1–72 | While/for loops, nested loops, pattern printing, mathematical operations |
| `loops_v2.py` | 1–50+ | Loop variations and extended practice |
| `loops_v3.py` — `loops_v5.py` | 1–50+ | Additional loop exercises and techniques |
| `string_slicing.py` | 1 | String indexing and slicing basics |
| `type_conversion.py` | — | Type conversion reference |
| `compare_two_bres.py` | — | Excel workbook comparison utility (uses pandas) |

## 🛠️ Excel Comparison Utility

Compare two Excel files cell-by-cell and generate a validation report:

```bash
python3 compare_two_bres.py
```

**Inputs:**
- `ADC_OLD_OG_v1.xlsx`
- `ADC_NEW_OG_v1.xlsx`

**Output:**
- `comparison_output_OG_v10.xlsx` (contains "Match" or "Mismatch" for each cell)

## 💡 Example Exercises

### Conditional Logic
```python
# Exercise 5: Check if numbers form a valid pair
# "Pair" if both divisible by 3 AND one divisible by 12
a = int(input())  # 12
b = int(input())  # 15
# Output: Pair
```

### Loops & Patterns
```python
# Exercise 11: Print triangle pattern
# Input: 3
# Output:
# *
# **
# ***
```

### Real-World Problem Solving
```python
# Exercise 34: Calculate electricity bill with tiered pricing
# Units 1–50: ₹2 per unit
# Units 51–150: ₹3 per unit
# Units 151–250: ₹5 per unit
# Units 250+: ₹8 per unit
# Plus 20% tax on total bill
```

## 📊 Topics Covered

- ✅ Arithmetic & logical operators
- ✅ Conditionals (if/elif/else, nested conditions)
- ✅ Loops (while, for, nested)
- ✅ String operations (indexing, slicing, concatenation)
- ✅ Pattern generation (ASCII art, mathematical patterns)
- ✅ Mathematical algorithms (factorials, powers, sums)
- ✅ Number properties (Armstrong numbers, divisibility, primes)
- ✅ Data validation & decision trees
- ✅ Input/output handling
- ✅ Data type conversions

## 🎯 How to Use This Repository

1. **Clone or fork** the repository
2. **Pick a file** based on your learning level
3. **Run exercises sequentially** or jump to specific problems
4. **Modify and experiment** — try variations on the problems
5. **Track progress** by completing all exercises in each file

## 💻 Requirements

- Python 3.6+
- `pandas` (only for `compare_two_bres.py`)

Install pandas if needed:
```bash
pip install pandas openpyxl
```

## 🤝 Contributing

Found a bug or want to add more exercises? Feel free to:
- Open an issue
- Submit a pull request with improvements
- Suggest new topics or exercises

## 📝 License

This project is open source and available under the MIT License.

---

**Happy learning!** 🐍 Start small, practice consistently, and level up your Python skills.

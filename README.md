# 🔁 Compare Two Values — Sequential IF Statements

A Python console program that compares two user-entered numeric values using **sequential IF statements** — three independent conditions evaluated one after another.

---

## Features

- Accepts two numeric values as input (integers or decimals)
- Compares them using three separate sequential `if` statements
- Reports: equal, less than, or greater than
- Input validation — catches non-numeric entries and re-prompts

---

## How It Works

The program uses **sequential (independent) IF statements**:

```python
if value1 == value2:   # always evaluated
    print("...are equal")

if value1 < value2:    # always evaluated (even if previous was true)
    print("...is less than")

if value1 > value2:    # always evaluated
    print("...is greater than")
```

Unlike the nested version, Python checks all three conditions on every run.

---

## Example Output

```
Enter the first value:
200
Enter the second value:
75.25
================================================================
VALUE #1 --->  200.00 is greater than VALUE #2 --->  75.25.
================================================================
```

---

## Screenshot

![Program Output](output.png)

---

## Technologies Used

- Python 3
- Sequential `if` statements — three independent conditions
- `format()` — formatted numeric output with commas and 2 decimal places
- `try/except` — input validation
- `while` loop — re-prompting on invalid input

---

## Sequential IF vs Nested IF

| Feature | Sequential IF (this project) | Nested IF |
|---|---|---|
| Structure | Three separate `if` statements | One `if` with an `else` containing another `if/else` |
| Evaluation | All three conditions checked every run | Stops at first true condition |

---

## Learning Outcomes

- Understanding sequential vs nested conditional logic
- How Python evaluates independent `if` statements
- Comparing numeric values with `<`, `>`, `==`
- Formatting output with `format()`
- Input validation with `try/except`

---

## How to Run

1. Make sure Python 3 is installed: https://www.python.org/downloads/
2. Clone or download this repo
3. Open a terminal in the repo folder
4. Run: `python compare_values_sequential_if.py`
5. Follow the prompts

---

## Folder Structure

```
compare-values-sequential-if/
├── compare_values_sequential_if.py
├── output.png
├── README.md
├── LICENSE
└── .gitignore
```

---

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

*Written by Marlena Fabrick — Computer Programming, Fall 2020*


---

✅ Done with Repo 4! Move on to **REPO5_shipping_charges_UPLOAD_GUIDE.md**

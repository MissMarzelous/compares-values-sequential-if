# PROGRAMMER:   Marlena Fabrick
# PROGRAM NAME: Comparing Two Values — Sequential IF Statements
# DATE WRITTEN: 9/21/2020
# UPDATED:      2026 — removed unused toFixed import, added input validation,
#                      added explanatory comment about sequential vs nested
#
# PURPOSE: Compare two numeric values entered by the user and report whether
#          they are equal, or which one is greater. Uses SEQUENTIAL IF statements:
#          three completely separate if statements, each evaluated independently.
#
# KEY CONCEPT — SEQUENTIAL IF:
#   if value1 == value2:   ← evaluated (always)
#   if value1 < value2:    ← evaluated (always, even if first was true)
#   if value1 > value2:    ← evaluated (always)
#
# All three conditions are checked every time the program runs.
# Compare this to compare_values_nested_if.py, which uses a nested if/else
# and stops checking once the first true condition is found.

# ============================================================
# Declare all variables in alphabetical order
# INPUT OPERATIONS — collect two numeric values from the user

# Loop until valid numeric input is provided for value 1
while True:
    try:
        print("Enter the first value: ")
        value1 = float(input())
        break  # Exit loop once valid input is received
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# Loop until valid numeric input is provided for value 2
while True:
    try:
        print("Enter the second value: ")
        value2 = float(input())
        break  # Exit loop once valid input is received
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

# OUTPUT LINE FOR SEPARATION OF OUTPUT
print("================================================================")

# ============================================================
# SEQUENTIAL IF STATEMENTS TO COMPARE TWO VALUES
# Each if is separate and independent — all three are checked every run

# Sequential IF #1 — check if values are equal
if value1 == value2:
    print("VALUE #1 ---> " + format(value1, " ,.2f") +
          " and VALUE #2 ---> " + format(value2, " ,.2f") + " are equal.")

# Sequential IF #2 — check if value1 is less than value2
if value1 < value2:
    print("VALUE #1 ---> " + format(value1, " ,.2f") +
          " is less than VALUE #2 ---> " + format(value2, " ,.2f") + ".")

# Sequential IF #3 — check if value1 is greater than value2
if value1 > value2:
    print("VALUE #1 ---> " + format(value1, " ,.2f") +
          " is greater than VALUE #2 ---> " + format(value2, " ,.2f") + ".")

# OUTPUT LINE FOR SEPARATION OF OUTPUT
print("================================================================")

# END PROGRAM

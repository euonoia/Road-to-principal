# Chapter 1 — Week 1
## Variables, Data Types, Operators, Input & Output

*Phase 1: Python Mastery — Week 1 of 24*

---

## Why This Week Matters

Before you can build an AI traffic system, before you can write a FastAPI endpoint, before you can even write a proper `if` statement — you need a rock-solid grip on how a program *holds* and *labels* information. That's what variables and data types are. Everything else in this entire 24-week program is built on top of this week.

Think of this week as learning the alphabet before writing sentences. It will feel simple. Resist the urge to skim — the mistakes people make with variables and types in Week 1 are the same mistakes that cause production bugs in Week 20. We are building habits, not just knowledge.

---

## Learning Objectives

By the end of this week, you will be able to:

1. Explain what a variable actually is in memory, not just "a box that holds a value"
2. Correctly choose between Python's core data types: `int`, `float`, `str`, `bool`
3. Use arithmetic, comparison, logical, and assignment operators correctly and predict their output
4. Read input from a user and safely convert it to the type you need
5. Format output cleanly using f-strings
6. Identify and avoid the five most common beginner mistakes with variables and types

---

## Day 1 (Monday) — What Is a Variable, Really?

### 10 min Review
*(This is Week 1, Day 1 — no prior material yet. Instead, spend these 10 minutes setting up your environment: install Python 3.11+, install VS Code, and confirm `python --version` works in your terminal.)*

### 20 min Learn — Theory

A **variable** is a name that points to a value stored in memory. In Python, when you write:

```python
age = 25
```

Python does three things:

```
┌─────────────┐
│   MEMORY    │
│             │        age  ──────►  [ 25 ]
│   [ 25 ]    │◄───────
│             │
└─────────────┘
```

1. It creates the integer object `25` somewhere in memory.
2. It creates a name, `age`.
3. It makes `age` **point to** that object.

This matters because Python variables are not boxes that *contain* values — they are labels that *point to* values. This distinction explains a huge number of beginner bugs later (especially with lists, which we cover in Week 4). For now, just remember:

> A variable is a name. A name points to a value. The value lives in memory independently of the name.

**Assignment (`=`) is not equality.** In math, `x = 5` is a statement of fact. In Python, `x = 5` is a *command*: "make the name `x` point to the value `5`, right now." This is why you can write:

```python
x = 5
x = x + 1   # perfectly valid — recompute, then re-point x
print(x)    # 6
```

This would be nonsense in algebra but is completely normal in programming.

### Naming Rules and Conventions

```
Valid:     age, total_score, user_name, _internal, item2
Invalid:   2item, user-name, class, total score (has a space)
```

- Names can contain letters, numbers, and underscores, but can't start with a number.
- Python reserves certain words (`class`, `if`, `for`, `return`, etc.) — you can't use them as variable names.
- **Convention (PEP 8):** use `snake_case` for variables — `total_price`, not `TotalPrice` or `totalPrice`. Professional Python code is judged on this immediately.

### 20 min Code — Guided Practice

```python
# Try this in a file called day1.py

first_name = "Maria"
age = 25
height_in_meters = 1.65
is_student = True

print(first_name)
print(age)
print(height_in_meters)
print(is_student)

# Re-assignment
age = age + 1
print(age)  # 26
```

Run it. Change the values. Watch what happens when you re-assign `age`.

### 10 min Coding Challenge

Write a program that stores your name, your favorite number, and whether you like coffee (`True`/`False`) in three variables, then prints all three on separate lines.

---

## Day 2 (Tuesday) — Data Types

### 10 min Review
What is the difference between a variable's *name* and its *value*? Say it out loud before continuing.

### 20 min Learn — Theory

Python has four core "primitive" data types you'll use constantly:

| Type | Example | Meaning |
|---|---|---|
| `int` | `25`, `-3`, `0` | Whole numbers |
| `float` | `3.14`, `-0.5`, `2.0` | Decimal numbers |
| `str` | `"hello"`, `'25'` | Text (always quoted) |
| `bool` | `True`, `False` | Truth values |

You can always check a variable's type with the built-in `type()` function:

```python
print(type(25))      # <class 'int'>
print(type(3.14))    # <class 'float'>
print(type("25"))    # <class 'str'>
print(type(True))    # <class 'bool'>
```

**The trap that catches almost everyone:** `25` and `"25"` are *not* the same thing.

```
   25          "25"
┌──────┐    ┌───────┐
│ int  │    │  str  │
│ math │    │ text  │
└──────┘    └───────┘
```

```python
print(25 + 25)      # 50   (adds numbers)
print("25" + "25")  # "2525"  (joins text — no math happens!)
print(25 + "25")    # ERROR: TypeError
```

This single confusion — mixing numbers and text-that-looks-like-numbers — is responsible for a huge share of beginner errors, and it comes back later when reading user input (which is *always* text) or reading data from files (which is often text too).

### Type Conversion (Casting)

You can convert between types on purpose:

```python
int("25")      # 25   (str → int)
str(25)        # "25" (int → str)
float("3.14")  # 3.14 (str → float)
int(3.9)       # 3    (float → int, truncates, does NOT round)
bool(0)        # False
bool(1)        # True
bool("")       # False (empty string is "falsy")
bool("hi")     # True  (non-empty string is "truthy")
```

### 20 min Code — Guided Practice

```python
# day2.py
price_text = "49.99"
price = float(price_text)
tax = price * 0.12
total = price + tax

print("Price:", price)
print("Tax:", tax)
print("Total:", total)
print(type(price), type(tax), type(total))
```

### 10 min Coding Challenge

Given `quantity_str = "7"` and `unit_price_str = "12.50"`, convert both to the correct numeric types and print the total cost.

---

## Day 3 (Wednesday) — Operators, Part 1: Arithmetic & Comparison

### 10 min Review
Convert `"100"` to an integer and `50` to a string, in your head, then check with code.

### 20 min Learn — Theory

**Arithmetic operators:**

```
+   addition
-   subtraction
*   multiplication
/   division        → always returns a float
//  floor division  → rounds DOWN to nearest whole number
%   modulus         → remainder after division
**  exponent
```

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
print(2 ** 3)   # 8
```

`%` (modulus) looks minor now but becomes essential later — it's how you check "is this number even?" (`n % 2 == 0`), build cycling patterns, and even how frame-counting logic works in video processing (Week 22+).

**Comparison operators** — these always return a `bool`:

```
==   equal to
!=   not equal to
>    greater than
<    less than
>=   greater than or equal
<=   less than or equal
```

```python
print(5 == 5)    # True
print(5 == "5")  # False  (different types — never equal in Python)
print(10 > 3)    # True
```

**Beginner trap:** `=` assigns, `==` compares. Using one instead of the other is a classic bug:

```python
if age = 18:   # SyntaxError — this is WRONG
if age == 18:  # correct — this COMPARES
```

### 20 min Code — Guided Practice

```python
# day3.py
a = 17
b = 5

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** 2)

print("Is a greater than b?", a > b)
print("Is a equal to b?", a == b)
```

### 10 min Coding Challenge

Write code that checks whether a number stored in `n` is even or odd, and prints `"Even"` or `"Odd"` using only `%` and comparison — no `if` yet (just print the boolean result, since we haven't covered `if` until Week 2).

---

## Day 4 (Thursday) — Operators, Part 2: Logical & Assignment

### 10 min Review
What does `17 % 5` evaluate to? What does `17 // 5` evaluate to? (Answers: `2` and `3`.)

### 20 min Learn — Theory

**Logical operators** combine boolean values:

```
and   → True only if BOTH sides are True
or    → True if AT LEAST ONE side is True
not   → flips True/False
```

```python
is_raining = True
has_umbrella = False

print(is_raining and has_umbrella)  # False
print(is_raining or has_umbrella)   # True
print(not is_raining)               # False
```

Visualized as truth tables:

```
AND            OR             NOT
T and T = T    T or T = T     not T = F
T and F = F    T or F = T     not F = T
F and T = F    F or T = T
F and F = F    F or F = F
```

**Augmented assignment operators** — shortcuts for "update a variable based on itself":

```python
score = 10
score += 5   # same as: score = score + 5   → 15
score -= 3   # → 12
score *= 2   # → 24
score /= 4   # → 6.0
```

These matter because you'll write hundreds of counters, totals, and accumulators over the next six months (counting vehicles, tallying detections, tracking frame numbers) — `+=` will become one of the most-typed pieces of syntax in your career.

### 20 min Code — Guided Practice

```python
# day4.py
temperature = 30
is_weekend = True

# Logical combos
print(temperature > 25 and is_weekend)   # good beach day?
print(temperature > 25 or is_weekend)

# Augmented assignment
vehicle_count = 0
vehicle_count += 1
vehicle_count += 1
vehicle_count += 1
print("Vehicles counted:", vehicle_count)
```

### 10 min Coding Challenge

You have `has_ticket = True` and `age = 15`. A person can ride a rollercoaster if they have a ticket **and** are at least 12 years old. Write the single boolean expression (no `if` yet) and print the result.

---

## Day 5 (Friday) — Input & Output

### 10 min Review
Write, from memory, one line using `+=` and one using `and`.

### 20 min Learn — Theory

**Output** with `print()` — but professionals rarely use plain commas. Use **f-strings** for clean, readable formatting:

```python
name = "Ana"
age = 30

# Clumsy (avoid in professional code):
print("Name:", name, "Age:", age)

# Professional (f-string):
print(f"Name: {name}, Age: {age}")
```

f-strings let you embed expressions directly:

```python
price = 49.99
print(f"Total with tax: {price * 1.12:.2f}")   # .2f = 2 decimal places
```

```
f"{value:.2f}"
        │  │└─ 2 decimal places
        │  └── fixed-point notation
        └───── the value being formatted
```

**Input** with `input()` — and the single most important fact about it:

> `input()` **always** returns a string. Always. Even if the user types `25`, you get back `"25"`.

```python
age = input("How old are you? ")
print(type(age))          # <class 'str'>  — even though they typed a number!
age = int(age)             # you must convert it yourself
print(type(age))           # <class 'int'>
```

This connects directly back to Day 2. Every single time you take numeric input from a user, you must consciously convert it. Forgetting this is, by a wide margin, the single most common beginner bug in all of Python.

### 20 min Code — Guided Practice

```python
# day5.py
name = input("What's your name? ")
age_str = input("What's your age? ")
age = int(age_str)

years_to_100 = 100 - age

print(f"Hello, {name}!")
print(f"You have {years_to_100} years until you turn 100.")
```

### 10 min Coding Challenge

Ask the user for the price of an item and the quantity they want to buy. Convert both to the correct numeric types, calculate the total, and print it formatted to 2 decimal places using an f-string.

---

## Saturday — Project Day

### Mini Project: **Simple Receipt Generator**

**Goal:** Combine everything from this week — variables, types, operators, input, output — into one working program.

**Requirements:**
1. Ask the user for an item name (string), price per unit (will need conversion), and quantity (will need conversion).
2. Calculate subtotal, a 12% tax, and the final total.
3. Print a neatly formatted receipt using f-strings, like this:

```
====== RECEIPT ======
Item:      Notebook
Quantity:  3
Unit Price: $2.50
----------------------
Subtotal:  $7.50
Tax (12%): $0.90
Total:     $8.40
======================
```

**Starter structure:**

```python
item_name = input("Item name: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))

subtotal = unit_price * quantity
tax = subtotal * 0.12
total = subtotal + tax

print("====== RECEIPT ======")
print(f"Item:      {item_name}")
print(f"Quantity:  {quantity}")
print(f"Unit Price: ${unit_price:.2f}")
print("----------------------")
print(f"Subtotal:  ${subtotal:.2f}")
print(f"Tax (12%): ${tax:.2f}")
print(f"Total:     ${total:.2f}")
print("======================")
```

**Stretch goal (optional, no `if` needed yet):** Add a second item and print a combined total. This foreshadows why we need loops and lists — doing this for 10 items by hand would be painful. That pain is the motivation for Week 2 and Week 4.

---

## Sunday — Review Day

### Quiz (answers at the end)

1. What does `type("42")` return?
2. What is the result of `9 // 2`? What about `9 % 2`?
3. Why does `5 + "5"` raise an error?
4. What does `input()` always return, regardless of what the user types?
5. What is the difference between `=` and `==`?
6. What does `not True and False` evaluate to?
7. Write an f-string that prints a float `x` rounded to 2 decimal places.

### Practical Coding Test

Write a program (no `if`, no loops — not covered yet) that:
- Takes a temperature in Celsius as input
- Converts it to Fahrenheit using `F = C * 9/5 + 32`
- Prints both values formatted to 1 decimal place

### Debugging Exercise

Find and fix the bugs in this code:

```python
name = input("Enter your name: ")
age = input("Enter your age: ")
years_left = 100 - age
print("Hello " + name + " you have " + years_left + " years left")
```

*(Hint: there are two separate type-related bugs here — one with `100 - age`, one with the final `print`.)*

### Code Review Checklist

Before you consider Week 1 "done," check:

- [ ] All variable names use `snake_case`
- [ ] No unconverted `input()` results are used in math
- [ ] f-strings are used instead of comma-separated `print()` arguments
- [ ] Every variable name is descriptive (`price`, not `p` or `x`)
- [ ] Code runs with no errors on a fresh terminal

### Quiz Answers

1. `<class 'str'>`
2. `9 // 2` → `4`; `9 % 2` → `1`
3. Because Python won't silently convert types for `+` — an `int` and a `str` are incompatible for addition, unlike `+`'s meaning for two strings (joining) or two numbers (adding).
4. A string (`str`), always.
5. `=` assigns a value to a name. `==` compares two values and returns a boolean.
6. `False` (`not True` is `False`; `False and False` is `False`)
7. `f"{x:.2f}"`

---

## Common Beginner Mistakes (Week 1 Edition)

1. **Forgetting to convert `input()`.** `age = input(...)` then trying `age + 1` crashes, because `age` is a string.
2. **Confusing `=` and `==`.** Especially once `if` is introduced next week — this bug becomes far more common.
3. **Mixing `int` division habits from other contexts.** Forgetting that `/` always gives a float, even `10 / 2` → `5.0`, not `5`.
4. **Using vague variable names** (`x`, `data`, `temp`) that make code unreadable a week later.
5. **Assuming `round()`-like behavior from `int()`.** `int(3.9)` is `3`, not `4` — it truncates, it does not round.

## Best Practices

- Always name variables for what they *represent*, not their type (`age`, not `int_value`).
- Convert `input()` immediately, on the same line if possible, so the "wrong type" state never lingers in your code.
- Prefer f-strings over string concatenation (`+`) for anything with more than one variable.
- Run small snippets in isolation when unsure what an operator does — don't guess, verify.
- Get comfortable with `type()` as a debugging tool — when something behaves strangely, check the type first.

---

## Summary

This week you learned that a variable is a name pointing to a value, and that Python cares deeply about *type* — numbers and text-that-looks-like-numbers are fundamentally different things. You learned the four core types (`int`, `float`, `str`, `bool`), how to convert between them, and the four families of operators: arithmetic, comparison, logical, and assignment. Finally, you learned that `input()` always hands you a string, and that clean output means f-strings, not comma soup.

Every later chapter assumes this is automatic for you. If anything above felt shaky, that's completely normal — replay this chapter's exercises once more before moving to Week 2. There's no reward for rushing here.

## Reflection Questions

1. Where in this week's material did you feel most confident? Where did you feel least confident?
2. Can you explain, in your own words (no code), why `"5" + "5"` doesn't equal `10`?
3. What's one habit from the "Best Practices" section you'll consciously try to apply this week?
4. If you had to teach the difference between `=` and `==` to someone else, what analogy would you use?

---

*End of Chapter 1. Once you've completed the Saturday project and Sunday review, let me know and we'll move to Chapter 2 — Week 2: Conditionals, Loops, Nested Loops, and Logic Building.*

# Homework 2: TDD Practice with Calc

## Final Version of Calc.py

![Calc.py](Calc.png)

## Final Version of CalcTest.py
![CalcTest.py](CalcTest.png)
## All Tests Passing

![CalcTest.py](run_test.png)

---

## Starting Point

The original `Calc.py` contained a single `add()` method. All new functionality was added using Test-Driven Development, following the **Red → Green → Refactor** cycle.

---

## TDD Cycle 1: subtract()

**Red:**
A failing test `test_subtract` was written in `CalcTest.py` before any implementation existed. The test covered three scenarios upfront: a positive result `(10, 4)` expecting `6`, a zero result `(4, 4)` expecting `0`, and a negative result `(4, 10)` expecting `-6`. Running the test produced `AttributeError: 'Calculator' object has no attribute 'subtract'`, confirming the test correctly failed.

![subtract_red](subtract_red.png)

**Green:**
The `subtract()` method was added to `Calc.py` with the implementation `return a - b`. All three assertions passed.

![subtract_green](subtract_green.png)

**Refactor:**
No changes were made to the implementation logic. The repeated `result =` variable assignments in `test_subtract` were removed, passing values directly into `assertEqual()` to improve code readability. All tests continued to pass.

![subtract_refactor](subtract_refactor.png)

---

## TDD Cycle 2: multiply()

**Red:**
A failing test `test_multiply` was written covering four scenarios upfront: two positives `(5, 5)` expecting `25`, multiply by zero `(5, 0)` expecting `0`, mixed signs `(5, -5)` expecting `-25`, and two negatives `(-5, -5)` expecting `25`. Running the test produced `AttributeError: 'Calculator' object has no attribute 'multiply'`, confirming the correct failure.

![multiply_red](multiply_red.png)

**Green:**
The `multiply()` method was added to `Calc.py` with the implementation `return a * b`. All four assertions passed.

![multiply_green](multiply_green.png)

**Refactor:**
No changes were made to the implementation logic. The repeated `result =` variable assignments in `test_multiply` were removed, passing values directly into `assertEqual()` to improve code readability. All tests continued to pass.

![multiply_refactor](multiply_refactor.png)

---

## TDD Cycle 3: divide()

Before writing any tests, two design decisions were made and encoded into the tests:

- `divide()` should return a **float**, not an integer.
- Division by zero should raise a **`ValueError`**.

### Cycle 3a: Basic Division

**Red:**
A failing test `test_divide` was written calling `calc.divide(9, 3)` and expecting `3.0`. Running the test produced `AttributeError: 'Calculator' object has no attribute 'divide'`, confirming the correct failure.

![divide_red](divide_red.png)

**Green:**
The `divide()` method was added to `Calc.py` with the implementation `return float(a) / float(b)`. The test passed.

![divide_green](divide_green.png)

**Refactor:**
No changes were made to the implementation logic. The `result =` variable assignment in `test_divide` was removed, passing the value directly into `assertEqual()` to improve code readability. All tests continued to pass.

![divide_refactor](divide_refactor.png)

### Cycle 3b: Division by Zero

**Red:**
Additional test cases were added to `test_divide`: negative divisor `(9, -3)` expecting `-3.0`, two negatives `(-9, -3)` expecting `3.0`, and division by zero using `assertRaises(ValueError, calc.divide, 9, 0)`. Running the tests produced `ZeroDivisionError` instead of the expected `ValueError`, confirming the correct failure.

![divide_red_2](divide_red_2.png)

**Green:**
A guard clause was added to `divide()`: `if b == 0: raise ValueError("Cannot divide by zero")`. All 4 tests passed.

![divide_green_2](divide_green_2.png)

**Refactor:**
No changes were made to the implementation logic. The remaining `result =` variable assignments in `test_divide` were removed, passing values directly into `assertEqual()` to improve code readability. All 4 tests continued to pass.

![divide_refactor_2](divide_refactor_2.png)
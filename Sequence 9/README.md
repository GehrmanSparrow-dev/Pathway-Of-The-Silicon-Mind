# Sequence 9: The Coder

Welcome to the **Sequence 9: The Coder** section of the *Pathway of the Silicon Mind* study plan. This folder contains the foundational Python assignments, projects, and guides completed during this sequence.

---

## Contents

### 1. Study Guide
* **[Sequence_9_The_Coder_Guide.pdf](file:///c:/Pathway%20of%20the%20Silicon%20Mind/Sequence%209/Sequence_9_The_Coder_Guide.pdf)**: The primary study guide detailing the objectives, theory, and curriculum for the sequence.

### 2. Checkpoint Scripts
These scripts cover the fundamental concepts of Python programming:

* **[Checkpoint 2: User Input & Basic Operations](file:///c:/Pathway%20of%20the%20Silicon%20Mind/Sequence%209/Checkpoint2.py)**
  * **Concepts**: Variables, data type conversion (`str` to `int` and vice-versa), standard input/output.
  * **Behavior**: Prompts the user to enter their name and birth year, then prints a personalized greeting stating their age based on the current year.

* **[Checkpoint 3: Prime Number Checker with Loops](file:///c:/Pathway%20of%20the%20Silicon%20Mind/Sequence%209/Checkpoint3.py)**
  * **Concepts**: Loops (`for`), range boundaries, conditional logic, break statements, `else` clause in loops.
  * **Behavior**: Loops 50 times, asking the user for a number during each iteration and instantly validating whether it is a prime number.

* **[Checkpoint 4: Celsius to Fahrenheit Converter](file:///c:/Pathway%20of%20the%20Silicon%20Mind/Sequence%209/Checkpoint4.py)**
  * **Concepts**: Lists, list comprehensions, arithmetic calculations, list filtering.
  * **Behavior**: Takes a list of Celsius temperatures, converts them to Fahrenheit, filters the list to only include temperatures below 50°F, and prints the result.

* **[Checkpoint 5: Bill Calculator with Stacked Discounts](file:///c:/Pathway%20of%20the%20Silicon%20Mind/Sequence%209/Checkpoint5.py)**
  * **Concepts**: Functions, default arguments, keyword arguments unpacking (`**kwargs`), numeric formatting.
  * **Behavior**: Calculates a checkout total from a list of item prices. It applies default or custom sales tax rates and stacks consecutive variable discounts (e.g., seasonal, loyalty, coupons) passed as keyword arguments.

* **[Checkpoint 6: Exception Handling and Cleanups](file:///c:/Pathway%20of%20the%20Silicon%20Mind/Sequence%209/Checkpoint6.py)**
  * **Concepts**: File streams, error handling (`try-except-finally`), exception catching (`FileNotFoundError`).
  * **Behavior**: Tries to read from a non-existent file (`missing_data.txt`), catches the resulting error to prevent a script crash, prints a user-friendly error message, and runs a cleanup confirmation in a `finally` block.

---

### 3. Projects
* **[Project 1: Directory File Organizer](file:///c:/Pathway%20of%20the%20Silicon%20Mind/Sequence%209/Project1.py)**
  * **Concepts**: Directory traversing (`os.listdir`), file movements (`shutil.move`), file format validation, log creation via CSV exporting (`csv.writer`).
  * **Behavior**: Organizes files in a target folder by sorting them into categorised subfolders (e.g. `Text/`, `Documents/`, `Images/`, `Data/`) depending on their extension. It logs all moved files and their destinations into a `file_movements.csv` document.

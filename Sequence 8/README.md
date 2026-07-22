# Sequence 8: The Data Sculptor

Welcome to the **Sequence 8: The Data Sculptor** section of the *Pathway of the Silicon Mind* study plan. This repository contains the mathematical and data manipulation assignments, projects, and guides completed during this sequence.

All the checkpoints in this directory were completed using the accompanying PDF guide as a study reference.

---

## Contents

### 1. Study Guide
* **[Sequence_8_The_Data_Sculptor_Guide.pdf](Sequence_8_The_Data_Sculptor_Guide.pdf)**: The primary study guide detailing the objectives, theory, and curriculum. This PDF was used as the guiding material for all the programming challenges in this sequence.

### 2. Checkpoint Scripts
These scripts cover the fundamental concepts of linear algebra, matrix manipulation, data cleaning, and statistical preprocessing using NumPy and Pandas:

* **[Checkpoint 1: Matrix-Vector Dot Product & Transpose](Checkpoint1.py)**
  * **Concepts**: NumPy arrays, dot product matrix multiplication (`np.dot`), shape transformation (`reshape`), transposition (`.T`).
  * **Behavior**: Prompts the user to enter values for a 3x3 score matrix and a 3-element weight vector, computes the dot product, converts the result into a column vector, and prints both the column vector and its transpose.

* **[Checkpoint 2: Salary Imputation & Duplicate Removal](Checkpoint2.py)**
  * **Concepts**: Pandas DataFrames, handling missing data (`fillna`), grouping and transformations (`groupby` + `transform`), duplicate entry removal (`drop_duplicates`).
  * **Behavior**: Creates an employee database DataFrame, replaces missing salary values with their department's average salary, and cleans up duplicate names (keeping the first occurrence).

* **[Checkpoint 3: Z-Score Outlier Filtering](Checkpoint3.py)**
  * **Concepts**: Pandas Series, statistical metrics (mean, standard deviation), Z-score calculation, boolean indexing/filtering.
  * **Behavior**: Analyzes a Pandas Series, computes Z-scores for each data point, and filters out outliers that fall outside 3 standard deviations from the mean.

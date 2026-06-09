# Morris Counter Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-Probabilistic_Data_Structures-blue?style=for-the-badge)

A Python-based implementation and statistical analysis of the **Morris Counter**, a probabilistic data structure used to count large events using very little memory (logarithmic space). 

This project explores the standard algorithm, improves its accuracy using multiple counters (mean/median averaging), generalizes the mathematical base for fine-tuned precision, and mathematically calculates the exact state probabilities.

---

## Table of Contents
1. [About the Morris Counter](#-about-the-morris-counter)
2. [Features & Variants](#-features--variants)
3. [Project Structure](#-project-structure)
4. [Getting Started](#-getting-started)

---

## About the Morris Counter
The Morris Counter allows you to approximate a count $n$ using a small counter $C$. Instead of incrementing $C$ on every event, it increments probabilistically based on the current value of $C$. 

* **Standard Base-2 Increment Probability:** $\frac{1}{2^C}$
* **Standard Estimation Formula:** $n = 2^C - 1$

While highly memory-efficient (e.g., counting to 1,000,000 requires only 5 bits), the base version suffers from high variance. This project explores methods to reduce that variance and optimize the bit usage.

---

##  Features & Variants

* **Base Morris Counter (`v1`):** The classic algorithm incrementing with probability $1/2^C$.
* **Multi-Counter Averaging (`v2`):** Runs $k$ independent counters simultaneously. It calculates both the **Mean** and the **Median** of the estimations to drastically reduce variance and standard deviation.
* **Generalized Base Counter (`v3`):** Instead of base 2, it uses a floating-point base $a$ (e.g., $a = 1.056$). The increment probability becomes $1/a^C$, and the estimation formula expands to:
  $$n = \frac{1}{a-1}(a^C - 1)$$
  This allows the algorithm to fully utilize available memory (e.g., maximizing the 255 limit of an 8-bit integer) for much higher accuracy.
* **Probability Matrix Analysis:** Calculates the exact, theoretical probability of the counter reaching state $k$ after $n$ steps using state-transition dynamics.

---

## Project Structure

```text
├── Enothta_A.ipynb              # Jupyter Notebook with full graphical analysis, boxplots, and Greek documentation
├── morris_counter.py            # The standard base-2 Morris Counter implementation
├── morris_counter_v2.py         # Multi-counter variant tracking Mean and Median estimations
├── morris_counter_v3.py         # Generalized base variant for fine-tuned accuracy
└── morris_probabilities.py      # Calculates and plots exact state-transition probabilities
```
##  Getting Started

### Prerequisites
Make sure you have Python 3 installed, along with the required scientific libraries:
```bash
pip install numpy matplotlib seaborn jupyter
```
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/Morris-Counter.git](https://github.com/yourusername/Morris-Counter.git)
   cd Morris-Counter
   ```
2. **Explore the Analysis:**
   The easiest way to understand the project is to open the Jupyter Notebook, which contains the complete workflow, tests, and matplotlib graphs.
   ```bash
   jupyter notebook Enothta_A.ipynb
   ```
3. **Run Code Manually:**
   You can also import any of the counter classes into your own Python scripts:
   ```python
   from morris_counter import morris_counter

   counter = morris_counter()
   counter.run_morris_counter(100000)
   counter.morris_graph()
   ```

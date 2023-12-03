# 202Unsold 📈

Welcome to **202unsold**.

This project involves statistical analysis for predicting unsold stock, using joint-law probabilities and variance calculations.

## Language and Tools 🛠️

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **Language:** Python
- **Compilation:** Via Makefile, including `re`, `clean`, and `fclean` rules.
- **Binary Name:** 202unsold

## Project Overview 🔎

The goal of 202unsold is to create a program that calculates the joint-law of two random variables, representing the number of unsold items of two types of suits. It computes the expected values and variances of these variables as well as their sum.

### Key Features

- **Joint-Law Probability:** Calculate the joint-law probability of two random variables.
- **Expected Values and Variances:** Compute expected values and variances for each variable and their sum.
- **Command-Line Interface:** Provide a user-friendly command-line interface for input and results display.

### Usage

```
∼/B-MAT-400> ./202unsold -h
USAGE
./202unsold a b
DESCRIPTION
a constant computed from past results
b constant computed from past results
```
### Exemple

```
∼/B-MAT-400> ./202unsold 60 70
--------------------------------------------------------------------------------
X=10 X=20 X=30 X=40 X=50 Y law
Y=10 0.100 0.080 0.060 0.040 0.020 0.300
Y=20 0.083 0.067 0.050 0.033 0.017 0.250
Y=30 0.067 0.053 0.040 0.027 0.013 0.200
Y=40 0.050 0.040 0.030 0.020 0.010 0.150
Y=50 0.033 0.027 0.020 0.013 0.007 0.100
X law 0.333 0.267 0.200 0.133 0.067 1.000
--------------------------------------------------------------------------------
z 20 30 40 50 60 70 80 90 100
p(Z=z) 0.100 0.163 0.193 0.193 0.167 0.100 0.053 0.023 0.007
--------------------------------------------------------------------------------
expected value of X: 23.3
variance of X: 155.6
expected value of Y: 25.0
variance of Y: 175.0
expected value of Z: 48.3
variance of Z: 330.6
--------------------------------------------------------------------------------
```

## Installation and Usage 💾

1. Clone the repository.
2. Compile the program using the provided Makefile.
3. Run the program: `./202unsold a b`.
4. For detailed usage instructions, refer to `202unsold.pdf`.

## License ⚖️

This project is released under the MIT License. See `LICENSE` for more details.

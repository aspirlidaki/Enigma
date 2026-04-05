# Enigma: The Cipher Toolkit

A beginner-friendly, command-line Python application for exploring classical cryptography techniques. This project demonstrates foundational programming concepts including loops, functions, string manipulation, and error handling through the lens of historical cipher algorithms.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [How It Works](#how-it-works)
  - [Caesar Cipher — Encryption](#caesar-cipher--encryption)
  - [Caesar Cipher — Decryption](#caesar-cipher--decryption)
  - [Brute-Force Cracker](#brute-force-cracker)
- [Project Structure](#project-structure)
- [Concepts Demonstrated](#concepts-demonstrated)
- [Example Session](#example-session)
- [License](#license)

---

## Overview

**Enigma** is an educational cryptography toolkit built in Python. It implements the **Caesar Cipher**, one of the oldest and most well-known substitution ciphers, first used by Julius Caesar to protect military communications (Suetonius, *The Twelve Caesars*, c. 121 AD).

The goal of this project is not only to produce a working tool, but to serve as a practical study of core Python programming principles in a real-world context.

---

## Features

| Option | Description |
|--------|-------------|
| `1` Encrypt | Encrypts a plaintext message using a Caesar Cipher with a user-defined shift key |
| `2` Decrypt | Decrypts a ciphertext message by reversing the shift |
| `3` Brute-Force | Tries all 25 possible Caesar Cipher keys and displays the results |
| `4` Exit | Exits the application |

---

## Getting Started

### Prerequisites

- Python **3.6** or higher
- A Unix/Linux terminal or Windows WSL environment

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aspirlidaki/Enigma.git
   cd Enigma
   ```

2. No external libraries are required. This project uses only the Python standard library.

### Usage

Run the script from your terminal:

```bash
python3 enigma.py
```

You will be presented with an interactive menu. Type the number corresponding to your desired action and press **Enter**.

---

## How It Works

### Caesar Cipher — Encryption

Each letter in the plaintext message is shifted forward in the alphabet by a fixed number of positions (the **shift key**). Non-alphabetic characters (spaces, punctuation, numbers) are left unchanged.

**Formula:**

```
C = (P - A + shift) mod 26 + A
```

Where:
- `P` = ASCII value of the plaintext character
- `A` = ASCII value of `'A'` (65) or `'a'` (97), depending on case
- `C` = ASCII value of the resulting ciphertext character

**Example** (shift = 3):

| Plaintext  | H  | e  | l  | l  | o  |   | W  | o  | r  | l  | d  |
|------------|----|----|----|----|----|---|----|----|----|----|----|
| Ciphertext | K  | h  | o  | o  | r  |   | Z  | r  | u  | o  | g  |

### Caesar Cipher — Decryption

Decryption applies the same function with a **negative shift**, adhering to the **DRY (Don't Repeat Yourself)** principle — no separate decryption function is needed.

```python
plaintext = caesar_encrypt(ciphertext, -shift)
```

### Brute-Force Cracker

Since the Caesar Cipher has only **25 possible keys** (a shift of 26 returns the original message), a brute-force attack is computationally trivial. The cracker iterates through all values from 1 to 25, decrypts the message with each, and prints the results for the user to inspect visually.

---

## Project Structure

```
Enigma/
│
├── enigma.py       # Main application file
├── README.md       # Project documentation
└── .gitignore      # Git ignore rules
```

---

## Concepts Demonstrated

This project covers the following Python and computer science concepts:

- **Functions** — Defining and calling reusable functions with parameters and return values
- **Loops** — `while True` for the menu loop; `for` with `range()` for the brute-force cracker
- **String manipulation** — Iterating over characters, using `ord()` and `chr()` for ASCII conversion
- **Modular arithmetic** — Using the `%` operator to implement wrap-around (e.g., `Z + 1 = A`)
- **Error handling** — Using `try/except ValueError` to handle invalid user input gracefully
- **The DRY Principle** — Reusing `caesar_encrypt()` for both encryption and decryption

---

## Example Session

```
Welcome to Enigma: The Cipher Toolkit! 🔐

--- Main Menu ---
1. Encrypt a message
2. Decrypt a message
3. Brute-force a Caesar Cipher
4. Exit
Choose an option (1-4): 1

--- Encryption ---
Enter the message you want to encrypt: Hello World
Enter your shift key (e.g., 3): 3

🔒 Your encrypted message is: Khoor Zruog

--- Main Menu ---
Choose an option (1-4): 3

--- Brute-Force Cracker ---
Enter the encrypted message to crack: Khoor Zruog

[Cracking] Trying all possible shifts...
------------------------------
Key 01: Jgnnq Yqtnf
Key 02: Ifmmp Xpsme
Key 03: Hello World   <-- ✅ Readable!
Key 04: Gdkkn Vnqkc
...
------------------------------
Look through the results above to find the readable message!
```

---

## License

This project is intended for **educational purposes only**. Cryptographic techniques demonstrated here are classical and should not be used to secure sensitive information in production systems.

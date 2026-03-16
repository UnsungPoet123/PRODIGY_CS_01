# Caesar Cipher Implementation in Python

## Overview

This project implements a simple encryption and decryption tool using the **Caesar Cipher algorithm**. The Caesar Cipher is one of the earliest known encryption techniques and works by shifting each letter in a message by a fixed number of positions in the alphabet.

For example:

HELLO → Shift 3 → KHOOR

This program allows users to input a message and a shift value to either encrypt or decrypt the text using Python.

---

## Features

* Encrypt plaintext messages
* Decrypt encrypted messages
* Supports both uppercase and lowercase letters
* Preserves spaces, numbers, and special characters
* Simple command-line interface

---

## How the Algorithm Works

The Caesar Cipher shifts each letter in the alphabet by a specified number of positions.

Example with a shift of **3**:

A → D
B → E
C → F

If the shift reaches the end of the alphabet, it wraps around:

X → A
Y → B
Z → C

Encryption shifts letters **forward**, while decryption shifts them **backward**.

---

## Requirements

* Python 3.x

No external libraries are required.

---

## How to Run the Program

1. Clone the repository

git clone https://github.com/UnsungPoet123/caesar-cipher-python.git

2. Navigate to the project folder

cd caesar-cipher-python

3. Run the Python script

python caesar_cipher.py

---

## Example Usage

=== Caesar Cipher Program ===

Enter your message: hello
Enter shift value: 3
Type 'encrypt' or 'decrypt': encrypt

Result: khoor

---

## Project Structure

caesar-cipher-python/
│
├── caesar_cipher.py
├── README.md
└── .gitignore

* **caesar_cipher.py** – Main Python program implementing the Caesar Cipher algorithm
* **README.md** – Project documentation


---

## Learning Objective

This project was completed as part of a cybersecurity internship task to demonstrate understanding of basic cryptographic techniques and Python programming concepts such as functions, loops, and string manipulation.

---

## Author

Apomah John Elike

---

## License

This project is open-source and available for educational purposes.

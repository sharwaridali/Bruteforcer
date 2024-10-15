# Bruteforcer

# ZIP File Password Brute-force

This Python script attempts to brute-force the password of a ZIP file using a wordlist, such as the popular `rockyou.txt`. The script will iterate over each password in the wordlist and try to extract the contents of the encrypted ZIP file.

## Requirements

- Python 3.x
- `rockyou.txt` wordlist (or another wordlist of your choice)
- The encrypted ZIP file (`enc.zip` in this case)
- `zipfile` Python module (pre-installed with Python)

## Installation

1. **Install Python**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install the `zipfile` module**:
   - The `zipfile` module comes pre-installed with Python, so you don't need to install it separately.
   - If you encounter any issues, ensure your Python installation is correct, as `zipfile` is part of Python's standard library.

3. **Download the rockyou.txt wordlist**:
   - You can get the `rockyou.txt` wordlist from various sources, including [SecLists](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz) or pre-installed in some Linux distributions.
   - Make sure the wordlist is in the same directory as the script or provide the correct path.

## Usage

1. **Prepare your ZIP file**:
   - Place the encrypted ZIP file (`enc.zip`) in the same directory as the script or modify the script to point to your ZIP file.

2. **Run the script**:
   - Open a terminal or command prompt in the directory where the script is located.
   - Run the script using Python:

   ```bash
   python3 zip_bruteforce.py

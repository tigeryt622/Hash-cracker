# 🔐 Basic Hash Cracker (Dictionary Attack)

This is a simple **Password Hash Cracker** tool I built to understand how dictionary attacks work in real life.  
It shows how attackers (and ethical hackers) test weak passwords by comparing hashes.

---

## 📌 **What It Does**

- Takes a **SHA-256 hash** as input.
- Loads a wordlist of possible passwords.
- Hashes each word and compares it to the target hash.
- If it finds a match, it shows the cracked password.
- Comes with a simple **Tkinter GUI** so anyone can test it easily.

---

## ⚡ **Why I Made This**

This mini project helped me learn:
- How hashing works with Python’s `hashlib`.
- How dictionary attacks crack weak passwords.
- How to build a basic GUI with Tkinter.
- How to make a tool that’s clear and beginner-friendly.

---

## 🚀 **How To Run**

**1️⃣ Requirements**
- Python 3.x
- VS Code or any Python IDE

---

**2️⃣ Clone or Download**

```bash
git clone https://github.com/yourusername/basic-hash-cracker
cd basic-hash-cracker
3️⃣ Files

cracker.py → The main hash cracker with GUI.

wordlist.txt → A file with possible passwords.

hash_generator.py → (Optional) Generates a test hash.

4️⃣ Steps

Open wordlist.txt and write some test passwords:
password, 123456, test123, secret

Use hash_generator.py to create a SHA-256 hash for testing:

python
Copy
Edit
import hashlib

password = "secret"
print(hashlib.sha256(password.encode()).hexdigest())
Copy the generated hash.

Open cracker.py, run it:

Paste the hash in the GUI.

Select your wordlist.txt.

Click Crack.

See if your wordlist finds the password!

✅ For Learning Only
This tool is for educational use only — do not use it on any real systems you do not own or have permission to test.

📣 Connect
This is part of my Cybersecurity Project Series — I build small, practical tools to strengthen my portfolio and share them with other learners.


Connect with me on LinkedIn: www.linkedin.com/in/prince-darji-4b9897331

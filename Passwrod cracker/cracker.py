import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import threading

def start_cracking():
    hash_to_crack = hash_entry.get().strip()
    if not hash_to_crack:
        messagebox.showerror("Error", "Please enter a hash.")
        return

    wordlist_path = filedialog.askopenfilename(title="Select Wordlist")
    if not wordlist_path:
        messagebox.showerror("Error", "Please select a wordlist.")
        return

    def crack():
        found = False
        with open(wordlist_path, "r") as file:
            for word in file:
                word = word.strip()
                hashed = hashlib.sha256(word.encode()).hexdigest()
                result_text.insert(tk.END, f"Trying: {word}\n")
                result_text.see(tk.END)  # auto-scroll
                if hashed == hash_to_crack:
                    result_text.insert(tk.END, f"\n✅ Password Found: {word}\n")
                    found = True
                    break
        if not found:
            result_text.insert(tk.END, "\n❌ Password Not Found.\n")

    threading.Thread(target=crack).start()

root = tk.Tk()
root.title("Password Cracker GUI")
root.geometry("600x500")

tk.Label(root, text="Enter SHA256 Hash to Crack:").pack(pady=5)

hash_entry = tk.Entry(root, width=70)
hash_entry.pack(pady=5)

tk.Button(root, text="Start Cracking", command=start_cracking).pack(pady=10)

result_text = tk.Text(root, height=20, width=80)
result_text.pack(pady=5)

root.mainloop()

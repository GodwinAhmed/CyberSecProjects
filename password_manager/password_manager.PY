# password_manager/password_manager.py
# ------------------------------------------------------------
# Simple password manager with bcrypt hashing and JSON storage.
# ------------------------------------------------------------

import bcrypt
import json
import os

DATA_FILE = "password_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def create_password(account, password):
    """Hash and save a new password."""
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    data = load_data()
    data[account] = hashed.decode()
    save_data(data)
    print(f"[+] Password stored for '{account}'.")


def verify_password(account, password):
    """Verify a password against stored hash."""
    data = load_data()
    if account not in data:
        print("[-] Account not found.")
        return
    stored_hash = data[account].encode()
    if bcrypt.checkpw(password.encode(), stored_hash):
        print("[+] Password verified!")
    else:
        print("[-] Incorrect password.")


if __name__ == "__main__":
    print("=== Simple Password Manager ===")
    action = input("(C)reate or (V)erify password? ").lower()

    if action == "c":
        account = input("Account name: ")
        pwd = input("Password: ")
        create_password(account, pwd)
    elif action == "v":
        account = input("Account name: ")
        pwd = input("Password: ")
        verify_password(account, pwd)
    else:
        print("Invalid choice.")

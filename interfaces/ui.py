import tkinter as tk

def update_balance(wallet, balance_user_entry, balance_label, transaction_history, audit_system):
    user = balance_user_entry.get()
    balance = wallet.get_balance(user)
    balance_label.config(text=f"Balance of {user}: {balance} Arc")
    transaction_history.delete(0, tk.END)
    for entry in audit_system.audit_log:
        if entry['transaction']:
            transaction_history.insert(tk.END, f"{entry['transaction'].sender} -> {entry['transaction'].receiver}: {entry['transaction'].amount} Arc")

def show_interface(wallet, audit_system):
    root = tk.Tk()
    root.title("RamanChain - Staking and Transaction Interface")

    tk.Label(root, text="Check Balance").grid(row=0)
    balance_user_entry = tk.Entry(root)
    balance_user_entry.grid(row=0, column=1)
    balance_label = tk.Label(root, text="")
    balance_label.grid(row=1, column=1)
    transaction_history = tk.Listbox(root, width=50, height=10)
    transaction_history.grid(row=2, column=1)
    tk.Button(root, text='Show Balance', command=lambda: update_balance(wallet, balance_user_entry, balance_label, transaction_history, audit_system)).grid(row=0, column=2)

    root.mainloop()

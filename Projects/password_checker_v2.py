import tkinter as tk

PASSWORD = "python123"

window = tk.Tk()
window.title("Password Checker")
window.geometry("300x200")

label = tk.Label(window, text="Enter password:")
label.pack(pady=10)

entry = tk.Entry(window, show="*")
entry.pack()

result = tk.Label(window, text="")
result.pack(pady=10)

def check_password():
    if entry.get() == PASSWORD:
        result.config(text="Access granted ✅", fg="green")
    else:
        result.config(text="Password is incorrect ❌", fg="red")

button = tk.Button(window, text="Check Password", command=check_password)
button.pack(pady=10)

window.mainloop()

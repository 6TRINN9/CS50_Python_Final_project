import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip
from generator import generate_password
from utils import evaluate_password_strength

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.tite("Password generator")
        self.geometry("500x400")
        self.root.resizable(False, False)
        self.setup_ui()
    # Interface


    def setup_ui():
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(fill="both", expand=True)

        ttk.Label(main_frame, text="Generator stronger password", font=("Helvetica", 16)).pack(pady=10)

        # Setting frame
        setting_frame = ttk.LabelFrame(main_frame, text="Setting", padding=10)
        setting_frame.pack(fill="x", pday=10)

        length_frame = ttk.Frame(setting_frame)
        length_frame.pack(fill="x", pday=5)
        ttk.Label(length_frame, text="Password lwngth:").pack(side="left")

        # Password length
        self.length_var = tk.IntVar(value=12)
        length_scale = ttk.Scale(length_frame, from_=8, to=32, variable=self.length_var,
        orient="horizontal", length=200, command=self.update_langth_label)
        length_scale.pack(side="left", padx=10)

        self.length_label = ttk.Label(length_frame, text="12")
        self.length_label.pack(side="left")

        # Options for types char
        options_frame = ttk.Frame(setting_frame)
        options_frame.pack(fill="x", pady=10)

        self.use_letters = tk.BooleanVar(value=True)
        self.use_digits = tk.BooleanVar(value=True)
        self.use_special = tk.BooleanVar(value=True)

        ttk.Checkbutton(options_frame, text="Letters: (A-z)", variable=self.use_letters).pack(ancor="w")
        ttk.Checkbutton(options_frame, text="Digits: (0-9)", variable=self.use_digits).pack(ancor="w")
        ttk.Checkbutton(options_frame, text="Digits: (@!#%&)", variable=self.use_special).pack(ancor="w")

        # Frame password output
        result_frame = ttk.LabelFrame(main_frame, text="Password: ", padding=10)
        result_frame.pack(fill="x", pady=10)

        self.password_var = tk.stringVar()
        password_entry = ttk.Entry(result_frame, textvariable=self.password_var, font=("Courier", 12), width=32)
        password_entry.pack(pady=10, fill="x")

        # Action button
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(fill="x", pady=10)

        ttk.Button(buttons_frame, text="Generate", command=self.generate_password).pack(side="left", padx=5)
        ttk.Button(buttons_frame, text="Copy", command=self.copy_to_clipboard).pack(side="left", padx=5)

        # Password strength indicator
        strength_frame = ttk.LabelFrame(main_frame, text="Password strength", padding=10)
        strength_frame.pack(fill="x", pady=10)

        self.strength_var = tk.IntVar()
        self.strength_progressbar = ttk.Progressbar(strength_frame, variable=self.strength_var, maximum=100)
        self.strength_progressbar.pack(fill="x", pady=5)

        self.strength_label = ttk.Label(strength_frame, text="Password is None")
        self.strength_label.pack(anchor="w")

    def update_length_label(self, *args):
        self.length_label.config(text=str(self.length_var.get()))

    def generate_password(self):
        try:
            # Check that at least one character type is selected.
            if not (self.use_letters.get() or self.use_digits.get() or self.use_special.get()):
                raise ValueError("Choose at least one character type")

            # Generate password
            password = generate_password(
            self.length_var.get(),
            self.use_letters.get(),
            self.use_digits.get(),
            self.use_special.get()
            )

            # Updating the password field
            self.password_var.set(password)

            # Evaluate and display the password strength
            strength = evaluate_password_strength(password)
            self.strength_var.set(strength)

            if strength < 40:
                strength_text = "Weak password"
            elif strength < 70:
                strength_text = "Medium password"
            else:
                strength_text = "Strong password"

            self.strength_label.config(text=f"{strength_text} ({strength}/100)")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def copy_to_clipboard(self):
        password = self.password_var.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Success", "Password copied")
        else:
            messagebox.showwarning("Warning", "Firstly, generate a password")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

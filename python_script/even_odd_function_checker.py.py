import tkinter as tk
from tkinter import messagebox
import numpy as np

# ---------------------------
# Backend: Original Logic
# ---------------------------

ALLOWED_NAMES = {
    'np': np,
    'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
    'arcsin': np.arcsin, 'arccos': np.arccos, 'arctan': np.arctan,
    'sinh': np.sinh, 'cosh': np.cosh, 'tanh': np.tanh,
    'exp': np.exp, 'log': np.log, 'log10': np.log10, 'sqrt': np.sqrt,
    'abs': np.abs, 'sign': np.sign, 'floor': np.floor, 'ceil': np.ceil,
    'deg2rad': np.deg2rad, 'rad2deg': np.rad2deg,
    'pi': np.pi, 'e': np.e,
}

def make_callable(expr: str):
    expr = expr.strip()
    if not expr:
        raise ValueError("Empty expression.")
    def f(x):
        x = np.asarray(x, dtype=float)
        return eval(expr, {"_builtins_": {}}, {**ALLOWED_NAMES, 'x': x})
    _ = f(0.5)
    return f

def classify_parity(f, *, samples=200, domain=(-10, 10), tol=1e-8, seed=0):
    rng = np.random.default_rng(seed)
    a, b = domain
    R = max(abs(a), abs(b))
    if R <= 0:
        R = 10.0
    xs = rng.uniform(0.0, R, size=samples)

    def safe_eval(g, x):
        try:
            y = g(x)
        except Exception:
            y = np.array([g(float(xi)) for xi in np.atleast_1d(x)], dtype=float)
        return np.asarray(y, dtype=float)

    x = xs
    xm = -xs
    fx = safe_eval(f, x)
    fxm = safe_eval(f, xm)

    even_residual = float(np.max(np.abs(fx - fxm)))
    odd_residual = float(np.max(np.abs(fx + fxm)))

    is_even = even_residual <= tol
    is_odd = odd_residual <= tol

    if is_even and not is_odd:
        return "Even Function"
    if is_odd and not is_even:
        return "Odd Function"
    if is_even and is_odd:
        return "Even and Odd (Zero Function)"
    return "Neither Even nor Odd"

# ---------------------------
# GUI Section (Beautiful Design)
# ---------------------------

def check_function():
    expr = entry.get().strip()
    if not expr:
        messagebox.showwarning("⚠ Input Error", "Please enter a function of x.")
        return

    try:
        f = make_callable(expr)
        result = classify_parity(f, samples=400, domain=(-10, 10), tol=1e-8, seed=42)
        result_label.config(text=f"🧾 Result: {result}", fg="#1A73E8")
    except Exception as e:
        messagebox.showerror("❌ Error", f"Invalid function!\n{e}")

# Main Window
root = tk.Tk()
root.title("Calculus Project — Even/Odd Function Checker")
root.geometry("600x400")
root.config(bg="#F3F6FB")

# Title Frame
title_frame = tk.Frame(root, bg="#1A73E8", pady=15)
title_frame.pack(fill="x")

tk.Label(title_frame, text="🎓 Calculus Project", font=("Helvetica", 20, "bold"), fg="white", bg="#1A73E8").pack()
tk.Label(title_frame, text="Function Parity Checker (Even / Odd / Neither)", font=("Arial", 12), fg="white", bg="#1A73E8").pack()

# Input Section
tk.Label(root, text="\nEnter a function of x:", font=("Arial", 13, "bold"), bg="#F3F6FB").pack()

entry = tk.Entry(root, width=40, font=("Consolas", 18), relief="solid", borderwidth=2, justify="center")
entry.pack(pady=15)
entry.focus()

# Example hint
tk.Label(root, text="Examples:  x*2   |   sin(x)   |   exp(-x*2) + x", font=("Arial", 11, "italic"), fg="#555", bg="#F3F6FB").pack()

# Button
tk.Button(
    root, text="Check Function", command=check_function,
    bg="#1A73E8", fg="white", font=("Arial", 14, "bold"),
    relief="flat", padx=20, pady=8, cursor="hand2"
).pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), bg="#F3F6FB")
result_label.pack(pady=20)

# Footer
tk.Label(root, text="Developed by Ghulam Mustafa💻", font=("Arial", 15, "italic"), bg="#F3F6FB", fg="#444").pack(side="bottom", pady=10)

root.mainloop()

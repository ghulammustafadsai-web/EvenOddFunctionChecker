# EvenOddFunctionChecker

A Python-based GUI application that analyzes a mathematical function and determines whether it is **Even**, **Odd**, or **Neither**.  

This project was developed as a **Final Semester Calculus Project** and demonstrates the application of mathematical concepts using Python programming.

---

## 🔍 Project Features

- **User-friendly GUI** built with Tkinter  
- **Accurate function analysis** using NumPy  
- Handles trigonometric, exponential, logarithmic, and custom expressions  
- Classifies functions as:
  - Even Function ✅
  - Odd Function ✅
  - Even and Odd (Zero Function) ✅
  - Neither Even nor Odd ❌
- Provides real-time feedback and error handling  

---

## 🧮 How It Works

1. User enters a function of `x`, e.g., `x**2`, `sin(x) + x`, `exp(-x*2)`  
2. Program converts the string into a callable Python function  
3. Randomly samples values from the domain [-10, 10]  
4. Compares `f(x)` and `f(-x)` to determine **evenness**  
5. Compares `f(x)` and `-f(-x)` to determine **oddness**  
6. Displays result in the GUI  

---

## 🖼 GUI Preview


<img width="960" height="511" alt="project_gui" src="https://github.com/user-attachments/assets/b682e54c-37a3-4900-b4d2-1a2654497ace" />

---

## ▶ Demo Video

Watch the 4-minute demo video here:  
https://drive.google.com/file/d/1U_XFRVUd4RL3oFlk98PK3WoG6FyvVCbn/view
*Note: The demo video is in Urdu.*

---

## 📂 Sample Inputs

| Function           | Result                     |
|------------------|----------------------------|
| x**2             | Even Function              |
| x**3             | Odd Function               |
| sin(x) + x       | Neither Even nor Odd       |
| 0                | Even and Odd (Zero Function) |

*More examples can be found in* `examples/sample_functions.txt`

---

## 🚀 How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/ghulammustafadsai/EvenOddFunctionChecker.git
cd EvenOddFunctionChecker

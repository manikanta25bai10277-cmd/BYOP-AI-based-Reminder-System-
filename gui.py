import tkinter as tk

def check_eye():
    try:
        usage = int(entry_usage.get())
    except:
        label_result.config(text="⚠️ Enter valid screen time")
        return

    dryness = dryness_var.get()
    redness = redness_var.get()
    itching = itching_var.get()

    if dryness == "yes" and redness == "yes":
        problem = "Dry Eye Syndrome"
    elif itching == "yes":
        problem = "Eye Allergy"
    else:
        problem = "Normal Eye Strain"

    result = f"🧠 Condition: {problem}\n\n"

    if problem == "Dry Eye Syndrome":
        result += "• Blink frequently\n• Use eye drops\n• Follow 20-20-20 rule"
    elif problem == "Eye Allergy":
        result += "• Avoid dust\n• Wash eyes\n• Consult doctor"
    else:
        result += "• Take breaks\n• Reduce brightness\n• Maintain distance"

    label_result.config(text=result)

# Window
root = tk.Tk()
root.title("Eye Care Assistant")
root.geometry("420x500")

# Title
tk.Label(root, text="👁️ Eye Care Assistant", font=("Arial", 16, "bold")).pack(pady=10)

# Frame for inputs
frame = tk.Frame(root)
frame.pack(pady=10)

# Screen time
tk.Label(frame, text="Screen Time (hours):").pack()
entry_usage = tk.Entry(frame)
entry_usage.pack(pady=5)

# Dryness
dryness_var = tk.StringVar(value="no")
tk.Label(frame, text="Dryness:").pack()
tk.Radiobutton(frame, text="Yes", variable=dryness_var, value="yes").pack()
tk.Radiobutton(frame, text="No", variable=dryness_var, value="no").pack()

# Redness
redness_var = tk.StringVar(value="no")
tk.Label(frame, text="Redness:").pack()
tk.Radiobutton(frame, text="Yes", variable=redness_var, value="yes").pack()
tk.Radiobutton(frame, text="No", variable=redness_var, value="no").pack()

# Itching
itching_var = tk.StringVar(value="no")
tk.Label(frame, text="Itching:").pack()
tk.Radiobutton(frame, text="Yes", variable=itching_var, value="yes").pack()
tk.Radiobutton(frame, text="No", variable=itching_var, value="no").pack()

# Button
tk.Button(root, text="Check Eye Health", command=check_eye, bg="blue", fg="white").pack(pady=15)

# Output
label_result = tk.Label(root, text="", wraplength=350, justify="left")
label_result.pack(pady=10)

root.mainloop()
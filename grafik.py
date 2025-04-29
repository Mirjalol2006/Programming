import tkinter as tk
from tkinter import filedialog, messagebox

def merge_files(f1_path, f2_path, f3_path):
    with open(f1_path, 'r') as f1, open(f2_path, 'r') as f2, open(f3_path, 'w') as f3:
        line1 = f1.readline()
        line2 = f2.readline()

        while line1 and line2:
            num1 = int(line1.strip())
            num2 = int(line2.strip())

            if num1 <= num2:
                f3.write(line1)
                line1 = f1.readline()
            else:
                f3.write(line2)
                line2 = f2.readline()
                

        while line1:
            f3.write(line1)
            line1 = f1.readline()

        while line2:
            f3.write(line2)
            line2 = f2.readline()

def choose_and_merge():
    file1 = filedialog.askopenfilename(title="1-faylni tanlang")
    file2 = filedialog.askopenfilename(title="2-faylni tanlang")
    output = filedialog.asksaveasfilename(title="Yangi faylni saqlash", defaultextension=".txt")

    if file1 and file2 and output:
        try:
            merge_files(file1, file2, output)
            messagebox.showinfo("Muvaffaqiyat", "Fayllar birlashtirildi!")
        except Exception as e:
            messagebox.showerror("Xatolik", str(e))
    else:
        messagebox.showwarning("Ogohlantirish", "Barcha fayllarni tanlang!")

# Asosiy oyna
root = tk.Tk()
root.title("Fayllarni birlashtirish")
root.geometry("500x500")
btn = tk.Button(root, text="Fayllarni tanlab birlashtirish", command=choose_and_merge)
btn.pack(padx=40, pady=40)

root.mainloop()




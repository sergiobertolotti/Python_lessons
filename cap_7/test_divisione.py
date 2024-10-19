from tkinter import messagebox

def main():
    a = 20
    b = 0
    try:
        q = a / b
    except ZeroDivisionError:
        messagebox.showerror("Divisione","Il divisore non può essere nullo")
        
main()
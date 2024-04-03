import tkinter as tk

def print_text():
    root = tk.Tk()
    root.title("Text Printer")

    text_widget = tk.Text(root, height=10, width=50, wrap="word")
    text_widget.pack()

    # Agregar texto al widget de texto
    text_widget.insert(tk.END, "Hola, esto es un ejemplo de texto.\n")
    text_widget.insert(tk.END, "Puedes agregar más líneas aquí.\n")

    root.mainloop()

if __name__ == "__main__":
    print_text()

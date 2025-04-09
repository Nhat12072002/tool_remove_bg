import tkinter as tk
from dashboard import BackgroundRemoverApp

def main():
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

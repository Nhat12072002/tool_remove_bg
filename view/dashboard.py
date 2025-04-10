import tkinter as tk

class DashboardView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="white")

        title = tk.Label(self, text="📊 Dashboard", font=("Helvetica", 18, "bold"), bg="white", fg="#2c3e50")
        title.pack(pady=(20, 10))

        self.log_listbox = tk.Listbox(self, font=("Helvetica", 11), width=80, height=20)
        self.log_listbox.pack(pady=10)

    def update_logs(self, logs):
        self.log_listbox.delete(0, tk.END)
        for log in logs:
            self.log_listbox.insert(tk.END, f"📝 {log}")

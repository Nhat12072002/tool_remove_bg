import tkinter as tk
from view.remover_view import RemoverView
from view.dashboard import DashboardView

class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Công cụ xóa nền ảnh chuyên nghiệp")
        self.root.geometry("800x500")
        self.root.configure(bg="white")

        # Menu trái
        self.menu_frame = tk.Frame(root, bg="#2c3e50", width=180)
        self.menu_frame.pack(side="left", fill="y")

        self.btn_dashboard = tk.Button(
            self.menu_frame, text="📊 Dashboard", font=("Helvetica", 12), fg="white",
            bg="#2c3e50", activebackground="#34495e", activeforeground="white",
            relief="flat", command=self.show_dashboard
        )
        self.btn_dashboard.pack(fill="x", pady=(20, 0), ipady=10)

        self.btn_remover = tk.Button(
            self.menu_frame, text="🧹 Xóa nền ảnh", font=("Helvetica", 12), fg="white",
            bg="#2c3e50", activebackground="#34495e", activeforeground="white",
            relief="flat", command=self.show_remover
        )
        self.btn_remover.pack(fill="x", pady=(10, 0), ipady=10)

        # Khung chính hiển thị nội dung
        self.content_frame = tk.Frame(root, bg="#ecf0f1")
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Khởi tạo các view
        self.dashboard_view = DashboardView(self.content_frame)
        self.remover_view = RemoverView(self.content_frame, log_callback=self.add_log)

        self.current_view = None
        self.logs = []

        self.show_dashboard()

    def show_view(self, view):
        if self.current_view:
            self.current_view.pack_forget()
        self.current_view = view
        self.current_view.pack(fill="both", expand=True)

    def show_dashboard(self):
        self.dashboard_view.update_logs(self.logs)
        self.show_view(self.dashboard_view)

    def show_remover(self):
        self.show_view(self.remover_view)

    def add_log(self, log_message):
        self.logs.append(log_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()

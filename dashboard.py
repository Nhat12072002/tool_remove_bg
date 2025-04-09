import tkinter as tk
from tkinter import messagebox
from background_remove import BackgroundRemove
from file_manager import FileManager

class BackgroundRemoverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Xóa nền ảnh")
        self.master.geometry("400x200")

        self.file_manager = FileManager()
        self.remover = BackgroundRemove()

        self.input_path = None
        self.output_folder = None

        # Giao diện
        self.label_info = tk.Label(master, text="Chọn ảnh và thư mục lưu:")
        self.label_info.pack(pady=10)

        self.btn_select_image = tk.Button(master, text="📷 Chọn ảnh", command=self.select_image)
        self.btn_select_image.pack(pady=5)

        self.btn_select_folder = tk.Button(master, text="📁 Chọn thư mục lưu", command=self.select_folder)
        self.btn_select_folder.pack(pady=5)

        self.btn_process = tk.Button(master, text="🚀 Xóa nền ảnh", command=self.process_image)
        self.btn_process.pack(pady=10)

    def select_image(self):
        self.input_path = self.file_manager.select_image_file()
        if self.input_path:
            messagebox.showinfo("Thông báo", f"Đã chọn ảnh:\n{self.input_path}")

    def select_folder(self):
        self.output_folder = self.file_manager.select_output_folder()
        if self.output_folder:
            messagebox.showinfo("Thông báo", f"Thư mục lưu:\n{self.output_folder}")

    def process_image(self):
        if not self.input_path:
            messagebox.showwarning("Thiếu ảnh", "Vui lòng chọn ảnh đầu vào!")
            return
        if not self.output_folder:
            messagebox.showwarning("Thiếu thư mục", "Vui lòng chọn thư mục lưu!")
            return

        output_path = self.remover.remove_background(self.input_path, self.output_folder)
        messagebox.showinfo("Thành công", f"Đã xóa nền và lưu ảnh tại:\n{output_path}")

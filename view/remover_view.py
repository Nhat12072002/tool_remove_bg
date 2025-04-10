import tkinter as tk
from tkinter import Toplevel, Label, Entry
from background_remove import BackgroundRemove
from file_manager import FileManager

class RemoverView(tk.Frame):
    def __init__(self, parent, log_callback=None):
        super().__init__(parent, bg="#f0f4f8")

        self.file_manager = FileManager()
        self.remover = BackgroundRemove()
        self.log_callback = log_callback

        self.input_path = None
        self.output_folder = None

        title = tk.Label(self, text="✨ Công cụ xóa nền ảnh", font=("Helvetica", 16, "bold"), bg="#f0f4f8", fg="#2c3e50")
        title.pack(pady=(20, 10))

        btn_frame = tk.Frame(self, bg="#f0f4f8")
        btn_frame.pack(pady=5)

        self.btn_select_folder = tk.Button(
            btn_frame, text="📁 Chọn thư mục lưu", command=self.select_folder,
            bg="#2ecc71", fg="white", font=("Helvetica", 12), padx=10, pady=5, relief="flat"
        )
        self.btn_select_folder.grid(row=0, column=0, padx=5, pady=5)

        self.folder_path_entry = tk.Entry(
            btn_frame, font=("Helvetica", 10), width=35, state="readonly", readonlybackground="white"
        )
        self.folder_path_entry.grid(row=0, column=1, padx=5)

        self.btn_select_image = tk.Button(
            btn_frame, text="📷 Chọn ảnh", command=self.select_image,
            bg="#3498db", fg="white", font=("Helvetica", 12), padx=10, pady=5, relief="flat"
        )
        self.btn_select_image.grid(row=1, column=0, columnspan=2, pady=10, ipadx=90)

        self.btn_process = tk.Button(
            self, text="🚀 Xóa nền ảnh", command=self.process_image,
            bg="#e67e22", fg="white", font=("Helvetica", 13, "bold"), padx=10, pady=8, relief="flat"
        )
        self.btn_process.pack(pady=20)

        self.add_hover_effect(self.btn_select_image, "#2980b9")
        self.add_hover_effect(self.btn_select_folder, "#27ae60")
        self.add_hover_effect(self.btn_process, "#d35400")

    def add_hover_effect(self, widget, hover_color):
        default_color = widget["bg"]
        widget.bind("<Enter>", lambda e: widget.config(bg=hover_color))
        widget.bind("<Leave>", lambda e: widget.config(bg=default_color))

    def show_custom_popup(self, title, message, bg="#ecf0f1"):
        popup = Toplevel(self)
        popup.title(title)
        popup.geometry("350x150")
        popup.configure(bg=bg)
        popup.resizable(False, False)
        popup.attributes('-topmost', True)

        Label(popup, text=message, bg=bg, fg="#2c3e50", font=("Helvetica", 11)).pack(expand=True, pady=20)
        tk.Button(popup, text="OK", command=popup.destroy, bg="#3498db", fg="white", padx=10).pack(pady=5)

    def select_image(self):
        self.input_path = self.file_manager.select_image_file()
        if self.input_path:
            self.show_custom_popup("✅ Ảnh đã chọn", self.input_path)

    def select_folder(self):
        self.output_folder = self.file_manager.select_output_folder()
        if self.output_folder:
            self.folder_path_entry.config(state="normal")
            self.folder_path_entry.delete(0, tk.END)
            self.folder_path_entry.insert(0, self.output_folder)
            self.folder_path_entry.config(state="readonly")
            self.show_custom_popup("✅ Thư mục đã chọn", self.output_folder)

    def process_image(self):
        if not self.input_path:
            self.show_custom_popup("⚠️ Thiếu ảnh", "Vui lòng chọn ảnh đầu vào!", bg="#fce4e4")
            return
        if not self.output_folder:
            self.show_custom_popup("⚠️ Thiếu thư mục", "Vui lòng chọn thư mục lưu!", bg="#fce4e4")
            return

        output_path = self.remover.remove_background(self.input_path, self.output_folder)
        self.show_custom_popup("🎉 Thành công", f"Ảnh đã được xử lý và lưu tại:\n{output_path}", bg="#dff9fb")

        if self.log_callback:
            self.log_callback(f"Đã xử lý: {self.input_path.split('/')[-1]}")

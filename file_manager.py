from tkinter import filedialog, Tk

class FileManager:
    def __init__(self):
        self.root = Tk()
        self.root.withdraw()

    def select_image_file(self) -> str:
        return filedialog.askopenfilename(
            title="Chọn ảnh",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )

    def select_output_folder(self) -> str:
        return filedialog.askdirectory(
            title="Chọn thư mục lưu ảnh"
        )

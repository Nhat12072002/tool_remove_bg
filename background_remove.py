from rembg import remove
from PIL import Image
from tkinter import Tk
from tkinter.filedialog import askopenfilename


class BackgroundRemover:
    def __init__(self):
        self.input_path = None
        self.output_path = None

    def choose_image(self):
        Tk().withdraw()
        self.input_path = askopenfilename(
            title='Chọn ảnh cần xóa nền',
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp")]
        )
        if not self.input_path:
            print("Bạn chưa chọn ảnh nào.")
            return False
        return True

    def remove_background(self):
        input_image = Image.open(self.input_path)
        output_image = remove(input_image)

        self.output_path = self.input_path.rsplit('.', 1)[0] + '_no_bg.png'
        output_image.save(self.output_path)

        print(f"✅ Ảnh đã lưu tại: {self.output_path}")
        output_image.show()

from rembg import remove
from PIL import Image
import os

class BackgroundRemove:
    def remove_background(self, input_path, output_folder):
        image = Image.open(input_path)
        result = remove(image)
        
        filename = os.path.basename(input_path)
        name, _ = os.path.splitext(filename)
        output_path = os.path.join(output_folder, f"{name}_no_bg.png")
        
        result.save(output_path)
        return output_path

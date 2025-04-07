from rembg import remove
from PIL import Image
input_path = '1.jpg'
output_path = '1.png'
input=Image.open(input_path)
output=remove(input)
output.save(output_path)
Image.open(output_path)
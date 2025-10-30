import os
from PIL import Image

# Input and output folders
current_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(current_dir, "images")
output_folder = os.path.join(current_dir, "output")

# Desired size (width, height)
new_size = (800, 600)

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize the image
        resized_img = img.resize(new_size)

        # Change format to JPG (optional)
        new_filename = os.path.splitext(filename)[0] + ".jpg"
        output_path = os.path.join(output_folder, new_filename)

        # Save resized image
        resized_img.save(output_path, "JPEG")

        print(f"✅ Resized and saved: {output_path}")

print("\n🎉 All images resized successfully!")

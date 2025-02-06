from PIL import Image
import os

def convert_jpg_to_png(input_folder, output_folder):
    """
    Converts all JPG images in the input_folder to PNG format and saves them in output_folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
            img_path = os.path.join(input_folder, file)
            img = Image.open(img_path)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".png")
            img.save(output_path, "PNG")
            print(f"Converted: {file} -> {os.path.basename(output_path)}")

if __name__ == "__main__":
    input_folder = "input_images"  # Change this to your input folder path
    output_folder = "output_images"  # Change this to your output folder path
    convert_jpg_to_png(input_folder, output_folder)

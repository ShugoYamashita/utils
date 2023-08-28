import os
from PIL import Image

INPUT_DIRECTORY = "./data/input/"
OUTPUT_DIRECTORY = "./data/output/"
IMG_SIZE = 640

def crop_center(img, crop_width, crop_height):
    img_width, img_height = img.size
    return img.crop(((img_width - crop_width) // 2,(img_height - crop_height) // 2,
        (img_width + crop_width) // 2,(img_height + crop_height) // 2))

def main():
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)

    # get files in INPUT_DIRECTORY
    for filename in os.listdir(INPUT_DIRECTORY):
        if filename.endswith(".png"):
            input_file_path = os.path.join(INPUT_DIRECTORY, filename)
            with Image.open(input_file_path) as img:
                # crop square
                img = crop_center(img, min(img.size), min(img.size))

                # resize
                img = img.resize((IMG_SIZE, IMG_SIZE))

                # save
                output_file_path = os.path.join(OUTPUT_DIRECTORY, filename)
                img.save(output_file_path)

if __name__ == "__main__":
    main()

# Python script to downsample PNG images to the size (4000, 4000) to use as input for ATS.

# Relevant libraries
import PIL
from PIL import Image
import os
from tqdm import tqdm
import glob
import shutil # Copy files from one folder to another one
from pathlib import Path # Same ^

# Copy files
def copyFiles():
    src_dir = '/home/andrewaever/Desktop/TestImagesPng/'
    dest_dir = '/home/andrewaever/Desktop/ResizePng'
    files = os.listdir(src_dir)

    for f_name in files:
        shutil.copy2(os.path.join(src_dir, f_name), dest_dir)

# Resize
def resizeImg(path="/home/andrewaever/Desktop/TestImagesPng/*", save_path="/home/andrewaever/Desktop/ResizePng/"):
    imageNames = glob.glob(path)
    numImages = len(imageNames)
    print("Detected : ", numImages, " images in the folder.")

    count = 0
    for name in tqdm(imageNames):
        image = Image.open(name)
        image = image.resize((4000, 4000), Image.ANTIALIAS)
        image.save(save_path + str(count), "png", quality=90)
        count += 1

#copyFiles()
resizeImg()
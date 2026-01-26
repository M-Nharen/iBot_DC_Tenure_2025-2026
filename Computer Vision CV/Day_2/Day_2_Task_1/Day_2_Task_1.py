import cv2
from sys import argv, exit
from PIL import Image
import os
import numpy as np

def main():
    argc = len(argv)
    if argc!=2:
        print(f"Usage: python3 {argv[0]} filepath")
        exit()
    
    img = cv2.imread(argv[1])
    height, width = img.shape[:2]

    os.makedirs("output",exist_ok=True)

    flip1img = cv2.flip(img,1)
    save(flip1img,"flip_horizontal.png")

    flip0img = cv2.flip(img,0)
    save(flip0img,"flip_vertical.png")

    center = (width//2,height//2)
    angle = 45
    scale = 1
    rotation_matrix = cv2.getRotationMatrix2D(center,angle,scale)
    rotated = cv2.warpAffine(img,rotation_matrix,(width,height))
    save(rotated,"rotated.png")

    scale_factor = 1.5
    scaled = cv2.resize(img,None,fx=scale_factor,fy=scale_factor)
    start_y = (scaled.shape[0]-height)//2
    start_x = (scaled.shape[1]-width)//2
    zoomed = scaled[start_y:start_y+height,start_x:start_x+width]
    save(zoomed,"zoomed.png")

    mean = 0
    std = 25
    gaussian_noise = np.random.normal(mean,std,img.shape)
    noisy = np.clip(img+gaussian_noise,0,255).astype(np.uint8)
    save(noisy,"noisy.png")


def save(img,name):
    PILimg = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    PILimg.save(os.path.join("output",name))

if __name__ == "__main__":
    main()
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def main():
    argc = len(sys.argv)
    if argc != 2:
        print("Usage: python3 {argv[0]} picture_address.")
        sys.exit()
    filepath = sys.argv[1]
    image = cv2.imread(filepath)
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image,(7,7),0)
    canny_image = auto_canny(blurred_image)
    _, threshold_image = cv2.threshold(blurred_image,127,255,cv2.THRESH_BINARY)

    fig,axes = plt.subplots(2,2)

    axes[0][0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axes[0][0].set_title("Original image")

    axes[0][1].imshow(blurred_image, cmap = "gray")
    axes[0][1].set_title("Gaussian Blurred image")

    axes[1][0].imshow(canny_image, cmap = "gray")
    axes[1][0].set_title("Canny image")

    axes[1][1].imshow(threshold_image, cmap = "gray")
    axes[1][1].set_title("Threshold image")

    plt.show()

def auto_canny(image):
    median = np.median(image)
    lower = int(0.67*median)
    upper = int(min(255,1.33*median))
    return cv2.Canny(image,lower,upper)

if __name__ == "__main__":
    main()
